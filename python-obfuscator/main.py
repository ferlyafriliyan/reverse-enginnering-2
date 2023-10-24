import subprocess

# Meminta pengguna untuk memasukkan nama file input
input_file = input("Input file: ")

# Meminta pengguna untuk memasukkan nama file output
output_file = input("Output file: ")

# Jalankan perintah pyobfuscate untuk mengobfuscate file input dan tangkap output
try:
    result = subprocess.check_output(f'pyobfuscate -i {input_file}', shell=True, text=True)
    print(f"File {input_file} telah dienkripsi.")
    
    # Simpan hasil obfuscation ke dalam file output
    with open(output_file, "w", encoding="utf-8") as output_f:
        output_f.write(result)
    print(f"Hasil obfuscation disimpan dalam {output_file}.")
except subprocess.CalledProcessError:
    print("Terjadi kesalahan dalam mengenkripsi file.")
