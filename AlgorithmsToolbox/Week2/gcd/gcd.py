# Uses python3
import sys

'''def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
'''

def gcd(a,b):
	new_a = a % b 

	while( new_a != 0):
		a = b
		b = new_a
		new_a = a % b 
		
	return b 
	
	

a, b = input().split()
a = int(a)
b = int(b) 
result = gcd(a,b)
print(result)
