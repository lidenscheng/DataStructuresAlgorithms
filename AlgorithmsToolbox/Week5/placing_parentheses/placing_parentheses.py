# Uses python3
import numpy as np

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(i,j, operators, minima, maxima):
	minimum = np.inf
	maximum = -np.inf

	for k in range(i,j):
		a = evalt(maxima[i-1][k-1], maxima[k][j-1], operators[k-1])
		b = evalt(maxima[i-1][k-1], minima[k][j-1], operators[k-1])
		c = evalt(minima[i-1][k-1], maxima[k][j-1], operators[k-1])
		d = evalt(minima[i-1][k-1], minima[k][j-1], operators[k-1])

		minimum = min(minimum, a, b, c, d)
		maximum = max(maximum, a, b, c, d)

	return(minimum, maximum) 

def get_maximum_value(dataset):
	operators = []
	digits = []
	for x in dataset:
		if( x in ["+", "-", "*"] ): 	
			operators.append(x)
		else:
			digits.append(x) 

	n = len(digits) 

	minima = np.zeros((n,n))
	maxima = np.zeros((n,n)) 

	for i in range(n):
		minima[i][i] = digits[i]
		maxima[i][i] = digits[i] 

	for s in range(1,n):
		for i in range(1,(n+1)-s):
			j = i+s
			minima[i-1][j-1], maxima[i-1][j-1] = MinAndMax(i,j, operators, minima, maxima)  

	return(int(maxima[0][n-1])) 


if __name__ == "__main__":
	print(get_maximum_value(input()))
