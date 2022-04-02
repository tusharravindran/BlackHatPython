import sqlite3 as sql
import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
import re
import urllib3
import hashlib
import os
import binascii
import random

try:
    handle = sql.connect("Population.db")
    cursor = handle.cursor()
    cursor.execute("CREATE TABLE USERS(USERNAME TEXT, PASSWORD TEXT)")
    handle.commit()
    handle.close()
except:
    cont = True

class student:
    nextid = 1 # class attribute

    def __init__(self):
        self.id = student.nextid
        self.age = student.__age(self) # private access modifier
        self.prob = random.random()
        student.nextid+=1

    def __age(self):
        number = random.randint(1, 6)
        if number == 1:
            #post-16
            number = random.randint(16, 18)
        else:
            #pre-16
            number = random.randint(12, 16)
        return number

    def showdetails(self):
        return self.id, self.age, self.prob

def age():
    number  = random.randint(1, 5)
    if number == 1:
        #post-16
        number = random.randint(16, 18)
    else:
        #pre-16
        number = random.randint(12, 15)
    return number

def average(cost1, cost2, prob1, prob2):
    total = 0
    for y in range(0, 1000):
        students = []
        cost = 0
        for c in range(0, 1200):
            temp = student()
            students.append(temp)
            chance = students[c].prob
            ages = students[c].age
            if ages >= 16 and chance > prob1:
                cost += cost1
            if ages < 16 and chance > prob2:
                cost += cost2
        total = total+cost
    average = total / 1000
    return average

class school:
    def __init__(self, pop):
        self.pop = pop
        self.students = []
        self.__populate()

    def __populate(self):
        for c in range(0, self.pop):
            temp = student()
            self.students.append(temp)

def hash_password(self, password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
        
def verify_password(self, stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

def closetab(result_tab):
            result_tab.destroy()

def newuser(IDentry, tab0):
    z = False
    handle = sql.connect("Population.db")
    cursor = handle.cursor()
    cursor.execute("SELECT USERNAME FROM USERS")
    allids = cursor.fetchall()
    handle.commit()
    handle.close()
    idsclean=[]
    for j in range(0, len(allids)):
        #call for new id if already exists, new tab with back button to main menu.
        a = str(allids[j])
        b = a.strip('(),')
        idsclean.append(b)
    nodup = 0
    ID_insert = IDentry.get()
    tab0.destroy()
    for r in range(0, len(idsclean)):
        idsclean[r] = idsclean[r][1:len(idsclean[r])-1]
        if idsclean[r] == ID_insert:
            z = True
            nodup = nodup+1
            if nodup == 1:
                error = ttk.Frame(tabcontrol)
                tabcontrol.add(error, text="Id taken")
                tabcontrol.select(error)
                tk.Label(error, text="Username is already taken...").grid(row=1)
                tk.Button(error, text="Back to Main Menu", command = lambda: [closetab(error), menu()]).grid(row=2)
    if z == False:
        tab6 = ttk.Frame(tabcontrol)
        tabcontrol.add(tab6, text="CREATE USER")
        tabcontrol.select(tab6)
        tk.Label(tab6, text="Username: ").grid(row=1)
        tk.Label(tab6, text=ID_insert).grid(row=1, column=1)
        Passwordentry = tk.Entry(tab6)
        Passwordentry.insert(END, "Password")
        Passwordentry.grid(row=2)
        tk.Button(tab6, text="Enter", command = lambda: loguser(Passwordentry, ID_insert, tab6)).grid(row=2, column=2)

def loguser(Passwordentry, ID_insert, tab6):
    Passwordentry = Passwordentry.get()
    handle = sql.connect("Population.db")
    cursor = handle.cursor()
    cursor.execute("INSERT INTO USERS VALUES(?,?)", (ID_insert, Passwordentry))
    handle.commit()
    handle.close()
    tab6.destroy()

def login(Passwordentry, IDENTentry, tab0):
    IDENT_insert = IDENTentry.get()
    PIN_insert = Passwordentry.get()
    tab0.destroy()
    handle = sql.connect("Population.db")
    cursor = handle.cursor()
    cursor.execute("SELECT USERNAME FROM USERS")
    ids = cursor.fetchall()
    handle.commit()
    idsclean = []
    for x in range(0, len(ids)):
        a = str(ids[x])
        b = a.strip('(),/\'')
        idsclean.append(b)
    ids = idsclean
    i = 0
    k = 0
    for x in range(0, len(ids)):
        if ids[i] == IDENT_insert:
            cursor.execute("SELECT USERS.PASSWORD FROM USERS WHERE USERS.USERID = ?", (IDENT_insert,))
            PINrecieved = cursor.fetchall()
            handle.commit()
            PINrecieved = PINrecieved[0]
            PINrecieved = str(PINrecieved)
            PINrecieved = PINrecieved.strip("/'(),'")
            TrueorFalse = verify_password(PINrecieved, PIN_insert)
            if TrueorFalse == True:
                cont2(IDENT_insert, PIN_insert)
                k = 8
        i = i+1
    # incorrect entry tab with a back to main menu button
    if k != 8:
        errorlogin = ttk.Frame(tabcontrol)
        tabcontrol.add(errorlogin, text="INVALID")
        tk.Label(errorlogin, text="ID or Password is incorrect", font="Ariel 15 bold italic").grid(row=1)
        tk.Button(errorlogin, text="Back to Main Menu", command= lambda: [closetab(errorlogin), menu()]).grid(row=2)

def cont2(IDENT_insert, PIN_insert):
    cont = True

def menu():
    tab0 = ttk.Frame(tabcontrol)
    tabcontrol.add(tab0, text="Catering Home")
    tabcontrol.select(tab0)
    tk.Label(tab0, text="LOGIN:", font="Ariel 15 bold italic").grid(row=10+1, columnspan=3)
    IDENTentry = tk.Entry(tab0)
    IDENTentry.insert(END, "ID")
    IDENTentry.grid(row=11+1, column=1)
    Passwordentry = tk.Entry(tab0)
    Passwordentry.insert(END, "Password")
    Passwordentry.grid(row=12+1, column=1)
    tk.Label(tab0, text="NEW USER:", font="Ariel 15 bold italic").grid(row=15+1, columnspan=3)
    IDentry = tk.Entry(tab0)
    IDentry.insert(END, "ID")
    IDentry.grid(row=19+1, column=1)
    tk.Button(tab0, text="Enter", command = lambda: login(Passwordentry, IDENTentry, tab0)).grid(row=14, column=1)
    tk.Label(tab0, text=" ").grid(row=15, column=1)
    tk.Button(tab0, text="Enter", command = lambda: newuser(IDentry, tab0)).grid(row=21, column=1)



window=tk.Tk()
window.title("Catering")
tabcontrol = ttk.Notebook(window)
menu()
tabcontrol.pack(expand=1, fill="both")
window.mainloop()