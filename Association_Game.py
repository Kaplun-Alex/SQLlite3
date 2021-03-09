import tkinter.font
from tkinter import *
import sqlite3
from _datetime import datetime

tk = tkinter.Tk()
tk.title("Association GAME")
tk.geometry("300x300+100+100")
BigFont = tkinter.font.Font(family='Hervetica', size=20, weight='bold')
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=5)
frame.pack(fill=BOTH, expand=1)
label_lw = tkinter.Label(frame, text="ОСТАННЄ СЛОВО:")
label_lw.pack(fill=X, expand=1)
last_label = Label(frame, text="**********", font=BigFont)
last_label.pack()
label_ew = Label(frame, text="ВВЕДИ СЛОВО АСОЦІАЦІЮ")
label_ew.pack(fill=X, expand=3)
entry_ew = Entry(frame, font=BigFont)
entry_ew.pack(fill=X)
button = tkinter.Button(frame, text="ВИХІД", command=tk.destroy, font=BigFont)
button.pack(side=BOTTOM)


def createdb():
    con = sqlite3.connect('Association.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS hrundel(N INTEGER, DT TEXT, WORD TEXT)')
    con.commit()
    cur.execute('select N from hrundel order by N desc')
    n = cur.fetchone()
    if None == n:
        cur_time = datetime.now()
        dt_string = cur_time.strftime("%d-%m-%Y %H:%M:%S")
        print(dt_string)
        print('Табле іс емпті, інзертінг фірст стрінг')
        cur.execute('INSERT INTO hrundel VALUES("0", "' + dt_string + '", "*****")')
    else:
        print('База створена, поля в нормі')
    con.commit()
    con.close()


createdb()


def lastword():
    con = sqlite3.connect('Association.db')
    cur = con.cursor()
    cur.execute('select * from hrundel order by N desc')
    selection = cur.fetchone()
    con.commit()
    con.close()
    try:
        print(selection[2])
        last_label.config(text=selection[2])
    except TypeError:
        print('Табле із емпті Братушка')


lastword()


def saveword():
    con = sqlite3.connect('Association.db')
    cur = con.cursor()
    cur_time = datetime.now()
    dt_string = cur_time.strftime("%d-%m-%Y %H:%M:%S")
    print(dt_string)
    cur.execute('select N from hrundel order by N desc')
    n = cur.fetchone()
    print(n)
    m = n[0] + 1
    s = str(m)
    print(s)
    con.commit()
    word = str(entry_ew.get())
    cur.execute('INSERT INTO hrundel VALUES("'+s+'", "' + dt_string + '" ,"'+word+'")')
    con.commit()
    con.close()
    last_label.config(text=word)
    entry_ew.delete(0, END)


set_button = tkinter.Button(frame, text="ДОДАТИ", command=saveword, font=BigFont)
set_button.pack(side=BOTTOM)

tk.mainloop()
