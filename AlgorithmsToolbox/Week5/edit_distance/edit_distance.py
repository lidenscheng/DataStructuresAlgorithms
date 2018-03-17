# Uses python3
import math 
import numpy as np 

def edit_distance(s, t):
	n = len(s)
	m = len(t)
	distance = np.zeros((n+1,m+1))
	#len(s)+1 and len(t)+1 for number of rows and columns because we add an extra row and column in just for numbering 0-n and 0-m 

	for i in range(n+1):	#this numbering happens here 
		for j in range(m+1):
			distance[i][0] = i
			distance[0][j] = j 

	for i in range(1, n+1):
		for j in range(1, m+1):

			insert = distance[i][j-1]+1
			delete = distance[i-1][j]+1
			match = distance[i-1][j-1]
			mismatch = distance[i-1][j-1]+1

			if( s[i-1] == t[j-1]): 
				distance[i][j] = min(insert, delete, match)

			else:
				distance[i][j] = min(insert, delete, mismatch)

	
	return int(distance[-1][-1]) 

if __name__ == "__main__":
	print(edit_distance(input(), input()))
#	edit_distance(input(), input())

