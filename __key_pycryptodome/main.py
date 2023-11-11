from Crypto.Cipher import AES
import zlib, base64, lzma, codecs, binascii
import os, sys
from marshal import dumps as md  # marshal.dumps

# Clear Terminal
def clear():
    if 'linux' in sys.platform.lower():os.system('clear')
    elif 'win' in sys.platform.lower():os.system('cls') # clear()

# Metode Obfuscate
def encrypt_text(text, method, use_marshal=True):
    if method == 'lzma':
        encrypted = lzma.compress(text.encode())
        if use_marshal:
            encrypted = md(encrypted)
    elif method == 'zlib':
        encrypted = base64.b85encode(zlib.compress(base64.b16encode(lzma.compress(text.encode()))))
        if use_marshal:
            encrypted = md(encrypted)
    elif method == 'base64':
        encrypted = base64.b85encode(zlib.compress(lzma.compress(base64.b32hexencode(binascii.a2b_base64(text.encode()))))).decode()
        if use_marshal:
            encrypted = md(encrypted)
    elif method == 'b64_lzma':
        encrypted = base64.b85encode(lzma.compress(base64.b32encode(zlib.compress(base64.b16encode(text.encode()))))).decode()
        if use_marshal:
            encrypted = md(encrypted)
    elif method == 'marshal':
        encrypted = md(compile(text, '', 'exec'))
    elif method == 'pycryptodome':
        encrypted_key = b'kontolivo jembut'
        cipher = AES.new(encrypted_key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(text.encode())
        encrypted = (nonce, ciphertext, tag)
    elif method == 'binascii.a2b_base64':
        encrypted = binascii.a2b_base64(text.encode())
    else:
        return text  # Tidak ada enkripsi, kembalikan teks asli

    return encrypted

clear()
# Input file
input_file = input("Input file : ")

# Open file Input
with open(input_file, 'r') as file:
    source_code = file.read()

# Variable Obfuscate
__key = encrypt_text(source_code, 'lzma', use_marshal=False)
__pubkey = encrypt_text(source_code, 'zlib')
_obfuscate_ = encrypt_text(source_code, 'base64')
__pyobfuscate__ = encrypt_text(source_code, 'b64_lzma')
_pycryptodome = encrypt_text(source_code, 'pycryptodome')
__marshal__ = encrypt_text(source_code, 'marshal')

# Output file
output_file = input("Output file : ")
with open(output_file, 'w') as file:
    file.write(f'\x23\x20\x41\x75\x74\x68\x6f\x72\x20\x3a\x20\x46\x65\x72\x6c\x79\x20\x41\x66\x72\x69\x6c\x69\x79\x61\x6e\x0a\x20\x20\x23\x20\x68\x74\x74\x70\x73\x3a\x2f\x2f\x66\x65\x72\x6c\x79\x61\x66\x72\x69\x6c\x69\x79\x61\x6e\x2e\x76\x65\x72\x63\x65\x6c\x2e\x61\x70\x70\x2f\x0a\x20\x20\x20\x20\x23\x20\x4f\x62\x66\x75\x73\x63\x61\x74\x65\x20\x77\x69\x74\x68\x20\x5f\x5f\x6b\x65\x79\n')
    file.write(f'__key = {repr(__key)}\n')
    file.write(f'__pubkey = {repr(__pubkey)}\n')
    file.write(f'_obfuscate_ = {repr(_obfuscate_)}\n')
    file.write(f'__pyobfuscate__ = {repr(__pyobfuscate__)}\n')
    file.write(f'_pycryptodome = {repr(_pycryptodome)}\n')
    file.write(f'__marshal__ = {repr(__marshal__)};')

    # Simpan metode enkripsi dengan marshal di bawah variabel
    file.write('\x69\x6d\x70\x6f\x72\x74\x20\x6d\x61\x72\x73\x68\x61\x6c')
    file.write(f';')
    file.write(f'encrypted_source = ({__marshal__});')
    file.write(f'exec(marshal.loads(encrypted_source))\ntry:\n\timport os, sys\nexcept (KeyboardInterrupt, Exception) as e:\n\tclear()\n\n')

print("\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x2c\x20\x6f\x62\x66\x75\x73\x63\x61\x74\x65\x20\x66\x69\x6c\x65\x20\x73\x61\x76\x65\x64\x20\x69\x6e", ("\x6f\x75\x74\x70\x75\x74\x5f\x66\x69\x6c\x65"))
try:
	import os, sys
except (KeyboardInterrupt, Exception) as e:
	clear()
