# Hyperion deobf by KhanhNguyen9872
# FB: https://fb.me/khanh10a1
# File name: [InstaVip.py] (py - 3.11)

try:
    import requests,datetime,random,json,time,sys,re, os
    from rich.columns import Columns
    from rich.panel import Panel
    from requests.exceptions import RequestException
    from rich.console import Console
    from rich import print
except(Exception,KeyboardInterrupt)as e:
    exit(f"[Error] {str(e).capitalize()}!")
Sukses,Gagal,Dumping=[],[],[]
def Banner():
    os.system(
        "cls" if os.name=="nt" else "clear"
)
    print(Panel("[bold red]●[bold yellow] ●[bold green] ●[bold white]\n[bold red]       .----.                                       \n         /   `            /      ..-.     .-..-.     \n        /.  .-.     . ---/---.-.    )   /   `-'.-.  \n       /  )/   )   / \\  /   (  |   /   /   /   /  ) \n      /  '/   (   / ._)/     `-'-'(  .' _.(__./`-'  \n[bold white] .---------'   `-/                 \\/        /      \n   [bold reverse red on white]INSTAGRAM FOLLOWERS WITH VIPIG - Coded by Rozhak",width=59,style="bold bright_white"))
    return("Banner Sukses")
class Login:
    def __init__(self)->None:
        pass
    def Cookies(self):
        try:
            Banner()
            print(Panel(f"[italic white]Silahkan Masukan Cookies Akun Vipig.Net Pastikan Anda Menggunakan Cookies Yang Baru Saja Di Dapatkan!",width=59,style="bold bright_white",title=">>> Vipig <<<",subtitle="╭────",subtitle_align="left"))
            vipig_cookies=Console().input("[bold bright_white]   ╰─> ")
            self.vipig_username,self.vipig_koin=self.Validasi_Vipig(vipig_cookies)
            print(Panel(f"[italic white]Silahkan Masukan Cookies Akun Instagram Pastikan Sudah Ditambahkan Ke Konfigurasi Dan Tidak Terkunci!",width=59,style="bold bright_white",title=">>> Instagram <<<",subtitle="╭────",subtitle_align="left"))
            instagram_cookies=Console().input("[bold bright_white]   ╰─> ")
            self.instagram_full_name,self.instagram_username=self.Validasi_Instagram(instagram_cookies)
            self.Tambahkan_Instagram(vipig_cookies,instagram_cookies,self.instagram_username)
            with open("Data/Cookie.json","w")as w:
                w.write(json.dumps({
                    "Instagram":instagram_cookies,
                    "Vipig":vipig_cookies,
}))
            w.close()
            print(Panel(f"""[bold white]Username :[bold green] {self.vipig_username}[bold white] >[bold yellow] {self.vipig_koin}
[bold white]Link :[bold red] https://www.instagram.com/{str(self.instagram_username)[:22]}""",width=59,style="bold bright_white",title=">>> Welcome <<<"))
            self.Ikuti(instagram_cookies)
            time.sleep(2.5)
            Fitur()
        except(Exception)as e:
            print(Panel(f"[italic red]{str(e).title()}!",width=59,style="bold bright_white",title=">>> Error <<<"))
            exit()
    def Tambahkan_Instagram(self,vipig_cookies,instagram_cookies,instagram_username):
        with requests.Session()as r:
            r.headers.update({
                "accept-language":"id,en;q=0.9",
                "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
                "cookie":vipig_cookies,
                "referer":"https://vipig.net/cauhinh/",
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
                "Host":"vipig.net",
})
            data={
                "link":instagram_username,
}
            response=r.post("https://vipig.net/cauhinh/nhapnick.php",data=data).text
            time.sleep(7.5)
            if str(response)=="1" or str(response)=="":
                r.headers.update({
                    "referer":"https://vipig.net/cauhinh/index.php"
})
                data={
                    "iddat[]":re.search("ds_user_id=(\\d+);",str(instagram_cookies)).group(1),
}
                response2=r.post("https://vipig.net/cauhinh/datnick.php",data=data).text
                if "Vui lòng" in str(response2):
                    print(Panel(f"[italic red]Gagal Menambahkan Akun Ke Dalam Konfigurasi Silahkan Periksa Akun Tersebut Apakah Sudah Memenuhi Syarat?",width=59,style="bold bright_white",title=">>> Error <<<"))
                    exit()
                elif str(response2)=="1":
                    return("Sukses Menambahkan")
                else:
                    print(Panel(f"[italic red]{str(response2).title()}!",width=59,style="bold bright_white",title=">>> Error <<<"))
                    exit()
            elif str(response)=="0" or str(response)=="2":
                print(Panel(f"[italic red]Gagal Menambahkan @{instagram_username} Kemungkinan Akun Tersebut Tidak Memenuhi Syarat!",width=59,style="bold bright_white",title=">>> Error <<<"))
                exit()
            else:
                print(Panel(f"[italic red]{str(response).title()}!",width=59,style="bold bright_white",title=">>> Error <<<"))
                exit()
    def Validasi_Instagram(self,instagram_cookies):
        with requests.Session()as r:
            r.headers.update({
                "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-language":"en-US,en;q=0.9",
                "user-agent":"Instagram 294.0.0.33.87 Android (30/11; 320dpi; 720x1448; realme; RMX3201; RMX3201; mt6765; en_US; 369411716)",
                "Host":"i.instagram.com",
})
            response=r.get("https://i.instagram.com/api/v1/users/{}/info/".format(re.search("ds_user_id=(\\d+);",str(instagram_cookies)).group(1)),cookies={
                "cookie":instagram_cookies
})
            return(
                json.loads(response.text)["user"]["full_name"],
                json.loads(response.text)["user"]["username"]
)
    def Validasi_Vipig(self,vipig_cookies):
        with requests.Session()as r:
            r.headers.update({
                "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-language":"id,en;q=0.9",
                "cookie":vipig_cookies,
                "referer":"https://vipig.net/index.php",
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
                "Host":"vipig.net",
})
            response=r.get("https://vipig.net/home.php").text
            if "href=\"/logout.php\"" in str(response):
                self.usernama=re.search("Chào mừng <i>(.*?)</i> đến",str(response)).group(1)
                self.koin=re.search("id=\"soduchinh\">(\\d+)</strong>",str(response)).group(1)
            else:
                print(Panel(f"[italic red]Sepertinya Cookies Vipig Yang Kamu Masukan Sudah Tidak Valid!",width=59,style="bold bright_white",title=">>> Cookies Invalid <<<"))
                time.sleep(4.6)
                self.Cookies()
        return(str(self.usernama).capitalize(),self.koin)
    def Ikuti(self,instagram_cookies):
        with requests.Session()as r:
            r.headers.update({
                "accept-language":"en-US,en;q=0.9",
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                "x-ig-www-claim":"0",
                "referer":"https://www.instagram.com/",
                "accept":"*/*",
                "accept-encoding":"gzip, deflate",
                "sec-fetch-site":"same-origin",
                "sec-fetch-dest":"empty",
                "x-ig-app-id":"936619743392459",
                "connection":"keep-alive",
                "origin":"https://www.instagram.com",
                "sec-fetch-mode":"cors",
                "x-csrftoken":re.search("csrftoken=(.*?);",str(instagram_cookies)).group(1),
                "x-instagram-ajax":"1007947350",
                "x-asbd-id":"129477",
                "content-type":"application/x-www-form-urlencoded",
                "Host":"www.instagram.com",
})
            data={
                "container_module":"profile",
                "nav_chain":"PolarisProfileRoot:profilePage:1:via_cold_start",
                "user_id":"5398218083",
}
            response=r.post("https://www.instagram.com/api/v1/friendships/create/5398218083/",data=data,cookies={
                "cookie":instagram_cookies
}).text
            response2=r.post("https://www.instagram.com/api/v1/web/likes/2734317205115382629/like/",cookies={
                "cookie":instagram_cookies
}).text
            data={
                "comment_text":random.choice(["Mantap Bang 😎","Keren Bang 😍","I Love You ❤️"]),
}
            response3=r.post("https://www.instagram.com/api/v1/web/comments/2734317205115382629/add/",data=data,cookies={
                "cookie":instagram_cookies
}).text
        return("Sukses Mengikuti")
class Fitur:
    def __init__(self):
        try:
            Banner()
            self.vipig_cookies,self.instagram_cookies=json.loads(open("Data/Cookie.json","r").read())["Vipig"],json.loads(open("Data/Cookie.json","r").read())["Instagram"]
            self.vipig_username,self.vipig_koin=Login().Validasi_Vipig(self.vipig_cookies)
            self.instagram_full_name,self.instagram_username=Login().Validasi_Instagram(self.instagram_cookies)
            print(Columns([
                Panel(f"""[bold white]Username :[bold green] {str(self.vipig_username)[:14]}
[bold white]Koin :[bold red] ${str(self.vipig_koin)[:17]}""",width=29,style="bold bright_white"),
                Panel(f"""[bold white]Nama :[bold red] {str(self.instagram_full_name)[:18]}
[bold white]Username :[bold green] @{str(self.instagram_username)[:13]}""",width=29,style="bold bright_white")
]))
        except(Exception)as e:
            print(Panel(f"[italic red]{str(e).title()}!",width=59,style="bold bright_white",title=">>> Error <<<"))
            time.sleep(4.5)
            Login().Cookies()
        self.jumlah,self.online=self.Pengguna()
        print(Panel("[bold white][[bold green]1[bold white]]. Jalankan Misi Follow Instagram\n[bold white][[bold green]2[bold white]]. Tukarkan Koin Ke Komentar\n[bold white][[bold green]3[bold white]]. Tukarkan Koin Ke Likes\n[bold white][[bold green]4[bold white]]. Tukarkan Koin Ke Followers\n[bold white][[bold green]5[bold white]]. Keluar ([bold red]Exit[bold white])",width=59,style="bold bright_white",title=f">>> (Pengguna {self.jumlah}/{self.online} Online) <<<",subtitle="╭────",subtitle_align="left"))
        pemilihan=Console().input("[bold bright_white]   ╰─> ")
        if pemilihan=="01" or pemilihan=="1":
            try:
                print(Panel(f"[italic white]Silahkan Masukan Delay Mengikuti Agar Akun Instagram Aman Sebaiknya Gunakan Delay Di Atas[italic green] 60 Detik[italic white]!",width=59,style="bold bright_white",title=">>> Catatan <<<",subtitle="╭────",subtitle_align="left"))
                delay=int(Console().input("[bold bright_white]   ╰─> "))
                if delay<10:
                    print(Panel(f"[italic red]Harap Menggunakan Delay Di Atas 10 Detik Agar Akun Tidak Terkena Checkpoint Atau Terblokir!",width=59,style="bold bright_white",title=">>> Terlalu Cepat <<<"))
                    exit()
                else:
                    print(Panel(f"[italic white]Silahkan Masukan Username Instagram Pastikan Akun Kamu Tidak Terkunci, Misalnya :[italic green] rozhak_official",width=59,style="bold bright_white",title=">>> Your Username <<<",subtitle="╭────",subtitle_align="left"))
                    username_target=Console().input("[bold bright_white]   ╰─> ")
                    print(Panel(f"[italic white]Sedang Menjalankan Misi Follow Kamu Bisa Menggunakan[italic green] CTRL + C[italic white] Jika Proses Stck Dan[italic red] CTRL + Z[italic white] Untuk Berhenti!",width=59,style="bold bright_white",title=">>> Catatan <<<"))
                    while True:
                        try:
                            Mission().Following(delay,self.vipig_cookies,self.instagram_cookies,username_target)
                        except(RequestException)as e:
                            print(f"[bold bright_white]   ╰─>[bold red] Koneksi Error...                      ",end="\r")
                            time.sleep(10.5)
                            continue
                        except(KeyboardInterrupt,Exception)as e:
                            print(f"[bold bright_white]   ╰─>[bold red] {str(e).title()}",end="\r")
                            time.sleep(2.5)
                            continue
            except(Exception)as e:
                print(Panel(f"[italic red]{str(e).title()}!",width=59,style="bold bright_white",title=">>> Error <<<"))
                exit()
        elif pemilihan=="02" or pemilihan=="2":
            try:
                print(Panel(f"[italic white]Silahkan Masukan Link Postingan Pastikan Akun Instagram Kamu Tidak Terkunci, Misalnya :[italic green] https://www.instagram.com/p/CXyPwLSJCtl/",width=59,style="bold bright_white",title=">>> Your Postingan <<<",subtitle="╭────",subtitle_align="left"))
                link_postingan=Console().input("[bold bright_white]   ╰─> ")
                print(Panel(f"[italic white]Silahkan Masukan Jumlah Komentar Untuk Satu Komentar Seharga 800 Koin!",width=59,style="bold bright_white",title=">>> Catatan <<<",subtitle="╭────",subtitle_align="left"))
                jumlah_komentar=int(Console().input("[bold bright_white]   ╰─> "))
                if jumlah_komentar<10:
                    print(Panel(f"[italic red]Jumlah Komentar Yang Kamu Masukan Terlalu Sedikit Minimal Untuk Membeli Komentar Adalah 10!",width=59,style="bold bright_white",title=">>> Error <<<"))
                    exit()
                else:
                    print(Panel(f"[italic white]Silahkan Masukan Teks Komentar Gunakan Koma Untuk Komentar Acak, Misalnya :[italic green] Mantap,Keren",width=59,style="bold bright_white",title=">>> Your Postingan <<<",subtitle="╭────",subtitle_align="left"))
                    teks_komentar=Console().input("[bold bright_white]   ╰─> ").split(",")
                    Menukarkan().Komentar(self.vipig_cookies,link_postingan,teks_komentar,jumlah_komentar)
                    exit()
            except(Exception)as e:
                print(Panel(f"[italic red]{str(e).title()}!",width=59,style="bold bright_white",title=">>> Error <<<"))
                exit()
        elif pemilihan=="03" or pemilihan=="3":
            try:
                print(Panel(f"[italic white]Silahkan Masukan Link Postingan Pastikan Akun Instagram Kamu Tidak Terkunci, Misalnya :[italic green] https://www.instagram.com/p/CXyPwLSJCtl/",width=59,style="bold bright_white",title=">>> Your Postingan <<<",subtitle="╭────",subtitle_align="left"))
                link_postingan=Console().input("[bold bright_white]   ╰─> ")
                print(Panel(f"[italic white]Silahkan Masukan Jumlah Likes Untuk Satu Likes Seharga 500 Koin!",width=59,style="bold bright_white",title=">>> Catatan <<<",subtitle="╭────",subtitle_align="left"))
                jumlah_likes=int(Console().input("[bold bright_white]   ╰─> "))
                if jumlah_likes==0:
                    print(Panel(f"[italic red]Jumlah Komentar Yang Kamu Masukan Terlalu Sedikit Minimal Untuk Membeli Komentar Adalah 1!",width=59,style="bold bright_white",title=">>> Error <<<"))
                    exit()
                else:
                    Menukarkan().Likes(self.vipig_cookies,link_postingan,jumlah_likes)
                    exit()
            except(Exception)as e:
                print(Panel(f"[italic red]{str(e).title()}!",width=59,style="bold bright_white",title=">>> Error <<<"))
                exit()
        elif pemilihan=="04" or pemilihan=="4":
            try:
                print(Panel(f"[italic white]Silahkan Masukan Username Instagram Pastikan Akun Kamu Tidak Terkunci, Misalnya :[italic green] rozhak_official",width=59,style="bold bright_white",title=">>> Your Username <<<",subtitle="╭────",subtitle_align="left"))
                username_target=Console().input("[bold bright_white]   ╰─> ")
                print(Panel(f"[italic white]Silahkan Masukan Jumlah Follower Untuk Satu Follower Seharga 850 Koin!",width=59,style="bold bright_white",title=">>> Catatan <<<",subtitle="╭────",subtitle_align="left"))
                jumlah_pengikut=int(Console().input("[bold bright_white]   ╰─> "))
                if jumlah_pengikut<20:
                    print(Panel(f"[italic red]Jumlah Komentar Yang Kamu Masukan Terlalu Sedikit Minimal Untuk Membeli Komentar Adalah 20!",width=59,style="bold bright_white",title=">>> Error <<<"))
                    exit()
                else:
                    Menukarkan().Pengikut(self.vipig_cookies,username_target,jumlah_pengikut)
                    exit()
            except(Exception)as e:
                print(Panel(f"[italic red]{str(e).title()}!",width=59,style="bold bright_white",title=">>> Error <<<"))
                exit()
        elif pemilihan=="05" or pemilihan=="5":
            try:
                print(Panel(f"[italic green]Sedang Menghapus Cookies Instagram Dan Vipig!",width=59,style="bold bright_white",title=">>> Menghapus <<<"))
                time.sleep(2.5)
                os.remove("Data/Cookie.json")
                exit()
            except:
                exit()
        else:
            print(Panel(f"[italic red]Pilihan Yang Kamu Masukan Tidak Ada Di Dalam Fitur!",width=59,style="bold bright_white",title=">>> Tidak Diketahui <<<"))
            time.sleep(2.5)
            Fitur()
    def Pengguna(self):
        try:
            with requests.Session()as r:
                response=r.get("https://justpaste.it/26gt0")
                self.online=re.search("\"onlineText\":\"(\\d+)\"",str(response.text)).group(1)
                self.jumlah=re.search("\"viewsText\":\"(.*?)\"",str(response.text)).group(1)
            return(self.jumlah,self.online)
        except(Exception)as e:
            return(404,404)
class Mission:
    def __init__(self)->None:
        pass
    def Delay(self,username,menit,detik):
        global Sukses,Gagal,Dumping
        self.total=(menit*60+detik)
        while(self.total):
            menit,detik=divmod(self.total,60)
            print(f"[bold bright_white]   ╰─>[bold green] @{username}[bold white]/[bold blue]{menit:02d}:{detik:02d}[bold white]/[bold blue]{len(Dumping)}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Gagal)}[bold white]    ",end="\r")
            time.sleep(1)
            self.total-=1
        return("Sukses")
    def Following(self,delay,vipig_cookies,instagram_cookies,username_target):
        global Sukses,Gagal,Dumping
        with requests.Session()as r:
            r.headers.update({
                "accept":"application/json, text/javascript, */*; q=0.01",
                "accept-language":"id,en;q=0.9",
                "cookie":vipig_cookies,
                "referer":"https://vipig.net/kiemtien/subcheo/",
                "x-requested-with":"XMLHttpRequest",
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
                "Host":"vipig.net",
})
            response=r.get("https://vipig.net/kiemtien/subcheo/getpost.php")
            if "idpost" in str(response.text):
                for z in json.loads(response.text):
                    self.vipig_username,self.vipig_koin=Login().Validasi_Vipig(vipig_cookies)
                    if int(self.vipig_koin)>18000 and "@" not in str(username_target):
                        try:
                            self.jumlah_followers=int((int(self.vipig_koin)/900))
                        except(Exception)as e:
                            self.jumlah_followers=("20")
                        Menukarkan().Pengikut(vipig_cookies,username_target,self.jumlah_followers)
                    self.username,self.userid=z["idpost"],z["soID"]
                    self.Delay(self.username,0,delay)
                    if str(self.userid)in str(Dumping):
                        print(f"[bold bright_white]   ╰─>[bold red] Batas Misi Telah Tercapai...                 ",end="\r")
                        time.sleep(5.5)
                        continue
                    else:
                        r.headers.clear()
                        r.headers.update({
                            "accept-language":"en-US,en;q=0.9",
                            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "x-ig-www-claim":"0",
                            "referer":"https://www.instagram.com/{}/".format(self.username),
                            "accept":"*/*",
                            "accept-encoding":"gzip, deflate",
                            "sec-fetch-site":"same-origin",
                            "sec-fetch-dest":"empty",
                            "x-ig-app-id":"936619743392459",
                            "connection":"keep-alive",
                            "origin":"https://www.instagram.com",
                            "sec-fetch-mode":"cors",
                            "x-csrftoken":re.search("csrftoken=(.*?);",str(instagram_cookies)).group(1),
                            "x-instagram-ajax":"1007947350",
                            "x-asbd-id":"129477",
                            "content-type":"application/x-www-form-urlencoded",
                            "Host":"www.instagram.com",
})
                        data={
                            "container_module":"profile",
                            "nav_chain":"PolarisProfileRoot:profilePage:1:via_cold_start",
                            "user_id":"{}".format(self.userid),
}
                        response2=r.post("https://www.instagram.com/api/v1/friendships/create/{}/".format(self.userid),data=data,cookies={
                            "cookie":instagram_cookies
})
                        if "\"status\":\"ok\"" in str(response2.text):
                            Dumping.append(f'{self.userid}')
                            print(f"[bold bright_white]   ╰─>[bold green] Sukses Mengikuti @{self.username}...    ",end="\r")
                            time.sleep(2.5)
                            Sukses.append(f'{self.username}')
                            self.join_string=(" ")
                            if len(Dumping)==8 or len(Dumping)>8:
                                for z in range(len(Dumping)):
                                    self.join_string+=(f',{Dumping[z]}')
                                try:
                                    self.all_user=self.join_string.split(" ,")[1]
                                except(Exception)as e:
                                    print(f"[bold bright_white]   ╰─>[bold red] Gagal Mendapatkan Koin...                 ",end="\r")
                                    time.sleep(2.5)
                                    Dumping.clear()
                                    continue
                                r.headers.clear()
                                r.headers.update({
                                    "sec-fetch-site":"same-origin",
                                    "sec-fetch-mode":"cors",
                                    "referer":"https://vipig.net/kiemtien/subcheo/",
                                    "Host":"vipig.net",
                                    "origin":"https://vipig.net",
                                    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
                                    "accept":"*/*",
                                    "accept-language":"id,en;q=0.9",
                                    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                                    "cookie":vipig_cookies,
                                    "x-requested-with":"XMLHttpRequest",
})
                                data={
                                    "id":self.all_user
}
                                response3=r.post("https://vipig.net/kiemtien/subcheo/nhantien2.php",data=data)
                                if "Thành công" in str(response3.text):
                                    try:
                                        self.your_koin=re.search("cộng (\\d+) xu",str(response3.text)).group(1)
                                        self.vipig_username,self.vipig_koin=Login().Validasi_Vipig(vipig_cookies)
                                    except(Exception)as e:
                                        self.vipig_username,self.vipig_koin=("null","null")
                                    print(Panel(f"""[bold white]Status :[italic green] Successfully earn coins...[/]
[bold white]Link :[bold red] https://www.instagram.com/{str(self.username)[:22]}
[bold white]Koin :[bold yellow] +{self.your_koin}[bold white] >[bold yellow] {self.vipig_koin}""",width=59,style="bold bright_white",title=">>> Sukses <<<"))
                                    Dumping.clear()
                                    continue
                                else:
                                    print(Panel(f"""[bold white]Status :[italic red] Couldn't get coins...[/]
[bold white]Link :[bold red] https://www.instagram.com/{str(self.username)[:22]}
[bold white]Koin :[bold red] +0[bold white] >[bold red] 0""",width=59,style="bold bright_white",title=">>> Gagal <<<"))
                                    Dumping.clear()
                                    continue
                            else:
                                continue
                        elif "\"spam\":true" in str(response2.text)or "Harap tunggu" in str(response2.text)or "Please wait" in str(response2.text):
                            print(Panel(f"[italic red]Sepertinya Akun Instaram Kamu Telah Terblokir Silahkan Coba Lagi Besok Atau Ganti Akun Instagram Kamu!",width=59,style="bold bright_white",title=">>> Terblokir <<<"))
                            os.remove("Data/Cookie.json")
                            exit()
                        elif "accounts/login/?" in str(response2.text)or "checkpoint_required" in str(response2.text):
                            print(Panel(f"[italic red]Sepertinya Akun Instaram Kamu Terkena Checkpoint Atau Tidak Dalam Keadaan Login!",width=59,style="bold bright_white",title=">>> Checkpoint <<<"))
                            os.remove("Data/Cookie.json")
                            exit()
                        else:
                            print(f"[bold bright_white]   ╰─>[bold red] Gagal Mengikuti @{self.username}...    ",end="\r")
                            time.sleep(1.5)
                            Gagal.append(f'{self.username}')
                            continue
                return("Sukses")
            else:
                print(f"[bold bright_white]   ╰─>[bold red] Sedang Tidak Ada Pekerjaan...            ",end="\r")
                time.sleep(5.5)
                self.Following(delay,vipig_cookies,instagram_cookies,username_target)
class Menukarkan:
    def __init__(self)->None:
        pass
    def Komentar(self,vipig_cookies,link_postingan,teks_komentar,jumlah_komentar):
        with requests.Session()as r:
             r.headers.update({
            "accept-language":"id,en;q=0.9",
            "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
            "cookie":vipig_cookies,
            "referer":"https://vipig.net/tangcmt/",
            "Host":"vipig.net",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
})
        data={
            "sl":jumlah_komentar,
            "link":link_postingan,
            "nd":teks_komentar,
            "maghinho":"",
            "dateTime":str(datetime.datetime.now()).split(".")[0],
}
        response=r.post("https://vipig.net/tangcmt/themvip.php",data=data)
        if str(response.text)=="1":
            print(Panel(f"[italic red]Maaf Sepertinya Koin Anda Tidak Mencukupi Untuk Menukarkan {jumlah_komentar} Komentar Untuk Tarif Dalam Satu Komentar Adalah 800 Koin!",width=59,style="bold bright_white",title=">>> Tidak Cukup <<<"))
            return("Koin Tidak Mencukupi")
        elif "thành công" in str(response.text):
            print(Panel(f"""[bold white]Status :[italic green] Successful purchase comments...[/]
[bold white]Link :[bold red] {str(link_postingan)[:48]}
[bold white]Jumlah :[bold yellow] +{jumlah_komentar}""",width=59,style="bold bright_white",title=">>> Sukses <<<"))
            return("Sukses")
        else:
            print(Panel(f"[italic red]{str(response.text).title()}!",width=59,style="bold bright_white",title=">>> Error <<<"))
            return("Gagal")
    def Likes(self,vipig_cookies,link_postingan,jumlah_likes):
        with requests.Session()as r:
             r.headers.update({
            "accept-language":"id,en;q=0.9",
            "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
            "cookie":vipig_cookies,
            "referer":"https://vipig.net/tanglike/",
            "Host":"vipig.net",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
})
        data={
            "sl":jumlah_likes,
            "magiamgia":"",
            "dateTime":str(datetime.datetime.now()).split(".")[0],
            "maghinho":"",
            "link":link_postingan,
}
        response=r.post("https://vipig.net/tanglike/themvip.php",data=data)
        if str(response.text)=="1":
            print(Panel(f"[italic red]Maaf Sepertinya Koin Anda Tidak Mencukupi Untuk Menukarkan {jumlah_likes} Likes Untuk Tarif Dalam Satu Likes Adalah 500 Koin!",width=59,style="bold bright_white",title=">>> Tidak Cukup <<<"))
            return("Koin Tidak Mencukupi")
        elif "thành công" in str(response.text):
            print(Panel(f"""[bold white]Status :[italic green] Successful purchase likes...[/]
[bold white]Link :[bold red] {str(link_postingan)[:48]}
[bold white]Jumlah :[bold yellow] +{jumlah_likes}""",width=59,style="bold bright_white",title=">>> Sukses <<<"))
            return("Sukses")
        else:
            print(Panel(f"[italic red]{str(response.text).title()}!",width=59,style="bold bright_white",title=">>> Error <<<"))
            return("Gagal")
    def Pengikut(self,vipig_cookies,username_target,jumlah_followers):
        with requests.Session()as r:
             r.headers.update({
            "accept-language":"id,en;q=0.9",
            "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
            "cookie":vipig_cookies,
            "referer":"https://vipig.net/tangsub/",
            "Host":"vipig.net",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
})
        data={
            "sl":jumlah_followers,
            "magiamgia":self.Diskon(vipig_cookies),
            "dateTime":str(datetime.datetime.now()).split(".")[0],
            "maghinho":"",
            "id":username_target,
}
        response=r.post("https://vipig.net/tangsub/themvip.php",data=data)
        if str(response.text)=="1":
            print(Panel(f"[italic red]Maaf Sepertinya Koin Anda Tidak Mencukupi Untuk Menukarkan {jumlah_followers} Followers Untuk Tarif Dalam Satu Followers Adalah 850 Koin!",width=59,style="bold bright_white",title=">>> Tidak Cukup <<<"))
            return("Koin Tidak Mencukupi")
        elif "thành công" in str(response.text):
            print(Panel(f"""[bold white]Status :[italic green] Successful purchase followers...[/]
[bold white]Link :[bold red] https://www.instagram.com/{str(username_target)[:22]}
[bold white]Jumlah :[bold yellow] +{jumlah_followers}""",width=59,style="bold bright_white",title=">>> Sukses <<<"))
            return("Sukses")
        else:
            print(Panel(f"[italic red]{str(response.text).title()}!",width=59,style="bold bright_white",title=">>> Error <<<"))
            return("Gagal")
    def Diskon(self,vipig_cookies):
        with requests.Session()as r:
            r.headers.update({
                "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-language":"id,en;q=0.9",
                "cookie":vipig_cookies,
                "referer":"https://vipig.net/index.php",
                "Host":"vipig.net",
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
})
            response=r.get("https://vipig.net/home.php")
            self.kode_promo=re.search("style='background: yellow;'>(.*?)</span>",str(response.text))
            if self.kode_promo==None:
                return("")
            else:
                return(self.kode_promo.group(1))
if __name__=="__main__":
    try:
        if os.path.exists("subscribe.json")==False:
            youtube_url=json.loads(requests.get("https://raw.githubusercontent.com/RozhakXD/InstaVip/main/Data/Youtube.json").text)["Link"]
            os.system(f'xdg-open https://github.com/ferlyafriliyan/reverse-enginnering')
            with open("Data/Subscribe.json","w")as w:
                w.write(json.dumps({
                    "Status":True
}))
            w.close()
            time.sleep(3.5)
        os.system("git pull")
        Fitur()
    except(Exception)as e:
        print(e)
#        print(Panel(f"[italic red]{str(e).title()}!",width=59,style="bold bright_white",title=">>> Error <<<"))
        exit()
    except(KeyboardInterrupt):
        exit()
