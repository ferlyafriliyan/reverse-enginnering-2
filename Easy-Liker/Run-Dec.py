#!/usr/bin/env python3
from requests.exceptions import TooManyRedirects
import requests, re, os, time
from requests.exceptions import ConnectionError
from rich.columns import Columns
from rich.panel import Panel
from rich.console import Console

def Banner():
    os.system(
        'cls' if os.name == 'nt' else 'clear'
    )
    Console(style="bold bright_white", width=61).print(Panel("""[bold red]___________              .____    .__ __                 
\_   _____/ _________.__.|    |   |__|  | __ ___________ 
 |    __)_ /  ___<   |  ||    |   |  |  |/ // __ \_  __ \\
 |        \\\___ \ \___  ||    |___|  |    <\  ___/|  | \/
[bold white]/_______  /____  >/ ____||_______ \__|__|_ \\\___  >__|   
        \/     \/ \/             \/       \/    \/       
Get Facebook Likes With Easy Liker - Coded by Rozhak"""))
    return 0

Dump, Type, Postingan, Sukses, Gagal, Percobaan = [], [], [], [], [], []

class Menu:

    def Pengguna(self):
        try:
            response = requests.get('https://justpaste.it/bsk7d').text
            self.jumlah, self.online = re.search('"viewsText":"(.*?)"', str(response)).group(1), re.search('"onlineText":"(\d+)"', str(response)).group(1)
            return (self.jumlah, self.online)
        except Exception as e:
            return (0, 0)

    def Utama(self):
        Banner()
        try:
            self.cookies = open('Data/Cookie.txt', 'r').read().splitlines()
            Dump.clear()
            for cookies in self.cookies:
                try:
                    if len(cookies) == 0:
                        continue
                    else:
                        self.c_user = re.search('c_user=(\d+);', str(cookies)).group(1)
                        Dump.append(f'{cookies}|{self.c_user}')
                except (AttributeError):
                    continue
            if len(Dump) == 0:
                Console(style="bold bright_white", width=61).print(Panel(f"[italic red]Semua Cookie Yang Kamu Masukan Salah Atau Tidak Valid!", title=">>> Error <<<"));time.sleep(3.5);Login().Cookie()
            else:
                Console(style="bold bright_white").print(Columns([
                    Panel(f"[bold white]IP : [bold green]{requests.get('https://ipinfo.io/json').json()['ip']}", width=30),
                    Panel(f"[bold white]Live Cookies :[bold green] {len(Dump)}", width=30),
                ]))
        except Exception as e:
            Console(style="bold bright_white", width=61).print(Panel(f"[italic red]{str(e).title()}!", title=">>> Error <<<"));time.sleep(3.5);Login().Cookie()
        
        self.jumlah, self.online = self.Pengguna()

        Console(style="bold bright_white", width=61).print(Panel("""[bold green]1[bold white]. Tambahkan Link Postingan ([bold green]required[bold white])
[bold green]2[bold white]. Pengaturan Type Reaction
[bold green]3[bold white]. Jalankan Unlimited Reaction
[bold green]4[bold white]. Keluar ([bold red]exit[bold white])""", title=f">>> (Pengguna {self.jumlah}/{self.online} Online) <<<", subtitle="╭────", subtitle_align="left"))
        choose = Console().input("[bold bright_white]   ╰─> ")
        if choose == '1' or choose == '01':
            try:
                Console(style="bold bright_white", width=61).print(Panel("[italic white]Silahkan Masukan[italic green] Link Postingan[italic white], Misalnya :[italic green] https://www.\nfacebook.com/rozhak.xyz/posts/10160515504093544", title=">>> Postingan <<<", subtitle="╭────", subtitle_align="left"))
                postingan = Console().input("[bold bright_white]   ╰─> ")
                self.link = postingan.split('facebook.com')[1]
                with open('Data/Postingan.txt', 'w') as w:
                    w.write(f'https://www.facebook.com{self.link}')
                w.close()
                Console(style="bold bright_white", width=61).print(Panel(f"[italic green]Selamat Kamu Berhasil Mengatur Link Postingan Publik!", title=">>> Sukses <<<"));time.sleep(3.5);Menu().Utama()
            except Exception as e:
                Console(style="bold bright_white", width=61).print(Panel(f"[italic red]{str(e).title()}!", title=">>> Error <<<"));exit()
        elif choose == '2' or choose == '02':
            try:
                Console(style="bold bright_white", width=61).print(Panel("[italic white]Silahkan Masukan[italic green] Type Reaction[italic white] Dari ([italic yellow]Like,Love,Wow,Haha,\n,Sad,Angry[italic white]) Wajib Pilih Salah Satu, Misalnya :[italic green] Love", title=">>> Reaction <<<", subtitle="╭────", subtitle_align="left"))
                reaction = Console().input("[bold bright_white]   ╰─> ")
                if reaction in ['Like', 'Love', 'Haha', 'Wow', 'Sad', 'Angry']:
                    with open('Data/Reaction.txt', 'w') as w:
                        w.write(f'{reaction}')
                    w.close()
                    Console(style="bold bright_white", width=61).print(Panel(f"[italic green]Selamat Kamu Behasil Mengatur Type Reaction Atau Liker!", title=">>> Sukses <<<"));time.sleep(3.5);Menu().Utama()
                else:
                    Console(style="bold bright_white", width=61).print(Panel(f"[italic red]Type Reaction Hanya : Like,Love,Wow,Haha,Sad,Angry!", title=">>> Error <<<"));exit()
            except Exception as e:
                Console(style="bold bright_white", width=61).print(Panel(f"[italic red]{str(e).title()}!", title=">>> Error <<<"));exit()
        elif choose == '3' or choose == '03':
            try:
                if os.path.exists('Data/Postingan.txt') == False:
                    Console(style="bold bright_white", width=61).print(Panel(f"[italic red]Tampaknya Kamu Belum Pernah Mengatur Link Postingan!", title=">>> Error <<<"));exit()
                else:
                    self.reaction, self.postingan = open('Data/Reaction.txt', 'r').read().splitlines()[0], open('Data/Postingan.txt', 'r').read().splitlines()[0]
                    Type.append(self.reaction);Postingan.append(self.postingan)
                    Console(style="bold bright_white", width=61).print(Panel(f"[italic white]Untuk Delay Satu Akun[italic red] 3 Jam[italic white], Jika Reaction[italic red] Gagal[italic white] Mungkin Cookie Telah Invalid Atau Akun Di[italic green] Mode Gratis[italic white]!", title=">>> Catatan <<<"))
                    Main().Submit_Cookie(Dump)
            except Exception as e:
                Console(style="bold bright_white", width=61).print(Panel(f"[italic red]{str(e).title()}!", title=">>> Error <<<"));exit()
        elif choose == '4' or choose == '04':
            try:
                os.remove('Data/Cookie.txt');Console(style="bold bright_white", width=61).print(Panel("[italic red]Kami Sedang Mencoba Untuk Menghapus Cookie Kamu!", title=">>> Keluar <<<"));exit()
            except:exit()
        else:
            Console(style="bold bright_white", width=61).print(Panel("[italic red]Pilihan Yang Kamu Masukan Tidak Ada Di Daftar Menu!", title=">>> Keluar <<<"));time.sleep(5.5);Menu().Utama()

class Login:

    def Cookie(self):
        Banner()
        try:
            Console(style="bold bright_white", width=61).print(Panel("[italic white]Silahkan Masukan[italic green] Cookie[italic white] Facebook, Gunakan Koma '[italic red],[italic white]' Untuk Random Cookie Dan Gunakan Akun[italic red] Tumbal[italic white] Untuk Login!", title=">>> Cookies <<<", subtitle="╭────", subtitle_align="left"))
            random_cookies = Console().input("[bold bright_white]   ╰─> ")
            for cookies in random_cookies.split(','):
                with open('Data/Cookie.txt', 'a+') as w:
                    w.write(f'{cookies}\n')
                w.close()
            if len(open('Data/Cookie.txt', 'r').readlines()) == 0:
                Console(style="bold bright_white", width=61).print(Panel(f"[italic red]Semua Cookie Yang Kamu Masukan Salah Atau Tidak Valid!", title=">>> Error <<<"));exit()
            else:
                Console(style="bold bright_white", width=61).print(Panel(f"[italic green]Login Behasil Silahkan Atur Type Reaction Dan Postingan!", title=">>> Login Sukses <<<"));time.sleep(3.5);Menu().Utama()
        except Exception as e:
            Console(style="bold bright_white", width=61).print(Panel(f"[italic red]{str(e).title()}!", title=">>> Error <<<"));exit()

class Main:

    def Submit_Cookie(self, Dump):
        while True:
            for z in Dump:
                try:
                    self.cookies, self.userid = z.split('|')[0], z.split('|')[1]
                    self.Get_User_Code(self.cookies, self.userid)
                except (ConnectionError):
                    Console().print("[bold bright_white]   ╰─>[bold red] Koneksi Error...                        ", end="\r");time.sleep(7.5);continue
                except (TooManyRedirects):
                    open('TooManyRedirects.txt', 'a+').write(f'{self.cookies}\n')
                    Console().print("[bold bright_white]   ╰─>[bold red] TooManyRedirects...                     ", end="\r");time.sleep(7.5);continue
                except (AttributeError):
                    Console().print("[bold bright_white]   ╰─>[bold red] AttributeError...                       ", end="\r");time.sleep(7.5);continue
            if len(Sukses) == 0:
                Console(style="bold bright_white", width=61).print(Panel(f"[italic red]Sepertinya Semua Cookie Telah Mati Atau Di Mode Gratis!", title=">>> Error <<<"));exit()
            else:
                for sleep in range(10800, 0, -1):
                    time.sleep(1.0);Console().print(f"[bold bright_white]   ╰─>[bold white] Delay[bold green] {sleep}[bold white]/[bold green]{len(Dump)}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Gagal)}         ", end='\r')
                continue

    def Get_User_Code(self, cookies, userid):
        with requests.Session() as r:
            r.headers.update({
                'accept-language': 'en-US,en;q=0.9',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
                'Host': 'pixinsta.net',
                'sec-fetch-dest': 'document',
            })

            response = r.get('https://pixinsta.net/account/facebook/login').text
            #open('Data/Index.html', 'w').write(str(response))

            self.user_code = re.search('data-href="https://m.facebook.com/device\\?user_code=(.*?)"', str(response)).group(1)
            self._token = re.search('name="csrf-token" content="(.*?)">', str(response)).group(1)
            self.deviceCode = re.search('data-devicecode="(.*?)"', str(response)).group(1)

            self.status = self.Validate_Code(cookies, self.user_code, userid)
            if 'Login Gagal' in str(self.status):
                return ("Login Gagal")
            else:
                data = {
                    '_token': self._token,
                    'deviceCode': self.deviceCode,
                }
                r.headers.update({
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://pixinsta.net/account/facebook/login',
                    'accept': '*/*',
                    'sec-fetch-mode': 'cors',
                    'origin': 'https://pixinsta.net',
                    'x-csrf-token': self._token,
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                })
                response6 = r.post('https://pixinsta.net/account/facebook/callback', data = data, cookies = {
                    'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                }).text
                #open('Data/Index6.html', 'w').write(str(response6))

                if 'Please confirm login on your device Checking ..' in str(response6):
                    Percobaan.append(response6)
                    Console().print(f"[bold bright_white]   ╰─>[bold yellow] Login @{userid} Gagal...", end="\r");time.sleep(3.5)
                    if len(Percobaan) > 2:
                        return ("Login Gagal")
                    else:
                        self.Get_User_Code(cookies, userid)
                elif 'Login successful' in str(response6):
                    Console().print(f"[bold bright_white]   ╰─>[bold green] Login @{userid} Sukses...", end="\r");time.sleep(2.5)
                    r.headers.pop('content-type');r.headers.pop('origin')

                    r.headers.update({
                        'sec-fetch-dest': 'document',
                        'referer': 'https://pixinsta.net/account/facebook',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'sec-fetch-mode': 'navigate',
                    })

                    response7 = r.get('https://pixinsta.net/account/facebook/likes', cookies = {
                        'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                    }).text
                    #open('Data/Index7.html', 'w').write(str(response7))
                    if 'Time to add new campaign' in str(response7):
                        self.campaign = re.search('Time to add new campaign.*?">(\d+)', str(response7)).group(1)
                        Console().print(f"[bold bright_white]   ╰─>[bold red] Limit @{userid}/{self.campaign} User...", end="\r");time.sleep(3.5)
                        return ("Limit")
                    else:
                        self.formToken = re.search('name="formToken" value="(.*?)">', str(response7)).group(1)
                        r.headers.update({
                            'content-type': 'application/x-www-form-urlencoded',
                            'referer': 'https://pixinsta.net/account/facebook/likes',
                            'origin': 'https://pixinsta.net',
                        })
                        data = {
                            'formToken': self.formToken,
                            'post_url': Postingan[0],
                            'type': Type[0].lower(),
                            '_token': self._token,
                        }
                        response8 = r.post('https://pixinsta.net/account/facebook/likes', data = data, cookies = {
                            'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                        }).text
                        #open('Data/Index8.html', 'w').write(str(response8))
                        if 'Campaign added successfully' in str(response8):
                            Console(style="bold bright_white", width=61).print(Panel(f"""[bold white]Status :[bold green] +20[bold white] >[bold red] Sedang Diproses
[bold white]Link :[bold green] {Postingan[0][:50]}
[bold white]Reaction :[bold red] {Type[0]}""", title=">>> Sukses <<<"))
                            Sukses.append(response8)
                            return ("Sukses")
                        elif 'Post url is invalid' in str(response8):
                            Console(style="bold bright_white", width=61).print(Panel(f"[italic red]Link Postingan Yang Kamu Masukan Tidak Bisa Digunakan!", title=">>> Error <<<"));exit()
                        else:
                            Console().print(f"[bold bright_white]   ╰─>[bold red] Submit @{userid} Gagal...", end="\r");time.sleep(3.5)
                            Gagal.append(response8)
                            return ("Submit Gagal")
                else:
                    Console().print(f"[bold bright_white]   ╰─>[bold red] Login @{userid} Gagal...", end="\r");time.sleep(3.5)
                    return ("Error")

    def Validate_Code(self, cookies, user_code, userid):
        with requests.Session() as r:
            r.headers.update({
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-site': 'none',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Host': 'mbasic.facebook.com',
                'sec-fetch-dest': 'document',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
                'sec-fetch-mode': 'navigate',
            })
            response2 = r.get('https://mbasic.facebook.com/device?_rdc=1&_rdr', cookies = {
                'cookie': cookies
            }).text
            #open('Data/Index2.html', 'w').write(str(response2))
            if '/login/?next=' in str(response2):
                Console().print(f"[bold bright_white]   ╰─>[bold red] Bagaimana Anda ingin masuk ke Facebook?", end="\r");time.sleep(2.5)
                return ("Login Gagal")
            else:
                self.next_action = re.search('method="post" action="(.*?)"', str(response2)).group(1).replace('amp;', '')
                self.jazoest = re.search('name="jazoest" value="(.*?)"', str(response2)).group(1)
                self.fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
                r.headers.update({
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://mbasic.facebook.com',
                    'sec-fetch-site': 'same-origin',
                    'referer': 'https://mbasic.facebook.com/device?_rdc=1&_rdr',
                })
                data = {
                    'fb_dtsg': self.fb_dtsg,
                    'jazoest': self.jazoest,
                    'qr': '0',
                    'user_code': user_code,
                }
                response3 = r.post('https://mbasic.facebook.com{}'.format(self.next_action), data = data, cookies = {
                    'cookie': cookies
                })
                #open('Data/Index3.html', 'w').write(str(response3.text))
                if 'https://mbasic.facebook.com/zero/toggle/nux/' in str(response3.url):
                    Console().print(f"[bold bright_white]   ╰─>[bold red] Akun Terkena Mode Gratis...", end="\r");time.sleep(2.5)
                    return ("Login Gagal")
                elif 'https://mbasic.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
                    r.headers.pop('content-type');r.headers.pop('origin')
                    response4 = r.get(response3.url, cookies = {
                        'cookie': cookies
                    }).text
                    #open('Data/Index4.html', 'w').write(str(response4))

                    self.next_action = re.search('method="post" action="(.*?)"', str(response4)).group(1).replace('amp;', '')
                    self.jazoest = re.search('name="jazoest" value="(.*?)"', str(response4)).group(1)
                    self.fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
                    self.from_post = re.search('name="from_post" value="(.*?)"', str(response4)).group(1)
                    self.response_type = re.search('name="response_type" value="(.*?)"', str(response4)).group(1)
                    self.auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
                    self.dialog_type = re.search('name="dialog_type" value="(.*?)"', str(response4)).group(1)
                    self.return_format = re.search('name="return_format" value="(.*?)"', str(response4)).group(1)
                    self.scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
                    self.logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
                    self.sheet_name = re.search('name="sheet_name" value="(.*?)"', str(response4)).group(1)
                    self.user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
                    self.tp = re.search('name="tp" value="(.*?)"', str(response4)).group(1)
                    self.encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
                    self.__CONFIRM__ = re.search('<input value="(.*?)" type="submit" name="__CONFIRM__" class=', str(response4)).group(1)

                    data = {
                        'dialog_type': self.dialog_type,
                        'jazoest': self.jazoest,
                        'response_type': self.response_type,
                        'fb_dtsg': self.fb_dtsg,
                        'auth_type': self.auth_type,
                        'scope': self.scope,
                        'return_format': self.return_format,
                        'logger_id': self.logger_id,
                        'from_post': self.from_post,
                        'tp': self.tp,
                        'sheet_name': self.sheet_name,
                        '__CONFIRM__': self.__CONFIRM__,
                        'user_code': user_code,
                        'encrypted_post_body': self.encrypted_post_body,
                    }
                    r.headers.update({
                        'content-type': 'application/x-www-form-urlencoded',
                    })
                    response5 = r.post('https://mbasic.facebook.com{}'.format(self.next_action), data = data, cookies = {
                        'cookie': cookies
                    })
                    #open('Data/Index5.html', 'w').write(str(response5.text))
                    if 'Kesalahan Masuk' in str(response5.text):
                        self.seen_scopes = re.search('name="seen_scopes" value="(.*?)"', str(response4)).group(1)
                        self.read = re.search('name="read" value="(.*?)"', str(response4)).group(1)
                        
                        data.update({
                            'seen_scopes': self.seen_scopes,
                            'read': self.read,
                        })
                        response10 = r.post('https://mbasic.facebook.com{}'.format(self.next_action), data = data, cookies = {
                            'cookie': cookies
                        })
                        #open('Data/Index10.html', 'w').write(str(response10.text))
                        if 'https://mbasic.facebook.com/device/logged_in/?user_code=' in str(response10):
                            Console().print(f"[bold bright_white]   ╰─>[bold green] Login Sukses...", end="\r");time.sleep(2.5)
                            return ("Login Sukses")
                        else:
                            Percobaan.append(response10)
                            Console().print(f"[bold bright_white]   ╰─>[bold yellow] Login Gagal...", end="\r");time.sleep(3.5)
                            if len(Percobaan) > 2:
                                return ("Login Gagal")
                            else:
                                self.Get_User_Code(cookies, userid)
                    else:
                        Console().print(f"[bold bright_white]   ╰─>[bold green] Login Sukses...", end="\r");time.sleep(2.5)
                        return ("Login Sukses")
                else:
                    Console().print(f"[bold bright_white]   ╰─>[bold blue] Kami menangguhkan akun Anda!", end="\r");time.sleep(2.5)
                    return ("Login Gagal")

if __name__ == '__main__':
    try:
        if int(re.search('columns=(\d+),', str(os.get_terminal_size())).group(1)) < 61:
            Console(style="bold bright_white", width=61).print(Panel(f"[italic red]Silahkan Kecilkan Tampilan Termux Lalu Coba Lagi!", title=">>> Error <<<"));exit()
        if os.path.exists('Data/Pengguna.txt') == False:
            os.system(f'xdg-open {requests.get("https://raw.githubusercontent.com/RozhakXD/Easy-Liker/main/Data/Youtube.json").json()["Youtube"]}');time.sleep(3.5)
            with open('Data/Pengguna.txt', 'w') as w:
                w.write('Lama')
            w.close()
            os.system('git pull');Menu().Utama()
        else:
            os.system('git pull');Menu().Utama()
    except Exception as e:
        print(e)