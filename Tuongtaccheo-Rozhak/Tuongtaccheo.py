#!/usr/bin/env python3
import os
import time
from requests.exceptions import RequestException
import requests
import re
import json
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.columns import Columns

try:
    pass
except (Exception, KeyboardInterrupt) as e:
    exit(f"[Error] {str(e).capitalize()}!")

def Banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Panel(
        """[bold red]●[bold yellow] ●[bold green] ●
[bold red]___________                _________ .__                  
[bold red]\\_   _____/____            \\_   ___ \\|  |__   ____  ____  
[bold red] |    __) \\__  \\    ______ /    \\  \\/|  |  \\_/ __ \\/  _ \\ 
[bold red] |     \\   / __ \\_ /_____/ \\     \\___|   Y  \\  ___(  <_> )
[bold white] \\___  /  (____  /          \\______  /___|  /\\___  >____/ 
[bold white]     \\/        \\/                  \\/     \\/     \\/       
[underline bold blue]   TOOLS FACEBOOK TUONGTACCHEO - Coded by Rozhak-XD/""",
        width=63, style="bold bright_white"))
    return 0


Data, Sukses, Gagal, Koin = [], [], [], {"Jumlah": 0}


class Login:
    def __init__(self):
        pass

    def TuongTaccheo_Facebook(self):
        try:
            Banner()
            print(Panel(
                f"[italic white]Silahkan Masukan[italic green] Cookies[italic white] Akun Tuongtaccheo, Untuk Cara Mendapatkannya Ada Di[italic red] Pengaturan[italic white] Akun Tuongtaccheo!",
                width=63, style="bold bright_white", subtitle="╭─────", subtitle_align="left",
                title=">>> Tuongtaccheo <<<"))
            cookies_ttc = Console().input(f"[bold bright_white]   ╰─> ")
            self.username, self.koin = self.Cek_Tuongtaccheo(cookies_ttc)
            print(Panel(
                f"[italic white]Silahkan Masukan[italic green] Cookies[italic white] Akun Facebook, Pastikan Akun Menggunakan[italic red] Bahasa Indonesia[italic white]!",
                width=63, style="bold bright_white", subtitle="╭─────", subtitle_align="left",
                title=">>> Facebook <<<"))
            cookies_fb = Console().input(f"[bold bright_white]   ╰─> ")
            self.name, self.user = self.Cek_Facebook(cookies_fb)
            
            with requests.Session() as r:
                r.headers.update({
                    'Host': 'tuongtaccheo.com',
                    'sec-fetch-mode': 'cors',
                    'accept': '*/*',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'cookie': cookies_ttc,
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-dest': 'empty',
                })
                data = {
                    'iddat[]': re.search('c_user=(\\d+);', str(cookies_fb)).group(1),
                    'loai': 'fb',
                }
                response = r.post('https://tuongtaccheo.com/cauhinh/datnick.php', data=data).text
                
                if str(response) == '2':
                    print(Panel(
                        f"[italic red]Silahkan Tambahkan Akun Facebook Tersebut Ke Konfigurasi!",
                        width=63, style="bold bright_white", title=">>> Tambahkan Konfigurasi <<<"))
                    exit()
                elif str(response) == '1':
                    print(Panel(
                        f"""[bold white]Username :[bold green] {self.username}\n[bold white]Link :[bold red] https://web.facebook.com/{self.user}""",
                        width=63, style="bold bright_white", title=">>> Welcome <<<"))
                    
                    with open('Data/Akun.json', 'w') as w:
                        w.write(json.dumps({
                            'Tuongtaccheo': cookies_ttc,
                            'Facebook': cookies_fb,
                        }))
                    w.close()
                    
                    Mision().Get_Data_Follow(cookies_fb, '100073125893802')
                    Daftar().Menu()
                else:
                    print(Panel(
                        f"[italic red]{str(response).title()}!",
                        width=63, style="bold bright_white", title=">>> Error <<<"))
                    exit()
        except Exception as e:
            print(Panel(
                f"[italic red]{str(e).title()}!",
                width=63, style="bold bright_white", title=">>> Error <<<"))
            exit()

    def Cek_Tuongtaccheo(self, cookies_ttc):
        with requests.Session() as r:
            r.headers.update({
                'Host': 'tuongtaccheo.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'cookie': cookies_ttc,
            })
            response = r.get('https://tuongtaccheo.com/caidat/').text
            Data.clear()
            for z in ['Tên tài khoản', 'Số dư']:
                self.finds = re.search(f'''<th scope="row">{z}</th>\n      <td>(.*?)</td>''', str(response)).group(1)
                Data.append(f'{self.finds}')
            self.username, self.koin = Data[0], Data[1]
            Koin.update({
                "Jumlah": self.koin
            })
        return (self.username, self.koin)


    def Cek_Facebook(self, cookies_fb):
        with requests.Session() as r:
            r.headers.update({
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-user': '?1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-dest': 'document',
                'Host': 'web.facebook.com',
            })
            response = r.get('https://web.facebook.com/', cookies={
                'cookie': cookies_fb
            }).text
            self.find_akun = re.search('{"ACCOUNT_ID":"(\\d+)","USER_ID":".*?","NAME":"(.*?)"', str(response))
            self.name, self.user = self.find_akun.group(2), self.find_akun.group(1)
            if len(self.name) == 0 and int(self.user) == 0:
                print(Panel(
                    f"[italic red]Sepertinya Cookies Kamu Sudah Tidak Valid Atau Kadaluarsa!",
                    width=63, style="bold bright_white", title=">>> Cookies Invalid <<<"))
                time.sleep(4.5)
                self.TuongTaccheo_Facebook()
            else:
                return (self.name, self.user)


class Daftar:
    def __init__(self) -> None:
        pass

    def Pengguna(self):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Host': 'justpaste.it',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                })
                response = r.get('https://justpaste.it/d7qrg').text
                self.online, self.jumlah = re.search('"onlineText":"(\\d+)"', str(response)).group(1), re.search('"viewsText":"(\\d+)"', str(response)).group(1)
            return (self.jumlah, self.online)
        except (Exception) as e:
            return (0, 404)

    def Menu(self):
        try:
            Banner()
            self.cookies_ttc = json.loads(open('Data/Akun.json', 'r').read())['Tuongtaccheo']
            self.cookies_fb = json.loads(open('Data/Akun.json', 'r').read())['Facebook']
            self.username, self.koin = Login().Cek_Tuongtaccheo(self.cookies_ttc)
            self.name, self.user = Login().Cek_Facebook(self.cookies_fb)
            print(Columns([
                Panel(f"""[bold white]Username :[bold green] {self.username[:14]}\n[bold white]Koin :[bold yellow] {self.koin[:18]}""", width=31, style="bold bright_white"),
                Panel(f"""[bold white]Name :[bold green] {self.name[:18]}\n[bold white]User :[bold yellow] {self.user[:18]}""", width=31, style="bold bright_white")
            ]))
        except (Exception) as e:
            print(Panel(f"[italic red]{str(e).title()}!", width=63, style="bold bright_white", title=">>> Error <<<"))
            time.sleep(3.5)
            Login().TuongTaccheo_Facebook()

        self.jumlah, self.online = self.Pengguna()

        print(Panel("""[bold green]1[bold white]. Jalankan Misi Follow Facebook\n[bold green]2[bold white]. Jalankan Misi Likes Facebook\n[bold green]3[bold white]. Tukarkan Koin Ke Pengikut\n[bold green]4[bold white]. Tukarkan Koin Ke Likes\n[bold green]5[bold white]. Keluar ([bold red]Exit[bold white])""", width=63, style="bold bright_white", title=f">>> (Pengguna {self.jumlah}/{self.online} Online) <<<", subtitle="╭─────", subtitle_align="left"))
        choose = Console().input(f"[bold bright_white]   ╰─> ")
        if choose == '01' or choose == '1':
            try:
                print(Panel(f"[italic white]Silahkan Masukan[italic green] Delay[italic white] Agar Tidak Terblokir Disarankan Untuk Menggunakan Delay Di Atas[italic red] 15 Detik[italic white] Agar Aman!", width=63, style="bold bright_white", subtitle="╭─────", subtitle_align="left", title=">>> Delay <<<"))
                delay = int(Console().input(f"[bold bright_white]   ╰─> "))
                if delay < 10:
                    print(Panel(f"[italic red]Delay Yang Terlalu Cepat Dapat Menyebabkan Akun Terblokir!", width=63, style="bold bright_white", title=">>> Error <<<"))
                    exit()
                else:
                    print(Panel(f"[italic white]Sedang Menjalankan[italic green] Misi Follow[italic white], Jika Semua Misi Gagal Kemungkinan Akun Facebook Kamu[italic red] Terblokir[italic white]!", width=63, style="bold bright_white", title=">>> Catatan <<<"))
                    while True:
                        try:
                            Mision().Tuongtaccheo_Follow(self.cookies_ttc, self.cookies_fb, delay)
                        except (RequestException) as e:
                            print(f"[bold bright_white]   ╰─>[bold red] Koneksi Error...                 ", end='\r')
                            time.sleep(7.5)
                            continue
                        except (KeyboardInterrupt):
                            continue
            except (Exception) as e:
                print(Panel(f"[italic red]{str(e).title()}!", width=63, style="bold bright_white", title=">>> Error <<<"))
                exit()
        elif choose == '02' or choose == '2':
            try:
                print(Panel(f"[italic white]Silahkan Masukan[italic green] Delay[italic white] Agar Tidak Terblokir Disarankan Untuk Menggunakan Delay Di Atas[italic red] 15 Detik[italic white] Agar Aman!", width=63, style="bold bright_white", subtitle="╭─────", subtitle_align="left", title=">>> Delay <<<"))
                delay = int(Console().input(f"[bold bright_white]   ╰─> "))
                if delay < 10:
                    print(Panel(f"[italic red]Delay Yang Terlalu Cepat Dapat Menyebabkan Akun Terblokir!", width=63, style="bold bright_white", title=">>> Error <<<"))
                    exit()
                else:
                    print(Panel(f"[italic white]Sedang Menjalankan[italic green] Misi Likes[italic white], Jika Semua Misi Gagal Kemungkinan Akun Facebook Kamu[italic red] Terblokir[italic white]!", width=63, style="bold bright_white", title=">>> Catatan <<<"))
                    while True:
                        try:
                            Mision().Tuongtaccheo_Likes(self.cookies_ttc, self.cookies_fb, delay)
                        except (RequestException) as e:
                            print(f"[bold bright_white]   ╰─>[bold red] Koneksi Error...                 ", end='\r')
                            time.sleep(7.5)
                            continue
                        except (KeyboardInterrupt):
                            continue
            except (Exception) as e:
                print(Panel(f"[italic red]{str(e).title()}!", width=63, style="bold bright_white", title=">>> Error <<<"))
                exit()
        elif choose == '03' or choose == '3':
            try:
                print(Panel(f"[italic white]Silahkan Masukan[italic green] Userid[italic white] Akun Facebook, Pastikan Akun Hanya Memiliki Tombol[italic red] Ikuti[italic white] Dan Akun Berada Dalam Mode Publik!", width=63, style="bold bright_white", subtitle="╭─────", subtitle_align="left", title=">>> Akun Target <<<"))
                target_id = int(Console().input(f"[bold bright_white]   ╰─> "))
                print(Columns([
                    Panel(f"[bold green]20[bold white] Follower :[bold red] 22.000 Koin", width=31, style="bold bright_white"),
                    Panel(f"[bold green]100[bold white] Follower :[bold red] 110.000", width=31, style="bold bright_white"),
                ]))
                print(Panel(f"[italic white]Silahkan Masukan[italic green] Jumlah Pengikut[italic white] Pastikan Hanya Memasukan[italic red] Angka[italic white] Dan Koin Sudah[italic red] Mencukupi[italic white]!", width=63, style="bold bright_white", subtitle="╭─────", subtitle_align="left", title=">>> Jumlah Pengikut <<<"))
                jumlah = int(Console().input(f"[bold bright_white]   ╰─> "))
                Tukarkan().Pengikut(self.cookies_ttc, jumlah, target_id, 'SUBNICK', 'tangsub')
            except (Exception) as e:
                print(Panel(f"[italic red]{str(e).title()}!", width=63, style="bold bright_white", title=">>> Error <<<"))
                exit()
        elif choose == '04' or choose == '4':
            try:
                print(Panel(f"[italic white]Silahkan Masukan[italic green] Id Postingan[italic white] Akun Facebook, Pastikan Postingan Bisa Disukai Oleh[italic red] Publik[italic white]!", width=63, style="bold bright_white", subtitle="╭─────", subtitle_align="left", title=">>> Postingan <<<"))
                target_id = int(Console().input(f"[bold bright_white]   ╰─> "))
                print(Columns([
                    Panel(f"[bold green]50[bold white] Likes :[bold red] 42.500 Koin", width=31, style="bold bright_white"),
                    Panel(f"[bold green]1000[bold white] Likes :[bold red] 850.000", width=31, style="bold bright_white"),
                ]))
                print(Panel(f"[italic white]Silahkan Masukan[italic green] Jumlah Likes[italic white] Pastikan Kamu Hanya Memasukan[italic red] Angka[italic white] Dan Koin Sudah[italic red] Mencukupi[italic white]!", width=63, style="bold bright_white", subtitle="╭─────", subtitle_align="left", title=">>> Jumlah Likes <<<"))
                jumlah = int(Console().input(f"[bold bright_white]   ╰─> "))
                Tukarkan().Pengikut(self.cookies_ttc, jumlah, target_id, 'LIKE', 'tanglike')
            except (Exception) as e:
                print(Panel(f"[italic red]{str(e).title()}!", width=63, style="bold bright_white", title=">>> Error <<<"))
                exit()
        elif choose == '05' or choose == '5':
            try:
                os.remove('Data/Akun.json')
                print(Panel(f"[italic red]Sedang Mencoba Untuk Menghapus Seluruh Cookies Kamu!", width=63, style="bold bright_white", title=">>> Delete <<<"))
                exit()
            except:
                pass
        else:
            print(Panel(f"[italic red]Pilihan Yang Kamu Masukan Tidak Tersedia Di Dalam Menu!", width=63, style="bold bright_white", title=">>> Wrong Input <<<"))
            time.sleep(2.5)
            self.Menu()

class Tukarkan:
    def __init__(self) -> None:
        pass

    def Pengikut(self, cookies_ttc, jumlah, target_id, loai, tang):
        with requests.Session() as r:
            r.headers.update({
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Host': 'tuongtaccheo.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'cookie': cookies_ttc,
            })
            data = {
                'id': target_id,
                'loai': loai,
                'sl': jumlah,
                'link': 'https://www.facebook.com/{}'.format(target_id),
            }
            response = r.post('https://tuongtaccheo.com/{}/themvip.php'.format(tang), data=data).text
            if str(response) == '1':
                print(Panel(f"[italic red]Koin Kamu Tidak Mencukupi Untuk Menukarkan Ke Pengikut Atau Likes Jalankan Misi Untuk Mendapatkan Koin!", width=63, style="bold bright_white", title=">>> Koin Tidak Cukup <<<"))
                exit()
            elif 'Mua th\xc3\xa0nh c\xc3\xb4ng' in str(response):
                if str(tang) == 'tanglike':
                    print(Panel(f"""[bold white]Status :[italic green] Being processed[/]\n[bold white]Link :[bold yellow] https://web.facebook.com/{target_id}\n[bold white]Likes :[bold green] +{jumlah}""", width=63, style="bold bright_white", title=">>> Sukses <<<"))
                    exit()
                else:
                    print(Panel(f"""[bold white]Status :[italic green] Being processed[/]\n[bold white]Link :[bold yellow] https://web.facebook.com/{target_id}\n[bold white]Followers :[bold green] +{jumlah}""", width=63, style="bold bright_white", title=">>> Sukses <<<"))
                    exit()
            else:
                print(Panel(f"[italic red]{str(response).title()}!", width=63, style="bold bright_white", title=">>> Error <<<"))
                exit()

class Mision:
    def __init__(self) -> None:
        pass

    def Tuongtaccheo_Likes(self, cookies_ttc, cookies_fb, delay):
        with requests.Session() as r:
            r.headers.update({
                'Host': 'tuongtaccheo.com',
                'referer': 'https://tuongtaccheo.com/kiemtien/',
                'sec-fetch-mode': 'cors',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'cookie': cookies_ttc,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'sec-fetch-dest': 'empty',
                'accept-language': 'en-US,en;q=0.9',
            })
            response = r.get('https://tuongtaccheo.com/kiemtien/getpost.php')
            if '"idpost":' in str(response.text):
                for z in json.loads(response.text):
                    self.idpost, self.profile_url = z['idpost'], z['link'].replace('\\', '')
                    r.headers.clear()
                    r.cookies.clear()
                    for sleep in range(delay, 0, -1):
                        time.sleep(1)
                        print(f"[bold bright_white]   ╰─>[bold blue] {self.idpost}[bold white]/[bold green]{sleep}[bold white] Sukses:-[bold blue]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Gagal)}[bold white]    ", end='\r')
                    self.status = self.Get_Data_Likes(cookies_fb, self.idpost)
                    if self.status == 'Sukses':
                        time.sleep(5)
                        r.headers.update({
                            'Host': 'tuongtaccheo.com',
                            'referer': 'https://tuongtaccheo.com/kiemtien/',
                            'sec-fetch-mode': 'cors',
                            'accept': '*/*',
                            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'cookie': cookies_ttc,
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                            'sec-fetch-site': 'same-origin',
                            'origin': 'https://tuongtaccheo.com',
                            'sec-fetch-dest': 'empty',
                            'x-requested-with': 'XMLHttpRequest',
                        })
                        data = {
                            'id': self.idpost
                        }
                        response2 = r.post('https://tuongtaccheo.com/kiemtien/nhantien.php', data=data).text
                        if 'Th\xc3\xa0nh c\xc3\xb4ng' in str(response2):
                            try:
                                self.dapat_berapa = re.search('c\xe1\xbb\x99ng (.*?) xu', str(response2)).group(1)
                                self.username, self.koin = Login().Cek_Tuongtaccheo(cookies_ttc)
                            except (AttributeError):
                                self.dapat_berapa, self.username, self.koin = (600, 'null', 404)
                            print(Panel(f"""[bold white]Status :[italic green] Liked successfully[/]\n[bold white]Link :[bold red] https://web.facebook.com/{str(self.idpost)[:23]}\n[bold white]Koin :[bold green] +{self.dapat_berapa}[bold white] >[bold yellow] {self.koin}""", width=63, style="bold bright_white", title=">>> Sukses <<<"))
                            Sukses.append(self.idpost)
                        elif "B\xe1\xba\xa1n ch\xc6\xb0a like ID n\xc3\xa0y, vui l\xc3\xb2ng t\xe1\xba\xa3i l\xe1\xba\xa1i l\xc3\xa0m l\xe1\xba\xa1i" in str(response2):
                            print(f"[bold bright_white]   ╰─>[bold red] Anda Belum Menyukai Postingan Ini...", end='\r')
                            time.sleep(2.5)
                            Gagal.append(self.idpost)
                            continue
                        else:
                            Gagal.append(self.idpost)
                            continue
                    else:
                        Gagal.append(self.idpost)
                        continue
            else:
                print(f"[bold bright_white]   ╰─>[bold red] Tidak Ada Misi...                 ", end='\r')
                time.sleep(5)
                return 1
    def Get_Data_Likes(self, cookies_fb, target_id):
        with requests.Session() as r:
            r.headers.update({
                'Host': 'web.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id,en;q=0.9',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'sec-fetch-site': 'none',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-mode': 'navigate',
            })
            response = r.get(f'https://web.facebook.com/{target_id}', cookies={'cookie': cookies_fb}).text
            try:
                self.lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                self.actorID = re.search('"actorID":"(\\d+)"', str(response)).group(1)
                self.__hs = re.search('"haste_session":"(.*?)"', str(response)).group(1)
                self.all_spin__ = re.search('"__spin_r":(\\d+),"__spin_b":"(.*?)","__spin_t":(\\d+),', str(response))
                self.__spin_r, self.__spin_b, self.__spin_t = self.all_spin__.group(1), self.all_spin__.group(2), self.all_spin__.group(3)
                self.__hsi = re.search('"hsi":"(\\d+)"', str(response)).group(1)
                self.fb_dtsg = re.search('"DTSGInitData",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                self.jazoest = re.search('&jazoest=(\\d+)"', str(response)).group(1)
                self.feedback_id = re.search('feedback":{"id":"(.*?)"', str(response)).group(1)
                self.tracking = re.findall('"encrypted_tracking":"(.*?)"', str(response))[3]
            except (AttributeError, IndexError):
                print(f"[bold bright_white]   ╰─>[bold yellow] AttributeError...                 ", end='\r')
                time.sleep(1.5)
                return 1
            self.status = self.Submit_Likes(cookies_fb, target_id, self.lsd, self.actorID, self.__hs, self.__spin_r, self.__spin_b, self.__spin_t, self.__hsi, self.fb_dtsg, self.jazoest, self.feedback_id, self.tracking)
            if self.status == 'Sukses':
                return 'Sukses'
            else:
                return 'Gagal'

    def Submit_Likes(self, cookies_fb, target_id, lsd, actorID, __hs, __spin_r, __spin_b, __spin_t, __hsi, fb_dtsg, jazoest, feedback_id, tracking):
        with requests.Session() as r:
            r.headers.update({
                'referer': 'https://web.facebook.com/',
                'x-fb-friendly-name': 'CometUFIFeedbackReactMutation',
                'accept': '*/*',
                'Host': 'web.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'accept-language': 'id,en;q=0.9',
                'x-asbd-id': '198387',
                'origin': 'https://web.facebook.com',
                'sec-fetch-dest': 'empty',
                'sec-fetch-site': 'same-origin',
                'x-fb-lsd': lsd,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-mode': 'cors',
            })
            data = {
                '__rev': __spin_r,
                'av': actorID,
                'fb_api_caller_class': 'RelayModern',
                '__user': actorID,
                '__hs': __hs,
                'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
                '__ccg': 'GOOD',
                '__hsi': __hsi,
                'server_timestamps': True,
                'fb_dtsg': fb_dtsg,
                '__a': '1',
                'jazoest': jazoest,
                'lsd': lsd,
                '__spin_b': __spin_b,
                '__csr': '',
                '__s': 'nuoh4g:afciv2:spgqb1',
                '__comet_req': '15',
                'doc_id': '5703418209680126',
                '__dyn': '',
                '__req': 's',
                '__spin_r': __spin_r,
                'dpr': '1.5',
                'variables': f'{{"input":{{"attribution_id_v2":"CometSinglePostRoot.react,comet.post.single,via_cold_start,1684054738994,342738,,","feedback_id":"{feedback_id}","feedback_reaction_id":"1635855486666999","feedback_source":"OBJECT","is_tracking_encrypted":true,"tracking":["{tracking}"],"session_id":"fa3b7bd8-b923-4a9e-8f43-5dd993158af5","actor_id":"{actorID}","client_mutation_id":"1"}},"useDefaultActor":false,"scale":1.5}}',
                '__spin_t': __spin_t,
            }
            response = r.post('https://web.facebook.com/api/graphql/', data=data, cookies={'cookie': cookies_fb}).text
            if '"can_viewer_react":true' in str(response):
                print(f"[bold bright_white]   ╰─>[bold green] Likes @{target_id} Sukses...           ", end='\r')
                time.sleep(0.5)
                return 'Sukses'
            else:
                print(f"[bold bright_white]   ╰─>[bold red] Likes @{target_id} Gagal...              ", end='\r')
                time.sleep(0.5)
                return 'Gagal'

    def Tuongtaccheo_Follow(self, cookies_ttc, cookies_fb, delay):
        with requests.Session() as r:
            r.headers.update({
                'Host': 'tuongtaccheo.com',
                'referer': 'https://tuongtaccheo.com/kiemtien/subcheo/',
                'sec-fetch-mode': 'cors',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'cookie': cookies_ttc,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'sec-fetch-dest': 'empty',
                'accept-language': 'en-US,en;q=0.9',
            })
            response = r.get('https://tuongtaccheo.com/kiemtien/subcheo/getpost.php')
            
            if '"idpost":' in response.text:
                for z in json.loads(response.text):
                    self.idpost, self.profile_url = z['idpost'], z['link'].replace('\\\\', '')
                    r.headers.clear()
                    r.cookies.clear()
                    
                    for sleep in range(delay, 0, -1):
                        time.sleep(1)
                        print(f"[bold bright_white]   ╰─>[bold blue] {self.idpost}[bold white]/[bold green]{sleep}[bold white] Sukses:-[bold blue]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Gagal)}[bold white]    ", end='\r')
                    
                    self.status = self.Get_Data_Follow(cookies_fb, self.idpost)
                    
                    if self.status == 'Sukses':
                        time.sleep(5)
                        r.headers.update({
                            'Host': 'tuongtaccheo.com',
                            'referer': 'https://tuongtaccheo.com/kiemtien/subcheo/',
                            'sec-fetch-mode': 'cors',
                            'accept': '*/*',
                            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'cookie': cookies_ttc,
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                            'sec-fetch-site': 'same-origin',
                            'origin': 'https://tuongtaccheo.com',
                            'sec-fetch-dest': 'empty',
                            'x-requested-with': 'XMLHttpRequest',
                        })
                        
                        data = {'id': self.idpost}
                        response2 = r.post('https://tuongtaccheo.com/kiemtien/subcheo/nhantien.php', data=data).text
                        
                        if 'Th\xc3\xa0nh c\xc3\xb4ng' in response2:
                            try:
                                self.dapat_berapa = re.search('c\xe1\xbb\x99ng (.*?) xu', response2).group(1)
                                self.username, self.koin = Login().Cek_Tuongtaccheo(cookies_ttc)
                            except AttributeError:
                                self.dapat_berapa, self.username, self.koin = (600, 'null', 404)
                            
                            print(Panel(f"""[bold white]Status :[italic green] Following successfully[/]\n[bold white]Link :[bold red] https://web.facebook.com/{self.idpost}\n[bold white]Koin :[bold green] +{self.dapat_berapa}[bold white] >[bold yellow] {self.koin}""", width=63, style="bold bright_white", title=">>> Sukses <<<"))
                            Sukses.append(self.idpost)
                        
                        elif 'H\xc3\xa3y m\xe1\xbb\x9f cho ng\xc6\xb0\xe1\xbb\x9di l\xe1\xba\xa1 xem danh s\xc3\xa1ch ng\xc6\xb0\xe1\xbb\x9di,trang m\xc3\xa0 b\xe1\xba\xa1n theo d\xc3\xb5i.' in response2:
                            print(Panel(f"[italic red]Buka Untuk Orang Asing Daftar Orang Dan Halaman Yang Anda Ikuti. Coba Gunakan Tangan Anda Untuk Mendapatkan Koin, Jika Anda Telah Mengikuti/Menyukai Pekerjaan Tersebut Dan Muncul Kembali, Batalkan Dan Lakukan Lagi!", width=63, style="bold bright_white", title=">>> Error <<<"))
                            exit()
                        
                        elif "B\xe1\xba\xa1n ch\xc6\xb0a theo d\xc3\xb5i nick n\xc3\xa0y, vui l\xc3\xb2ng t\xe1\xba\xa3i l\xe1\xba\xa1i l\xc3\xa0m l\xe1\xba\xa1i" in response2:
                            print(f"[bold bright_white]   ╰─>[bold red] Anda Belum Mengikuti Nick Ini...", end='\r')
                            time.sleep(2.5)
                            Gagal.append(self.idpost)
                            continue
                        
                        else:
                            Gagal.append(self.idpost)
                            continue
                        
                    else:
                        Gagal.append(self.idpost)
                        continue
                    
            else:
                print(f"[bold bright_white]   ╰─>[bold red] Tidak Ada Misi...                 ", end='\r')
                time.sleep(5)
                return 1
    

    def Get_Data_Follow(self, cookies_fb, target_id):
        with requests.Session() as r:
            r.headers.update({
                'Host': 'web.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id,en;q=0.9',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'sec-fetch-site': 'none',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-mode': 'navigate',
            })
            response = r.get(f'https://web.facebook.com/{target_id}', cookies={'cookie': cookies_fb}).text
            try:
                self.lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                self.actorID = re.search('"actorID":"(\\d+)"', str(response)).group(1)
                self.__hs = re.search('"haste_session":"(.*?)"', str(response)).group(1)
                self.all_spin__ = re.search('"__spin_r":(\\d+),"__spin_b":"(.*?)","__spin_t":(\\d+),', str(response))
                self.__spin_r, self.__spin_b, self.__spin_t = self.all_spin__.group(1), self.all_spin__.group(2), self.all_spin__.group(3)
                self.__hsi = re.search('"hsi":"(\\d+)"', str(response)).group(1)
                self.fb_dtsg = re.search('"DTSGInitData",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                self.jazoest = re.search('&jazoest=(\\d+)"', str(response)).group(1)
            except (AttributeError, IndexError):
                print(f"[bold bright_white]   ╰─>[bold yellow] AttributeError...                 ", end='\r')
                time.sleep(1.5)
                return 1
            self.status = self.Submit_Follow(cookies_fb, target_id, self.lsd, self.actorID, self.__hs, self.__spin_r, self.__spin_b, self.__spin_t, self.__hsi, self.fb_dtsg, self.jazoest)
            if self.status == 'Sukses':
                return 'Sukses'
            else:
                return 'Gagal'

    def Submit_Follow(self, cookies_fb, target_id, lsd, actorID, __hs, __spin_r, __spin_b, __spin_t, __hsi, fb_dtsg, jazoest):
        with requests.Session() as r:
            r.headers.update({
                'referer': 'https://web.facebook.com/',
                'x-fb-friendly-name': 'CometUserFollowMutation',
                'accept': '*/*',
                'Host': 'web.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'accept-language': 'id,en;q=0.9',
                'x-asbd-id': '198387',
                'origin': 'https://web.facebook.com',
                'sec-fetch-dest': 'empty',
                'sec-fetch-site': 'same-origin',
                'x-fb-lsd': lsd,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-mode': 'cors',
            })
            data = {
                '__rev': __spin_r,
                'av': actorID,
                'fb_api_caller_class': 'RelayModern',
                '__user': actorID,
                '__hs': __hs,
                'fb_api_req_friendly_name': 'CometUserFollowMutation',
                '__ccg': 'GOOD',
                '__hsi': __hsi,
                'server_timestamps': True,
                'fb_dtsg': fb_dtsg,
                '__a': '1',
                'jazoest': jazoest,
                'lsd': lsd,
                '__spin_b': __spin_b,
                '__csr': '',
                '__s': '66tl9r:afciv2:6uzrkk',
                '__comet_req': '8',
                'doc_id': '6808144429201900',
                '__dyn': '',
                '__req': 's',
                '__spin_r': __spin_r,
                'dpr': '1.5',
                'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1684058243113,789303,190055527696468,","subscribe_location":"PROFILE","subscribee_id":"' + str(target_id) + '","actor_id":"' + str(actorID) + '","client_mutation_id":"1"},"scale":1.5}',
                '__spin_t': __spin_t,
            }
            response = r.post('https://web.facebook.com/api/graphql/', data=data, cookies={'cookie': cookies_fb}).text
            if '"actor_subscribe":{"subscribee":' in str(response):
                print(f"[bold bright_white]   ╰─>[bold green] Follow @{target_id} Sukses...           ", end='\r')
                time.sleep(0.5)
                return 'Sukses'
            elif 'A server error field_exception occured. Check server logs for details.' in str(response):
                if str(target_id) == '100006609458697':
                    return 'Gagal'
                else:
                    print(Panel(f"[italic red]Sepertinya Akun Facebook Kamu Telah Terblokir Silahkan Tunggu 24 Jam Atau Ganti Cookies Akun Facebook Kamu!", width=63, style="bold bright_white", title=">>> Terblokir <<<"))
                    exit()
            else:
                print(f"[bold bright_white]   ╰─>[bold red] Follow @{target_id} Gagal...              ", end='\r')
                time.sleep(0.5)
                return 'Gagal'

if __name__ == '__main__':
    try:
        os.system('git pull')
        if os.path.exists('Data/Subscribe.json') == False:
            youtube_video = requests.get('https://raw.githubusercontent.com/RozhakXD/Tuongtaccheo/main/Data/Youtube.json').json()['Youtube']
            os.system(f'xdg-open {youtube_video}')
            with open('Data/Subscribe.json', 'w') as w:
                w.write(json.dumps({
                    "Sudah": True
                }))
            w.close()
            time.sleep(2.5)
            Daftar().Menu()
        else:
            Daftar().Menu()
    except (KeyboardInterrupt):
        exit()
    except (Exception) as e:
        print(Panel(f"[italic red]{str(e).title()}!", width=63, style="bold bright_white", title=">>> Error <<<"))
        exit()