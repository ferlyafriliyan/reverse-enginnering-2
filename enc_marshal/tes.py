import marshal
from random import randint as rr;import random
import os

# Fungsi untuk mengenkripsi dan mengacak teks dalam variable
def obfuscate_text(text):
    lines = text.split("\n")
    num_lines = len(lines)
    random.shuffle(lines)
    return "\n".join(lines)

os.system("clear")
print("\n")
print("gh : github.com/ferlyafriliyan")
print("-" * 20)

# Meminta input dari pengguna
input_file = input("Input File : ")
num_iterations = int(input("Pengulangan encrypt : "))
text_variable = input("Teks dalam Variable enc_marshal : ")
output_file = input("Output File : ")

# Baca kode dari file input
with open(input_file, "r") as f:
    code_to_encrypt = f.read()

# Compile kode menggunakan marshal
compiled_code = marshal.dumps(compile(code_to_encrypt, '', 'exec'))

# Enkripsi dan acak teks dalam kode sesuai jumlah pengulangan
for _ in range(num_iterations):
    code_to_encrypt = obfuscate_text(code_to_encrypt)

# Jumlah baris yang diacak antara 140 hingga 1409
num_lines = rr(140, 1409)

# Simpan teks terenkripsi dalam file output
with open(output_file, "w") as f:
    f.write("#  Encrypt By : Ferly Afriliyan\n")
    f.write(f'enc_marshal = [')
    for _ in range(num_lines):
        f.write(f'"{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}", "{text_variable}{text_variable}{text_variable}{text_variable}", {str(["from", "marshal", "import", "loads", "from", "zlib", "import", "decompress", "from", "base64", "import", "b64decode"])}, "{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}", "{text_variable};exec(;{text_variable};marshal.loads(b\';{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}", "{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}",\n')
    f.write(f']\n')
    f.write(f'kangrikode_kontol = [')
    for _ in range(num_lines):
        f.write(f'"enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "Encrypt By Ferly Afriliyan", "enc_marshal",\n')
    f.write(f']\n\n')
    f.write('import marshal\n')
    f.write('exec(marshal.loads(')
    f.write(repr(compiled_code))
    f.write('))\n\n')
    f.write(f'enc_marshal = [')
    for _ in range(num_lines):
        f.write(f'"{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}", "{text_variable}{text_variable}{text_variable}{text_variable}", {str(["from", "marshal", "import", "loads", "from", "zlib", "import", "decompress", "from", "base64", "import", "b64decode"])}, "{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}", "{text_variable};exec(;{text_variable};marshal.loads(b\';{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}", "{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}{text_variable}",\n')
    f.write(f']\n')
    f.write(f'kangrikode_kontol = [')
    for _ in range(num_lines):
        f.write(f'"enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "enc_marshal", "Encrypt By Ferly Afriliyan", "enc_marshal",\n')
    f.write(f']\n')

print(f"Kode telah dienkripsi dan disimpan dalam file '{output_file}'")
