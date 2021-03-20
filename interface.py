from tkinter import *
import os

def register_user():
  username_info = username.get()
  password_info = password.get()

  file = open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  
  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Successful!", fg = "green", font = ("calibri", 11)).pack()

def register():
  global screen1
  global username
  global password
  global username_entry
  global password_entry
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("400x300")

  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  
  Label(screen1, text = "Username *").pack()
  
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()  
  
  Label(screen1, text = "Password *").pack()  
  password_entry = Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()  
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()
  
def delete4():
  screen5.destroy()

def function1():

    os.system("python ajout.py")

def function2():

    os.system("python traitement.py")

def function3():

    os.system("python reconnaissance.py")

def function4():

    os.system("python absence.py")

def function6():
  
  screen6.destroy()
  

def session():
  global screen6
  screen6 = Toplevel(screen) 
  screen6.title("Dashboard")
  screen6.geometry("500x400")
  Label(screen6, text = "Welcome to the main dashboard!").pack()
  Label(screen6, text = "").pack()
  Button(screen6, text = "Ajouter un etudiant",height = "2", width = "30", command = function1).pack()
  Label(screen6, text = "").pack()
  Button(screen6, text = "Traitement",height = "2", width = "30", command = function2).pack()
  Label(screen6, text = "").pack()
  Button(screen6, text = "reconnaissance faciale",height = "2", width = "30", command = function3).pack()
  Label(screen6, text = "").pack()
  Button(screen6, text = "absence",height = "2", width = "30",command = function4).pack()
  Label(screen6, text = "").pack()
  Button(screen6, text = "quiter",height = "2", width = "30",command = function6).pack()

def login_success():
  session()
  
def incorrect_password():
  global screen4

  screen4 = Toplevel(screen)
  screen4.title("Denied!")
  screen4.geometry("400x300")

  Label(screen4, text = "Password not recognized!").pack()
  Button(screen4, text = "OK", command = delete3).pack()

def user_not_found():
  global screen5
  
  screen5 = Toplevel(screen)
  screen5.title("Not found!")
  screen5.geometry("400x300")
  
  Label(screen5, text = "User not found!").pack()
  Button(screen5, text = "OK", command = delete4).pack()


def login_verify():
  username1 = username_verify.get()
  password1 = password_verify.get()
 
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)
  
  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    
    verify = file1.read().splitlines()
    if password1 in verify:
      login_success()
    else:
      incorrect_password()
  else:
    user_not_found()
  


def login():
  global screen2
  global username_verify
  global password_verify
  global username_entry1
  global password_entry1

  username_verify = StringVar()
  password_verify = StringVar()

  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("400x300")
  
  Label(screen2, text = "Please enter login details below").pack()
  Label(screen2, text = "").pack()
  

  
  Label(screen2, text = "Username * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()  
  
  Label(screen2, text = "").pack()
  
  Label(screen2, text = "Password * ").pack()  
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()

  Button(screen2, text = "Login", width = 12, height = 1, command = login_verify).pack()

def main_screen():
  global screen

  screen = Tk()
  screen.geometry("400x300")
  screen.title("gestion d'absence")

  Label(text = "gestion d'absence", bg = "grey", width = "400", height = "2", font = ("Calibri", 14)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register", height = "2", width = "30", command = register).pack()

  screen.mainloop()

main_screen() 