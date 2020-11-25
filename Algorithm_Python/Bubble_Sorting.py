#################################
#         Bubble Sorting        #
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

# Bubble Sorting
for i in range(List_Length-1):
	for j in range(List_Length-1):
		if (Input_List[j] > Input_List[j+1]):
			# Swap
			Input_List[j],Input_List[j+1] = Input_List[j+1],Input_List[j]
			
# Display List after Sorting
print("\nYour List after \"Bubble Sorting\":",Input_List)