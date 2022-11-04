import os
import sys
import requests

banner = """ __    _____ _____ ____  _____ _____ 
|  |  |     |  _  |    \|   __| __  |
|  |__|  |  |     |  |  |   __|    -|
|_____|_____|__|__|____/|_____|__|__|
\033[1;97m\033[1;44m     LOADER SCRIPT     \033[0;00m                              


"""
os.system("clear")
print(banner)

if os.path.exists(".key"):
     key = open('.key',mode='r').read()
     l = requests.get("https://pastebin.com/raw/MpFtYBWq").text
     if key in str(l):
          pass
     else:
          print("[!] Key expired, please get new key!")
          print("[!] Please re-run script!")
          os.remove(".key")
          sys.exit()

if not os.path.exists(".key"):
     print("[-] Get Free Key : https://safelink.id/K1IxUaqN")
     input_key = input("\n[-] Enter Key : ")
     with open(".key","w") as f:
          f.write(input_key)
     
     key_auth = open(".key","r").read()
     p_l = requests.get("https://pastebin.com/raw/MpFtYBWq").text
     if key_auth in str(p_l):
          pass
          #os.system(f"cyptofy {sys.argv[1]}")
     
     else:
          print("[!] Key wrong!")
          print("[!] Please re-run script!")
          os.remove(".key")
          sys.exit()
