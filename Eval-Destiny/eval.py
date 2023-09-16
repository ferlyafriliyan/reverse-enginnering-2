import os
import base64
import codecs
import platform
import time
import py_compile
import marshal
import zlib
import datetime
from sys import argv
from rich import print

# Definisi warna teks ANSI
Hitam = "\x1b[0;90m"     # Hitam
Merah = "\x1b[38;5;196m" # Merah
Hijau = "\x1b[38;5;46m"  # Hijau
Kuning = "\x1b[38;5;226m" # Kuning
Biru = "\x1b[38;5;44m"  # Biru
Ungu = "\x1b[0;95m"     # Ungu
Putih = "\x1b[38;5;231m" # Putih
Jingga = "\x1b[38;5;208m" # Jingga
Abu = "\x1b[38;5;248m" # Abu-Abu

# Definisi warna teks Rich
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

def encrypt_and_save_code(source_code, output_file):
    encrypt = lambda data: base64.b64encode(zlib.compress(marshal.dumps(compile(data, "", "exec")))).decode("utf-8")
    
    encrypted_code = encrypt(source_code)
    current_time = datetime.datetime.now()
    
    with open(output_file, "w") as f:
        f.write(f'__Author__ = "Ferly Afriliyan"\n__MadeBy__ = "[ MZB_OBF ( Marshal Zlib Base64 ) ]"\n__Github__ = "https://github.com/ferlyafriliyan"\n\n')
        f.write(f"# One of the best Python3.11 obfuscators.\n\n")
        f.write(f"# Di Buat Pada Tanggal : 15-8-2023\n\nimport base64, zlib, marshal\n")
        f.write(f"uncompile6__=(marshal.loads(zlib.decompress(base64.b64decode(z'{encrypted_code}'))));exec(uncompile6__)")

    print(f"{H2}[ {A2}• {H2}] Berhasil Obfuscated File - Hasil Encrypt : {output_file}")

def custom_encrypt(input_file, output_file):
    note = f'# Coded by : Ferly Afriliyan\n# Do not share Original Files\n'   \
           

    try:
        with open(input_file, 'r') as f:
            original_code = f.read()
    except IOError:
        os.sys.exit('[!] File Not Found [!]')

    fer4 = output_file
    ntaa = base64.b64encode(original_code.encode()).decode()

    h1 = []
    h2 = []
    h3 = []
    h4 = ''

    for x in ntaa:
        h1.append(ord(x))

    z = 0
    while True:
        h2.append(h1[z])
        if z >= len(h1) // 2:
            break
        z += 1

    v = len(h1) // 2 + 1
    try:
        while True:
            h3.append(h1[v])
            v += 1
    except IndexError:
        pass

    for s in h3:
        h4 += chr(s)

    nta_xe = codecs.encode(h4, 'rot_13')

    obf_note = note + "trust = '" + str(nta_xe) + "'\t\t\n"

    h6 = open(fer4, 'w')
    h6.write(obf_note + '\nimport codecs, base64\n' + 'magic = ' + str(h2) + '\t\t\n' + "love = '" + str(nta_xe) + "'\t\t\n")
    h6.write("god = '\\x72\\x6f\\x74\\x5f\\x31\\x33'\t\t\n")
    h6.write("destiny = codecs.decode(eval('\\x6c\\x6f\\x76\\x65'), eval('\\x67\\x6f\\x64'))\t\t\n")
    h6.write("joy = base64.b64decode(''.join([chr(ferz) for ferz in magic])+eval('\\x64\\x65\\x73\\x74\\x69\\x6e\\x79'))\t\t\n")
    h6.write("eval(compile(eval('\\x6a\\x6f\\x79'),'<string>','exec'))\t\t\n")
    h6.close()

    # Compile the encrypted file
    py_compile.compile(fer4)

    print('[-] Successfully Encrypted and Compiled ' + fer4)

if __name__ == '__main__':
    os.system('clear')

    print(f"""
{B2}╔═╗┬ ┬   ╔═╗┌─┐┌┬┐┌─┐┬┬  ┌─┐
{H2}╠═╝└┬┘───║  │ ││││├─┘││  ├┤ 
{P2}╩   ┴    ╚═╝└─┘┴ ┴┴  ┴┴─┘└─┘ Version : 0.1
-----------------------------------------
Author : Ferly Afriliyan
Github : https:github.com/ferlyafriliyan
-----------------------------------------
""")

    file = input(f"{Putih}File : ")
    if not file:
        print(f"{M2}[ {A2}• {M2}] {P2}Isi dengan benar {M2}!")
        exit()

    if not os.path.isfile(file):
        print(f"{M2}[ {A2}• {M2}] {P2}File tidak ada {M2}!")
        exit()

    out = input(f"{Putih}Output : ")
    if not out:
        out = "Enc_Marshal_py3.py"

    try:
        source_code = open(file, "r", encoding="utf-8").read()
        encrypt_and_save_code(source_code, out)
        custom_encrypt(out, out)  # Encrypt the obfuscated output
    except UnicodeDecodeError:
        print(f"{K2}[ {A2}• {K2}] {P2}Terjadi kesalahan dalam membaca file{K2}!")