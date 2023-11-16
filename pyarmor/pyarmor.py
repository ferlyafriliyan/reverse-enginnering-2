import subprocess
import os

k = '\033[1;33m'  # Warna Kuning
a = '\033[1;30m'  # Warna Hitam/Abu-Abu
m = '\033[1;31m'  # Warna Merah
h = '\033[1;32m'  # Warna Hijau
p = '\033[1;37m'  # Warna Putih
b = '\033[1;34m'  # Warna Biru
v = '\033[1;35m'  # Warna Violet
u = '\033[1;36m'  # Warna Ungu
j = '\033[1;38;5;202m'  # Warna Jingga

# Logo
Pyarmor = r"""

█ ▄▄ ▀▄    ▄ ██   █▄▄▄▄ █▀▄▀█ ████▄ █▄▄▄▄ 
█   █  █  █  █ █  █  ▄▀ █ █ █ █   █ █  ▄▀ 
█▀▀▀    ▀█   █▄▄█ █▀▀▌  █ ▄ █ █   █ █▀▀▌  
█       █    █  █ █  █  █   █ ▀████ █  █  
 █    ▄▀        █   █      █          █   
  ▀            █   ▀      ▀          ▀    
              ▀                           """
#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')

def check_module(module_name, install_command):
    try:
        __import__(module_name)
        return True
    except ImportError:
        print(f"{h}[{m}•{h}] {p}Error: Module {a}{module_name} {p}not found.")
        print(f"{h}[{m}•{h}] {p}To install, run: {a}{install_command} {p}")
        return False

def obfuscate_file(input_file):
    if not check_module("pyarmor", "pip3 install pyarmor"):
        return
    
    # Periksa apakah perintah 'pyarmor' dapat dijalankan di terminal
    try:
        subprocess.run("pyarmor", shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"{h}[{m}•{h}] {p}Error: 'pyarmor' is not recognized as an internal or external command.")
        print(f"{h}[{m}•{h}] {p}Make sure 'pyarmor' is installed and accessible in the terminal.")
        return

    try:
        # Mengeksekusi perintah PyArmor untuk menghasilkan versi obfuscated
        result = subprocess.run(f"pyarmor gen {input_file}", shell=True, check=True, capture_output=True, text=True)
        
        # Mengganti header dengan string kosong
        modified_output = result.stdout.replace(
            "INFO     Python 3.11.6\nINFO     Pyarmor 8.4.3 (trial), 000000, non-profits\nINFO     Platform windows.x86_64\n", "")

        # Mencetak informasi proses PyArmor
        print(modified_output)
        print(f"""INFO     Python 3.11.6
INFO     Pyarmor 8.4.3 (trial), 000000, non-profits
INFO     Platform windows.x86_64
INFO     search inputs ...
INFO     find script {input_file}
INFO     find 1 top resources
INFO     start to generate runtime files
INFO     target platforms {'windows.amd64'}
INFO     write dist\pyarmor_runtime_000000\pyarmor_runtime.pyd
INFO     generate runtime files OK
INFO     start to obfuscate scripts
INFO     process resource "pyarmor"
INFO     obfuscating file {input_file}
INFO     write dist\{input_file}
INFO     obfuscate scripts OK
""")

        # Mencetak informasi obfuscation
        print(f"{h}[{m}•{h}] {p}Berhasil menghasilkan versi obfuscated: {a}dist\{input_file} {p}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    clear()
    print(Pyarmor)
    if not check_module("pyarmor", "pip install pyarmor"):
        exit(1)

    # User file input
    input_file = input(f"{h}[{a}•{h}] {p}Input file {a}: {p}")
    if not input_file:
        print(f"└──>{m}[{a}!{m}] {p}File '{input_file}' tidak ditemukan.")
        exit()
    elif not input_file.endswith(".py"):
        print(f"└──>{m}[{a}!{m}] {p}File harus memiliki ekstensi .py {p}")
        exit()
    # Pastikan file yang dimasukkan oleh pengguna ada
    if not os.path.isfile(input_file):
        print(f"File '{input_file}' tidak ditemukan.")
    else:
        # Menjalankan obfuscation
        obfuscate_file(input_file)
