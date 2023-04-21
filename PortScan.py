# -*- coding: utf-8 -*
#!/usr/bin/python
#Port Scan !
#My Friendo : JametKNTLS -  h0d3_g4n - Moslem And All Coders
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
#CONTACT ME :(
       # ICQ : https://icq.im/Shin403
       # Telegram : t.me/Shin_code
       # Youtube : Smile Of Beauty 
import requests,time,re,sys,random
import socket
import subprocess
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore,Style, init
init(autoreset=True)

r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL

def portS(url):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(2)
		result = sock.connect_ex((url,int(PORTE)))
		if result == 0:
			print (g + 'Port is open' + ' ' + o + url+':'+PORTE)
			open('Port_Res.txt','a').write(url+':'+PORTE+'\n')
		else:
			print (r + 'Port is not open' + ' ' + o + url+':'+ PORTE)
		
	except:
		pass
		
print "{} Port Simple Scanner  | Shin Code\n".format(y)
url = open(raw_input(o+'List:~# '),'r').read().replace('http://','').replace('https://','').splitlines()
PORTE = raw_input(o+'Port:~# ')
pool = ThreadPool(int(1))
pool.map(portS, url)
pool.close()
pool.join()