# -*- coding: UTF-8 -*-

import os
import base64
import sys
import time
import marshal
import zlib
import binascii
import lzma
import bz2
import gzip
from pprint import pformat
import random

# Emoji unicode list
Alpha_Var_Emoj = [
    "\U0001f600",  # 😀
    "\U0001f603",  # 😃
    "\U0001f604",  # 😄
    "\U0001f601",  # 😁
    "\U0001f605",  # 😅
    "\U0001f923",  # 🤣
    "\U0001f602",  # 😂
    "\U0001f609",  # 😉
    "\U0001f60A",  # 😊
    "\U0001f61b",  # 😛
    "\U0001F5FF",  # 🗿 (Emoji Batu)
]

MAX_STR_LEN = 350
OFFSET = 150

# Basic colors
J2 = "\x1b[38;5;208m"
H3 = "\033[0;30m"
M2 = "\033[0;31m"
green = "\033[0;32m"
K2 = "\033[0;33m"
B2 = "\033[0;34m"
U2 = "\033[0;35m"
C2 = "\033[0;36m"
P2 = "\033[0;37m"
A2 = "\x1b[38;5;248m"

# Snippets
ask = green + '\n[' + P2 + '?' + green + '] ' + K2
success = green + '\n[' + P2 + '√' + green + '] '
error = M2 + '\n[' + P2 + '!' + M2 + '] '
info = K2 + '\n[' + P2 + '+' + K2 + '] ' + C2

# Current Directory
pwd = os.getcwd()

# Logo of Enc-Moji
logo = f"""
{J2}╦  ╦┌─┐┬─┐┬┌─┐┌┐ ┬  ┌─┐  ╔╗╔┌─┐┌┬┐┌─┐
{C2}╚╗╔╝├─┤├┬┘│├─┤├┴┐│  ├┤───║║║├─┤│││├┤
{B2} ╚╝ ┴ ┴┴└─┴┴ ┴└─┘┴─┘└─┘  ╝╚╝┴ ┴┴ ┴└─┘
"""

# Normal slowly printer
def sprint(sentence, second=0.05):
    for word in sentence + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(second)

# About section of script
def about():
    os.system("clear")
    sprint(logo, 0.01)
    print(f"{C2}[ToolName]  {U2} :[Obfuscate Variable]")
    print(f"{C2}[Version]   {U2} :[0.2]")
    print(f"{C2}[Developer] {U2} :[Ferly Afriliyan]")
    print(f"{C2}[Github]    {U2} :[https://github.com/ferlyafriliyan]")
    print(f"{C2}[Email]     {U2} :[ferlyafrliyn@gmail.com]\n")
    ret = input(ask + "1 for main menu, 0 for exit  > " + green)
    if ret == "1":
        main()
    else:
        exit()

# Custom path chooser
def mover(out_file):
    move = input(ask + "Move to a custom path?(y/n) > " + green)
    if move == "y":
        mpath = input(ask + "Enter the path > " + green)
        if os.path.exists(mpath):
            os.rename(out_file, os.path.join(mpath, out_file))
            sprint(f"{success}{out_file} moved to {mpath}\n")
        else:
            sprint(error + "Path does not exist!\n")
    else:
        print("\n")
    exit()

# ...
# Base64 encoder function
def obfuscate(VARIABLE_NAME, file_content):
    b64_content = base64.b64encode(file_content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'

    return code

# Encrypting python file into base64 variable, easily decryptable
def encryptvar():
    var = input(ask + "Contoh variable = __CODEPEOPLE__ :  " + green)
    if var == "":
        sprint(error + " Variable tidak terbaca")
        os.system("sleep 3")
        encryptvar()
    if var.find(" ") != -1:
        sprint(error + " Hanya satu kata!")
        os.system("sleep 3")
        encryptvar()
    iteration = input(ask + "Hitungan iterasi untuk variabel : " + green)
    try:
        iteration = int(iteration)
    except Exception:
        iteration = 500
    VARIABLE_NAME = var * iteration
    in_file = input(ask + "Input  > " + C2)
    if not os.path.isfile(in_file):
        print(error + ' File tidak ada !')
        os.system("sleep 2")
        encryptvar()
    out_file = input(ask + "Output file  > " + green)
    with open(in_file, 'r', encoding='utf-8', errors='ignore') as in_f, open(out_file, 'w') as out_f:
        file_content = in_f.read()
        obfuscated_content = obfuscate(VARIABLE_NAME, file_content)
        out_f.write("# Encrypted By : Ferly Afriliyan\n# Github : https://github.com/ferlyafriliyan\n" + obfuscated_content)
    sprint(f"{success}{out_file} Tersimpan Di {pwd}")

    mover(out_file)

# Encrypting python file into emoji
def encryptem():
    try:
        in_file = input(ask + "Input File  > " + C2)
        if not os.path.isfile(in_file):
            raise FileNotFoundError(f"File not found: {in_file}")

        out_file = input(ask + "Output File  > " + C2)
        if not out_file:
            raise ValueError("Output file name is required")

        with open(in_file, 'rb') as in_f, open(out_file, "w", encoding="utf-8") as out_f:
            out_f.write("# Encrypted By : Quantum\n# Github : https://github.com/ferlyafriliyan\n")
            out_f.write(encode_string(in_f.read(), Alpha_Var_Emoj))
        sprint(f"{success}{out_file} saved in {pwd}")
        mover(out_file)

    except Exception as e:
        sprint(error + str(e))

# Main function
def main():
    os.system("clear")
    sprint(logo, 0.01)
    print(f"{J2}[{A2}01{J2}]{P2} Encrypt{C2} Python {A2}into {B2}Variable")
    print(f"{J2}[{A2}02{J2}]{P2} Encrypt{C2} Python {A2}into {K2}Emoji")
    print(f"{J2}[{A2}03{J2}]{P2} About Me")
    print(f"{J2}[{A2}00{J2}]{P2} Exit")

    while True:
        choose = input(f"{ask}{B2}Choose an option : {C2}")

        if choose == "1" or choose == "01":
            encryptvar()
        elif choose == "2" or choose == "02":
            encryptem()
        elif choose == "3" or choose == "03":
            about()
        elif choose == "0" or choose == "00":
            exit()
        else:
            sprint(error + 'Wrong input!')
            exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sprint(info + "Thanks for using. Have a good day!")
        exit()
    except Exception as e:
        sprint(error + str(e))

