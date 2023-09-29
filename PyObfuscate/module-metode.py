# Import Modules
import os, sys; from os import system as jembutngeclear
import marshal, zlib, base64, time; import py_compile
import datetime, platform; from colorama import Fore, init

# Inisialisasi colorama
init(autoreset=True)

# Definisi warna teks ANSI
Hitam = Fore.BLACK
Merah = Fore.RED
Hijau = Fore.GREEN
Kuning = Fore.YELLOW
Orange = Fore.LIGHTYELLOW_EX
Biru = Fore.BLUE
Biru_muda = Fore.CYAN
Pink = Fore.LIGHTMAGENTA_EX
Violet = Fore.MAGENTA
Abu = Fore.LIGHTBLACK_EX
Orange_muda = Fore.LIGHTYELLOW_EX
Putih = Fore.WHITE

current_time = datetime.datetime.now()
current_time_str = current_time.strftime("%A, %B %d, %Y %H:%M:%S")

# Menu
def menu():
    print(f"{Hijau}[{Putih}01{Hijau}]{Putih} Encode Marshal\n{Hijau}[{Putih}02{Hijau}]{Putih} Encode Marshal, Zlib, Base64\n{Hijau}[{Putih}03{Hijau}]{Putih} Exit")

# Select raw_input() or input()
if sys.version_info[0] == 2:
    _input = "raw_input('%s')"
elif sys.version_info[0] == 3:
    _input = "input('%s')"
else:
    sys.exit(f"\n{Merah}[{Biru}!!{Merah}]{Putih} Your Python Version is not Supported!")

# Encoding
zlb = lambda in_: zlib.compress(in_)
b64 = lambda in_: base64.b64encode(in_)
mar = lambda in_: marshal.dumps(compile(in_, "", "exec"))
note = f"""# Obfuscated by : Ferly Afriliyan (Ryougaa Hideki)
# Time  :  {current_time_str}\n# Platform : {platform.system()}-{platform.machine()}\n"""

# Program Banner
def banner():
    print(f"\n{Violet}╔═╗┬ ┬╔═╗┌┐ ┌─┐┬ ┬┌─┐┌─┐┌─┐┌┬┐┌─┐  \n{Hijau}╠═╝└┬┘║ ║├┴┐├┤ │ │└─┐│  ├─┤ │ ├┤   \n{Biru}╩   ┴ ╚═╝└─┘└  └─┘└─┘└─┘┴ ┴ ┴ └─┘   \n")

# Class untuk mendapatkan ukuran file
class FileSize:
    def datas(self, z):
        for x in ['Byte', 'KB', 'MB', 'GB']:
            if z < 1024.0:
                return f"{z:.1f} {x}"
            z /= 1024.0

    def __init__(self, path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(f" {Biru}[{Abu}-{Abu}{Biru}]{Putih} Encoded File Size : {Orange}{self.datas(dts)}\n")

# Fungsi Encode
def Encode(option, data, output):
    loop = int(eval(_input % f" {Hijau}[{Abu}-{Hijau}]{Putih} Encode Count : "))
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    else:
        exit(f"\n{Merah}[{Abu}•{Merah}]{Putih} Invalid Option {Merah}!")

    for x in range(loop):
        try:
            data = "Jembut__nge__exec=((_)(%s));exec(Jembut__nge__exec)" % repr(eval(xx))
        except TypeError as s:
            sys.exit(f" TypeError : {s}")
    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()