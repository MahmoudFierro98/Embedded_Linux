#################################
# Author: Mahmoud Mohamed Kamal	#
# Date  : 20 NOV 2020		    #
#################################

def SET_BIT(VAR,BITNO):
	Output = int(VAR) | (1 << int(BITNO))
	return Output
	
def CLR_BIT(VAR,BITNO):
	Output = int(VAR) & (~(1 << int(BITNO)))
	return Output
	
def GET_BIT(VAR,BITNO):
	return ((int(VAR) >> int(BITNO)) & (1))
	
def TOG_BIT(VAR,BITNO):
	Output = int(VAR) ^ (1 << int(BITNO))
	return Output
