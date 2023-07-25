import json
import os

BASE_PATH = '.'
INPUTS_PATH = os.path.join(BASE_PATH, 'inputs')
OUTPUT_PATH = os.path.join(BASE_PATH, 'outputs')


def get_all_tests(prefix):
    test_files = [f for f in os.listdir(INPUTS_PATH) if os.path.isfile(os.path.join(INPUTS_PATH, f))]
    return list(filter(lambda f: f.startswith(prefix), test_files))


def scan_test_input(test):
    with open(os.path.join(INPUTS_PATH, test), 'r') as f:
        test_lines = f.readlines()[::-1]
    n = int(test_lines.pop()[:-1])
    n_next_lines = [test_lines.pop()[:-1] for _ in range(n)]
    result = test_lines.pop()[:-1]

    return n, n_next_lines, result


def _clean_result(result):
    return ' '.join(map(str, result)) if ' ' not in result else result


def is_result_valid(test: str, result: dict):
    with open(f'{OUTPUT_PATH}/{test.replace("in", "out")}', 'r') as f:
        outcome = f.readlines()

    return ''.join(outcome) == result
