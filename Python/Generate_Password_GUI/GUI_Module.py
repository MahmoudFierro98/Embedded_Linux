#################################
#       Generate Password       #
# Author: Mahmoud Mohamed Kamal	#
# Date  : 29 JAN 2021		    #
# File  : GUI_Module.py         #
#################################

''' Import tkinter module '''
try:
	''' For Python 3.x '''
	from tkinter import *
	import tkinter.messagebox as msgbox
except:
	''' For Python 2.7 '''
	from Tkinter import *
	import tkMessageBox as msgbox

''' Import others modules '''
import random
import string
import pyperclip

''' Passwords List '''
Passwords = list()

''' NewPassword Variable '''
NewPassword = ''

''' Create Main Window '''
def Create_MainWindow():
	global MainWindow
	MainWindow = Tk()
	MainWindow.geometry("460x350+200+200")
	MainWindow.title("Password Generator Application")
	MainWindow.configure(background="gold")
	MainWindow.resizable(width=False, height=False)
	i = 0
	while i<6:
		MainWindow.columnconfigure(i,minsize='10m')
		i += 1
	i = 0
	while i<9:	
		MainWindow.rowconfigure(i,minsize='10m')
		i += 1
	Welcome_Label = Label(MainWindow,text='Password Generator Application',font=30,bg='gold').grid(row=0,column=2,columnspan=2)
	Length_Label = Label(MainWindow,text='Length:',font=30,bg='gold').grid(row=3,column=2)
	global Length_Spinbox
	Length_Spinbox = Spinbox(MainWindow,from_=8,to=32)
	Length_Spinbox.grid(row=3,column=3)
	Generate_Button = Button(MainWindow,text="Generate",fg='white',bg='blue',font=30,command=Generate_Button_Fn)
	Generate_Button.grid(row=6,column=3)
	Exit_MainWindow_Button = Button(MainWindow,text=" Exit ",fg='white',bg='red',font=30,command=MainWindow.destroy)
	Exit_MainWindow_Button.grid(row=7,column=3)
	Developer_Label = Label(MainWindow,text='By: Mahmoud M.Kamal',bg='gold').grid(row=8,column=3)

''' Generate Button Function '''
def Generate_Button_Fn():
	if (7<int(Length_Spinbox.get())<33):
		global NewPassword
		NewPassword = Generate_Password(int(Length_Spinbox.get()))
		if NewPassword not in Passwords:
			MainWindow.withdraw()
			global PasswordWindow
			PasswordWindow = Toplevel()
			PasswordWindow.geometry("500x200+200+200")
			PasswordWindow.title("Password Generator Application")
			PasswordWindow.configure(background="gold")
			PasswordWindow.resizable(width=False, height=False)
			Welcome_Label = Label(PasswordWindow,text='Password Generator Application',font=30,bg='gold').pack()
			Password_Label = Label(PasswordWindow,text='Password: '+NewPassword,font=30,bg='gold').pack()
			Copy_Button = Button(PasswordWindow,text="Copy",fg='white',bg='blue',font=30,command=Copy_Button_Fn)
			Copy_Button.pack()
			Close_MainWindow_Button = Button(PasswordWindow,text=" Close ",fg='white',bg='red',font=30,command=Close_Button_Fn)
			Close_MainWindow_Button.pack()
			Developer_Label = Label(PasswordWindow,text='By: Mahmoud M.Kamal',bg='gold').pack()
			Passwords.append(NewPassword)
			Passwords_File = open('Passwords.txt','w')
			for i in range(len(Passwords)):
				Passwords_File.write(str(i)+': '+Passwords[i]+'\n')
			Passwords_File.close()
		else:
			msgbox.showerror('Error!',"Password generated before\nTry again!")
	else:
		msgbox.showerror('Error!',"Length of the Password has to be between 8-32 character\nTry again!")

''' Generate Password Function '''
def Generate_Password(length):
	password_characters = string.ascii_letters + string.digits + string.punctuation
	password = ''.join(random.choice(password_characters) for i in range(length))
	return password

''' Copy Button Function '''
def Copy_Button_Fn():
	pyperclip.copy(NewPassword)
	msgbox.showinfo("Done!","The Password was Copied")	
	
''' Close PasswordWindow Button Function '''
def Close_Button_Fn():
	PasswordWindow.destroy()
	MainWindow.deiconify()
