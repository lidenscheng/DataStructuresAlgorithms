# Uses python3
#import sys

'''
def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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

def fibonacci_partial_sum(from_, to):

	if(to <= 1):
		return (to - from_)

	period = get_period(10) 
	value_from = (from_ + 1) % period
	value_to = (to + 2) % period 
	

	FibList = [0]*(value_to + 1)  
	FibList[0] = 0
	FibList[1] = 1

	for i in range(2, value_to + 1):
		FibList[i] = FibList[i-1] + FibList[i-2]

	totalSum = FibList[value_to] - 1
	lowerSum = FibList[value_from] - 1

	partialSum = totalSum - lowerSum
	return (partialSum % 10) 
	

#if __name__ == '__main__':
#    input = sys.stdin.read();
#    from_, to = map(int, input.split())
from_, to = input().split()
from_ = int(from_)
to = int(to)
print(fibonacci_partial_sum(from_, to))


