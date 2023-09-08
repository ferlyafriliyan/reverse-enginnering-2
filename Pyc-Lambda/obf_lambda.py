import os, sys
import marshal, zlib, base64, py_compile

import random
import secrets 

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

from rich import print

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

os.system("clear")
_notice = f"""
{J2}[{A2}•{J2}] {P2}Peringatan {M2} !.
{H2} [{A2}•{H2}] {P2}File yang telah ter Obfuscate {A2}:
{B2} [{A2}•{B2}] {P2}Tidak bisa digunakan untuk Obfuscate File itu sendiri
"""
pyc_lambda = f"""
{B2}     ____  _  _  ___        __     __   _  _  ____  ____   __  
{A2}    (  _ \( \/ )/ __)      (  )   / _\ ( \/ )(  _ \(    \ / _\  
{H2}  _  ) __/ )  /( (__  ____ / (_/\/    \/ \/ \ ) _ ( ) D (/    \ 
{J2} (_)(__)  (__/  \___)(____)\____/\_/\_/\_)(_/(____/(____/\_/\_/ 
"""

print(pyc_lambda)
def UltimateRandomNumber():
    return random.randint(50, 70)

def UltimateRandomNumberlow2():
    return secrets.randbelow(2)

if sys.version_info[0] == 2:
    _input = raw_input(f"{Hijau}[{Abu}•{Hijau}] {Putih}Enter the input file path : ")
elif sys.version_info[0] == 3:
    _input = input(f"{Hijau}[{Abu}•{Hijau}] {Putih}Enter the input file path: ")

def get_size_readable(size):
    for x in ['Byte', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"%3.1f {x}" % (size)
        size /= 1024.0

class FileSize:
    def datas(self, z):
        dts = os.stat(z).st_size
        return get_size_readable(dts)

def Encode(data, output):
    loop = UltimateRandomNumber()
    x1 = "b32(zlb(data.encode('utf8')))[::-1]"
    heading1 = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
    x2 = "b64(zlb(data.encode('utf8')))[::-1]"
    heading2 = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
    b32 = lambda in_: base64.b32encode(in_)
    b64 = lambda in_: base64.b64encode(in_)
    zlb = lambda in_: zlib.compress(in_)
    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(x1))
        except TypeError as s:
            sys.exit(f"{Merah}[{Abu}•{Merah}] {Putih}TypeError: " + str(s))
    ab = (heading1 + data)
    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(x2))
        except TypeError as s:
            sys.exit(f"{Merah}[{Abu}•{Merah}] {Putih}TypeError: " + str(s))
    abc = (heading2 + ab)
    with open(output, 'w') as f:
        f.write(abc)
        f.close()

def SEncode(data, output):
    for x in range(5):
        method = repr(b64(zlb(marshal(data.encode('utf8')))))[::-1]
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(f"exec(str(chr(35)%s));" % '+chr(1)'*10000)
        f.write(sata)
        f.close()
    py_compile.compile(output, output)

def MainMenu():
    try:
        data = open(_input).read()
    except IOError:
        sys.exit(f"{Merah}[{Abu}•{Merah}] {Putih}File Not Found {Merah}!")
    output = input(f"{Hijau}[{Abu}•{Hijau}] {Putih}Enter the output file path : ")
    Encode(data, output)
    file_size = FileSize()
    file_size_text = file_size.datas(output)
    print(_notice)
    print(f"\n{H2}[{A2}+{H2}] {P2}Encoded File Size:", file_size_text)
    print(f"\n{H2}[{A2}>{H2}] {P2}Compiling the output file...")
    py_compile.compile(_input, output)
    print(f"\n{H2}[{A2}!{H2}] {P2}Compilation complete.\n")

if __name__ == "__main__":
    MainMenu()#80FF00