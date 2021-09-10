import os
from colorama import Fore, Back, Style

os.system("clear")
os.system("figlet zshTOOLS - MEER")

print(Fore.RED+"1. Airgeddon")
print("2. Routersploit")
print("3. Xerosploit")
print("4. Evillimiter")
print("5. TBomb")
print("0. EXIT")

print(Style.RESET_ALL)

ask = input(Fore.GREEN+"Enter Your Choice : ")

if ask == "0":
	print("Exiting...")
	
if ask == "1":
	print("Opening...")
	os.system("clear")
	os.system("figlet Airgeddon")
	os.system("sudo bash /home/redskull-linux/airgeddon/airgeddon.sh")

if ask == "2":
	print("Opening...")
	os.system("clear")
	os.system("figlet Routersploit")
	os.system("sudo python3 /home/redskull-linux/routersploit/rsf.py")
	
if ask == "3":
	print("Opening...")
	os.system("clear")
	os.system("figlet Xerosploit")
	os.system("sudo python3 /home/redskull-linux/xerosploit/xerosploit.py")

if ask == "4":
	print("Opening...")
	os.system("clear")
	os.system("figlet Evillimiter")
	os.system("sudo python3 /home/redskull-linux/evillimiter/bin/evillimiter")
	
if ask == "5":
	print("Opening..")
	os.system("clear")
	os.system("figlet TBomB")
	os.system("sudo bash /home/redskull-linux/TBomb/TBomb.sh")
	