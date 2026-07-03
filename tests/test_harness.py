#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Unit tests for testharness module."""
from __future__ import print_function
import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from testharness import load_test_vector, compute_hash

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

if __name__ == '__main__':
    unittest.main()
