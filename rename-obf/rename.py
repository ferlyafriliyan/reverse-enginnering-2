import importlib
import requests as r
from bs4 import BeautifulSoup as bs
import os, sys

import datetime, time
import platform

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
input_file = input("Masukkan nama file Input: ")

# Membaca teks dari file input
try:
    with open(input_file, "r", encoding="utf-8") as file:
        input_text = file.read()
except FileNotFoundError:
    print(f"File '{input_file}' tidak ditemukan.")
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
    output_file = input("Masukkan nama file output: ")

    # Simpan teks yang telah dienkripsi ke dalam file output
    if result:
        encrypted_code = result.text
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(f'# Take the encryption method from the website = {Take_the_encryption}\n')
            file.write(f'created_by = "Ferly Afriliyan"\n')
            file.write(f'# Time : {current_time_str}\n')
            file.write(f'# Platform : {platform.system()}-{platform.machine()}\n' + encrypted_code)
        print(f"Berhasil, file {input_file} tersimpan Di : {output_file}")
    else:
        print("Tidak dapat menemukan kode Obfuscate.")
else:
    print("Prosess Obfuscate dibatalkan karena file Input tidak ditemukan.")
