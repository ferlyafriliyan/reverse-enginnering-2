from marshal import dumps
import os, random, zlib, lzma
from rich.panel import Panel
from rich import print

# Definisi warna teks ANSI
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
V2 = "[#FF00FF]"  # Violet

lzma_logo = f"""
{U2}╦  ┌─┐┌┬┐┌─┐   ╔═╗┬ ┬┌─
{A2}║  ┌─┘│││├─┤───╠═╝└┬┘│  
{P2}╩═╝└─┘┴ ┴┴ ┴   ╩   ┴ └─┘        VERSION = {O2}0{A2}.{O2}2
"""
# Panel logo
logo_panel = Panel(lzma_logo, title='[bold yellow][[green]By Ferly Afriliyan [yellow]]',
                   subtitle='[bold yellow][[green]Obfuscate Your Python File [yellow]]',  style='#FF00FF')

os.system('cls' if os.name == 'nt' else 'clear')

def purplepink(text):
    os.system(""); faded = ""
    red = 40
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

print(logo_panel)

__Variable__XV4 = "__Variable__" * 4444

file = input('└──>\u001b[32m[\u001b[35m•\u001b[32m]\u001b[37mMasukan Nama File \u001b[90m: \u001b[37m')
count = int(input('└──>\u001b[32m[\u001b[35m•\u001b[32m]\u001b[37mMasukan jumlah berapa kali Encrypt (1-10): '))
output_file = input('└──>\u001b[32m[\u001b[35m•\u001b[32m]\u001b[37mMasukkan nama file Output (Tanpa Extensi ".py"): ')

if output_file.endswith('.py'):
    print('\n[•] Kesalahan: Masukkan nama File hasil Encrypt tanpa Extensi.')
    exit()

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def genvar():
    var = ''
    for i in range(10):
        var += random.choice(chars)
    return var

def compress(text):
    ok = zlib.compress(text.encode())
    ok = lzma.compress(ok)
    return ok

def encrypt(text, count):
    if count > 10:
        print('Kesalahan: Jumlah tidak boleh melebihi 10.')
        exit()
    for _ in range(count):
        text = encrypt1(text)
        text = encrypt2(text)
    return text

def encrypt1(text):
    src = compile(text, 'Kontolivo', 'exec')
    ma = dumps(src)
    s = f'{__Variable__XV4}="{__Variable__XV4}";{__Variable__XV4}="{__Variable__XV4}";{__Variable__XV4}="{__Variable__XV4}";exec(loads({ma}));{__Variable__XV4}="{__Variable__XV4}";{__Variable__XV4}="{__Variable__XV4}"'
    compresse = compress(s)
    oke = f"# Obfuscated File Python by : Ferly Afriliyan\n# Github.com : ferlyafriliyan\n__Python__ = '3.11.4'\nimport zlib,lzma\nexec(zlib.decompress(lzma.decompress({compresse})))"
    return oke

def encrypt2(text):
    sta = genvar()
    code = text
    s = compile(code, 'Kontolivo', 'exec')
    maa = dumps(s)
    stub2 = f'# Obfuscated File Python by : Ferly Afriliyan\n# Github.com : ferlyafriliyan\n__Python__ = "3.11.4"\nfrom marshal import loads;exec(loads({maa}));'
    fin = f'{__Variable__XV4}="{__Variable__XV4}";{__Variable__XV4}="{__Variable__XV4}";{stub2}{__Variable__XV4}="{__Variable__XV4}";{__Variable__XV4}="{__Variable__XV4}";'
    return fin

if not os.path.isfile(file):
    print('File not found')
    exit()

if count < 1 or count > 10:
    print('Hitungan tidak valid. Masukkan nilai antara 1-10.')
    exit()

print(f'\n[+] Encrypting {count} times ...')
code = open(file, 'r').read()
code = encrypt(code, count)

output_path = f'{output_file}.py'
with open(output_path, 'w') as f:
    f.write(code)

os.system('cls' if os.name == 'nt' else 'clear')
print(f'Berhasil...! File hasil Encrypt tersimpan di : {output_path}\n')
print('[+] Terimakasih karena Telah menggunakan Code saya !')
exit()
