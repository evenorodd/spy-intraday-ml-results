#!/usr/bin/env python3
"""Verify published aggregate evidence; no model, database or network access."""
from pathlib import Path
from collections import Counter, defaultdict
import csv
import hashlib
import json
import math
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_FILES = {
    'evidence/stage2d_confirmation_report.json': '8a52292d5fc9139f977fa7cdd4174840cc046b0c95401df7cc3bc91002120e72',
    'evidence/stage2e_oracle_summary.json': '2f4341fdefd5e39aa658ce1c72ec298f2e35dc97b8a202cb5f35965a4628c9ca',
}
SEEDS = set(range(32000001, 32000021))
EFFECTS = {1.0, 0.5, 0.25, 0.1, 0.05}
SHAPES = {'linear', 'conditional'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def close(actual, expected, message):
    require(math.isfinite(float(actual)) and math.isclose(float(actual), float(expected), rel_tol=1e-11, abs_tol=1e-11), message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load_report(relative):
    data = (ROOT / relative).read_bytes()
    require(sha(data) == EXPECTED_FILES[relative], 'Original file hash mismatch: ' + relative)
    obj = json.loads(data)
    payload = {k: v for k, v in obj.items() if k != 'payload_sha256'}
    digest = sha(json.dumps(payload, sort_keys=True, separators=(',', ':'), allow_nan=False).encode())
    require(digest == obj['payload_sha256'], 'Payload seal mismatch: ' + relative)
    for field in ('raw_returns_persisted', 'raw_scores_persisted', 'daily_input_vectors_persisted',
                  'real_walk_forward_access_permitted', 'final_holdout_access_permitted',
                  'real_model_promotion_authorized', 'trading_or_real_backtesting_authorized',
                  'real_data_gate_changed', 'automatic_retry_permitted'):
        require(obj[field] is False, 'Unexpected scope flag: ' + field)
    require(obj['synthetic_only'] is True, 'Report is not synthetic-only')
    return obj


def verify_manifest():
    checked = set()
    for line in (ROOT / 'CHECKSUMS.sha256').read_text().splitlines():
        digest, relative = line.split('  ', 1)
        path = Path(relative)
        require(len(digest) == 64 and all(c in '0123456789abcdef' for c in digest), 'Invalid manifest digest')
        require(not path.is_absolute() and '..' not in path.parts, 'Unsafe manifest path')
        require(relative not in checked and relative != 'CHECKSUMS.sha256', 'Duplicate/self manifest entry')
        require(sha((ROOT / relative).read_bytes()) == digest, 'Release checksum mismatch: ' + relative)
        checked.add(relative)
    require(set(EXPECTED_FILES) | {'README.md', 'CLOSEOUT.md', 'METHODS.md', 'tools/verify_results.py'} <= checked,
            'Required release files missing from checksum manifest')
    return len(checked)


def csv_rows(relative):
    with (ROOT / relative).open(newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


def verify_confirmation(d):
    require(d['study_id'] == 'stage2d_development_quantile_confirmation_20261005_v2', 'Stage 2D study mismatch')
    require(d['contract_sha256'] == '7cbcc840cfcf25c1c7ded85efc5c94fda9c57a1c9eee8772e1acc3503dfc2d1b', 'Stage 2D contract mismatch')
    require(d['status'] == 'registered_confirmation_nonpass', 'Stage 2D result changed')
    require(d['completed_cases'] == 220 and len(d['source_case_file_sha256']) == 220, 'Incomplete Stage 2D case catalog')
    require(d['strategy_count_per_case'] == 36 and d['historical_dsr_trial_count'] == 360, 'Strategy/ledger count mismatch')
    require(d['outer_prediction_fits'] == 21120 and d['estimator_fit_calls'] == 35200, 'Fit accounting mismatch')
    require(d['count_requirement'] == 16600 and d['capacity_passed'] is True, 'Capacity result mismatch')
    require(d['capacity_cells'] == 396 and len(d['capacity_results']) == 396, 'Incomplete capacity cells')
    minimum, maximum = math.inf, -math.inf
    seen = set()
    for cell in d['capacity_results']:
        key = (cell['shape'], cell['effect_bps'], cell['trial_id'])
        require(key not in seen, 'Duplicate capacity cell')
        seen.add(key)
        require(set(map(int, cell['counts_by_seed'])) == SEEDS, 'Missing/extra capacity seed')
        counts = list(cell['counts_by_seed'].values())
        require(all(isinstance(n, int) and n >= 16600 for n in counts), 'Count floor failure')
        require(cell['count_successes'] == 20 and cell['passed'] is True, 'Capacity successes mismatch')
        minimum = min(minimum, min(counts)); maximum = max(maximum, max(counts))
    require((minimum, maximum) == (20214, 37831), 'Published count range mismatch')
    require({(x['shape'], x['planted_effect_bps']) for x in d['detection_results']} ==
            {(s, a) for s in SHAPES for a in EFFECTS} and len(d['detection_results']) == 10,
            'Missing/duplicate positive settings')
    require(all(x['successes'] == 0 and x['attempted_seeds'] == 20 and x['operational_screen_passed'] is False
                and x['population_power_guarantee'] is False for x in d['detection_results']), 'Detection summary changed')
    require(d['null_seed_count'] == 20 and d['null_seeds_with_any_candidate_would_pass'] == 0
            and d['null_candidates_would_pass'] == 0, 'Null result mismatch')
    require(d['population_false_promotion_rate_at_most_5_percent_established'] is False
            and d['population_power_at_least_80_percent_established'] is False
            and d['real_procedure_bridge_completed'] is False, 'Unsupported inference/real bridge claim')
    close(d['zero_of_20_one_sided_95_percent_upper_bound'], 1 - 0.05 ** (1 / 20), 'Retained null bound arithmetic mismatch')
    return minimum, maximum


def verify_strongest_export(d):
    rows = csv_rows('evidence/stage2d_strongest_strategy_summary.csv')
    require(len(rows) == 1440, 'Strongest export must have 1,440 rows')
    sources = json.loads((ROOT / 'evidence/stage2d_strongest_source_hashes.json').read_text())
    expected_cases = {f'spy_synthetic_confirmation_{seed}_{shape}_1p00bps' for seed in SEEDS for shape in SHAPES}
    require(set(sources) == expected_cases, 'Strongest source inventory mismatch')
    for case_id, record in sources.items():
        require(record['file_sha256'] == d['source_case_file_sha256'][case_id], 'Strongest source hash mismatch')
        require(len(record['payload_sha256']) == 64, 'Invalid source payload hash')
    filters = {'all_eligible_times', 'exclude_opening_period', 'exclude_opening_and_closing_periods'}
    models = {f'logistic_C_{c}' for c in ('0.01', '0.1', '1', '10')}
    models |= {f'xgboost_depth_{depth}_lr_{rate}_child_{child}' for depth in (2, 3)
               for rate in ('0.03', '0.05') for child in (20, 100)}
    per_case = defaultdict(set)
    improvements = Counter()
    primary = Counter()
    seen = set()
    for row in rows:
        case_id = row['case_id']
        require(case_id in sources and row['source_case_sha256'] == sources[case_id]['file_sha256'], 'CSV source binding mismatch')
        seed, shape = int(row['seed']), row['shape']
        require(seed in SEEDS and shape in SHAPES and float(row['plant_amplitude_bps']) == 1, 'CSV scope mismatch')
        require(case_id == f'spy_synthetic_confirmation_{seed}_{shape}_1p00bps', 'CSV case identity mismatch')
        trial = row['trial_id']; key = (case_id, trial)
        require(key not in seen, 'Duplicate CSV strategy')
        seen.add(key)
        require(row['model_id'] in models and row['time_filter'] in filters, 'Unknown CSV strategy')
        require(trial == 'q30_' + row['model_id'] + '_' + row['time_filter'], 'CSV trial identity mismatch')
        per_case[case_id].add((row['model_id'], row['time_filter']))
        is_primary = row['model_id'].startswith('logistic_') and row['time_filter'] == 'all_eligible_times'
        require(int(row['primary']) == int(is_primary), 'Primary strategy classification mismatch')
        primary[shape] += is_primary
        mean = float(row['mean_base_net_bps']); baseline = float(row['best_deterministic_mean_bps'])
        require(mean < 0 and int(row['positive_folds']) == 0 and float(row['hac_ci_upper_bps']) < 0,
                'Strongest-case economic finding mismatch')
        require(int(row['completed_trades']) >= 16600 and int(row['would_pass_candidate_gates']) == 0, 'Strongest gate mismatch')
        require(int(row['random_draws_beaten']) == 100 and int(row['random_draw_count']) == 100, 'Random comparison mismatch')
        require(float(row['reality_check_p_value']) == 1, 'Retained Reality Check mismatch')
        close(row['baseline_improvement_bps'], mean - baseline, 'Baseline arithmetic mismatch')
        improvements[shape] += (mean - baseline) >= 0.1
    require(set(per_case) == expected_cases and all(v == {(m, f) for m in models for f in filters} for v in per_case.values()),
            'Missing/extra model/filter combinations')
    require(dict(primary) == {'conditional': 80, 'linear': 80}, 'Primary row count mismatch')
    require(dict(improvements) == {'conditional': 700, 'linear': 720}, 'Baseline improvement totals mismatch')
    return len(rows)


def verify_oracle(e):
    require(e['study_id'] == 'stage2e_synthetic_oracle_feasibility_20261008_v1', 'Stage 2E study mismatch')
    require(e['execution_contract_sha256'] == '332a4a8be50433e4d65fe88027af7358217036e110d2a788fa1780108ad8e28d', 'Stage 2E contract mismatch')
    require(e['status'] == 'ORACLE_DIAGNOSTIC_COMPLETED' and e['original_nonpass_unchanged'] is True, 'Stage 2E status mismatch')
    require(e['completed_seed_analyses'] == 20 and len(e['source_analysis_sha256']) == 20, 'Incomplete Stage 2E source inventory')
    require(e['fold_outcome_materializations'] == 1760 and e['positive_setting_summaries'] == 200, 'Stage 2E scope mismatch')
    require(all(e[k] == 0 for k in ('new_datasets', 'new_seeds', 'new_model_fits', 'outer_prediction_fits', 'estimator_fit_calls')), 'Unexpected new fitting/data')
    require(e['fresh_confirmation_evidence'] is False and e['population_power_claim_authorized'] is False
            and e['full_candidate_gates_evaluated'] is False, 'Oracle interpretation changed')
    require(len(e['cells']) == 10, 'Incomplete oracle cells')
    expected = {(s, a) for s in SHAPES for a in EFFECTS}
    seen, counts = set(), {}
    pooled = {}
    for cell in e['cells']:
        key = (cell['shape'], cell['effect_bps'])
        require(key in expected and key not in seen, 'Unknown/duplicate oracle cell')
        seen.add(key)
        rows = cell['per_seed']
        require(len(rows) == 20 and {r['source_seed'] for r in rows} == SEEDS, 'Oracle seed coverage mismatch')
        require(cell['seed_denominator'] == 20 and cell['seed_screen_successes'] == 0 and cell['economic_reference_met'] is False,
                'Oracle diagnostic result mismatch')
        means = cell['pooled_trade_weighted_mean_bps']; total = sum(r['completed_trades'] for r in rows)
        for row in rows:
            require(row['completed_trades'] >= 16600 and row['economic_count_screen_met'] is False and row['positive_fold_count'] == 0,
                    'Oracle seed screen mismatch')
            m = row['mean_bps']
            require(m['base_net_bps'] < 0, 'Oracle net finding mismatch')
            close(m['planted_gross_bps'] - m['base_cost_drag_bps'], m['base_net_bps'], 'Oracle seed gross/net mismatch')
            close(m['proportional_drag_bps'] + m['spread_drag_bps'] + m['fee_drag_bps'], m['base_cost_drag_bps'], 'Oracle seed component mismatch')
            close(m['planted_gross_bps'] - m['unplanted_gross_bps'], m['gross_plant_increment_bps'], 'Oracle seed paired gross mismatch')
            close(m['base_net_bps'] - m['zero_effect_base_net_bps'], m['net_plant_increment_bps'], 'Oracle seed paired net mismatch')
            count_key = (cell['shape'], row['source_seed'])
            require(count_key not in counts or counts[count_key] == row['completed_trades'], 'Selections changed across effects')
            counts[count_key] = row['completed_trades']
        for field, value in means.items():
            close(value, sum(r['completed_trades'] * r['mean_bps'][field] for r in rows) / total, 'Oracle pooled mean mismatch: ' + field)
        close(cell['pooled_trade_weighted_net_mean_bps'], means['base_net_bps'], 'Oracle redundant net field mismatch')
        pooled[key] = means
    require(seen == expected, 'Missing oracle setting')
    exported = csv_rows('evidence/stage2e_setting_summary.csv')
    require(len(exported) == 10, 'Oracle CSV coverage mismatch')
    exported_keys = set()
    fields = {'gross_bps': 'planted_gross_bps', 'modeled_cost_bps': 'base_cost_drag_bps',
              'net_bps': 'base_net_bps', 'plant_increment_bps': 'gross_plant_increment_bps'}
    for row in exported:
        key = (row['shape'], float(row['plant_amplitude_bps']))
        require(key in pooled and key not in exported_keys, 'Unknown/duplicate oracle CSV row')
        exported_keys.add(key)
        for column, source in fields.items():
            close(row[column], pooled[key][source], 'Oracle CSV value mismatch')
        require(int(row['seed_screen_successes']) == 0 and int(row['seed_denominator']) == 20, 'Oracle CSV screen mismatch')
    require(exported_keys == expected, 'Missing oracle CSV row')
    return sum(len(c['per_seed']) for c in e['cells'])


def verify_capacity_arithmetic():
    cap = ((390 - 60) // 30) * 8 * 146
    coefficient = (1.959963984540054 + 0.8416212335729143) ** 2 / 0.25 ** 2
    counts = {sigma: 100 * math.ceil(coefficient * sigma ** 2 / 100) for sigma in (8, 10, 12, 15, 20, 23)}
    require(cap == 12848 and counts == {8: 8100, 10: 12600, 12: 18100, 15: 28300, 20: 50300, 23: 66500},
            'Public capacity arithmetic mismatch')
    close(math.sqrt(12800 / coefficient), 10.095809709658953, 'Rounded planning limit mismatch')
    return cap


def main():
    checked = verify_manifest()
    d = load_report('evidence/stage2d_confirmation_report.json')
    e = load_report('evidence/stage2e_oracle_summary.json')
    minimum, maximum = verify_confirmation(d)
    strongest = verify_strongest_export(d)
    oracle = verify_oracle(e)
    capacity = verify_capacity_arithmetic()
    print(json.dumps({'status': 'PUBLISHED_AGGREGATES_VERIFIED', 'release_files_checked': checked,
                      'original_report_hashes_and_payloads_verified': 2,
                      'stage2d_capacity_cells': 396, 'stage2d_count_range': [minimum, maximum],
                      'stage2d_strongest_strategy_rows': strongest, 'stage2e_seed_summaries': oracle,
                      'thirty_minute_planning_capacity': capacity,
                      'scientific_reruns': 0, 'model_fits': 0, 'registry_access': False}, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print('VERIFICATION FAILED: ' + str(exc), file=sys.stderr)
        sys.exit(1)
