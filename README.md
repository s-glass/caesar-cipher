# Lab - Class 18
## Project: caesar-cipher

Author: Sarah Glass for Python 401

Collaborated with Logan Reece and Anthony Sinitsa on the code.

## Overview

Devise:
(1) a method to encrypt a message that can then be decrypted when supplied with the corresponding key AND
(2) a way to decipher the encrypted message event when you do NOT have the key!

Create an `encrypt` function that takes in a plain text phrase and a numeric shift.
  - the phrase will then be `shifted` that many letters.
  - E.g. encrypt(‘abc’,1) would return ‘bcd’. = E.g. encrypt(‘abc’, 10) would return ‘klm’.
  - shifts that exceed 26 should wrap around.
  - E.g. encrypt(‘abc’,27) would return ‘bcd’.
  - shifts that push a letter out or range should wrap around.
  - E.g. encrypt(‘zzz’,1) would return ‘aaa’.

Create a `decrypt` function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

Create a `crack` function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.

Devise a method for the computer to determine if code was broken with minimal human guidance.

## Links and Resources

* TA and peer help.
* Google searches around "ord"
* Unicode Values for the ASCII Character Set: https://docs.hexagonppm.com/r/en-US/Full-Text-Retrieval-FTR-Help/Version-2012-R1-SP5-3.6.6/97693 


## Setup

No .env requirements; gitignore invludes venv.

## How to initialize/run your application

* python3 caesar_cipher.cipher
* pytest tests/test_caesar.py

## How to use your library

* nltk as a toolkit for the corpus of English words

* one line of regex in the `count_words` function

## Tests

Tests all passing.