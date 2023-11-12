from Crypto.Cipher import AES
import zlib, base64, lzma, binascii
import os, sys
from marshal import dumps as md
import marshal
import base64

# Clear Terminal
def clear():
    if 'linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')  # clear()

def Alt(text: str, evalCode: bool = True) -> str:
    formated = '+'.join(f'chr({char})' for char in [ord(char_) for char_ in text])
    return f'eval(eval({formated!r}))' if evalCode else f'eval({formated!r})'

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

# Input file
clear()
input_file = input("Input file : ")

# Open file Input
with open(input_file, 'r') as file:
    source_code = file.read()

code__ = marshal.dumps(compile(source_code, '', 'exec'))
code__ = base64.b16encode(code__).decode()
code__ = base64.b32encode(code__.encode()).decode()
code__ = base64.b64encode(code__.encode()).decode()
code__ = base64.b85encode(code__.encode()).decode()

# Variable Obfuscate
__key = encrypt_text(source_code, 'lzma', use_marshal=False)
__pubkey = encrypt_text(source_code, 'zlib')
_obfuscate_ = encrypt_text(source_code, 'base64')
__pyobfuscate__ = encrypt_text(source_code, 'b64_lzma')
_pycryptodome = encrypt_text(source_code, 'pycryptodome')
__marshal__ = encrypt_text(source_code, 'marshal')

infos_ = f"""# Author : Ferly Afriliyan
  # https://ferlyafriliyan.vercel.app/
    # Obfuscate with __key
"""

# Variable Obfuscate
EncryptVar = f"""
import os, sys
import time

class Apocalipthic():
    def __init__(self, md_code, base64_import, globals, alt_code):
        self.md_code = md_code
        self.base64_import = base64_import
        self.globals = globals
        self.alt_code = alt_code

    def _key(self):
        print("Hello world from _key!")
        if __name__ == '__main__':
            try:
                {__key},
                {_obfuscate_}
            except (KeyboardInterrupt, Exception) as e:
                exit(print(f"[Error] {{str(e).capitalize()}}!"))

    def obfuscate(self):
        print("Hello world from obfuscate!")
        time.sleep(1)
        if __name__ == '__main__':
            try:
                {__marshal__}
            except (KeyboardInterrupt, Exception) as e:
                exit(print(f"[Error] {{str(e).capitalize()}}!"))

    def _pubkey(self):
        print("Hello world from _pubkey!")
        if __name__ == '__main__':
            try:
                {__pubkey},
                {__pyobfuscate__}
            except (KeyboardInterrupt, Exception) as e:
                exit(print(f"[Error] {{str(e).capitalize()}}!"))
"""

code_ = f"""
{infos_}
{EncryptVar}
if __name__ == '__main__':
    try:
        Apocalipthic({code__!r},
        {Alt('__import__("base64")')}, globals(),
        {base64.b16encode(marshal.dumps(Alt.__code__))!r}
        ).obfuscate()
    except (KeyboardInterrupt, Exception) as e:
        exit(f"[Error] {{str(e).capitalize()}}!")
# Lu Kontool
"""

end_ = f"""
try:
    if "linux" in sys.platform.lower(): os.system('clear')
    elif "win" in sys.platform.lower(): os.system('cls')
except (KeyboardInterrupt, Exception) as e:
    clear()
"""

# Output file
output_file = input("Output file : ")
with open(output_file, 'w') as file:
    file.write(f'{code_}')
    file.write(f'_pycryptodome = {repr(_pycryptodome)};')

    # Simpan metode enkripsi dengan marshal di bawah variabel
    file.write('\x69\x6d\x70\x6f\x72\x74\x20\x6d\x61\x72\x73\x68\x61\x6c')
    file.write(f';')
    file.write(f'encrypted_source = ({__marshal__});')
    file.write(f'exec(marshal.loads(encrypted_source))')
    file.write(f'{end_}')

print("\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x2c\x20\x6f\x62\x66\x75\x73\x63\x61\x74\x65\x20\x66\x69\x6c\x65\x20\x73\x61\x76\x65\x64\x20\x69\x6e", ("\x6f\x75\x74\x70\x75\x74\x5f\x66\x69\x6c\x65"))
if __name__ == '__main__':
    try:
        import os, sys
    except (KeyboardInterrupt, Exception) as e:
        exit(f"[Error] {{str(e).capitalize()}}!")
