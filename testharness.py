#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test harness for decryption CLI tool using JSON test vectors.
Supports Python 2 and Python 3.
"""
from __future__ import print_function
import sys
import os
import json
import subprocess
import hashlib

PYTHON_VERSION = sys.version_info[0]

def load_test_vector(json_path):
    with open(json_path, 'r') as f:
        return json.load(f)

def compute_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

def run_decrypt(cli_path, payload_path, passphrase, output_path, cmd_template):
    cmd = []
    for arg in cmd_template:
        arg = arg.replace('{CLI}', cli_path)
        arg = arg.replace('{IN}', payload_path)
        arg = arg.replace('{OUT}', output_path)
        arg = arg.replace('{PASSPHRASE}', passphrase)
        cmd.append(arg)
    try:
        result = subprocess.call(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        return result
    except Exception as e:
        return -1

def verify_test(test_vector, payload_dir, cli_path, cmd_template):
    comment = test_vector.get('comment', '')
    expect = test_vector['expect']
    passphrase = test_vector.get('passphrase', '')
    payload_file = test_vector.get('payload_file', '')
    expected_canon = test_vector.get('expected_canon', '')
    payload_path = os.path.join(payload_dir, payload_file)
    output_path = payload_path + '.dec'
    if not os.path.exists(payload_path):
        return False, comment + ' [missing payload]'
    result = run_decrypt(cli_path, payload_path, passphrase, output_path, cmd_template)
    passed = False
    if expect == 'success':
        if result == 0:
            if os.path.exists(output_path):
                actual_hash = compute_hash(output_path)
                expected_path = os.path.join(payload_dir, expected_canon)
                if os.path.exists(expected_path):
                    expected_hash = compute_hash(expected_path)
                    passed = actual_hash == expected_hash
                else:
                    passed = False
            else:
                passed = False
        else:
            passed = False
    elif expect == 'no match':
        passed = result != 0
    elif expect in ('HMAC failure', 'header failure', 'payload failure', 'armor failure'):
        passed = result != 0
    else:
        passed = False
    if os.path.exists(output_path):
        os.remove(output_path)
    return passed, comment

def main():
    if len(sys.argv) < 3:
        print("Usage: python testharness.py <cli_path> <test_vectors_dir> [cmd_template]")
        print("  cmd_template: e.g. '{CLI} -d --password {PASSPHRASE} {IN} {OUT}'")
        sys.exit(1)
    cli_path = sys.argv[1]
    test_vectors_dir = sys.argv[2]
    if len(sys.argv) >= 4:
        cmd_template = sys.argv[3].split()
    else:
        cmd_template = [cli_path, '-d', '-o', '{OUT}', '-p', '{PASSPHRASE}', '{IN}']
    passed = 0
    failed = 0
    for filename in sorted(os.listdir(test_vectors_dir)):
        if not filename.endswith('.json'):
            continue
        json_path = os.path.join(test_vectors_dir, filename)
        tv = load_test_vector(json_path)
        result, comment = verify_test(tv, test_vectors_dir, cli_path, cmd_template)
        if result:
            passed += 1
            print("PASS: %s - %s" % (filename, comment))
        else:
            failed += 1
            print("FAIL: %s - %s" % (filename, comment))
    print("\nResults: %d passed, %d failed" % (passed, failed))
    sys.exit(0 if failed == 0 else 1)

if __name__ == '__main__':
    main()
