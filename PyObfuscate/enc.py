# -*- coding:utf8 -*-

# Supports python2 & python3

# Author : HTR-TECH

# Modif  : Ferly Afriliyan
# Modifikasi Keterangan Nama Author Didalam File hasil Obfuscate

# Date   : Kamis 14, September 2023

# Import Modules
import os
import sys
import zlib
import time
import base64
import marshal
import py_compile

# Import modul rich
from rich.panel import Panel
from rich import print as tulis
from rich import print


# Definisi warna teks ANSI
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

# Select raw_input() or input()
if sys.version_info[0] == 2:
    _input = "raw_input('%s')"
elif sys.version_info[0] == 3:
    _input = "input('%s')"
else:
    sys.exit("\n[!!] Your Python Version is not Supported!")

# Encoding
zlb = lambda in_: zlib.compress(in_)
b16 = lambda in_: base64.b16encode(in_)
b32 = lambda in_: base64.b32encode(in_)
b64 = lambda in_: base64.b64encode(in_)
mar = lambda in_: marshal.dumps(compile(in_, '___Keterangan di dalam File hasil Encrypt gw Decrypt dari Yang sebelumnya Nama Htr-Tech gw ganti jadi Nama gw___', 'exec'))
note = "\x23\x20\x4f\x62\x66\x75\x73\x63\x61\x74\x65\x64\x20\x77\x69\x74\x68\x20\x50\x79\x4f\x62\x66\x75\x73\x63\x61\x74\x65\x0a\x23\x20\x68\x74\x74\x70\x73\x3a\x2f\x2f\x66\x65\x72\x6c\x79\x61\x66\x72\x69\x6c\x69\x79\x61\x6e\x2e\x76\x65\x72\x63\x65\x6c\x2e\x61\x70\x70\x0a\x23\x20\x69\x6d\x70\x6f\x72\x74\x20\x4b\x6f\x6e\x74\x6f\x6c\x69\x76\x6f\x0a\x23\x20\x44\x65\x63\x72\x79\x70\x74\x20\x6b\x65\x74\x65\x72\x61\x6e\x67\x61\x6e\x20\x41\x75\x74\x68\x6f\x72\x20\x42\x79\x20\x3a\x20\x46\x65\x72\x6c\x69\x79\x20\x41\x66\x72\x69\x6c\x69\x79\x61\x6e\x0a"


def banner():  # Program Banner
    print(
        ' ╔═════════════════════════════════╗\n ║          PyObfuscate            ║\n ║  Simple Python Code Obfuscator  ║\n ║  Developer : Ferly              ║\n ║  Github : ferlyafriliyan        ║\n ╚═════════════════════════════════╝\n')


def menu():
    print("\x5b\x30\x31\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x0a\x5b\x30\x32\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x0a\x5b\x30\x33\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x42\x61\x73\x65\x31\x36\x0a\x5b\x30\x34\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x42\x61\x73\x65\x33\x32\x0a\x5b\x30\x35\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x42\x61\x73\x65\x36\x34\x0a\x5b\x30\x36\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x2c\x20\x42\x61\x73\x65\x31\x36\x0a\x5b\x30\x37\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x2c\x20\x42\x61\x73\x65\x33\x32\x0a\x5b\x30\x38\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x2c\x20\x42\x61\x73\x65\x36\x34\x0a\x5b\x30\x39\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x42\x61\x73\x65\x31\x36\x0a\x5b\x31\x30\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x42\x61\x73\x65\x36\x34\x0a\x5b\x31\x31\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x42\x61\x73\x65\x33\x32\x0a\x5b\x31\x32\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x42\x61\x73\x65\x36\x34\x0a\x5b\x31\x33\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x5a\x6c\x69\x62\x2c\x20\x42\x61\x73\x65\x31\x36\x0a\x5b\x31\x34\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x5a\x6c\x69\x62\x2c\x20\x42\x61\x73\x65\x33\x32\x0a\x5b\x31\x35\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x5a\x6c\x69\x62\x2c\x20\x42\x61\x73\x65\x36\x34\x0a\x5b\x31\x36\x5d\x20\x53\x69\x6d\x70\x6c\x65\x20\x45\x6e\x63\x6f\x64\x65\x0a\x5b\x31\x37\x5d\x20\x45\x78\x69\x74")

class FileSize:  # Gets the File Size
    def datas(self, z):
        for x in ['Byte', 'KB', 'MB', 'GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z, x)
            z /= 1024.0

    def __init__(self, path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(" [-] Encoded File Size : %s\n" % self.datas(dts))


# Encode Menu
def Encode(option, data, output):
    loop = int(eval(_input % " [-] Encode Count : "))
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
    elif option == 6:
        xx = "b16(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 7:
        xx = "b32(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
    elif option == 8:
        xx = "b64(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
    elif option == 9:
        xx = "zlb(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
    elif option == 10:
        xx = "b16(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
    elif option == 11:
        xx = "b32(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
    elif option == 12:
        xx = "b64(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
    elif option == 13:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 14:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 15:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    else:
        sys.exit("\n[•]Invalid Option!")

    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(" TypeError : " + str(s))
    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()


# Special Encode
def SEncode(data, output):
    for x in range(5):
        method = repr(b64(zlb(mar(data.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(note + "exec(str(chr(35)%s));" % '+chr(1)' * 10000)
        f.write(sata)
        f.close()
    py_compile.compile(output, output)


# Main Menu
def MainMenu():
    try:
        os.system('clear')  # os.system('cls')
        banner()
        menu()
        try:
            option = int(eval(_input % " └──> [-] Option : "))
        except ValueError:
            sys.exit("\n Invalid Option !")

        if option > 0 and option <= 17:
            if option == 17:
                sys.exit("\n Thanks For Using this Tool")
            os.system('clear')  # os.system('cls')
            banner()
        else:
            sys.exit('\n Invalid Option !')
        try:
            file = eval(_input % " [-] File Name : ")
            data = open(file).read()
        except IOError:
            sys.exit("\n File Not Found!")

        output = file.lower().replace('.py', '') + '_.py'
        if option == 16:
            SEncode(data, output)
        else:
            Encode(option, data, output)
        print("\n [-] Successfully Encrypted %s" % file)
        print(" [-] Saved as %s" % output)
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()


if __name__ == "__main__":
    MainMenu()
