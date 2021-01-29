#################################
#              ATM              #
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
	import Tkinter.tkMessageBox as msgbox

''' Passwords List '''
Passwords = list()

''' Special Ch '''
Sp_Ch = ('~','!','@','#','$','%','^','&','*','(',')','_','-','=','+','>','<','\\','\/','\'','\"')

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
	Developer_Label = Label(MainWindow,text='By: Mahmoud M.Kamal',bg='gold').grid(row=8,column=3)
	ID_Label = Label(MainWindow,text='Password:',font=30,bg='gold').grid(row=3,column=2)
	global Pass_Entry
	Pass_Entry = Entry(MainWindow,font=30,bg='gold')
	Pass_Entry.grid(row=3,column=3)
	Save_Button = Button(MainWindow,text="Save",fg='white',bg='blue',font=30,command=Save_Button_Fn)
	Save_Button.grid(row=5,column=3)
	Copy_Button = Button(MainWindow,text="Copy",fg='white',bg='blue',font=30,)
	Copy_Button.grid(row=6,column=3)
	Exit_MainWindow_Button = Button(MainWindow,text=" Exit ",fg='white',bg='red',font=30,command=MainWindow.destroy)
	Exit_MainWindow_Button.grid(row=7,column=3)

def Save_Button_Fn():
	if (7<len(Pass_Entry.get())<33):
		if Validate_Password(Pass_Entry.get()) == 1:
			if (Pass_Entry.get()) not in Passwords:
				NewPassword = Pass_Entry.get()
				Passwords.append(NewPassword)
				msgbox.showinfo("Done!","The Password was saved")
				Passwords_File = open('Passwords.txt','w')
				for i in range(len(Passwords)):
					Passwords_File.write(str(i)+': '+Passwords[i]+'\n')
				Passwords_File.close()
			else:
				msgbox.showerror('Error!',"Password generated before\nTry again!")
		else:
			msgbox.showerror('Error!',"The Password shall have upper letter, lower letter, number and a special character\nTry again!")
	else:
		msgbox.showerror('Error!',"Length of the Password has to be between 8-32 character\nTry again!")

def Validate_Password(Password):
	Flag_Upper = Flag_Lower = Flag_Num = Flag_Sp = 0
	for i in range(len(Pass_Entry.get())):
		if 'A'<=(Pass_Entry.get()[i])<='Z':
			Flag_Upper = 1
		elif 'a'<=(Pass_Entry.get()[i])<='z':
			Flag_Lower = 1
		elif '0'<=(Pass_Entry.get()[i])<='9':
			Flag_Num = 1
		elif (Pass_Entry.get()[i]) in Sp_Ch:
			Flag_Sp = 1
	if (Flag_Upper == 1) and (Flag_Lower == 1) and (Flag_Num == 1) and (Flag_Sp == 1):
		return 1
	else:
		return 0
	
def Copy_Button_Fn():
	if (7<len(Pass_Entry.get())<33):
		if (Pass_Entry.get()) not in Passwords:
			NewPassword = Pass_Entry.get()
			Passwords.append(NewPassword)
			msgbox.showinfo("Done!","The Password was saved")
			Passwords_File = open('Passwords.txt','w')
			for i in range(len(Passwords)):
				Passwords_File.write(str(i)+': '+Passwords[i]+'\n')
			Passwords_File.close()
		else:
			msgbox.showerror('Error!',"Password generated before\nTry again!")
	else:
		msgbox.showerror('Error!',"Length of the Password has to be between 8-32 character\nTry again!")