# Uses python3
import sys
import numpy as np

def optimal_weight(W, w, n):
# again add in extra column and row for numbering and initialize them to 0 
	values = np.empty((W+1,n+1))

	for j in range(W+1):
		for i in range(n+1):
			values[0][i] = 0
			values[j][0] = 0



	for j in range(1, W+1):
		for i in range(1, n+1):
			values[j][i] = values[j][i-1]
			if( w[i-1] <= j):
				val = values[j-w[i-1]][i-1] + w[i-1]
				if(values[j][i] < val):
					values[j][i] = val

	return int(values[-1][-1]) 
	


'''    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result
'''
if __name__ == '__main__':
	input = sys.stdin.read()
	W, n, *w = list(map(int, input.split()))
	print(optimal_weight(W, w, n))
#	optimal_weight(W, w, n)
