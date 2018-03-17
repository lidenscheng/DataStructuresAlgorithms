# Uses python3
import sys

def get_change(m):
    #write your code here
	
	change_number = int(m/10)
	
	if( (m%10) == 0):
		return change_number

	else:
		m = m % 10

	change_number = change_number + int(m/5)

	if( (m%5) == 0):
		return change_number

	else:
		m = m % 5

	return change_number + m 


m = int(input()) 
print(get_change(m))

