import random, sys
from hashlib import sha256
from tkinter import *
from tkinter import Text
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
from datetime import datetime

#main Window
root = tk.Tk()
root.title('passwordGenerator')
root.resizable(0,0)

canvas = tk.Canvas(root, height=430, width=450)
canvas.pack()
master = tk.Frame(root)
master.config(borderwidth=1, highlightthickness=1, highlightbackground='#bebebe', bg='#f0f0f0')
master.place(height=330, width=435, x=9, y=76)
global sm, length
pstype = ""

def datetimee():
    global t1
    t = datetime.now()
    t1 = t.strftime('%H:%M:%S')

def hashpassword(passwords):
    global hashed_password
    bpass = bytes(passwords, 'utf-8')
    h = sha256()
    h.update(bpass)
    hashed_password = h.hexdigest()
    for things in hashframe.winfo_children():
        things.destroy()
    hashbox = tk.Text(hashframe, font=('monospace', 9), bg='white')
    hashbox.insert(tk.INSERT, f'{hashed_password}')
    hashbox.pack()

def generatePass():
    global password
    global pstype
    global var1
    ans = var1.get()
    length=l1.get("1.0", "end-1c")
    try:
        length = int(length)
    except ValueError:
        messagebox.showwarning('Warning!', "Enter length first!")
        return
    passtype = entrybox.get()
    password = ""
    lower = 'abcdefghijklmnopqrstuvwxyz'
    UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SYM = '!@#$%&*()_-=<>/?{~}\+'
    NUM = '0123456789'
    lsecure = lower+UPPER
    msecure = lower+UPPER+NUM
    usecure = UPPER+lower+SYM+NUM
    if passtype == 'Alpha Characteres':
        for i in range(0, length):
            password = password + random.choice(lsecure)
        outputpass(password)
        pstype = 'Low Secure'
        if (length < 5):
            pstype = 'Very Low Secure'
        statusupdate()
        if ans == 1:
            hashpassword(password)
        else:
            pass
    elif passtype == 'Alphanumeric (A-Z, a-z, 0-9)':
        for i in range(0, length):
            password = password + random.choice(msecure)
        outputpass(password)
        pstype = 'Fairly Secure'
        if (length < 5):
            pstype = 'Low Secure'
        statusupdate()
        if ans == 1:
            hashpassword(password)
    elif passtype == 'Mixed Sequence Characters':
        for i in range(0, length):
            password = password + random.choice(usecure)
        outputpass(password)
        pstype = 'High Secure'
        if (length < 5):
            pstype = 'Less Secure'
        statusupdate()
        if ans == 1:
            hashpassword(password)

def outputpass(passw):
    for things in pswdframe.winfo_children():
        things.destroy()
    pswdbox = tk.Text(pswdframe, font=('monospace', 11), bg='white')
    pswdbox.insert(tk.INSERT, f'{passw}')
    pswdbox.pack()

def resetall():
    for things in pswdframe.winfo_children():
        things.destroy()
    for things in statustext.winfo_children():
        things.destroy()
    for things in hashframe.winfo_children():
        things.destroy()
    l1.delete("1.0", "end")

def statusupdate():
    datetimee()
    for things in statustext.winfo_children():
        things.destroy()
    statbox = tk.Label(statustext, text=f'[{t1}]  A {pstype} Password was generated!')
    statbox.pack()

def close():
    sys.exit()
#User Interface design

header = tk.Label(root, text="      passwordGenerator      ",font=('AdobeClean-Bold',30), bg='black', fg='white')
header.place(x=0, y=10)

status = tk.Label(master, text='Status:', font=('AdobeClean-Bold',10))
status.place(x=15, y=10)
statustext = tk.Frame(master)
statustext.config(highlightthickness=0.5, highlightbackground='black')
statustext.place(x=15, y=35, height=24, width=300)
strength = tk.Label(master, text="Password Strength: ")
strength.place(x=15, y=69)
entrybox = Combobox(master, width=25, state='readonly')
entrybox['values'] = ('Alpha Characteres','Alphanumeric (A-Z, a-z, 0-9)','Mixed Sequence Characters')
entrybox.current(1)
entrybox.place(x=142, y=69)

length = tk.Label(master, text="Password length: ")
length.place(x=15, y=99)
l1 = Text(master, height=1, width=13)
l1.config(highlightthickness=0.5, highlightbackground='grey')
l1.place(x=142, y=99)

pswd = tk.Label(master, text='Resulting Password:')
pswd.place(x=15, y=230)

hashbtn = tk.Frame(master)
hashbtn.place(height=25, width=167, x=138, y=130)
var1 = IntVar()
Checkbutton(hashbtn, text="Show Password hash value", variable=var1).grid(row=0, sticky=W)
hashlabel = tk.Label(master, text="Hashed value of the password: ")
hashlabel.place(x=15, y=160)
hashframe = tk.Frame(master)
hashframe.config(highlightthickness=0.5, highlightbackground='black')
hashframe.place(height=35, width= 404,x=15,y=185)
pswdframe = tk.Frame(master)
pswdframe.config(highlightthickness=0.5, highlightbackground='#2d90de')
pswdframe.place(height=25, width= 404,x=15, y=255)
gen = tk.Button(master, text="Generate", bd=1, width=10, command=generatePass)
gen.config(highlightthickness=1, highlightbackground='black', bg='#e1e1e1')
gen.place(x=340, y=130)
resetbtn = tk.Button(master, text="RESET", width=10, bd=1, command=resetall)
resetbtn.config(bg='#e1e1e1')
resetbtn.place(x=340, y=33)

closebtn = tk.Button(master, text='Close', width=10, bd=1, command=close)
closebtn.config(bg='#e1e1e1')
closebtn.place(x=340, y=290)
copy = tk.Label(root, text=" © 2020 Shawan Mandal ", fg='grey')
copy.place(x=155, y=395)

root.mainloop()
