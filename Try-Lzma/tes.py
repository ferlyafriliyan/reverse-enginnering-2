#!/usr/bin/env python
# coding: utf-8
# By Sandaru Ashen: https://github.com/Sl-Sanda-Ru, https://t.me/Sl_Sanda_Ru

import os
import sys
import random
import time
import marshal
import lzma
import gzip
import bz2
import binascii
import zlib

def prett(text):
    return text.title().center(os.get_terminal_size().columns)

def encode(source: str) -> str:
    selected_mode = random.choice((lzma, gzip, bz2, binascii, zlib))
    marshal_encoded = marshal.dumps(compile(source, "Py-Fuscate", "exec"))
    if selected_mode is binascii:
        return "import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(binascii.a2b_base64({})))".format(
            binascii.b2a_base64(marshal_encoded)
        )
    return "import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads({}.decompress({})))".format(
        selected_mode.__name__, selected_mode.compress(marshal_encoded)
    )

def main():
    print("\n" + prett("[+] Py-Fuscate Python File Encryptor [+]\n"))

    input_file = input(prett("Enter the input Python file name (tes.py): "))
    output_file = input(prett("Enter the output Python file name (tes_enc.py): "))
    complexity = int(input(prett("Enter the complexity of obfuscation (ex : 100): ")))

    print("\n" + prett("[+] Encrypting... [+]\n"))

    with open(input_file, 'r') as file:
        source_code = file.read()

    with open(output_file, 'w') as file:
        for _ in range(complexity):
            source_code = encode(source_code)
            time.sleep(0.1)
        file.write(
            f'# Encoded By Try-Lzma\n# Make Sure You\'re Running The Program With Python {sys.version_info[0]}.{sys.version_info[1]} Otherwise It May Crash\n# To Check Your Python Version Run "python -V" Command\ntry:\n\t{source_code}\nexcept KeyboardInterrupt:\n\texit()'
        )

    print("\n" + prett("[+] Encryption completed! Output saved as ") + output_file + prett(" [+]\n"))

if __name__ == "__main__":
    main()
