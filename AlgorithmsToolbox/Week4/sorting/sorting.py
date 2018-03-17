# Uses python3
import sys
import random

def partition3(a, l, r):    
	x = a[l]
	left_region = l
	right_region = r
	i = l+1

	while( i <= right_region):
		if( a[i] < x):
			a[i], a[left_region] = a[left_region], a[i]
			left_region = left_region + 1
			i = i + 1

		elif( a[i] > x ):
			a[i], a[right_region] = a[right_region], a[i]
			right_region = right_region - 1 

		else:
			i = i + 1

	return left_region, right_region 

			

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
	if l >= r:
		return

	k = random.randint(l, r)
	a[l], a[k] = a[k], a[l]

#    m = partition2(a, l, r)
	(m1, m2) = partition3(a, l, r)

#	randomized_quick_sort(a, l, m - 1);
#	randomized_quick_sort(a, m + 1, r);

	randomized_quick_sort(a, l, m1 - 1);
	randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
