# __Author__ : Ferly Afriliyan
# __Github__ : https://github.com/ferlyafriliyan

import requests
import random
import os
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

get_user_agent = f"""
{J2}  __  __                ___                __ 
{H2} / / / /__ ___ ________/ _ |___ ____ ___  / /_
{A2}/ /_/ (_-</ -_) __/___/ __ / _ `/ -_) _ \/ __/
{P2}\____/___/\__/_/     /_/ |_\_, /\__/_//_/\__/ 
                          /___/       Baca Keterangan Script Dulu
"""

def print_menu():
    print(get_user_agent)
    print(f"{H2}[{A2}1{H2}] {P2}Mendapatkan User Agent")
    print(f"{H2}[{A2}2{H2}] {P2}Baca Keterangan Script")

def get_user_agents(url, num_agents):
    response = requests.get(url)
    user_agents = response.text.split('\n')
    user_agents = [agent.strip() for agent in user_agents if agent.strip()]  # Filter out empty lines
    
    if num_agents > len(user_agents):
        print(f"{M2}[{A2}×{M2}] {P2}Batas user agent dalam link hanya {A2}: {B2}{len(user_agents)}")
        exit()

    selected_agents = random.sample(user_agents, num_agents)
    return selected_agents

url = "https://raw.githubusercontent.com/ferlyafriliyan/List-User-Agent/main/list_user-agent.txt" # Ganti dengan link yang lu mau
os.system("clear")

while True:
    print_menu()
    choice = input(f"\n└──>{Hijau}[{Abu}•{Hijau}] {Putih}Pilih menu : ")

    if choice == '1':
        while True:
            num_agents_str = input(f"└──>{Hijau}[{Abu}•{Hijau}] {Putih}Ingin berapa user agent : ")

            if not num_agents_str.isdigit():
                print(f"\n{M2}[{A2}×{M2}] {P2}Isi Yang Benar {M2}! {O2}/ {P2}Masukan Angka Saja\n")
            else:
                num_agents = int(num_agents_str)
                user_agents = get_user_agents(url, num_agents)

                for i, agent in enumerate(user_agents, start=1):
                    print(f"\n{H2}[{A2}-{H2}] {P2}User agent {i}{A2}: {J2}{agent}\n")
                exit()
    elif choice == '2':
        print(f"\n{O2}[{A2}•{O2}] {P2}Peringatan {K2}!!!\n{P2}└──>{J2}[{A2}•{J2}] {P2}Harap memasukan 100 saja terlebih dahulu karena jika terlalu banyak nantinya akan tidak tercetak semuanya")
        exit()
    else:
        print(f"{M2}[{A2}×{M2}] {P2}Pilihan tidak valid {M2}!")
        exit()