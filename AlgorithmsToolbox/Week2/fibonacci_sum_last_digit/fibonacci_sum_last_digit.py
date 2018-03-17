# Uses python3
#import sys
import math 

'''
def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10
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

def fibonacci_sum(n): 
	if (n <= 1):
		return n

	period = get_period(10)
	value = (n+2) % period 
	
	FibList = [0]*(value + 1)
	FibList[0] = 0
	FibList[1] = 1

	for i in range(2, value + 1):
		FibList[i] = FibList[i-1] + FibList[i-2]

	totalSum = FibList[value] - 1
	return (totalSum % 10)  	



#if __name__ == '__main__':
#    input = sys.stdin.read()
n = int(input())
print(fibonacci_sum(n))



