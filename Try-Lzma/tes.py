#!/usr/bin/env python
# coding: utf-8
# Developed By : Ferly Afriliyan
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

mlgb_bz = f"""
            ╔╦╗┬  ┌─┐┌┐     ╔╗ ┌─┐
            ║║║│  │ ┬├┴┐    ╠╩╗┌─┘
            ╩ ╩┴─┘└─┘└─┘────╚═╝└─┘
            [ Marszhal Lzma Gzip Bz2 Binascii Zlib]
"""

def prett(text):
    return text.title().center(os.get_terminal_size().columns)

def encode(source: str) -> str:
    selected_mode = random.choice((lzma, gzip, bz2, binascii, zlib))
    marshal_encoded = marshal.dumps(compile(source, "Py-Fuscate", "exec"))
    if selected_mode is binascii:
        return "import marshal, lzma, gzip, bz2, binascii, zlib;exec(marshal.loads(binascii.a2b_base64({})))".format(
            binascii.b2a_base64(marshal_encoded)
        )
    return "import marshal, lzma, gzip, bz2, binascii, zlib;exec(marshal.loads({}.decompress({})))".format(
        selected_mode.__name__, selected_mode.compress(marshal_encoded)
    )

def main():
    os.system("clear")
    print(mlgb_bz)
    print("\n" + prett("[+] Try-Lzma Python File Encryptor [+]\n"))

    input_file = input("\t\tMasukan Nama File Input, Contoh : 'tes.py' : ")

    # Periksa ekstensi file
    if not input_file.endswith('.py'):
        print("[•] File harus memiliki ekstensi .py")
        exit()

    # Periksa apakah file ada
    if not os.path.exists(input_file):
        print("[•] File tidak ditemukan")
        exit()

    output_file = input("\t\tMasukkan Nama File Output, Contoh : 'tes_enc.py' : ")

    # Periksa ekstensi output file
    if not output_file.endswith('.py'):
        print("[•] Output file harus memiliki ekstensi .py")
        exit()

    complexity = int(input("\t\tFor Loop, Batasan : '100' (ex : 100): "))

    if complexity > 100:
        print("[•] Batas For Loop Hanya 100")
        exit()

    print("\n" + prett("[+] Encrypting... [+]\n"))

    with open(input_file, 'r') as file:
        source_code = file.read()

    with open(output_file, 'w') as file:
        for _ in range(complexity):
            source_code = encode(source_code)
            time.sleep(0.1)
        file.write(
            f'# Encoded By : Ferly Afriliyan\n# Script ini Sudah Dimodifikasi agar lebih Simpel untuk Digunakan# To Check Your Python Version Run "python -V" Command\ntry:\n\t{source_code}\nexcept KeyboardInterrupt:\n\texit()'
        )

    print("\n[+] Berhasil.. File hasil Encrypt tersimpan Di :", output_file)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
