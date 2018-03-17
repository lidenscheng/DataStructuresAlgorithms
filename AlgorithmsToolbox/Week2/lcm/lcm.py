# Uses python3
#import sys

'''def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
'''

def gcd(a,b):
	new_a = a % b 

	while( new_a != 0):
		a = b
		b = new_a
		new_a = a % b 
		
	return b 
	

def lcm(a,b):

	gcd_number = gcd(a,b)
	lcm_number = (a*b) // gcd_number #running into int and float issue here so I used // for int dividing 
	print(lcm_number) 
	

a, b = input().split()
a = int(a)
b = int(b) 
lcm(a,b)

