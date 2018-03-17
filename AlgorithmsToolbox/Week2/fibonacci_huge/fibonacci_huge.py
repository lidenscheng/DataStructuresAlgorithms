# Uses python3
#import sys

'''
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m
'''

def get_period(m): 
	a = 0
	b = 1
	c = a+b
	for i in range(0, m*m):
		c = (a+b) % m
		a = b 
		b = c
		if(a ==0 and b == 1):
			return i+1 

def get_fibonacci(number): 
	if(number <= 1):
		return number 
	
	else:
		FibList = [0]*(number + 1)
		FibList[0] = 0
		FibList[1] = 1

		for i in range(2, number + 1):
			FibList[i] = FibList[i-1] + FibList[i-2]

		return FibList[number] 		

def get_fibonacci_mod(n,m):
	if(n <= 1):
		return n

	else:
		period = get_period(m)
#		print(n, period) 
		number = n % period 
		fibonacci_value = get_fibonacci(number)  
		return (fibonacci_value % m) 

		
n, m = input().split()
n = int(n)
m = int(m)
print(get_fibonacci_mod(n, m))




