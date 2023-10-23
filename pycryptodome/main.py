import importlib
import requests as r
from bs4 import BeautifulSoup as bs
import os, sys

import datetime, time
import platform

# Clear Terminal
def clear():
    if 'linux' in sys.platform.lower():os.system('clear')
    elif 'win' in sys.platform.lower():os.system('cls')

# Memeriksa apakah modul Crypto (pycryptodome) terinstall
try:
    clear()
    importlib.import_module('Crypto')
    crypto_module_installed = True
except ImportError:
    crypto_module_installed = False

if not crypto_module_installed:
    print(f"Modul Crypto   : (pycryptodome) belum terinstall. Anda perlu menginstal modul ini sebelum menggunakan program ini.")
    print(f"Ketik perintah : pip install pycryptodome")

# Memeriksa apakah modul requests terinstall
try:
    importlib.import_module('requests')
    requests_module_installed = True
except ImportError:
    requests_module_installed = False

# Memeriksa apakah modul bs4 terinstall
try:
    importlib.import_module('bs4')
    bs4_module_installed = True
except ImportError:
    bs4_module_installed = False

if not crypto_module_installed or not requests_module_installed or not bs4_module_installed:
    print("Beberapa modul belum terinstal. Anda perlu menginstal modul-modul berikut:")
    if not crypto_module_installed:
        print("  - pycryptodome (Crypto)")
        print("  - requests")
        print("  - bs4 (Beautiful Soup)")
    print("Ketik perintah: pip install pycryptodome bs4 requests")
else:
    # Clear Terminal
    if 'linux' in platform.system().lower():os.system('clear')
    elif 'win' in platform.system().lower():os.system('cls')

    Take_the_encryption = "https://pyobfuscate.com/pyd"
    current_time = datetime.datetime.now()
    current_time_str = current_time.strftime("%A, %B %d, %Y %H:%M:%S")

    # Meminta pengguna untuk memasukkan nama file input
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
        response = r.post('https://pyobfuscate.com/pyd', data={'input_text': input_text})

        # Parsing hasil respons
        source = bs(response.text, 'html.parser')

        # Cari elemen textarea dengan id 'myTextarea2'
        result = source.find('textarea', {'id': 'myTextarea2'})

        # Meminta pengguna untuk memasukkan nama file output
        while True:
            output_file = input("Masukkan nama file Output: ")
            if not output_file:
                print("Isi dengan benar!")
                exit()
            elif not output_file.endswith(".py"):
                print("File output harus memiliki ekstensi .py")
                exit()
            else:
                break

        # Simpan teks yang telah dienkripsi ke dalam file output
        if result:
            encrypted_code = result.text
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(f'# Take the encryption method from the website = {Take_the_encryption}\n')
                file.write(f'created_by = "Ferly Afriliyan and Merch"\n')
                file.write(f'# Time : {current_time_str}\n')
                file.write(f'# Platform : {platform.system()}-{platform.machine()}\n' + encrypted_code)
            print(f"Berhasil, file {input_file} tersimpan di: {output_file}")
        else:
            print("Tidak dapat menemukan kode Obfuscate.")
    else:
        print("Proses Obfuscate dibatalkan karena file Input tidak ditemukan.")
