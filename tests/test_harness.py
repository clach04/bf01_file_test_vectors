#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Unit tests for testharness module."""
from __future__ import print_function
import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from testharness import load_test_vector, compute_hash, run_crypt_tool

class TestLoadTestVector(unittest.TestCase):
    def test_load_json(self):
        json_path = os.path.join(os.path.dirname(__file__), '..', 'testvectors', 'example_success.json')
        if os.path.exists(json_path):
            tv = load_test_vector(json_path)
            self.assertIn('comment', tv)
            self.assertIn('expect', tv)

class TestComputeHash(unittest.TestCase):
    def test_hash(self):
        test_file = os.path.join(os.path.dirname(__file__), 'test_data.bin')
        with open(test_file, 'wb') as f:
            f.write(b'test data')
        h = compute_hash(test_file)
        self.assertEqual(len(h), 64)
        os.remove(test_file)

class TestCmdTemplate(unittest.TestCase):
    def test_custom_template(self):
        template = ['{CLI}', '-d', '--password', '{PASSPHRASE}', '{IN}', '{OUT}']
        result = run_crypt_tool('cli', 'in.bin', 'pass', 'out.bin', template)
        self.assertEqual(result, -1)

    def test_custom_template_with_salt(self):
        template = ['{CLI}', '-d', '--password', '{PASSPHRASE}', '-s', '{SALT}', '{IN}', '{OUT}']
        result = run_crypt_tool('cli', 'in.bin', 'pass', 'out.bin', template, salt='mysalt')
        self.assertEqual(result, -1)

    def test_encrypt_template(self):
        template = ['{CLI}', '{ENCRYPT}', '--password', '{PASSPHRASE}', '{IN}', '{OUT}']
        result = run_crypt_tool('cli', 'in.bin', 'pass', 'out.bin', template, encrypt=True)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
