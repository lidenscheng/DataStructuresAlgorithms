# Uses python3
import sys
import numpy as np 

def get_optimal_value(capacity, weights, values):
#	amounts = [0] * len(values)
	amounts =  np.zeros((len(values),), dtype=int) 
#	ratios = sorted([a/b for a,b in zip(values, weights)], reverse = True)

	ratios = values/weights
	indices = ratios.argsort()[::-1] #get corresponding indices when sorting weighted values in descending order 
	ratios = ratios[indices]
	values = values[indices]
	weights = weights[indices]

	amounts = amounts[indices]  #holds the amount of each item that will be in sack 

	value = 0.
	a = 0

	for i in range(len(ratios)):
		if(capacity == 0.0):
			print(amounts) 
			return value

		a = min(weights[i], capacity)
		value = value + a*ratios[i]
		weights[i] = weights[i] - a
		amounts[i] = amounts[i] + a
		capacity = capacity - a

	print(amounts)
	return value 



if __name__ == "__main__":
	data = list(map(int, sys.stdin.read().split()))
	n, capacity = data[0:2]
	values = np.array(data[2:(2 * n + 2):2]) #make these numpy arrays so can use numpy capabilities later 
	weights = np.array(data[3:(2 * n + 2):2]) 
	opt_value = get_optimal_value(capacity, weights, values)
	print("{:.10f}".format(opt_value))

