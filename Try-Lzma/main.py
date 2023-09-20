#!/usr/bin/env python
# coding: utf-8
# Developed By : Ferly Afriliyan
import os, sys, datetime, random, platform
import marshal, zlib, binascii
import gzip, bz2, lzma
import time  # Import modul time

# Impory modul rich
from rich import print

# Warna Text
Hitam = "\u001b[30m"
Merah = "\u001b[31m"
Hijau = "\u001b[32m"
Kuning = "\u001b[33m"
Orange = "\u001b[38;5;208m"
Biru = "\u001b[34m"
Biru_muda = "\u001b[36m"
Pink = "\u001b[38;5;205m"
Violet = "\u001b[35m"
Abu = "\u001b[90m"
Orange_muda = "\u001b[38;5;214m"
Putih = "\u001b[37m"

# Kode warna ANSI
Z2 = "[#000000]"  # Hitam
M2 = "[#FF0000]"  # Merah
H2 = "[#00FF00]"  # Hijau
K2 = "[#FFFF00]"  # Kuning
B2 = "[#00C8FF]"  # Biru
U2 = "[#AF00FF]"  # Ungu
N2 = "[#FF00FF]"  # Pink
O2 = "[#00FFFF]"  # Biru Muda
P2 = "[#FFFFFF]"  # Putih
J2 = "[#FF8F00]"  # Jingga
A2 = "[#AAAAAA]"  # Abu-Abu
T2 = "[#FFA500]"  # Oranye
V2 = "[#800080]"  # Violet

mlgb_bz = f"""
            {T2}╔╦╗┬  ┌─┐┌┐     ╔╗ ┌─┐
            {J2}║║║│  │ ┬├┴┐    ╠╩╗┌─┘
            {U2}╩ ╩┴─┘└─┘└─┘────╚═╝└─┘
    {H2}[ {P2}Marszhal Lzma Gzip Bz2 Binascii Zlib {H2}]
"""

num_iterations = random.randint(150, 6105)
try_variable_ = [f'''
__N00B_3NC0DE3 = "https://ferlyafriliyan.vercel.app"
__D3v_N00B = "https://github.com/N00B-3NC0DE3"
["from", "import", "as", "marshal", ".loads", "base64", ".b64decode", ".b64encode", "zlib", ".decompress", "lzma", "gzip", "bz2", "exec("]
''']

__try__variable__two = [f'''
__FA4__XCODE = "https://www.facebook.com/freya.xyz"
__XCODE__XD = "https://github.com/ferlyafriliyan"
["import","as","from","marshal",".loads","base64","zlib","b64decode","b64encode","decompress","exec(",]
''']

current_time = datetime.datetime.now()
current_time_str = current_time.strftime("%A, %B %d, %Y %H:%M:%S")

def prett(text):
    return text.title().center(os.get_terminal_size().columns)

def encode(source: str) -> str:
    selected_mode = random.choice((lzma, gzip, bz2, binascii, zlib))
    marshal_encoded = marshal.dumps(compile(source, "__N00B-3NC0DE3", "exec"))
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
    print(prett(f"\t{M2}•{K2}•{H2}• {P2}Try-Lzma Python File Encryptor {H2}•{K2}•{M2}•\n"))

    input_file = input(f"└──>{Hijau}[{Abu}•{Hijau}] {Putih}Masukan Nama File Input : ")

    # Periksa ekstensi file
    if not input_file.endswith('.py'):
        print(f"{B2}[{A2}•{B2}] {P2}File harus memiliki ekstensi {K2}.py")
        exit()

    # Periksa apakah file ada
    if not os.path.exists(input_file):
        print(f"{V2}[{A2}•{V2}] {P2}File tidak ditemukan")
        exit()

    output_file = input(f"\t{Hijau}[{Abu}•{Hijau}] {Putih} Masukkan Nama File Output : ")

    # Periksa ekstensi output file
    if not output_file.endswith('.py'):
        print(f"{V2}[{A2}•{V2}] {P2}Output file harus memiliki ekstensi {K2}.py")
        exit()

    complexity = int(input(f"     └──>{Hijau}[{Abu}•{Hijau}] {Putih} For Loop, (ex : 100): "))

    if complexity > 100:
        print(f"{V2}[{A2}•{V2}] {P2}Batas For Loop Hanya {K2}100")
        exit()

    # Generate variabel __try__ dengan teks acak
    try_text = ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?") for _ in range(random.randint(150, 4065)))

    # Animasi loading
    total_iterations = num_iterations
    current_iteration = 0
    while current_iteration <= total_iterations:
        loading_percentage = (current_iteration / total_iterations) * 100
        print(f"{T2}[{J2}+{V2}] {P2}Encrypting: [{loading_percentage:.2f}%]", end='\r')
        time.sleep(0.1)  # Perubahan kecepatan animasi
        current_iteration += 1

    print(f"\n{H2}[{B2}!!{H2}] {P2}Berhasil.. File hasil Encrypt tersimpan Di : {K2}", output_file)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
