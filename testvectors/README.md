# Tombo test files

  * Some files are generated/encrypted with original Tombo win32 desktop application
      * Some from TomboCrypt win32 cli tool
      * Some from chi_crypt win32 cli tool
  * Unencrypted Plaintext files are mostly Windows newlines, rather than Unix and need .gitattribute binary mappings to preserve file contents

Use:

    py gen_json.py *txt *chi *chs

To generate copy/pasteable json files.

## Test file overviews

Some extracted from https://github.com/clach04/puren_tonbo/tree/main/puren_tonbo/tests/data

  * aesop.plaintext - plain text version of shortest Aesop fable there is,
    so suitable for realistic test data.
      * has window (CR+LF) newlines
      * us-ascii encoding
      * Contains long lines (one is 1435 bytes)
      * Approx 1.5Kb.

  * aesop.chi -  Tombo Blowfish encrypted from `aesop.plaintext`
    Created with Windows win32 Tombo http://tombo.sourceforge.jp/En/
      * password is `password`
      * Approx 1.5Kb.

  * pg28_the_fables_of_aesop_utf8.plaintext - plain text file, utf-8 multi byte encoding
      * Approx 100Kb.
      * utf-8 encoding
      * From https://www.gutenberg.org/ebooks/28 - larger than 64Kb, yet not too big
      * NOTE includes BOM at start of file
      * compatabilty notes
        * Tombo 1.17 - Windows
          * will load BUT will display question mark for the BOM that is present (even when utf-8 is the encoding option)
          * will save cleanly - not sure how with 30Kb limits seen when copy/pasting
        * Tombo 2.0 beta 5 - Windows
          * will load BUT will display question mark for the BOM that is present (even when utf-8 is the encoding option)
          * will save cleanly
        * Kumagusu 1.21 - Android
          * will load, no BOM issues

  * pg28_the_fables_of_aesop_utf8.chi - Tombo Blowfish encrypted from `pg28_the_fables_of_aesop_utf8.plaintext`
      * Approx 100Kb.
      * has Unix (LF) newlines
      * utf-8 encoding
      * NOTE includes BOM at start of file
      * Created with `TomboCrypt.exe enc pg28_the_fables_of_aesop_utf8.chi password<pg28_the_fables_of_aesop_utf8.plaintext` from Tombo https://github.com/clach04/tombo
      * compatabilty notes
        * Tombo 1.17 - Windows
          * similar to the text file will load BUT will display question mark for the BOM that is present (even when utf-8 is the encoding option)
          * new lines missing, not a problem with text file (or Tombo 2.0 beta 5)
        * Tombo 2.0 beta 5 - Windows
          * will load BUT will display question mark for the BOM that is present (even when utf-8 is the encoding option)
          * no new line issues, that 1.17 has
          * will save cleanly
        * Kumagusu 1.21 - Android
          * will load, no BOM issues
          * will save cleanly

  * pg28_the_fables_of_aesop_utf8_salted00.chi - Tombo Blowfish encrypted from `pg28_the_fables_of_aesop_utf8.plaintext`
      * Similar to pg28_the_fables_of_aesop_utf8.chi, except this was encrypted using `chi_crypt_salted` using salt of all zeros, `--salt 0000000000000000`
      * This should be decryptable by any Tombo compatible tool, BUT not all Tombo compatible tools will be able to generate this exact file, reasons for failure to match:
          * no salt support - the obvious reason
          * difference in behavior for how the (essentially unused) padding at the end is handled - chi_io/ptcipher do some but twiddling (also don't have salt support, but that is easier to hack in)
