# Uses python3
import sys

def get_number_of_inversions(a, e, left, right):

	if(len(a) == 1):
		return a, 0

	mid = len(a)//2
#	print(mid, type(mid))

	B, left_inversions = get_number_of_inversions( a[:mid], e, left, mid ) 
	C, right_inversions = get_number_of_inversions( a[mid:], e, mid+1, right ) 

	e, number_of_inversions = Merge(B, C)


#	print(new_a, number_of_inversions+left_inversions+right_inversions) 
#	print(new_a) 
	return e, (number_of_inversions + left_inversions + right_inversions) 


def Merge(B,C):
	e = [] 
	countPairs = 0
	while(B and C):
		b = B[0]
		c = C[0]

		if(b <= c):
			e.append(b)
			B.remove(b)

		else:
			e.append(c)
			C.remove(c) 
			countPairs += len(B)
	
	if(B):
		e += B

	elif(C):
		e += C


	return e, countPairs 




if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	e = []  
	print( get_number_of_inversions(a, e, 0, n-1)[1] )



