#!/usr/bin/env python3
try:
    import requests, datetime, re, os, time, json, random, string
    from rich.columns import Columns
    from rich.panel import Panel
    from requests_toolbelt import MultipartEncoder
    from rich import print
    from rich.console import Console
    from rich.tree import Tree
    from requests.exceptions import RequestException
except (Exception, KeyboardInterrupt) as e:
    exit(f"[Error] {str(e).title()}")

Dump, Image, Sukses, Gagal, Teks, Gambar, Komentar = [], {"Type": "Satu"}, [], [], {"Teks": "Satu"}, [], {"Type": "Satu"}

def Banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    Console(width=65, style="bold deep_sky_blue3").print(Panel("""   [bold blue]||Author : Rozhak||Github : @RozhakXD||Version : 10.0||
[bold red]_________                                       __          
\_   ___ \  ____   _____   _____   ____   _____/  |_  ______
/    \  \/ /  _ \ /     \ /     \_/ __ \ /    \   __\/  ___/
\     \___(  <_> )  Y Y  \  Y Y  \  ___/|   |  \  |  \___ \ 
 \______  /\____/|__|_|  /__|_|  /\___  >___|  /__| /____  >
        \/             \/      \/     \/     \/          \/ 
[bold green]\t\tFacebook Comments Timeline""")) # Coded by Rozhak-XD

class Login:

    def Cek_Login(self, cookies):
        with requests.Session() as r:
            r.headers.update({
                'sec-fetch-mode': 'navigate',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'Host': 'mobile.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-dest': 'document',
                'sec-fetch-site': 'same-origin',
            })
            response = r.get('https://mobile.facebook.com/?_rdc=1&_rdr', cookies = {
                'cookie': cookies
            }).text
            self.find_account = re.search('"USER_ID":"(\d+)","NAME":"(.*?)"', str(response))
        return (self.find_account.group(2), self.find_account.group(1))

    def Cookies(self):
        try:
            Banner()
            print(Panel("[italic white]Silahkan Masukan[italic green] Cookie Facebook[italic white], Pastikan Tidak Menggunakan[italic red] Mode Gratis[italic white] Dan Menggunakan Bahasa Indonesia!", width=65, style="bold deep_sky_blue3", title = "[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Catatan[bold red] <[bold yellow]<[bold green]<", subtitle="[bold deep_sky_blue3]╭────", subtitle_align="left"))
            cookies = Console().input("[bold deep_sky_blue3]   ╰─> ")
            self.name, self.id = self.Cek_Login(cookies)
            print(Panel(f"""[bold white]Nama :[bold green] {self.name.title()}
[bold white]User :[bold yellow] https://m.facebook.com/profile.php?id={self.id}""", width=65, style="bold deep_sky_blue3", title = "[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Welcome[bold red] <[bold yellow]<[bold green]<"))
            with open('Data/Cookie.json', 'w') as w:
                w.write(json.dumps({
                    'Cookie': cookies
                }))
            w.close()
            Daftar().Menu()
        except Exception as e:
            print(Panel(f"[italic red]{str(e).title()}!", width=65, style="bold deep_sky_blue3", title="[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Error[bold red] <[bold yellow]<[bold green]<"));exit()

class Daftar:

    def Menu(self):
        try:
            Banner()
            self.cookies = json.loads(open('Data/Cookie.json', 'r').read())['Cookie']
            self.name, self.id = Login().Cek_Login(self.cookies)
            print(Columns([
                Panel(f"[bold white]Name :[bold green] {self.name[:20]}", width=32, style="bold deep_sky_blue3"), 
                Panel(f"[bold white]User :[bold yellow] {self.id[:20]}", width=32, style="bold deep_sky_blue3")
            ]))
        except Exception as e:
            print(Panel(f"[italic red]{str(e).title()}!", width=65, style="bold deep_sky_blue3", title="[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Error[bold red] <[bold yellow]<[bold green]<"))
            time.sleep(2.5);Login().Cookies()

        self.jumlah, self.online = Pengguna_Online()

        print(Panel("""[bold green]1.[bold white] Komentar Gambar Dan Reaction ([bold green]Ephoto360[bold white])
[bold green]2.[bold white] Komentar Dan Reaction ([bold green]Textpro.me[bold white])
[bold green]3.[bold white] Ganti Teks Komentar Bergambar
[bold green]4.[bold white] Komentar Gambar Target ([bold green]New[bold white])
[bold green]5.[bold white] Keluar ([bold red]Exit[bold white])""", width=65, style="bold deep_sky_blue3", title = f"[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] (Pengguna {self.jumlah}/{self.online} Online)[bold red] <[bold yellow]<[bold green]<", subtitle="[bold deep_sky_blue3]╭────", subtitle_align="left"))
        choose = Console().input("[bold deep_sky_blue3]   ╰─> ")
        if choose == '01' or choose == '1':
            try:
                print(Panel("[italic white]Silahkan Masukan[italic green] Delay[italic white] Atau Jeda Reaction Dan Komentar, Saya Sarankan Menggunakan Delay[italic red] 60-180 Detik[italic white], Misalnya :[italic green] 60 Detik", width=65, style="bold deep_sky_blue3", title = "[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Catatan[bold red] <[bold yellow]<[bold green]<", subtitle="[bold deep_sky_blue3]╭────", subtitle_align="left"))
                delay = int(Console().input("[bold deep_sky_blue3]   ╰─> "))
                print(Panel("[italic white]Sedang Menjalankan[italic green] Komentar[italic white] Dan[italic green] Reaction[italic white], Jika Muncul Tulisan[italic red] Error[italic white] Abaikan Saja, Tekan[italic yellow] CTRL + Z[italic white] Untuk Berhenti!", width=65, style="bold deep_sky_blue3", title = "[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Catatan[bold red] <[bold yellow]<[bold green]<"))
                Image.update({
                    "Type": "Dua"
                })
                while True:
                    try:
                        Likes_Komentar().Get_Postingan(self.cookies, delay)
                    except (RequestException) as e:
                        print("[bold deep_sky_blue3]   ╰─>[bold yellow] RequestException!             ", end='\r');time.sleep(7.5)
                        continue
                    except (KeyboardInterrupt):
                        continue
            except Exception as e:
                print(Panel(f"[italic red]{str(e).title()}!", width=65, style="bold deep_sky_blue3", title="[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Error[bold red] <[bold yellow]<[bold green]<"));exit()
        elif choose == '02' or choose == '2':
            try:
                print(Panel("[italic white]Silahkan Masukan[italic green] Delay[italic white] Atau Jeda Reaction Dan Komentar, Saya Sarankan Menggunakan Delay[italic red] 60-180 Detik[italic white], Misalnya :[italic green] 60 Detik", width=65, style="bold deep_sky_blue3", title = "[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Catatan[bold red] <[bold yellow]<[bold green]<", subtitle="[bold deep_sky_blue3]╭────", subtitle_align="left"))
                delay = int(Console().input("[bold deep_sky_blue3]   ╰─> "))
                print(Panel("[italic white]Sedang Menjalankan[italic green] Komentar[italic white] Dan[italic green] Reaction[italic white], Jika Muncul Tulisan[italic red] Error[italic white] Abaikan Saja, Tekan[italic yellow] CTRL + Z[italic white] Untuk Berhenti!", width=65, style="bold deep_sky_blue3", title = "[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Catatan[bold red] <[bold yellow]<[bold green]<"))
                while True:
                    try:
                        Likes_Komentar().Get_Postingan(self.cookies, delay)
                    except (RequestException) as e:
                        print("[bold deep_sky_blue3]   ╰─>[bold yellow] RequestException!             ", end='\r');time.sleep(7.5)
                        continue
                    except (KeyboardInterrupt):
                        continue
            except Exception as e:
                print(Panel(f"[italic red]{str(e).title()}!", width=65, style="bold deep_sky_blue3", title="[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Error[bold red] <[bold yellow]<[bold green]<"));exit()
        elif choose == '03' or choose == '3':
            try:
                print(Panel("[italic white]Silahkan Masukan[italic green] Teks[italic white] Komentar, Gunakan ',' Untuk Komentar Berbeda Dan Gunakan '{}' Untuk Tag Name, Pastikan '{}' Hanya Satu, Misalnya :[italic green] Hallo Bang {},Keren {}", width=65, style="bold deep_sky_blue3", title = "[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Catatan[bold red] <[bold yellow]<[bold green]<", subtitle="[bold deep_sky_blue3]╭────", subtitle_align="left"))
                teks = Console().input("[bold deep_sky_blue3]   ╰─> ")
                if os.path.exists('Komentar/Teks.txt') == True:
                    os.remove('Komentar/Teks.txt')
                for z in teks.split(','):
                    finds_kurawal = re.findall('{}', str(z))
                    if len(finds_kurawal) == 1:
                        with open('Komentar/Teks.txt', 'a+') as w:
                            w.write(f'{z}\n')
                    else:
                        continue
                if os.path.exists('Komentar/Teks.txt') == False or len(open('Komentar/Teks.txt', 'r').readlines()) < 1:
                    print(Panel("[italic red]Sepertinya Kamu Memasukan Format Komentar Dengan Salah, Silahkan Baca Lagi Catatan Nya!", width=65, style="bold deep_sky_blue3", title="[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Error[bold red] <[bold yellow]<[bold green]<"));exit()
                else:
                    print(Panel("[italic white]Selamat Kamu Berhasil Mengubah Teks Silahkan Running Ulang!", width=65, style="bold deep_sky_blue3", title = "[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Sukses[bold red] <[bold yellow]<[bold green]<"));exit()
            except Exception as e:
                print(Panel(f"[italic red]{str(e).title()}!", width=65, style="bold deep_sky_blue3", title="[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Error[bold red] <[bold yellow]<[bold green]<"));exit()
        elif choose == '4' or choose == '04':
            try:
                print(Panel("[italic white]Silahkan Masukan Link Post, Wajib Sesuai Contoh, Misalnya :[italic green] https://web.facebook.com/story.php?story_fbid=pfbid0gvEwezHWjqEMmQL9mx3FdjwtNPfEzyRimbrypQ7FSHFSBDwHV7Bt3NqVYwJHZMbcl&id=757953543", width=65, style="bold deep_sky_blue3", title = "[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Catatan[bold red] <[bold yellow]<[bold green]<", subtitle="[bold deep_sky_blue3]╭────", subtitle_align="left"))
                link_posts = Console().input("[bold deep_sky_blue3]   ╰─> ")
                if 'https://web.facebook.com/' in str(link_posts):
                    Dump.append(link_posts)
                    print(Panel("[italic white]Silahkan Masukan[italic green] Delay[italic white] Atau Jeda Reaction Dan Komentar, Saya Sarankan Menggunakan Delay[italic red] 60-180 Detik[italic white], Misalnya :[italic green] 60 Detik", width=65, style="bold deep_sky_blue3", title = "[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Catatan[bold red] <[bold yellow]<[bold green]<", subtitle="[bold deep_sky_blue3]╭────", subtitle_align="left"))
                    delay = int(Console().input("[bold deep_sky_blue3]   ╰─> "))
                    print(Panel("[italic white]Sedang Menjalankan[italic green] Komentar[italic white] Dan[italic green] Reaction[italic white], Jika Muncul Tulisan[italic red] Error[italic white] Abaikan Saja, Tekan[italic yellow] CTRL + Z[italic white] Untuk Berhenti!", width=65, style="bold deep_sky_blue3", title = "[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Catatan[bold red] <[bold yellow]<[bold green]<"))
                    Komentar.update({
                        "Type": "Dua"
                    })
                    Likes_Komentar().Get_Postingan(self.cookies, delay)
                    # RecursionError: maximum recursion depth exceeded while calling a Python object
                    exit()
                else:
                    print(Panel(f"[italic red]Format Postingan Yang Kamu Masukan Tidak Di Ketahui Server!", width=65, style="bold deep_sky_blue3", title="[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Keluar[bold red] <[bold yellow]<[bold green]<"));exit()
            except Exception as e:
                print(Panel(f"[italic red]{str(e).title()}!", width=65, style="bold deep_sky_blue3", title="[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Error[bold red] <[bold yellow]<[bold green]<"));exit()
        elif choose == '5' or choose == '05':
            try:
                print(Panel(f"[italic red]Sedang Menghapus Cookies Akun Facebook Kamu Silahkan Tunggu..", width=65, style="bold deep_sky_blue3", title="[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Keluar[bold red] <[bold yellow]<[bold green]<"))
                os.remove('Data/Cookie.json');time.sleep(2.5);exit()
            except:pass
        else:
            print(f"[bold deep_sky_blue3]   ╰─>[bold green] Pilihan Tidak Diketahui...                                ", end='\r');time.sleep(2.5);Daftar().Menu()

class Likes_Komentar:

    def Get_Postingan(self, cookies, delay):
        with requests.Session() as r:
            if Komentar['Type'] == 'Satu':
                r.headers.update({
                    'Host': 'web.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-US,en;q=0.9',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-mode': 'navigate',
                })
                response = r.get('https://web.facebook.com/', cookies = {
                    'cookie': cookies
                }).text
                self.find_all_postingan = re.findall('"story":{"creation_time":\d+,"url":"(.*?)"', str(response))
                for z in self.find_all_postingan:
                    if str(z) in str(Dump):# or 'groups' in str(z) or 'reel' in str(z):
                        continue
                    else:
                        Dump.append(f'{str(z)}')
                if len(Dump) != 0:
                    self.Eksekusi_Postingan(cookies, delay)
                else:
                    print(f"[bold deep_sky_blue3]   ╰─>[bold green] Looking for Recent Posts...     ", end='\r');time.sleep(1.5)
                    self.Get_Postingan(cookies, delay)
            else:
                self.Eksekusi_Postingan(cookies, delay)
            return 0

    def Eksekusi_Postingan(self, cookies, delay):
        with requests.Session() as r:
            for self.post_url in Dump:
                r.headers.update({
                    'Host': 'web.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-US,en;q=0.9',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-mode': 'navigate',
                })
                response = r.get(self.post_url.replace('\\', ''), cookies = {
                    'cookie': cookies
                }).text
                try:
                    self.lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                    self.actorID = re.search('"actorID":"(\d+)"', str(response)).group(1)
                    self.__hs = re.search('"haste_session":"(.*?)"', str(response)).group(1)
                    self.all_spin__ = re.search('"__spin_r":(\d+),"__spin_b":"(.*?)","__spin_t":(\d+),', str(response))
                    self.__spin_r, self.__spin_b, self.__spin_t = self.all_spin__.group(1), self.all_spin__.group(2), self.all_spin__.group(3)
                    self.__hsi = re.search('"hsi":"(\d+)"', str(response)).group(1)
                    self.fb_dtsg = re.search('"DTSGInitData",\\[\\],{"token":"(.*?)",', str(response)).group(1)
                    self.jazoest = re.search('&jazoest=(\d+)"', str(response)).group(1)
                    self.feedback_id = re.search('{"__typename":"CommentComposerLiveTypingBroadcastPlugin","feedback_id":"(.*?)"', str(response)).group(1)
                    self.tracking = re.search('"encrypted_tracking":"(.*?)"', str(response)).group(1)
                    self.story = re.search('"story":{"id":".*?","actors":\\[{"__typename":"User","name":"(.*?)","id":"(\d+)"', str(response))
                    self.name, self.ids = self.story.group(1), self.story.group(2)
                    if '"story_fbid"' in str(response):
                        self.ft_ent_identifier = re.search('{"story_fbid":"(.*?)"', str(response)).group(1)
                    else:
                        self.ft_ent_identifier = re.search('"story_token":"(.*?)"', str(response)).group(1)
                    if str(self.ft_ent_identifier) in str(open('Data/Sukses.txt', 'r').read().splitlines()):
                        continue
                    else:
                        if len(self.name) > 30:
                            self.Send_Reaction(cookies, self.lsd, self.actorID, self.__hs, self.__spin_r, self.__spin_b, self.__spin_t, self.__hsi, self.fb_dtsg, self.jazoest, self.feedback_id, self.tracking)
                            open('Data/Sukses.txt','a+').write(f'{self.post_url}\n')
                            continue
                        else:
                            for sleep in range(delay, 0, -1):
                                time.sleep(1.0);print(f"[bold deep_sky_blue3]   ╰─>[bold green] {sleep}[bold white]/[bold green]{len(Dump)}[bold white]/[bold green]{self.ids}[bold white] Sukses:-[bold yellow]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Gagal)}[bold white]     ", end = '\r')
                            if Image['Type'] == "Satu":
                                Generate_Images().Textpro(self.name)
                            else:
                                Generate_Images().Ephoto360(self.name)
                except (AttributeError, IndexError):
                    try:
                        self.Send_Reaction(cookies, self.lsd, self.actorID, self.__hs, self.__spin_r, self.__spin_b, self.__spin_t, self.__hsi, self.fb_dtsg, self.jazoest, self.feedback_id, self.tracking)
                    except Exception as e:
                        continue
                    continue
                self.Upload_Likes_Komentar(cookies, self.post_url.replace('\\', ''), self.name, self.ids, self.lsd, self.actorID, self.__hs, self.__spin_r, self.__spin_b, self.__spin_t, self.__hsi, self.fb_dtsg, self.jazoest, self.feedback_id, self.tracking, self.ft_ent_identifier)
            if Komentar['Type'] == 'Satu':
                Dump.clear()
                self.Get_Postingan(cookies, delay)
            else:
                exit()

    def Upload_Likes_Komentar(self, cookies, post_url, name, ids, lsd, actorID, __hs, __spin_r, __spin_b, __spin_t, __hsi, fb_dtsg, jazoest, feedback_id, tracking, ft_ent_identifier):
        with requests.Session() as r:
            params = {
                'target_id': actorID,
                'av': actorID,
                '__comet_req': '15',
                '__hs': __hs,
                'source': '19',
                'profile_id': actorID,
                '__req': 't',
                '__spin_b': __spin_b,
                'dpr': '1.5',
                '__hsi': __hsi,
                '__csr': '',
                '__spin_t': __spin_t,
                '__user': actorID,
                '__a': '1',
                '__ccg': 'EXCELLENT',
                '__dyn': '',
                '__s': '',
                '__rev': __spin_r,
                'fb_dtsg': fb_dtsg,
                'lsd': '',
                'jazoest': jazoest,
                '__spin_r': __spin_r,
            }
            boundary = '----WebKitFormBoundary' \
                + ''.join(random.sample(string.ascii_letters + string.digits, 16))
            r.headers.update({
                'Host': 'web.facebook.com',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'x-asbd-id': '198387',
                'origin': 'https://web.facebook.com',
                'x-fb-lsd': lsd,
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-dest': 'empty',
                'accept': '*/*',
                'content-type': 'multipart/form-data; boundary={}'.format(boundary),
                'sec-fetch-site': 'same-origin',
                'referer': 'https://web.facebook.com/',
                'sec-fetch-mode': 'cors',
            })
            with open('Data/Foto.jpg', 'rb') as q:
                self.images = q.read()
            data = MultipartEncoder({
                'file': (f'TextPro.me_{str(int(time.time()))}.jpg', self.images, 'image/jpeg'),
            }, boundary = boundary)
            response = r.post('https://web.facebook.com/ajax/ufi/upload/', params = params, data = data, cookies = {
                'cookie': cookies
            })
            try:
                self.photo_ids = json.loads(response.text.replace('for (;;);', ''))['payload']['fbid']
            except (KeyError, json.decoder.JSONDecodeError, IndexError, TypeError):
                print("[bold deep_sky_blue3]   ╰─>[bold yellow] JSONDecodeError!                             ", end='\r');time.sleep(2.5)
                return 1
            params = {
                'ft_ent_identifier': ft_ent_identifier,
                'comment_logging': '',
                'fs': '8',
                'actionsource': '0',
            }
            r.headers.update({
                'x-asbd-id': '198387',
                'content-type': 'application/x-www-form-urlencoded',
                'x-response-format': 'JSONStream',
                'x-fb-lsd': lsd,
                'Host': 'm.facebook.com',
            })
            self.comment_text = (f"""{self.Teks_Komentar(Teks['Teks'], ids)}

{datetime.datetime.now().strftime('%A, %d/%B/%Y:%H.%M.%S')}""")
            data = {
                'conversation_guide_shown': None,
                'fb_dtsg': fb_dtsg,
                'comment_text': self.comment_text,
                'lsd': lsd,
                'conversation_guide_session_id': '',
                'jazoest': jazoest,
                'waterfall_source': 'photo_comment',
                '__user': actorID,
                f'photo_ids[{self.photo_ids}]': self.photo_ids,
                'submit': 'Posting',
            }
            response2 = r.post('https://m.facebook.com/a/comment.php?fs=8&actionsource=2&comment_logging&ft_ent_identifier={}'.format(ft_ent_identifier), data = data, cookies = {
                'cookie': cookies
            })
            if 'https://mobile.facebook.com/story.php?story_fbid=' in str(response2.url) or 'https://m.facebook.com/story.php?story_fbid=' in str(response2.url):
                time.sleep(5.0)
                r.headers.update({
                    'Host': 'mobile.facebook.com',
                })
                self.reaction_type = random.choice([1,2,16,4,3,7,8])
                data = {
                    'reaction_type': self.reaction_type,
                    'jazoest': jazoest,
                    'lsd': lsd,
                    'ft_ent_identifier': ft_ent_identifier,
                    'fb_dtsg': fb_dtsg,
                }
                response3 = r.post('https://mobile.facebook.com/ufi/reaction/?story_render_location=timeline&feedback_source=0&is_sponsored=0', data = data, cookies = {
                    'cookie': cookies
                }).text
                if 'for (;;);{"payload":' in str(response3):
                    print("\r                                                                    ", end='\r')
                    tree = Tree(Panel.fit("[bold green]SUCCESSFUL COMMENTS", style="bold white"))
                    tree.add(Panel(post_url, width=61, style="bold deep_sky_blue3"))
                    tree.add(Panel(self.comment_text, width=61, style="bold deep_sky_blue3"))
                    tree.add(Columns([
                        Panel(self.name, width=30, style="bold deep_sky_blue3"),
                        Panel(self.Type_Reaction(str(self.reaction_type)), width=30, style="bold deep_sky_blue3")
                    ]))
                    print(tree);time.sleep(2.5)
                    open('Data/Sukses.txt','a+').write(f'{post_url}\n')
                    Sukses.append(f'{post_url}')
                    return 0
                else:
                    print(f"[bold deep_sky_blue3]   ╰─>[bold red] Gagal @[{ids}] Username...             ", end='\r');time.sleep(2.5)
                    Sukses.append(f'{post_url}')
                    return 4
            elif 'https://mobile.facebook.com/error/?' in str(response2.url):
                print(f"[bold deep_sky_blue3]   ╰─>[bold red] @[{ids}] Tidak Dapat Dikomentari...             ", end='\r');time.sleep(2.5)
                self.Send_Reaction(cookies, lsd, actorID, __hs, __spin_r, __spin_b, __spin_t, __hsi, fb_dtsg, jazoest, feedback_id, tracking)
                return 3
            else:
                print(f"[bold deep_sky_blue3]   ╰─>[bold yellow] Gagal @[{ids}] Username...             ", end='\r');time.sleep(2.5)
                self.Send_Reaction(cookies, lsd, actorID, __hs, __spin_r, __spin_b, __spin_t, __hsi, fb_dtsg, jazoest, feedback_id, tracking)
                return 2

    def Type_Reaction(self, numbers):
        if numbers == '1':
            return ('Like')
        elif numbers == '2':
            return ('Super')
        elif numbers == '16':
            return ('Peduli')
        elif numbers == '4':
            return ('Haha')
        elif numbers == '3':
            return ('Wow')
        elif numbers == '7':
            return ('Sedih')
        else:
            return ('Marah')
        
    def Teks_Komentar(self, numbers, object_id):
        if numbers == 'Satu':
            self.random_komentar = random.choice(open('Komentar/Teks.txt', 'r').read().splitlines()).format(f'@[{object_id}:]')
        else:
            self.random_komentar = '{}\n{}'.format(''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8)),f'@[{object_id}:]')
        return (self.random_komentar)
    
    def Send_Reaction(self, cookies, lsd, actorID, __hs, __spin_r, __spin_b, __spin_t, __hsi, fb_dtsg, jazoest, feedback_id, tracking):
        time.sleep(7.5)
        with requests.Session() as r:
            r.headers.update({
            'referer': 'https://web.facebook.com/',
            'x-fb-friendly-name': 'CometUFIFeedbackReactMutation',
            'accept': '*/*',
            'Host': 'web.facebook.com',
            'content-type': 'application/x-www-form-urlencoded',
            'accept-language': 'en-US,en;q=0.9',
            'x-asbd-id': '198387',
            'origin': 'https://web.facebook.com',
            'sec-fetch-dest': 'empty',
            'sec-fetch-site': 'same-origin',
            'x-fb-lsd': lsd,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-fetch-mode': 'cors',
        })
        self.feedback_reaction_id = (random.choice(['444813342392137', '908563459236466', '115940658764963', '613557422527858', '1678524932434102', '1635855486666999', '478547315650144']))
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
            '__s': '1mjxb8:3uueue:itbg9v',
            '__comet_req': '15',
            'doc_id': '5703418209680126',
            '__dyn': '',
            '__req': 'f',
            '__spin_r': __spin_r,
            'dpr': '1.5',
            'variables': '{"input":{"attribution_id_v2":"CometSinglePostRoot.react,comet.post.single,via_cold_start,1684059070714,710171,,","feedback_id":"' + str(feedback_id) + '","feedback_reaction_id":"' + str(self.feedback_reaction_id) + '","feedback_source":"OBJECT","is_tracking_encrypted":true,"tracking":["' + str(tracking) + '"],"session_id":"beb810fd-2143-4ffb-9e1c-3b60f46cced6","actor_id":"' + str(actorID) + '","client_mutation_id":"1"},"useDefaultActor":false,"scale":1.5}',
            '__spin_t': __spin_t,
        }
        response = r.post('https://web.facebook.com/api/graphql/', data = data, cookies = {
            'cookie': cookies
        }).text
        if '"can_viewer_react":true' in str(response):
            print(f"[bold deep_sky_blue3]   ╰─>[bold green] You Have Liked The Post...          ", end='\r');time.sleep(1.5)
            Sukses.append(str(response))
            return 0
        else:
            return 1
    
class Generate_Images:

    def Textpro(self, name):
        if os.path.exists('Data/Foto.jpg') == True:
            os.remove('Data/Foto.jpg')
        with requests.Session() as r:
            r.headers.update({
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'host': 'textpro.me',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'en-US,en;q=0.9',
            })
            self.url_textpro = self.Get_Textpro()
            response2 = r.get(self.url_textpro).text
            boundary = '----WebKitFormBoundary' \
                + ''.join(random.sample(string.ascii_letters + string.digits, 16))
            r.headers.update({
                'content-type': 'multipart/form-data; boundary={}'.format(boundary)
            })
            try:
                self.token = re.search('name="token" value="(.*?)"', str(response2)).group(1)
                self.build_server = re.search('name="build_server" value="(.*?)"', str(response2)).group(1)
                self.build_server_id = re.search('name="build_server_id" value="(.*?)"', str(response2)).group(1)
            except (AttributeError):
                print(f"[bold deep_sky_blue3]   ╰─>[bold red] AttributeError...                     ", end='\r');time.sleep(1.5)
                self.Textpro(name)

            if 'Background*' in str(response2):
                print(f"[bold deep_sky_blue3]   ╰─>[bold red] Background...                           ", end='\r');time.sleep(1.5)
                self.Textpro(name)
            else:
                data = MultipartEncoder({
                    'token': (None, self.token),
                    'text[]': (None, name),
                    'build_server_id': (None, self.build_server_id),
                    'submit': (None, 'Go'),
                    'build_server': (None, self.build_server),
                }, boundary = boundary)
                response3 = r.post(self.url_textpro, data = data).text
                if 'You must enter this field' in str(response3):
                    print(f"[bold deep_sky_blue3]   ╰─>[bold yellow] You Must Enter This Field...           ", end='\r');time.sleep(1.5)
                    self.Textpro(name)
                else:
                    try:
                        self.find_data = re.search('">{"id":"(\d+)","token":"(.*?)","text":\\["(.*?)"\\],"build_server_id":"(\d+)","build_server":"(.*?)","sign":"(.*?)"}', str(response3))
                        self.id, self.text, self.token, self.build_server, self.build_server_id, self.sign = self.find_data.group(1), self.find_data.group(3), self.find_data.group(2).replace('\\', ''), self.find_data.group(5).replace('\\', ''), self.find_data.group(4), self.find_data.group(6).replace('\\', '')
                    except (AttributeError):
                        print(f"[bold deep_sky_blue3]   ╰─>[bold red] AttributeError...                     ", end='\r');time.sleep(1.5)
                        self.Textpro(name)
                    r.headers.update({
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'host': 'textpro.me',
                        'origin': 'https://textpro.me',
                        'accept': '*/*',
                    })
                    data = {
                        'build_server_id': self.build_server_id,
                        'text[]': self.text,
                        'id': self.id,
                        'token': self.token,
                        'build_server': self.build_server,
                        'sign': self.sign,
                    }
                    response4 = r.post('https://textpro.me/effect/create-image', data = data)
                    if '"success":true' in str(response4.text):
                        r.headers.clear()
                        self.json_response4 = x = json.loads(response4.text)
                        r.headers.update({
                            'sec-fetch-dest': 'image',
                            'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                            'accept-language': 'en-US,en;q=0.9',
                        })
                        response5 = r.get('https://textpro.me{}'.format(self.json_response4['image']))
                        with open('Data/Foto.jpg', 'wb') as w:
                            w.write(response5.content)
                        w.close();time.sleep(2.5)
                        if bool(os.path.exists('Data/Foto.jpg')) == False:
                            print(f"[bold deep_sky_blue3]   ╰─>[bold red] Gambar Tidak Ada...     ", end='\r');time.sleep(1.5)
                            self.Textpro(name)
                        else:
                            return 0
                    else:
                        print(f"[bold deep_sky_blue3]   ╰─>[bold red] Generate Ulang Image...     ", end='\r');time.sleep(1.5)
                        self.Textpro(name)

    def Get_Textpro(self):
        with requests.Session() as r:
            r.headers.update({
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'host': 'textpro.me',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'en-US,en;q=0.9',
            })
            url = random.choice(['https://textpro.me/light-style-c27', 'https://textpro.me/metallic-style-c28', 'https://textpro.me/misc-style-c29', 'https://textpro.me/food-style-text-effect-c30', 'https://textpro.me/3d-text-effect-c32', 'https://textpro.me/graffiti-style-c34', 'https://textpro.me/christmas-c35', 'https://textpro.me/happy-new-year-c36'])
            response = r.get(url).text
            find_all_url = re.findall('href="(/.*?.html)">', str(response))
            for self.lengkapin in find_all_url:
                Gambar.append('https://textpro.me{}'.format(self.lengkapin))
            if len(Gambar) == 0:
                self.Get_Textpro()
            else:
                 return (random.choice(Gambar))

    def Ephoto360(self, name):
        if os.path.exists('Data/Foto.jpg') == True:
            os.remove('Data/Foto.jpg')
        with requests.Session() as r:
            try:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                    'host': 'en.ephoto360.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'en-US,en;q=0.9',
                })
                self.url_ephoto360 = self.Get_Ephoto360()
                response2 = r.get(self.url_ephoto360).text
                boundary = '----WebKitFormBoundary' \
                    + ''.join(random.sample(string.ascii_letters + string.digits, 16))
                r.headers.update({
                    'content-type': 'multipart/form-data; boundary={}'.format(boundary)
                })
                try:
                    token = re.search('name="token" value="(.*?)"', str(response2)).group(1)
                    build_server = re.search('name="build_server" value="(.*?)"', str(response2)).group(1)
                    build_server_id = re.search('name="build_server_id" value="(.*?)"', str(response2)).group(1)
                except (AttributeError):
                    print(f"[bold deep_sky_blue3]   ╰─>[bold red] AttributeError...                     ", end='\r');time.sleep(1.5)
                    self.Ephoto360(name)
                data = MultipartEncoder({
                    'build_server': (None, build_server),
                    'text[]': (None, name),
                    'submit': (None, 'GO'),
                    'token': (None, token),
                    'build_server_id': (None, build_server_id),
                }, boundary = boundary)
                response3 = r.post(self.url_ephoto360, data = data).text
                if 'You must enter this field' in str(response3):
                    self.Ephoto360()
                else:
                    try:
                        self.id = re.search('id&quot;:&quot;(\d+)&', str(response3)).group(1)
                        self.text = re.search('\[&quot;(.*?)&quot;\]', str(response3)).group(1)
                        self.token = str(re.search('token&quot;:&quot;(.*?)&', str(response3)).group(1)).replace('\\','')
                        self.build_server = str(re.search('build_server&quot;:&quot;(.*?)&', str(response3)).group(1)).replace('\\','')
                        self.build_server_id = re.search('build_server_id&quot;:&quot;(.*?)&', str(response3)).group(1)
                        self.sign = str(re.search('sign&quot;:&quot;(.*?)&', str(response3)).group(1)).replace('\\','')
                        print(self.sign)
                    except (AttributeError):
                        print(f"[bold deep_sky_blue3]   ╰─>[bold yellow] AttributeError...                     ", end='\r');time.sleep(1.5)
                        self.Ephoto360(name)
                    r.headers.update({
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'Host': 'en.ephoto360.com',
                        'origin': 'https://en.ephoto360.com',
                        'accept': '*/*',
                    })
                    data = {
                        'build_server': self.build_server,
                        'text[]': self.text,
                        'id': self.id,
                        'token': self.token,
                        'build_server_id': self.build_server_id,
                        'sign': self.sign,
                    }
                    response4 = r.post('https://en.ephoto360.com/effect/create-image', data = data)
                    if '"success":true' in str(response4.text):
                        r.headers.clear()
                        self.json_response4 = json.loads(response4.text)
                        r.headers.update({
                            'sec-fetch-dest': 'image',
                            'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                            'accept-language': 'en-US,en;q=0.9',
                        })
                        response5 = r.get('https://e2.yotools.net/save-image/{}/{}'.format(self.json_response4['image_code'], self.json_response4['session_id']))
                        with open('Data/Foto.jpg', 'wb') as w:
                            w.write(response5.content)
                        w.close();time.sleep(2.5)
                        if bool(os.path.exists('Data/Foto.jpg')) == False:
                            print(f"[bold deep_sky_blue3]   ╰─>[bold red] Gambar Tidak Ada...     ", end='\r');time.sleep(1.5)
                            self.Ephoto360(name)
                        else:
                            if 'Rất tiếc ảnh không còn tồn tại' in str(response5.text):
                                print(f"[bold deep_sky_blue3]   ╰─>[bold red] Rất tiếc ảnh không còn tồn tại...     ", end='\r');time.sleep(1.5)
                                self.Ephoto360(name)
                            else:
                                return 0
                    else:
                        if bool(os.path.exists('Data/Foto.jpg')) == False:
                            print(f"[bold deep_sky_blue3]   ╰─>[bold yellow] Gambar Tidak Ada...     ", end='\r');time.sleep(1.5)
                            self.Ephoto360(name)
                        else:
                            return 0
            except Exception as e:
                print(f"[bold deep_sky_blue3]   ╰─>[bold red] {str(e).title()}!", end='\r');time.sleep(1.5)
                self.Ephoto360(name)

    def Get_Ephoto360(self):
        with requests.Session() as r:
            r.headers.update({
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'host': 'en.ephoto360.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'en-US,en;q=0.9',
            })
            self.url = (f'https://en.ephoto360.com/text-effects-c6-p{random.randrange(1, 12)}')
            response = r.get(self.url).text
            self.find_all_url = re.findall('href="(/.*?.html)">', str(response))
            for self.lengkapin in self.find_all_url:
                Gambar.append('https://en.ephoto360.com{}'.format(self.lengkapin))
            if len(Gambar) == 0:
                self.Get_Textpro()
            else:
                 return (random.choice(Gambar))
            
def Pengguna_Online():
    try:
        with requests.Session() as r:
            response = r.get('https://justpaste.it/9p0su').text
            jumlah = re.search('"viewsText":"(.*?)"', str(response)).group(1)
            online = re.search('"onlineText":"(.*?)"', str(response)).group(1)
        return (jumlah, online)
    except Exception as e:
        return (0, 404)

if __name__ == '__main__':
    try:
        if int(re.search('columns=(\d+),', str(os.get_terminal_size())).group(1)) < 65:
            Console(width=65, style="bold deep_sky_blue3").print(Panel("[italic red]Silahkan Kecilkan Tampilan Termux Sampai Panel Ini Tidak Terlihat Putus-Putus!", title="[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Error[bold red] <[bold yellow]<[bold green]<"));exit()
        else:
            os.system('git pull')
            Daftar().Menu()
    except (KeyboardInterrupt):
        exit()
    except Exception as e:
        print(Panel(f"[italic red]{str(e).title()}!", width=65, style="bold deep_sky_blue3", title="[bold green]>[bold yellow]>[bold red]>[bold deep_sky_blue3] Error[bold red] <[bold yellow]<[bold green]<"))
        exit()