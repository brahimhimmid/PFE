import tkinter as tk
from tkinter import *
from tkinter import ttk
import cx_Oracle

conn = cx_Oracle.connect('SYSTEM/lghazwa2020@localhost')
cursor = conn.cursor()

sql = "SELECT * FROM absence"
cursor.execute(sql)
rows = cursor.fetchall()
total = cursor.rowcount
print("TOTAL DATA Entries: "+str(total))


win = Tk()

frm = Frame(win)
frm.pack(side=tk.LEFT, padx=20)

tv = ttk.Treeview(frm, columns=(1,2), show="headings", height="5")
tv.pack()

tv.heading(1, text="NOM ET PRENOM")
tv.heading(2,text="DATE")


for i in rows:
	tv.insert("",'end', values=i)


win.title("ID's of absent student")
win.geometry("450x250")
win.resizable(False, False)
win.mainloop()