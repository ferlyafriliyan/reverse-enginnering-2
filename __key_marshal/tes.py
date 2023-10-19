import zlib
import codecs
import base64
import gzip
import marshal
import os
import sys

# Clear Terminal
def clear():
    if 'linux' in sys.platform.lower():os.system('clear')
    elif 'win' in sys.platform.lower():os.system('cls')
      
# Metode Obfuscate
def encrypt_text(text, method):
    if method == 'codecs':
        return codecs.encode(text, 'rot_13')
    elif method == 'zlib':
        return zlib.compress(text.encode())
    elif method == 'base64':
        return base64.b64encode(text.encode()).decode()
    elif method == 'gzip':
        return base64.b64encode(gzip.compress(text.encode())).decode()
    elif method == 'marshal':
        return marshal.dumps(compile(text, '', 'exec'))
    else:
        return text  # Tidak ada enkripsi, kembalikan teks asli
clear()
# Input file
input_file = input("Masukkan nama file sumber Python yang ingin dienkripsi: ")

# Open file Input
with open(input_file, 'r') as file:
    source_code = file.read()

# Variable Obfuscate
__key = encrypt_text(source_code, 'codecs')
__pubkey = encrypt_text(source_code, 'zlib')
_obfuscate_ = encrypt_text(source_code, 'base64')
__pyobfuscate__ = encrypt_text(source_code, 'gzip')
__marshal__ = encrypt_text(source_code, 'marshal')

# Output file
output_file = input("Masukkan nama file output untuk kode yang dienkripsi: ")
with open(output_file, 'w') as file:
    file.write(f'__key = {repr(__key)}\n')
    file.write(f'__pubkey = {repr(__pubkey)}\n')
    file.write(f'_obfuscate_ = {repr(_obfuscate_)}\n')
    file.write(f'__pyobfuscate__ = {repr(__pyobfuscate__)}\n')

    # Simpan metode enkripsi dengan marshal di bawah variabel
    file.write('\n\x69\x6d\x70\x6f\x72\x74\x20\x6d\x61\x72\x73\x68\x61\x6c')
    file.write(f'\n')
    file.write(f'encrypted_source = {repr(__marshal__)}\n')
    file.write(f'exec(marshal.loads((encrypted_source)))\n')

print("File yang telah dienkripsi telah disimpan dalam", output_file)
try:
  import os, sys
except:
  clear()
