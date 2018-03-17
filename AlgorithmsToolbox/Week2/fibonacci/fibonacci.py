# Uses python3
def calc_fib(n):

	if(n<=1):
		return n 

	else:

		FibList = [0]*(n+1)
		FibList[0] = 0
		FibList[1] = 1

		for i in range(2,n+1):
			FibList[i] = FibList[i-1] + FibList[i-2]

		return FibList[n] 

'''    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)
'''

n = int(input())
print(calc_fib(n))
