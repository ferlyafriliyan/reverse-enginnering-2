import datetime

import platform
from rich import print
import marshal, zlib, base64
import binascii, lzma, bz2, gzip
from os import system as auto
import os, sys

# Clear Terminal
def clear():
    if "linux" in sys.platform.lower():
        os.system("clear")
    elif "win" in sys.platform.lower():
        os.system("cls")


# Kode Warna Print
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


# Logo ; Input, Output File
logo_input_output = f"""{O2}
╔═╗┬ ┬   ╦  ╦┌─┐┬─┐┬┌─┐┌┐ ┬  ┌─┐
╠═╝└┬┘───╚╗╔╝├─┤├┬┘│├─┤├┴┐│  ├┤
╩   ┴     ╚╝ ┴ ┴┴└─┴┴ ┴└─┘┴─┘└─┘"""

# Clear screen menggunakan teks "kontolngeclear"
clear()
print(logo_input_output)
input_file = input(
    f"{Biru_muda}[{Hijau}•{Biru_muda}]{Putih} Input File {Hijau}: {Putih}"
)

# Request file output

output_file = input(
    f"{Biru_muda}[{Hijau}•{Biru_muda}]{Putih} Output File {Hijau}: {Putih}"
)
output_path = os.path.join(output_file)

# Number of encryption iterations
num_iterations = 44

# Function to encrypt files
def encrypt_file():
    current_time = datetime.datetime.now()
    current_time_str = current_time.strftime("%A, %B %d, %Y %H:%M:%S")
    encrypted_code = (
        f"\n# You Cant Bypass My Codes Security\n"
        f"# Time : {current_time}\n"
        f"# Platform : {platform.system()}-{platform.machine()}\n"
        f"# Obfuscate By Ferly Afriliyan >_<\n\n"
        f"#\n\n"
        f'__File__       = "Py3-Variable ; Encryptions File Python3"\n'
        f'__instagram__  = "www.instagram.com/afriliyanferlly_shishigami"\n\n'
        f"#\n\n"
        f'__website__    = "https://ferlyafriliyan.vercel.app/"\n'
        f'__github__     = "https://github.com/ferlyafriliyan/Py3-Variable"\n\n\n'
        f"# Dont Change My Code >_<\n\n"
    )
    encrypted_code += f"Ferly_XV4 = [\n"
    for _ in range(3500):
        encrypted_code += f'"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000",\n'
    encrypted_code += f"]\n\n"
    encrypted_code += f"License_XV4 = [\n"
    for _ in range(444):
        encrypted_code += f'"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000",\n'
    encrypted_code += f"]\n\n"

    # Read code from input file
    with open(input_file, "rb") as file:
        code = compile(file.read(), "string", "exec")

    # Encrypt the code as many iterations as specified
    for _ in range(num_iterations):
        # Code encryption using marshal, zlib, and base64
        encrypted_data = base64.b64encode(zlib.compress(marshal.dumps(code))).decode()

        # Generate random keys for XOR encryption
        key = os.urandom(32)

        # Key encryption using marshal, zlib, and base64
        encrypted_key = base64.b64encode(zlib.compress(marshal.dumps(key))).decode()

        # Encrypt data using XOR with key
        encrypted_data = "".join(
            chr(ord(c) ^ key[i % len(key)]) for i, c in enumerate(encrypted_data)
        )

        # Convert encrypted data to hexadecimal string
        encrypted_data_hex = binascii.hexlify(encrypted_data.encode()).decode()

        # Obfuacated File
        with open(output_path, "w") as file:
            file.write(encrypted_code)
            file.write(
                f"import datetime, platform, marshal, zlib, base64, binascii, os\n\n"
            )
            file.write(f'encrypted_key = "{encrypted_key}"\n')
            file.write(
                f"decrypted_key = marshal.loads(zlib.decompress(base64.b64decode(encrypted_key)))\n"
            )
            file.write(f'encrypted_data_hex = "{encrypted_data_hex}"\n')
            file.write(
                f'decrypted_data = "".join(chr(ord(c) ^ decrypted_key[i % len(decrypted_key)]) for i, c in enumerate(binascii.unhexlify(encrypted_data_hex).decode()))\n'
            )
            file.write(
                f"code = marshal.loads(zlib.decompress(base64.b64decode(decrypted_data)))\n"
            )
            file.write(f"exec(code)\n\n")
            file.write(f"Afriliyan_XV4 = [\n")
            for _ in range(3500):
                file.write(
                    f'"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000",\n'
                )
            file.write(f"]\n\n")

    print(f"\n{H2}[{A2}!!{H2}]{P2} Berhasil, File tersimpan di {A2}: {output_file}")


if __name__ == "__main__":
    encrypt_file()
