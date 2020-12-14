#################################
#  Algorithm_Functions_Python   #
# Author: Mahmoud Mohamed Kamal #
# Date  : 14 DEC 2020           #
#################################
import Algorithm as AL

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

#AL.Bubble_Sort(List_Length,Input_List)
#AL.Selection_Sort(List_Length,Input_List)
#AL.Linear_Search(List_Length,Input_List)
#AL.Binary_Search(List_Length,Input_List)

# Display List after Sorting
print("\nYour List after \"Sorting\":",Input_List)
