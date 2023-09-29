import marshal, base64, zlib
import time;import datetime
import platform;from random import randint as rr
from os import system as autoclear
from rich.panel import Panel
from rich import print as tulis;from rich import print

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
V2 = "[#AF00FF]"  # Violet

autoclear('clear')
variable_value = 'if _ else None))=(:__:-_= __, lambda c; _ = ,__ .' * rr(14, 44)

current_time = datetime.datetime.now()
current_time_str = current_time.strftime("%A, %B %d, %Y %H:%M:%S")

platform_info = f"# Platform : {platform.system()}-{platform.machine()}\n";author_info = "# Obfuscated by : Ferly Afriliyan (Ryougaa Hideki)\n";variable_info = f"# Variable Value : {len(variable_value)}\n"

# Membuat variabel lambda_marshal sesuai dengan permintaan Anda
lambda_marshal = "Lambda_Marshal = (\n" + ",\n".join(['"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000", {str(["import", "as", "from", "marshal", "zlib", "base64"])}'] * rr(140, 1410)) + "\n)\n"

# Membuat variabel Ryougaa_Hidekii__ dengan jumlah elemen yang sama seperti N00B_D3V
ryougaa_hidekii = "Ryougaa_Hidekii__ = (\n" + ",\n".join(['"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000", {str(["import", "as", "from", "marshal", "zlib", "base64"])}'] * rr(140, 1410)) + "\n)\n"
tulis(Panel("""[#AF00FF]    ╦  ┌─┐┌┬┐┌┐ ┌┬┐┌─┐   ╔╦╗[#808080]Python3 with lambda[#AF00FF]
    ║  ├─┤│││├┴┐ ││├─┤───║║║
    ╩═╝┴ ┴┴ ┴└─┘─┴┘┴ ┴   ╩ ╩
        """, title='[#FF8F00][ [#00FF33]By Ferly Afriliyan [#FF8F00]]',
        subtitle='[#FF8F00][ [#00FF33]Obfuscate Your Python File [#FF8F00]]', style='#AF00FF'))
try:
    from rich import print as rprint
    from rich.prompt import Prompt

    file = Prompt.ask(f"{J2}[{H2}•{J2}]{P2} Input File : ")
    total = int(Prompt.ask(f"{J2}[{H2}•{J2}]{P2} Limit : "))

    if total < 101:
        out = Prompt.ask(f"{J2}[{H2}•{J2}]{P2} Output File : ")
        xos = open(file, 'rb').read()
        
        # Metode Enkripsi
        encoded_data = base64.b64encode(zlib.compress(marshal.dumps(compile(xos, '', 'exec')))).decode()

        with open(out, 'wb') as w:
            w.write(b"\n")
            w.write(f"# Time : {current_time_str}\n".encode())
            w.write(platform_info.encode())
            w.write(author_info.encode())
            w.write(b"\n")
            w.write(variable_info.encode())
            w.write(lambda_marshal.encode())
            w.write(b"import marshal\n")
            w.write(b"import base64\n")
            w.write(b"import zlib\n")
            w.write(f"'{variable_value}';exec((lambda _ : (marshal.loads(zlib.decompress(base64.b64decode(_))) if _ else None))('{encoded_data}'))\n".encode())
            w.write(b"\n\n")
            w.write(ryougaa_hidekii.encode())

        komter = 0
        while total >= komter:
            encoded_data = base64.b64encode(zlib.compress(marshal.dumps(compile(open(out, 'rb').read(), '', 'exec')))).decode()

            with open(out, 'wb') as w:
                w.write(b"\n")
                w.write(f"# Time : {current_time_str}\n".encode())
                w.write(platform_info.encode())
                w.write(author_info.encode())
                w.write(b"\n")
                w.write(variable_info.encode())
                w.write(lambda_marshal.encode())
                w.write(b"import marshal\n")
                w.write(b"import base64\n")
                w.write(b"import zlib\n")
                w.write(f"'{variable_value}';exec((lambda _ : (marshal.loads(zlib.decompress(base64.b64decode(_))) if _ else None))('{encoded_data}'))\n".encode())
                w.write(b"\n\n")
                w.write(ryougaa_hidekii.encode())

            current_iteration = komter
            total_iterations = total
            loading_percentage = (current_iteration / total_iterations) * 100
            print(f" └──>{J2}[{H2}•{J2}]{P2} Encrypting: [{H2}{loading_percentage:.2f}%{P2}]", end='\r')
            time.sleep(0.00)
            komter += 1

        print(f"\n{J2}[{H2}+{J2}]{P2} Compiled file saved to {A2}: {K2}{out}")

except Exception as e:
    rprint(f"{Merah}Error: {str(e)}")
