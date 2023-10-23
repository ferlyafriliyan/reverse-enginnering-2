import importlib
import requests as r
from bs4 import BeautifulSoup as bs
import os, sys
import datetime, time
import platform

k = '\033[1;33m'
a = '\033[1;30m'
m = '\033[1;31m'
h = '\033[1;32m'
p = '\033[1;37m'

# Clear Terminal
def clear():
    if 'linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')

Take_the_encryption = "https://pyobfuscate.com/pyd"
current_time = datetime.datetime.now()
current_time_str = current_time.strftime("%A, %B %d, %Y %H:%M:%S")

# Meminta pengguna untuk memasukkan nama file input
clear()
input_file = input(f"{h}[{a}•{h}] {p}Masukkan nama file Input {a}: {p}")

# Membaca teks dari file input
try:
    with open(input_file, "r", encoding="utf-8") as file:
        input_text = file.read()
except FileNotFoundError:
    print(f"{p}File '{input_file}' tidak ditemukan.")
    input_text = None

# Jika teks input berhasil dibaca, maka lakukan proses enkripsi
if input_text:
    # Kirim permintaan POST
    response = r.post('https://pyobfuscate.com/rename-obf', data={'input_text': input_text})

    # Parsing hasil respons
    source = bs(response.text, 'html.parser')

    # Cari elemen textarea dengan id 'myTextarea2'
    result = source.find('textarea', {'id': 'myTextarea2'})

    # Meminta pengguna untuk memasukkan nama file output
    output_file = input(f"{h}[{a}•{h}] {p}Masukkan nama file Output {a}: {p}")

    # Simpan teks yang telah dienkripsi ke dalam file output
    if result:
        encrypted_code = result.text
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(f'# Take the encryption method from the website = {Take_the_encryption}\n')
            file.write(f'created_by = "Ferly Afriliyan"\n')
            file.write(f'# Time : {current_time_str}\n')
            file.write(f'# Platform : {platform.system()}-{platform.machine()}\n' + encrypted_code)
        print(f"{h}[{a}•{h}] {p}Berhasil, file {input_file} tersimpan di {a}: {output_file} {p}")
    else:
        print(f"{m}[{a}!{m}] {p}Tidak dapat menemukan kode Obfuscate.")
else:
    print(f"{h}[{k}+{h}] {p}Proses Obfuscate dibatalkan karena file Input tidak ditemukan.")
