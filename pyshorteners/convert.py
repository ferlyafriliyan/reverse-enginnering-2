#  Coded by Ferly Afriliyan (Ryougaa Hidekii)
import pyshorteners
from os import system as clear

converting_url = pyshorteners.Shortener()
clear("clear")

url = input("Input url : ")
print("Converting link ...")

short_url = converting_url.tinyurl.short(url)

print("Ressult convert link : \n [-]",short_url)