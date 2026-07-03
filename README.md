# Test Vectors Harness

Python test harness for testing decryption CLI tools using JSON test vectors.

## Usage

```bash
python testharness.py <path_to_cli> <test_vectors_dir>
```

## JSON Schema

Each test vector JSON file contains:

- `comment` - Description of the test
- `passphrase` - Password for symmetric encryption
- `expect` - Expected outcome (success, no match, etc.)
- `payload_file` - Input encrypted file
- `expected_canon` - Expected decrypted output file

## Running Tests

```bash
python -m pytest tests/
```