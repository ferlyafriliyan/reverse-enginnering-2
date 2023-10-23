# Take the encryption method from the website = https://pyobfuscate.com/pyd
created_by = "Ferly Afriliyan"
# Time : Monday, October 23, 2023 23:06:52
# Platform : Windows-AMD64
import importlib ,requests as r 
from bs4 import BeautifulSoup as bs 
import os ,sys ,datetime ,time ,platform 
IlIIIIIIIIlIIlIIl ='\x1b[1;33m'
IIlIIllIIllllIlII ='\x1b[1;30m'
IllIIlIIIlIIlllIl ='\x1b[1;31m'
IIlIlIllIlllIIIII ='\x1b[1;32m'
IlIllllIllIllIllI ='\x1b[1;37m'
def IIIIllllllIllIIIl ():
	if 'linux'in sys .platform .lower ():os .system ('clear')
	elif 'win'in sys .platform .lower ():os .system ('cls')
IIlIIllllIIIlllII ='https://pyobfuscate.com/pyd'
IllIIlIlIIIIllllI =datetime .datetime .now ()
IlIllIIIIIlIIlIll =IllIIlIlIIIIllllI .strftime ('%A, %B %d, %Y %H:%M:%S')
IIIIllllllIllIIIl ()
IIllIIIIlIIlllIll =input (f"{IIlIlIllIlllIIIII}[{IIlIIllIIllllIlII}•{h}] {IlIllllIllIllIllI}Masukkan nama file Input {a}: {p}")
try :
	with open (IIllIIIIlIIlllIll ,'r',encoding ='utf-8')as IIlIlIlIIllIllIIl :IlIIIlIIIlIIIlIlI =IIlIlIlIIllIllIIl .read ()
except FileNotFoundError :print (f"{IlIllllIllIllIllI}File '{IIllIIIIlIIlllIll}' tidak ditemukan.");IlIIIlIIIlIIIlIlI =None 
if IlIIIlIIIlIIIlIlI :
	IIIllIlIlIIIllIll =r .post ('https://pyobfuscate.com/rename-obf',data ={'input_text':IlIIIlIIIlIIIlIlI });IIIIIlIIIlIIIIIIl =bs (IIIllIlIlIIIllIll .text ,'html.parser');IIIlllllIIllIIIIl =IIIIIlIIIlIIIIIIl .find ('textarea',{'id':'myTextarea2'});IIlIIIIlIlllIIlll =input (f"{IIlIlIllIlllIIIII}[{IIlIIllIIllllIlII}•{h}] {IlIllllIllIllIllI}Masukkan nama file Output {a}: {p}")
	if IIIlllllIIllIIIIl :
		IIllIIIIlllIlllIl =IIIlllllIIllIIIIl .text 
		with open (IIlIIIIlIlllIIlll ,'w',encoding ='utf-8')as IIlIlIlIIllIllIIl :IIlIlIlIIllIllIIl .write (f"# Take the encryption method from the website = {IIlIIllllIIIlllII}\n");IIlIlIlIIllIllIIl .write (f'created_by = "Ferly Afriliyan"\n');IIlIlIlIIllIllIIl .write (f"# Time : {IlIllIIIIIlIIlIll}\n");IIlIlIlIIllIllIIl .write (f"# Platform : {platform.system()}-{platform.machine()}\n"+IIllIIIIlllIlllIl )
		print (f"{IIlIlIllIlllIIIII}[{IIlIIllIIllllIlII}•{h}] {IlIllllIllIllIllI}Berhasil, file {IIllIIIIlIIlllIll} tersimpan di {a}: {IIlIIIIlIlllIIlll} {p}")
	else :print (f"{IllIIlIIIlIIlllIl}[{IIlIIllIIllllIlII}!{m}] {IlIllllIllIllIllI}Tidak dapat menemukan kode Obfuscate.")
else :print (f"{IIlIlIllIlllIIIII}[{IlIIIIIIIIlIIlIIl}+{h}] {IlIllllIllIllIllI}Proses Obfuscate dibatalkan karena file Input tidak ditemukan.")