import marshal
from random import randint as rr;from random import choice as rc
import random;import os
from os import system as kontolngeclear
_sarkas = '__rikod mulu goblok__', '__rikod terus sampe mampus__', '__LGBT : Langsung Gas Bolongan Tai__', '__Kontolodon__'
text_sarkas = rc(_sarkas)
# Fungsi untuk mengenkripsi dan mengacak teks dalam variable
def obfuscate_text(text):
    lines = text.split("\n")
    num_lines = len(lines)
    random.shuffle(lines)
    return "\n".join(lines)

kontolngeclear("clear")
print("\n")
print("gh : github.com/ferlyafriliyan")
print("-" * 20)

# Meminta input dari pengguna
input_file = input("Input File : ")
num_iterations = int(input("Pengulangan encrypt : "))
user_variable_name = input("Nama Variable : ")
text_variable = input("Teks dalam Variable enc_marshal : ")
output_file = input("Output File : ")

# Mendeteksi adanya Spasi dalam nama Variable
deteksi_spasi = user_variable_name.replace(" ", "_")

# Baca kode dari file input
with open(input_file, "r") as f:
    code_to_encrypt = f.read()

# Compile kode menggunakan marshal
compiled_code = marshal.dumps(compile(code_to_encrypt, '', 'exec'))

# Enkripsi dan acak teks dalam kode sesuai jumlah pengulangan
for _ in range(num_iterations):
    code_to_encrypt = obfuscate_text(code_to_encrypt)

# Jumlah baris yang diacak antara 140 hingga 1409
num_lines = rr(140, 914)

# Simpan teks terenkripsi dalam file output
with open(output_file, "w") as f:
    f.write("#  Encrypt By : Ferly Afriliyan\n")
    f.write(f'enc_marshal = [')
    for _ in range(num_lines):
        f.write(f'"{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_sarkas}", "{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_sarkas}", {str(["from", "marshal", "import", "loads", "from", "zlib", "import", "decompress", "from", "base64", "import", "b64decode"])}, "{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_sarkas}", "__{text_variable}__;exec(;__{text_variable}__;marshal.loads(b\';__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__", "__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_sarkas}",\n')
    f.write(f']\n')
    f.write(f'{deteksi_spasi} = [')
    for _ in range(num_lines):
        f.write(f'"enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "exec", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "__Rikod Terus__ Sampe__ Mampus", "marshal.loads",\n')
    f.write(f']\n\n')
    f.write('import marshal\n')
    f.write('exec(marshal.loads(')
    f.write(repr(compiled_code))
    f.write('));')
    f.write(f'enc_marshal = [')
    for _ in range(num_lines):
        f.write(f'"{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_sarkas}", "{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_sarkas}", {str(["from", "marshal", "import", "loads", "from", "zlib", "import", "decompress", "from", "base64", "import", "b64decode"])}, "{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_sarkas}", "__{text_variable}__;exec(;__{text_variable}__;marshal.loads(b\';__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__", "__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_variable}__{text_sarkas}",\n')
    f.write(f']\n')
    f.write(f'{deteksi_spasi} = [')
    for _ in range(num_lines):
        f.write(f'"enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "exec", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "__Rikod Terus__ Sampe__ Mampus", "marshal.loads",\n')
    f.write(f']\n\n')

print(f"Kode telah dienkripsi dan disimpan dalam file '{output_file}'")
