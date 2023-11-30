import subprocess
import os, sys

# Clear Terminal
def clear_terminal():
    if "linux" in sys.platform.lower():
        os.system("clear")
    elif "win" in sys.platform.lower():
        os.system("cls")
        
k = "\033[1;33m"  # Warna Kuning
a = "\033[1;30m"  # Warna Hitam/Abu-Abu
m = "\033[1;31m"  # Warna Merah
h = "\033[1;32m"  # Warna Hijau
p = "\033[1;37m"  # Warna Putih
b = "\033[1;34m"  # Warna Biru
v = "\033[1;35m"  # Warna Violet
u = "\033[1;36m"  # Warna Ungu
j = "\033[1;38;5;202m"  # Warna Jingga

# Logo
PyPI = r"""

█ ▄▄ ▀▄    ▄ █ ▄▄  ▄█     ████▄ ███   ▄████  
█   █  █  █  █   █ ██     █   █ █  █  █▀   ▀ 
█▀▀▀    ▀█   █▀▀▀  ██     █   █ █ ▀ ▄ █▀▀    
█       █    █     ▐█     ▀████ █  ▄▀ █      
 █    ▄▀      █     ▐           ███    █     
  ▀            ▀                        ▀    
                                             """


def check_module(module_name, install_command):
    try:
        __import__(module_name)
        return True
    except ImportError:
        print(f"{h}[{a}•{h}] {p}Module : {a}{module_name} {p}belum terinstall.")
        print(f"{h}[{a}•{h}] {p}Ketik perintah : {a}{install_command} {p}")
        return False


def obfuscate_file(input_file, output_file):
    # Periksa apakah modul PyObfuscator sudah terinstall
    if not check_module("PyObfuscator", "pip install PyObfuscator"):
        return

    # Konstruksi perintah untuk menjalankan PyObfuscator
    command = f"PyObfuscator -o {output_file} {input_file}"

    # Menjalankan perintah menggunakan subprocess
    try:
        # Menangkap output dari subprocess
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True
        )

        # Mengganti header dengan string kosong
        modified_output = result.stdout.replace(
            "PyObfuscator  Copyright (C) 2021, 2022, 2023  Maurice Lambert\nThis program comes with ABSOLUTELY NO WARRANTY.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions.",
            "",
        )

        # Menambahkan keterangan pada file hasil obfuscate
        with open(output_file, "a") as f:
            f.write(f"\n")
            f.write("\n# Obfuscated by: Ferly Afriliyan\n")
            f.write(
                "# Encryption method: PyPI PyObfuscator\n"
            )  # Gantilah dengan metode encrypt yang sesuai

        # Menampilkan output yang sudah dimodifikasi dengan pemisah baris
        print(
            f"\n{h}[{a}•{h}] {p}Berhasil, file {input_file} tersimpan di {a}: {output_file} {p}{modified_output.strip()}"
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    clear_terminal()
    print(PyPI)
    if not check_module("PyObfuscator", "pip install PyObfuscator"):
        exit(1)

    # User file input
    input_file = input(f"{h}[{a}•{h}] {p}Input file {a}: {p}")
    if not input_file:
        print(f"└──>{m}[{a}!{m}] {p}File '{input_file}' tidak ditemukan.")
        exit()
    elif not input_file.endswith(".py"):
        print(f"└──>{m}[{a}!{m}] {p}File harus memiliki ekstensi .py {p}")
        exit()

    # User file output
    output_file = input(f"{h}[{a}•{h}] {p}Output file {a}: {p}")
    if not output_file:
        print(f"\n{m}[{a}!{m}] {p}Isi dengan benar {m}! {p}")
        exit()
    elif not output_file.endswith(".py"):
        print(f"\n{m}[{a}!{m}] {p}File output harus memiliki ekstensi .py {p}")
        exit()

    # Run method obfuscate
    obfuscate_file(input_file, output_file)
