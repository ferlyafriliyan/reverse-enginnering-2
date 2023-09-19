#!/usr/bin/env python
# coding: utf-8
# Developed By : Ferly Afriliyan
import os, sys, datetime, random, platform
import marshal, zlib, binascii
import gzip, bz2, lzma

mlgb_bz = f"""
            ╔╦╗┬  ┌─┐┌┐     ╔╗ ┌─┐
            ║║║│  │ ┬├┴┐    ╠╩╗┌─┘
            ╩ ╩┴─┘└─┘└─┘────╚═╝└─┘
            [ Marszhal Lzma Gzip Bz2 Binascii Zlib]
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
    print(prett("======[+] Try-Lzma Python File Encryptor [+]======\n"))

    input_file = input("\t[•] Masukan Nama File Input : ")

    # Periksa ekstensi file
    if not input_file.endswith('.py'):
        print("[•] File harus memiliki ekstensi .py")
        exit()

    # Periksa apakah file ada
    if not os.path.exists(input_file):
        print("[•] File tidak ditemukan")
        exit()

    output_file = input("\t[•] Masukkan Nama File Output : ")

    # Periksa ekstensi output file
    if not output_file.endswith('.py'):
        print("[•] Output file harus memiliki ekstensi .py")
        exit()

    complexity = int(input("\t[•] For Loop, (ex : 100): "))

    if complexity > 100:
        print("[•] Batas For Loop Hanya 100")
        exit()

    # Generate variabel __try__ dengan teks acak
    try_text = ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?") for _ in range(random.randint(150, 4065)))

    print("\n" + prett("[+] Encrypting... [+]\n"))

    with open(input_file, 'r') as file:
        source_code = file.read()

    with open(output_file, 'w') as f:
        f.write(
            f''
            f'# Time : {current_time_str}\n'
            f'# Platform : {platform.system()}-{platform.machine()}\n'
            f'# Obfuscated by : N00B-3NC0DE3 ( Ferly Afriliyan )\n\n'
            f'# Variable teks : {num_iterations} Line\n\n'
        )
        for _ in range(num_iterations):
            f.write(try_variable_[0] + '\n')
        f.write('\n')
        f.write(f'try:\n\t{encode(source_code)}\nexcept KeyboardInterrupt:\n\texit()\n\n')
        for _ in range(num_iterations):
            f.write(__try__variable__two[0] + '\n')

    print("\n[+] Berhasil.. File hasil Encrypt tersimpan Di :", output_file)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
