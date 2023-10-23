import importlib
import requests as r
from bs4 import BeautifulSoup as bs
import os, sys

# Clear Terminal
def clear():
    if 'linux' in sys.platform.lower():os.system('clear')
    elif 'win' in sys.platform.lower():os.system('cls')

# Memeriksa apakah modul Crypto (pycryptodome) terinstal
try:
    clear()
    importlib.import_module('Crypto')
    crypto_module_installed = True
except ImportError:
    crypto_module_installed = False

if not crypto_module_installed:
    print(f"Modul Crypto   : (pycryptodome) belum terinstall. Anda perlu menginstal modul ini sebelum menggunakan program ini.")
    print(f"Ketik perintah : pip install pycryptodome")
else:
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
        response = r.post('https://pyobfuscate.com/pyd', data={'input_text': input_text})

        # Parsing hasil respons
        source = bs(response.text, 'html.parser')

        # Cari elemen textarea dengan id 'myTextarea2'
        result = source.find('textarea', {'id': 'myTextarea2'})

        # Meminta pengguna untuk memasukkan nama file output
        output_file = input("Masukkan nama file Output: ")

        # Simpan teks yang telah dienkripsi ke dalam file output
        if result:
            encrypted_code = result.text
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(f'created_by = "Ferly Afriliyan and Merch"\n' + encrypted_code)  # Menambahkan komentar di baris pertama
            print(f"Berhasil, file {input_file} tersimpan Di : {output_file}")
        else:
            print("Tidak dapat menemukan kode Obfuscate.")
    else:
        print("Prosess Obfuscate dibatalkan karena file Input tidak ditemukan.")
