import pyshorteners
converting_url = pyshorteners.Shortener()
url = input("Input url : ")
print("Converting link ...")

short_url = converting_url.tinyurl.short(url)

print("Ressult convert link : \n [-]",short_url)