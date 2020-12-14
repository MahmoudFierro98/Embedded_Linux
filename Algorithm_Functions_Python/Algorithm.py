#################################
#  Algorithm_Functions_Python   #
# Author: Mahmoud Mohamed Kamal #
# Date  : 14 DEC 2020           #
#################################

# Bubble Sorting
def Bubble_Sort(List_Length, Input_List):
	for i in range(List_Length-1):
		for j in range(List_Length-1-i):
			if (Input_List[j] > Input_List[j+1]):
				# Swap
				Input_List[j],Input_List[j+1] = Input_List[j+1],Input_List[j]
				
# Selection Sorting
def Selection_Sort(List_Length, Input_List):
	for i in range(List_Length-1):
		for j in range(i+1,List_Length):
			if (Input_List[i] > Input_List[j]):
				# Swap
				Input_List[i],Input_List[j] = Input_List[j],Input_List[i]
			
# Linear Search
def Linear_Search(List_Length, Input_List):
	# Scan the value to search\
	Num   = float(input("Enter a number to count its existance: "))
	Count = 0
	for i in range(List_Length):
		if (Input_List[i] == Num):
			Count += 1
	# Display number exist # times
	print("\nThe number exist",Count,"Times")
	
# Binary Search
def Binary_Search(List_Length, Input_List):
	# Scan the value to search
	Num = float(input("\nPlease Enter number to search: "))
	# Sort
	Input_List.sort()
	# Binary Search 
	Flag  = 0
	Start = 0
	End   = List_Length - 1
	while(Start <= End):
		Center = (Start + End) // 2
		if   (Num == Input_List[Center]):
			Flag = 1
			break
		elif (Num > Input_List[Center]):
			Start = Center + 1
		elif (Num < Input_List[Center]):
			End   = Center - 1
	if (Flag == 1):
		print(Num,"is Found")
	else:
		print(Num,"is Not Exist")