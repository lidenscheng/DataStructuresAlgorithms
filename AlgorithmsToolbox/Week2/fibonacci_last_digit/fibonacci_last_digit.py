# Uses python3
#import sys

def get_fibonacci_last_digit_naive(n):

	FibList = [0]*(n+1)
	FibList[0] = 0%10
	FibList[1] = 1%10

	for i in range(2,n+1):
		FibList[i] = (FibList[i-1] + FibList[i-2]) % 10 

	return FibList[n] 	



'''    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10
'''

#if __name__ == '__main__':
#    input = sys.stdin.read()
n = int(input())
print(get_fibonacci_last_digit_naive(n))
