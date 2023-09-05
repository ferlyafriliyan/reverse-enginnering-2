import marshal
import base64

print('PYO\nPython Obfuscator\n\n')

# Prompt user for input file name
input_file = input("Masukkan nama file input: ")

# Prompt user for output file name
output_file = input("Masukkan nama file output: ")

try:
    with open(input_file, 'r') as f:
        content = f.read()
    print("[1/5] Membaca isi file input")

    # Prompt user for the file to encrypt (template or tempnoerror)
    encrypt_file = input("Masukkan nama file yang ingin dienkripsi (template.py atau tempnoerror.py): ")
    with open(encrypt_file, 'r') as f:
        temp = f.read()
    print("[2/5] Membaca file yang akan dienkripsi")

    cc = compile(content, "__PYO__obfuscated", 'exec')
    print("[3/5] Mengompilasi kode ke bentuk biner")

    encoded_cc = base64.b85encode(marshal.dumps(cc)).decode('utf-8')
    res = temp.replace("__PYO__386x45152", encoded_cc)
    print("[4/5] Melakukan marshalling kode objek, mengkodekan ke base85, dan menambahkannya ke template")

    encoded_res = base64.b64encode(res.encode('utf-8')).decode('utf-8')
    with open(output_file, 'w') as f:
        f.write(f"import base64 as b;exec(b.b64decode('{encoded_res}'))")
    print("[5/5] Mengkodekan ke base64 dan menulis ke file output")

except Exception as e:
    print(f"\n\n[PYO] Gagal mengompilasi. Pastikan kode input Anda valid. Error: {str(e)}")
else:
    print(f"\n\n[PYO] Kompilasi selesai. Hasilnya tersimpan di {output_file}")
