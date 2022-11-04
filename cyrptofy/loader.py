import os
import sys
import requests

GREEN = "\033[1;32m"
RED = "\033[1;91m"
WHITE = "\033[1;97m"

if os.path.exists(".key"):
     key = open('.key',mode='r').read()
     l = requests.get("https://pastebin.com/raw/MpFtYBWq").text
     if key in str(l):
          pass
     else:
          print(f"{WHITE}[{RED}!{WHITE}] Key expired, please get new key!")
          print(f"{WHITE}[{RED}!{WHITE}] Please re-run script!")
          os.remove(".key")
          sys.exit()

if not os.path.exists(".key"):
     print(f"{WHITE}[{GREEN}-{WHITE}] Get Free Key : https://safelink.id/K1IxUaqN")
     input_key = input("\n{WHITE}[{GREEN}-{WHITE}] Enter Key : ")
     with open(".key","w") as f:
          f.write(input_key)
     
     key_auth = open(".key","r").read()
     p_l = requests.get("https://pastebin.com/raw/MpFtYBWq").text
     if key_auth in str(p_l):
          pass
          #os.system(f"cyptofy {sys.argv[1]}")
     
     else:
          print("[!] Key wrong!")
          print(f"{WHITE}[{RED}!{WHITE}] Please re-run script!")
          os.remove(".key")
          sys.exit()
