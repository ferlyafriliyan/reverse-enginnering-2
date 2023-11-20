from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from urllib.parse import quote
import base64
import marshal
import zlib
import random
import os
import sys

# Clear Terminal
def clear():
    if 'linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')

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
    input_file = input(f"{h}[{a}•{h}] {p}Masukkan nama file Input {a}: {p}")
    if not input_file:
        print(f"{m}[{a}!{m}] {p}File '{input_file}' tidak ditemukan.")
        exit()
    elif not input_file.endswith(".py"):
        print(f"{m}[{a}!{m}] {p}File harus memiliki ekstensi .py {p}")
        exit()

    output_file = input(f"{h}[{a}•{h}] {p}Masukkan nama file Output {a}: {p}")
    if not output_file:
        print(f"{m}[{a}!{m}] {p}Isi dengan benar {m}! {p}")
        exit()
    elif not output_file.endswith(".py"):
        print(f"{m}[{a}!{m}] {p}File output harus memiliki ekstensi .py {p}")
        exit()

    with open(input_file, encoding="utf-8") as file:
        data = file.read()

    original_code = data

    obfuscated = base64.b64encode(base64.b32encode(zlib.compress(marshal.dumps(compile(original_code, "", "exec")))))[::-1]

    gotobase64 = base64.b64encode(obfuscated)

    gotobase64x2 = base64.b64encode(gotobase64)

    gotobase32 = base64.b32encode(gotobase64x2)

    gotobase64x3 = base64.b64encode(gotobase32)

    randomnum = random.randint(10, 500)

    randomnum2 = random.randint(10, 500)

    randomnum3 = random.randint(10, 500)

    randomnum4 = random.randint(10, 500)

    randomnum5 = random.randint(10, 500)

    # Generate AES key and initialization vector (IV)
    aes_key = get_random_bytes(32)
    iv = get_random_bytes(16)

    # Encrypt the base64-encoded data with AES
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(gotobase64x3, AES.block_size))

    # Convert AES key and IV to hex strings
    hex_aes_key = aes_key.hex()
    hex_iv = iv.hex()

    stub = f"""try:
    import base64 as ______;import marshal as ____;import zlib as __________;from Crypto.Cipher import AES;from Crypto.Util.Padding import pad, unpad;from Crypto.Random import get_random_bytes;import base64;__vare__ = lambda x: ____.loads(__________.decompress(______.b32decode(______.b64decode(x[::-1]))));__mycip__= AES.new(bytes.fromhex("{hex_aes_key}"), AES.MODE_CBC, bytes.fromhex("{hex_iv}"));__step1__=bytes.fromhex("{encrypted_data.hex()}");__step2__=__mycip__.decrypt(__step1__);__decr__=base64.b64decode(__step2__);__decrdata__=__decr__;__gotnew__=base64.b32decode(__decr__);__newdecr__={random.randint(999999,999999999999)};__getnew__=__newdecr__;__myb64code__=base64.b64decode(__gotnew__);__myb64codee__=base64.b64decode(__myb64code__);___ = __myb64codee__;exec(__vare__(___))
except (KeyboardInterrupt, Exception) as e:
    from os import system
    __import__('os').system('xdg-open https://facebook.com/freya.xyz')
    exit(f"[Error] {{str(e).capitalize()}}!")"""

    with open(output_file, "w", encoding="utf-8", errors="ignore") as file:
        file.write(stub)

if __name__ == '__main__':
    clear()
    try:
        main()
    except (KeyboardInterrupt, Exception) as e:
        exit(f"[Error] {str(e).capitalize()}!")
