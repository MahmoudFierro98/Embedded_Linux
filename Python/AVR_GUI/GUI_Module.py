#################################
# Author: Mahmoud Mohamed Kamal	#
# Date  : 23 JAN 2021		    #
#################################

from tkinter import *
import tkinter.messagebox as msgbox

# Lists
Labels          = list()
Radio_Inputs    = list()
Radio_Outputs   = list()
Radio_Variables = list()

# Main Window Configuration
def Init_MainWindow():
	global MainWindow
	MainWindow = Tk()
	MainWindow.geometry("320x380+150+150")
	MainWindow.title("Avr DIO Configuration")
	MainWindow.configure(background="gold")
	MainWindow.resizable(width=False, height=False)
	i = 0
	while i<5:
		MainWindow.columnconfigure(i,minsize='10m')
		i += 1
	i = 0
	while i<10:
		MainWindow.rowconfigure(i,minsize='10m')
		i += 1

# Create Buttons
def Create_Buttons():
	Generate_Button = Button(MainWindow,text='Generate',bg='blue',fg='white',command=Generate)
	Exit_Button = Button(MainWindow,text='Exit',bg='blue',fg='white',command=MainWindow.destroy)
	Generate_Button.grid(row=9,column=3)
	Exit_Button.grid(row=9,column=4)

# Create Labels
def Create_Labels():
	for i in range(8):
		Labels.append(Label(MainWindow,text="Pin "+str(i)+" Mode",bg="gold"))
		Labels[i].grid(row=i,column=0)

# Create RadioButtons
def Create_Radiobuttons():
	for i in range(8):
		Radio_Variables.append(IntVar())
		Radio_Inputs.append(Radiobutton(MainWindow,text='Input',value=0,variable=Radio_Variables[i],bg="gold"))
		Radio_Outputs.append(Radiobutton(MainWindow,text='Output',value=1,variable=Radio_Variables[i],bg="gold"))
		Radio_Inputs[i].grid(row=i,column=2)
		Radio_Outputs[i].grid(row=i,column=3)

# Create DIO_prog.c file
def Generate():
	DDRA = str()
	for i in range(8):
		Value = Radio_Variables[i].get()
		DDRA  = str(Value) + DDRA
	file = open("DIO_prog.c","w")
	file.write("MDIO_voidInitPortA(void)\n{\n\tDDRA = 0b"+DDRA+";\n}")
	file.close()
	msgbox.showinfo("Avr DIO Configuration", "Done!")