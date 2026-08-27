# BF01 Tombo CHI/CHS Test Vectors Harness

Python test harness for testing decryption CLI tools using JSON test vectors.

## Usage

```bash
python testharness.py <cli_path> <test_vectors_dir> [cmd_template]
```

### Command Template

The optional `cmd_template` argument specifies the CLI command with placeholders:

- `{CLI}` - Path to the CLI tool
- `{IN}` - Input file path
- `{OUT}` - Output file path
- `{PASSPHRASE}` - Passphrase for decryption/encryption
- `{ENCRYPT}` - Mode flag: `-e` for encrypt, `-d` for decrypt
- `{SALT}` - Salt value from test vector (empty string if not set)

Example:

Using binary built from https://github.com/clach04/tombo/blob/my_changes/contrib/TomboCrypt/chi_crypt.c

```bash
py -3  testharness.py chi_crypt_salted testvectors/ "{CLI} {ENCRYPT} --password {PASSPHRASE} {IN} {OUT}" "{CLI} {ENCRYPT} --salt {SALT} --password {PASSPHRASE} {IN} {OUT}"
py -3 testharness.py C:/code/py/chi_io/chi_tool.py testvectors/ "py -3 {CLI} {ENCRYPT} -o {OUT} --password {PASSPHRASE} --salt {SALT} {IN}"

python testharness.py chi_crypt testvectors/ "{CLI} -d --password {PASSPHRASE} {IN} {OUT}"
py -3  testharness.py chi_crypt testvectors/ "{CLI} -d --password {PASSPHRASE} {IN} {OUT}"
py -3  testharness.py chi_crypt testvectors/ "{CLI} {ENCRYPT} --password {PASSPHRASE} {IN} {OUT}"
```

Using binary built (without salt override support) from https://github.com/clach04/puren_tonbo/blob/main/puren_tonbo/tools/ptcipher.py

```bash
py -3  testharness.py ptcipher  testvectors/ "{CLI} -d --password {PASSPHRASE} --cipher=chi -o {OUT} {IN}"

py -3  testharness.py ptcipher  testvectors/ "{CLI} -d --password {PASSPHRASE} --cipher=chi -o {OUT} {IN}" "{CLI} -e --password {PASSPHRASE} --cipher=chi -o {OUT} {IN}"
```

If not provided, defaults to: `{CLI} {ENCRYPT} -o {OUT} -p {PASSPHRASE} {IN}`

## JSON Schema

Each test vector JSON file contains:

- `comment` - Description of the test
- `passphrase` - Password for symmetric encryption
- `expect` - Expected outcome (success, no match, etc.)
- `payload_file` - Input encrypted file
- `expected_canon` - Expected decrypted output file
- `encrypt` - (optional) Set to `true` for encryption tests
- `salt` - (optional) Salt value injected as `{SALT}` in template
- `ignore_tail` - (optional) Set to `true` to compare output ignoring the
  trailing bytes of the final cipher block (and for `.chi` output, bytes
  past the header-declared ciphertext length). Useful when comparing
  implementations that differ only in end-of-stream padding handling.
  Can also be enabled for all tests with the `--ignore-tail` harness flag.

## Running Tests

```bash
python -m pytest tests/
```

Harness (no salt support):

```bash
py -3 testharness.py /path/to/chi_crypt.exe testvectors/ "{CLI} {ENCRYPT} --password {PASSPHRASE} {IN} {OUT}"
```

With salt-supporting build:

```bash
py -3 testharness.py /path/to/chi_crypt_salted.exe testvectors/ \
    "{CLI} {ENCRYPT} --password {PASSPHRASE} {IN} {OUT}" \
    "{CLI} {ENCRYPT} --salt {SALT} --password {PASSPHRASE} {IN} {OUT}"
```