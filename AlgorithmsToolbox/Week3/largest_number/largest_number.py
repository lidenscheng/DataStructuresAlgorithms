#Uses python3

import sys

def largest_number(a):
    #write your code here
	res = ""
	
	while( len(a) != 0):
		max_digit = '0'
		for number in a:
			if( number + max_digit >= max_digit + number): 
				max_digit = number 
		
		res += max_digit
		a.remove(max_digit)

	return res 





'''	for i in range(0, len(a)-1):
		if( len(a[i+1]) == 1 and a[i][0] == a[i+1][0]):
			res += a[i+1] 

		else:
			res += a[i] 

	return res 
	'''	


'''    for x in a:
        res += x
    return res
'''



if __name__ == '__main__':
	inputs = sys.stdin.read()
	data = inputs.split() 
	a = data[1:]
	print(largest_number(a))
  
