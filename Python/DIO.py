#################################
# Author: Mahmoud Mohamed Kamal	#
# Date  : 20 NOV 2021		    #
#################################

file = open("DIO_prog.c",'w')
file.write("MDIO_voidInit(void)\n{\n")
DDRA = ""

for i in range(8):
	flag = 1
	while(flag):
		user_input = input("Pin " + str(i) + ": ")
		user_input = user_input.lower()
		if user_input == 'input':
			flag = 0
			DDRA = '0' + DDRA
		elif user_input == 'output':
			flag = 0
			DDRA = '1' + DDRA 
		else:
			print("Error :: Enter Input or Output only")
DDRA = "0b" + DDRA;
file.write("\tDDRA = "+DDRA+";\n}")
file.close()