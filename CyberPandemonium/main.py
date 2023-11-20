from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import marshal
import zlib
import random
import os
import sys

# Clear Terminal
def clear_terminal():
    if 'linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')

def display_logo():
    print("""
    CyberPandemonium
""")

k = '\033[1;33m'  # Warna Kuning
a = '\033[1;30m'  # Warna Hitam/Abu-Abu
m = '\033[1;31m'  # Warna Merah
h = '\033[1;32m'  # Warna Hijau
p = '\033[1;37m'  # Warna Putih
b = '\033[1;34m'  # Warna Biru
v = '\033[1;35m'  # Warna Violet
u = '\033[1;36m'  # Warna Ungu
j = '\033[1;38;5;202m'  # Warna Jingga

# Minta input dari pengguna
def main():
    input_filename = input(f"{h}[{a}•{h}] {p}Masukkan nama file Input {a}: {p}")
    if not input_filename:
        print(f"{m}[{a}!{m}] {p}File '{input_file}' tidak ditemukan.")
        exit()
    elif not input_filename.endswith(".py"):
        print(f"{m}[{a}!{m}] {p}File harus memiliki ekstensi .py {p}")
        exit()

    output_filename = input(f"{h}[{a}•{h}] {p}Masukkan nama file Output {a}: {p}")
    if not output_filename:
        print(f"{m}[{a}!{m}] {p}Isi dengan benar {m}! {p}")
        exit()
    elif not output_filename.endswith(".py"):
        print(f"{m}[{a}!{m}] {p}File output harus memiliki ekstensi .py {p}")
        exit()

    with open(input_filename, encoding="utf-8") as file:
        original_code = file.read()
        obf = marshal.dumps(compile(original_code, "", "exec"))

    obfuscated_code = base64.b64encode(base64.b32encode(zlib.compress(obf)))[::-1]

    base64_encoded = base64.b64encode(obfuscated_code)
    base64x2_encoded = base64.b64encode(base64_encoded)
    base32_encoded = base64.b32encode(base64x2_encoded)
    base64x3_encoded = base64.b64encode(base32_encoded)

    random_number = random.randint(10, 500)
    random_number2 = random.randint(10, 500)
    random_number3 = random.randint(10, 500)
    random_number4 = random.randint(10, 500)
    random_number5 = random.randint(10, 500)

    aes_key = get_random_bytes(32)
    iv = get_random_bytes(16)

    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(base64x3_encoded, AES.block_size))

    hex_aes_key = aes_key.hex()
    hex_iv = iv.hex()

    obfuscated_stub = f"""__author__ = 'Ferly Afriliyan'
__madeBy__ = 'CyberPandemonium '
__git__ = 'https://github.com/ferlyafriliyan'

# Obfuscated with CyberPandemonium

try:
    import base64 as ______;import marshal as ____;import zlib as __________;from Crypto.Cipher import AES;from Crypto.Util.Padding import pad, unpad;from Crypto.Random import get_random_bytes;import base64;__vare__ = lambda x: ____.loads(__________.decompress(______.b32decode(______.b64decode(x[::-1]))));__mycip__= AES.new(bytes.fromhex("{hex_aes_key}"), AES.MODE_CBC, bytes.fromhex("{hex_iv}"));__step1__=bytes.fromhex("{encrypted_data.hex()}");__step2__=__mycip__.decrypt(__step1__);__decr__=base64.b64decode(__step2__);__decrdata__=__decr__;__gotnew__=base64.b32decode(__decr__);__newdecr__={random.randint(999999,999999999999)};__getnew__=__newdecr__;__myb64code__=base64.b64decode(__gotnew__);__myb64codee__=base64.b64decode(__myb64code__);___ = __myb64codee__;exec(__vare__(___))
except (KeyboardInterrupt, Exception) as e:
    from os import system
    __import__('os').system('xdg-open https://facebook.com/freya.xyz')
    exit(f"[Error] {{str(e).capitalize()}}!")"""

    with open(output_filename, "w", encoding="utf-8", errors="ignore") as file:
        file.write(obfuscated_stub)

def display_banner():
    clear_terminal()
    display_logo()

if __name__ == '__main__':
    display_banner()
    try:
        main()
    except (KeyboardInterrupt, Exception) as e:
        exit(f"[Error] {str(e).capitalize()}!")
