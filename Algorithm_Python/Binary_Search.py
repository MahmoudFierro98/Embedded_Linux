#################################
#         Binary Search         #     
# Author: Mahmoud Mohamed Kamal #
# Date  : 25 NOV 2020           #
#################################

# Enter N Numbers
List_Length = int(input("Enter the Length of list: "))
Input_List  = []
print("\n")

# Scan the Values
for i in range(List_Length):
	print("Enter #",i,": ",end="")
	New_Number    = float(input())
	Input_List.append(New_Number)

# Display List
#print("\nYour List:",Input_List)

# Sort the Values using Bubble Sorting
for i in range(List_Length-1):
	for j in range(List_Length-1):
		if (Input_List[j] > Input_List[j+1]):
			# Swap
			Input_List[j],Input_List[j+1] = Input_List[j+1],Input_List[j]
			
# Display List after Sorting
#print("\nYour List after \"Bubble Sorting\":",Input_List)

# Scan the value to search
Num = float(input("\nPlease Enter number to search: "))

# Binary Search 
Flag  = 0
Start = 0
End   = List_Length - 1
while(Start <= End):
	Center = (Start + End) // 2
	print(Center)
	if   (Num == Input_List[Center]):
		Flag = 1
	elif (Num > Input_List[Center]):
		Start = Center + 1
	elif (Num < Input_List[Center]):
		End   = Center - 1
if (Flag == 1):
	print(Num,"is Found")
else:
	print(Num,"is Not Exist")