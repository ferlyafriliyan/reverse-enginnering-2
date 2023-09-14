# Import Metode Encrypr
import os
import marshal
import zlib
import base64
# Import Keterangan
import datetime
import platform
# Import Modul Random
import random
from random import randint
# Module Rich
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

num_iterations = random.randint(150, 6105)

# Tambahkan isi dari variabel Obfuscated_F dan Hidekii__

Obfuscated_F = [f'Ryougaa__=("https://ferlyafriliyan.github.io");Hidekii_=("https://github.com/ferlyafriliyan");["from","import","as","marshal","base64","zlib","((","))","exec","exec(",]']
# Variable teks : {len(num_iterations)} Line
Hidekii__ = [f'Ferly__ = ("https://ferlyafriliyan.github.io");Dev__ = ("https://github.com/ferlyafriliyan");["from","import","as","marshal","base64","zlib","((","))","exec","exec(",]']

# Fungsi enkripsi dan penyimpanan kode
def encrypt_and_save_code(source_code, output_file):
    encrypt = lambda data: base64.b64encode(zlib.compress(marshal.dumps(compile(data, "", "exec")))).decode("utf-8")
    current_time = datetime.datetime.now()

    encrypted_code = encrypt(source_code)
    with open(output_file, "w") as f:
        f.write(f'# Enc by : Ryougaa__XD\n# Github : https://github.com/ferlyafriliyan\n# Terima kasih sudah menggunakan script ini :)\n\n')
      
        # Menambahkan baris Ryougaa__XD dan Hidekii__
        for _ in range(num_iterations):
            f.write(Obfuscated_F[0] + '\n')
        f.write('\n')

        f.write(f"# One of the best Python3.11 obfuscators.\n\n")
        f.write(f"# __Time__ = {current_time}\n")
        f.write(f"# Di Buat Pada Tanggal : 15-8-2023\n\n")

        f.write(f"import marshal, zlib, base64\nRyougaa_Hidekii__=(marshal.loads(zlib.decompress(base64.b64decode('''{encrypted_code}'''))));exec(Ryougaa_Hidekii__)")
    
        f.write('\n\n')
        for _ in range(num_iterations):
            f.write(Hidekii__[0] + '\n')
        f.write('\n')

    print(f"{H2}[ {A2}• {H2}] Berhasil Obfuscated File - Hasil Encrypt : {output_file}")

def main():
    os.system('clear')

    print(f"""
{B2}╔═╗┬ ┬╔═╗┌┐ ┌─┐┬ ┬┌─┐┌─┐┌─┐┌┬┐┌─┐
{H2}╠═╝└┬┘║ ║├┴┐├┤ │ │└─┐│  ├─┤ │ ├┤ 
{P2}╩   ┴ ╚═╝└─┘└  └─┘└─┘└─┘┴ ┴ ┴ └─┘  Version : 0.1
-----------------------------------------
Author : Ferly Afriliyan
Github : https:github.com/ferlyafriliyan
-----------------------------------------
    """)

    file = input(f"{Putih}File : ")
    if not file:
        print(f"{M2}[ {A2}• {M2}] {P2}Isi dengan benar {M2}!")
        return

    if not os.path.isfile(file):
        print(f"{M2}[ {A2}• {M2}] {P2}File tidak ada {M2}!")
        return

    out = input(f"{Putih}Output : ")
    if not out:
        out = "Enc_Marshal_py3.py"

    try:
        source_code = open(file, "r", encoding="utf-8").read()
        encrypt_and_save_code(source_code, out)
    except UnicodeDecodeError:
        print(f"{K2}[ {A2}• {K2}] {P2}Terjadi kesalahan dalam membaca file{K2}!")

if __name__ == "__main__":
    main()
