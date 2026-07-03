# Design Notes

## Current Implementation

- External payload files only (not embedded in JSON)
- Symmetric encryption with passphrase
- Python 2.6+ and Python 3.x compatible

## Future Considerations

### Support tools that output to stdout

Remove the need for temporary files, reduce file IO.

### Hex Payload in JSON

Allow embedding hex-encoded payloads directly in JSON files alongside external file references.

### Encryption Testing

- Use fixed IV for reproducible encryption tests
- Test encryption direction with known plaintext/ciphertext pairs
- Consider adding `encrypt` expect value for encryption tests

### Additional Expect Values

Current implementation supports:
- success
- no match
- HMAC failure
- header failure
- payload failure
- armor failure

Similar to https://github.com/C2SP/CCTV/tree/main/age#test-file-format

Future: May add more granular error types as needed.