import glob
import json
import os
import sys

argv = sys.argv

filename_dict = {}

for file_pattern in argv[1:]:
    print(file_pattern)
    for filename in glob.glob(file_pattern):
        filename_dict[filename] = False
print(filename_dict)


dumb_template = """
{
    "comment": "Basic successful decryption test, Tombo v1 win32 created file",
    "passphrase": "password",
    "expect": "success",
    "payload_file": "tombo_test.chs",
    "expected_canon": "tombo_test.plaintext"
}
"""

PLAINTEXT_PREFIX = '.plaintext'
CRYPTTEXT_PREFIX = '.chi'  # note, might be `.chs` BUT it's the same length as chi

for filename in filename_dict:
    if filename_dict[filename]:
        continue  # skip, already done

    # TODO option to flip payload_file / expected_canon
    if filename .endswith(PLAINTEXT_PREFIX):
        expected_canon = filename
        filename_basename = filename[:-len(PLAINTEXT_PREFIX)]
        payload_file = filename_basename + CRYPTTEXT_PREFIX
    else:
        payload_file = filename
        filename_basename = filename[:-len(CRYPTTEXT_PREFIX)]
        expected_canon = filename_basename + PLAINTEXT_PREFIX
    filename_dict[filename] = True

    temp_dict = {
        "comment": "FIXME",
        "passphrase": "password",
        "expect": "success",
        "payload_file": payload_file,
        "expected_canon": expected_canon,
    }
    print('%s %s' % (payload_file, expected_canon))
    print('%s.json' % (filename_basename,))
    #print('')
    print('%s' % (json.dumps(temp_dict, indent=4),))
    print('\n\n')
