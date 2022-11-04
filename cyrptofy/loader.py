import os
import sys
import requests


if os.path.exists(".key"):
     key = open('.key',mode='r').read()
     l = requests.get("https://pastebin.com/raw/MpFtYBWq").text
     if key in str(l):
          pass
     else:
          print(f"[\033[1;32m!\033[1;97m] Key expired, please get new key!")
          print(f"[!] Please re-run script!")
          os.remove(".key")
          sys.exit()

if not os.path.exists(".key"):
     print(f"[\033[1;32m-\033[1;97m] Get Free Key : https://safelink.id/K1IxUaqN")
     input_key = input(f"\n[-] Enter Key : ")
     with open(".key","w") as f:
          f.write(input_key)
     
     key_auth = open(".key","r").read()
     p_l = requests.get("https://pastebin.com/raw/MpFtYBWq").text
     if key_auth in str(p_l):
          pass
          #os.system(f"cyptofy {sys.argv[1]}")
     
     else:
          print("[!] Key wrong!")
          print(f"[!] Please re-run script!")
          os.remove(".key")
          sys.exit()
