# Jangan Hapus Nama Gw Bangsat
# Gw Yang Ngembangin Nih File


import sys, argparse, codecs, binascii, time
from os import system, remove

from sys import argv
from random import choice, shuffle

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

# Definisi warna teks Rich
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

lambda_pyobf = f"""
{K2}╦  ┌─┐┌┬┐┌┐ ┌┬┐┌─┐   ╔═╗┬ ┬┌─┐┌┐ ┌─┐
{J2}║  ├─┤│││├┴┐ ││├─┤───╠═╝└┬┘│ │├┴┐├┤ 
{H2}╩═╝┴ ┴┴ ┴└─┘─┴┘┴ ┴   ╩   ┴ └─┘└─┘└  
"""

class NamaMenurun(object):
    def __init__(self, string):
        for i in string + '\n':
            sys.stdout.write(str(i))
            sys.stdout.flush()
            time.sleep(5e-05)

class LambdaEncode:
    def __init__(self):
        self.xncodepe = '# Developed_By : Ferly Afriliyan\nexec((lambda __, _, : _(%s,__))("%s",__import__(\'codecs\').decode))'
        self.Eksekusi()

    def Eksekusi(self):
        system('clear')
        print(lambda_pyobf)
        try:
            print (f"\n{H2}[{A2}01{H2}] {P2}Encode Lambda python3 Rot 13\n{K2}[{A2}00{K2}] {P2}Keluar\n")
            inp = int(input(f"{Biru}[{Abu}•{Biru}] {Putih}Pilih : {Putih}"))
            if inp == 1:
                lapis = 0
                file = input(f"\n{Hijau}[{Abu}•{Hijau}] {Putih}Input File : {Putih}")
                total = int(input(f"\n{Hijau}[{Abu}•{Hijau}] {Putih} Berapa Lapis Compile.? Max 10\n : {Putih}"))
                if ( total < 11 ):
                    out = input(f"\n{Hijau}[{Abu}•{Hijau}] {Putih}Output : {Putih}")
                    sex = open(file).read()
                    fer = repr(codecs.encode(sex, 'rot_13'))
                    f = open(out, 'w')
                    f.write(self.xncodepe % (fer, 'rot_13'))
                    f.close()
                    while ( total >= lapis ):
                        xn = open(out).read()
                        ses = repr(codecs.encode(xn, 'rot_13'))
                        f = open(out, 'w')
                        f.write(self.xncodepe % (ses,'rot_13'))
                        f.close()
                        print(f"{H2}[{A2}•{H2}] {P2}Compile ke {A2}: {O2}\r{lapis}")
                        lapis += 1
                    print (f"\nFile {file} Berhasil Di Compile")
                    print(f"\nNama File :  {out}")
            elif inp == 0:
                exit(f'Good Bye')
            else:
                exit("\nEngkau Buta Kah Anjing")
        except (KeyboardInterrupt,EOFError):
            exit("\nSelamat Tinggal")
        except ValueError:
            exit("\nHarus Angka...")
        except FileNotFoundError:
            exit(f"\nNama File Dari > [ {file} ] Tidak Ada")

if __name__ == '__main__':
    LambdaEncode()
