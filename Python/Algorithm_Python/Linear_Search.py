#################################
#         Linear Search         #
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
print("\nYour List:",Input_List)

# Linear Search
Num   = float(input("Enter a number to count its existance: "))
Count = 0
for i in range(List_Length):
	if (Input_List[i] == Num):
		Count += 1

# Display number exist # times
print("\nThe number exist",Count,"Times")