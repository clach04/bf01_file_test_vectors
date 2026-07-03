# BF01 Tombo CHI/CHS Test Vectors Harness

Python test harness for testing decryption CLI tools using JSON test vectors.

## Usage

```bash
python testharness.py <cli_path> <test_vectors_dir> [cmd_template]
```

### Command Template

The optional `cmd_template` argument specifies the CLI command with placeholders:

- `{CLI}` - Path to the CLI tool
- `{IN}` - Input encrypted file path
- `{OUT}` - Output decrypted file path
- `{PASSPHRASE}` - Passphrase for decryption

Example:

Using binary built from https://github.com/clach04/tombo/blob/my_changes/contrib/TomboCrypt/chi_crypt.c

```bash
python testharness.py chi_crypt testvectors/ "{CLI} -d --password {PASSPHRASE} {IN} {OUT}"
py -3  testharness.py chi_crypt testvectors/ "{CLI} -d --password {PASSPHRASE} {IN} {OUT}"
```

Using binary built from https://github.com/clach04/puren_tonbo/blob/main/puren_tonbo/tools/ptcipher.py

```bash
py -3  testharness.py ptcipher  testvectors/ "{CLI} -d --password {PASSPHRASE} --cipher=chi -o {OUT} {IN}"
```

If not provided, defaults to: `{CLI} -d -o {OUT} -p {PASSPHRASE} {IN}`

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