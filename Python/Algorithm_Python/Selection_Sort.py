#################################
#         Selection Sort        #
# Author: Mahmoud Mohamed Kamal #
# Date  : 26 NOV 2020           #
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

# Selection Sorting
for i in range(List_Length-1):
	for j in range(i+1,List_Length):
		if (Input_List[i] > Input_List[j]):
			# Swap
			Input_List[i],Input_List[j] = Input_List[j],Input_List[i]
			
# Display List after Sorting
print("\nYour List after \"Selection Sorting\":",Input_List)