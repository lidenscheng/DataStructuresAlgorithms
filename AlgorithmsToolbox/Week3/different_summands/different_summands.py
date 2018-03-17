# Uses python3

def optimal_summands(n):
	summands = []
	totalSum = 0
    #write your code here	
	k = n
	l = 1

	while( k!= 0):
		if(k <= 2*l):
			summands.append(k)
			return summands 

		else:
			summands.append(l) 
			k = k - l
			l = l + 1


#	return summands



n = int(input())
summands = optimal_summands(n)
print(len(summands))
for x in summands:
	print(x, end=' ')
