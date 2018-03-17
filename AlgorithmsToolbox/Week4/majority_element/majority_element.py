# Uses python3
import sys

def get_majority_element(A, left, right):
	n = right+1
	if left == right:
		return A[right]
	if left + 1 == right:
		if(A[right] == A[left]):
			return A[left]
		else:
			return -1

	m = left + ((right - left) // 2)
	B = get_majority_element(A, left, m)
	C = get_majority_element(A, m+1, right)

	if (B != -1) and (A[left:right + 1].count(B) > ((n-left)//2) ):
		return(B)
	elif (C != -1) and (A[left:right + 1].count(C) > ((n-left)//2) ):
		return(C)

	return -1

	

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    if get_majority_element(A, 0, n-1) != -1:
        print(1)
    else:
        print(0)
