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
from colorama import Fore, init

# Inisialisasi colorama
init(autoreset=True)

# Definisi warna teks ANSI
Hitam = Fore.BLACK
Merah = Fore.RED
Hijau = Fore.GREEN
Kuning = Fore.YELLOW
Orange = Fore.LIGHTYELLOW_EX
Biru = Fore.BLUE
Biru_muda = Fore.CYAN
Pink = Fore.LIGHTMAGENTA_EX
Violet = Fore.MAGENTA
Abu = Fore.LIGHTBLACK_EX
Orange_muda = Fore.LIGHTYELLOW_EX
Putih = Fore.WHITE

# Menu
def menu():
    print(f"{Hijau}[{Putih}01{Hijau}]{Putih} Encode Marshal\n{Hijau}[{Putih}02{Hijau}]{Putih} Encode Zlib\n{Hijau}[{Putih}03{Hijau}]{Putih} Encode Base16\n{Hijau}[{Putih}04{Hijau}]{Putih} Encode Base32\n{Hijau}[{Putih}05{Hijau}]{Putih} Encode Base64\n{Hijau}[{Putih}06{Hijau}]{Putih} Encode Zlib, Base16\n{Hijau}[{Putih}07{Hijau}]{Putih} Encode Zlib, Base32\n{Hijau}[{Putih}08{Hijau}]{Putih} Encode Zlib, Base64\n{Hijau}[{Putih}09{Hijau}]{Putih} Encode Marshal, Base16\n{Hijau}[{Putih}10{Hijau}]{Putih} Encode Marshal, Base64\n{Hijau}[{Putih}11{Hijau}]{Putih} Encode Marshal, Base64\n{Hijau}[{Putih}12{Hijau}]{Putih} Encode Marshal, Zlib, Base16\n{Hijau}[{Putih}13{Hijau}]{Putih} Encode Marshal, Zlib, Base32\n{Hijau}[{Putih}14{Hijau}]{Putih} Encode Marshal, Zlib, Base64\n{Hijau}[{Putih}15{Hijau}]{Putih} Simple Encode\n{Hijau}[{Putih}16{Hijau}]{Putih} Exit")

# Select raw_input() or input()
if sys.version_info[0] == 2:
    _input = "raw_input('%s')"
elif sys.version_info[0] == 3:
    _input = "input('%s')"
else:
    sys.exit(f"\n{Merah}[{Biru}!!{Merah}]{Putih} Your Python Version is not Supported!")

# Encoding
zlb = lambda in_: zlib.compress(in_)
b16 = lambda in_: base64.b16encode(in_)
b32 = lambda in_: base64.b32encode(in_)
b64 = lambda in_: base64.b64encode(in_)
mar = lambda in_: marshal.dumps(compile(in_, '___Keterangan di dalam File hasil Encrypt gw Decrypt dari Yang sebelumnya Nama Htr-Tech gw ganti jadi Nama gw___', 'exec'))
note = "\x23\x20\x4f\x62\x66\x75\x73\x63\x61\x74\x65\x64\x20\x77\x69\x74\x68\x20\x50\x79\x4f\x62\x66\x75\x73\x63\x61\x74\x65\x0a\x23\x20\x68\x74\x74\x70\x73\x3a\x2f\x2f\x66\x65\x72\x6c\x79\x61\x66\x72\x69\x6c\x69\x79\x61\x6e\x2e\x76\x65\x72\x63\x65\x6c\x2e\x61\x70\x70\x0a\x23\x20\x69\x6d\x70\x6f\x72\x74\x20\x4b\x6f\x6e\x74\x6f\x6c\x69\x76\x6f\x0a\x23\x20\x44\x65\x63\x72\x79\x70\x74\x20\x6b\x65\x74\x65\x72\x61\x6e\x67\x61\x6e\x20\x41\x75\x74\x68\x6f\x72\x20\x42\x79\x20\x3a\x20\x46\x65\x72\x6c\x69\x79\x20\x41\x66\x72\x69\x6c\x69\x79\x61\x6e\x0a"

# Program Banner
def banner():
    print(f"\n{Violet}╔═╗┬ ┬╔═╗┌┐ ┌─┐┬ ┬┌─┐┌─┐┌─┐┌┬┐┌─┐  \n{Hijau}╠═╝└┬┘║ ║├┴┐├┤ │ │└─┐│  ├─┤ │ ├┤   \n{Biru}╩   ┴ ╚═╝└─┘└  └─┘└─┘└─┘┴ ┴ ┴ └─┘   \n")

# Class untuk mendapatkan ukuran file
class FileSize:
    def datas(self, z):
        for x in ['Byte', 'KB', 'MB', 'GB']:
            if z < 1024.0:
                return f"{z:.1f} {x}"
            z /= 1024.0

    def __init__(self, path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(f" {Biru}[{Abu}-{Abu}{Biru}]{Putih} Encoded File Size : {Orange}{self.datas(dts)}\n")

# Fungsi Encode
def Encode(option, data, output):
    loop = int(eval(_input % f" {Hijau}[{Abu}-{Hijau}]{Putih} Encode Count : "))
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
        sys.exit(f"\n{Merah}[{Abu}•{Merah}]{Putih} Invalid Option {Merah}!")

    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(f" TypeError : {s}")
    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()
