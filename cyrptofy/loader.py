import os
import sys
import requests

if os.path.exists(".key"):
     key = open('.key',mode='r').read()
     l = requests.get("https://pastebin.com/raw/MpFtYBWq").text
     if key in str(l):
          print(sys.argv[1])
          #os.system(f"cyptofy {sys.argv[1]}")
     else:
          print("[!] Key expired, please get new key!")
          print("[!] Please re-run script!")
          os.remove(".key")

if not os.path.exists(".key"):
     print("[-] Get Free Key : ")
     input_key = input("\nEnter Key : ")
     with open(".key","w") as f:
          f.write(input_key)
     
     key_auth = open(".key","r").read()
     p_l = requests.get("https://pastebin.com/raw/MpFtYBWq").text
     if key_auth in str(p_l):
          os.system(f"cyptofy {sys.argv[1]}")
     
     else:
          print("[!] Key wrong!")
          print("[!] Please re-run script!")
          os.remove(".key")
