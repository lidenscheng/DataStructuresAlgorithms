# Uses python3
import sys

def fast_count_segments(starts, ends, points):
	cnt = [0] * len(points)

	all_sets = []

	#0: it's the start of a segment
	#1: it's a point 
	#2: it's the end of a segment 

	for start in starts:
		all_sets.append((start, 0))

	for idx, point in enumerate(points):
		all_sets.append((point, 1, idx)) #looks like (point, 1, index) 

	for end in ends:
		all_sets.append((end, 2))

	#the key idea here is that all the segment beginnings, ends, and points are put in increasing order. so if a point is between a segment's beginning and a segment's ending, it would be in
	#the middle of the two tuples in the list 

	all_sets = sorted(all_sets, key=lambda x: (x[0], x[1]) )
#	print(all_sets)

	found_at_start = 0

	for seg in all_sets: 
		if(seg[1] == 0):
			found_at_start += 1

		elif(seg[1] == 1):
			cnt[seg[2]] = found_at_start 

		elif(seg[1] == 2):
			found_at_start -= 1

		else:
			continue 

	#when we iterate through this ordered list of tuples, if we get 0 1 then there's a point in a segment. if we get 0 2 then there is no point in the segment 
	#if we get 0 0 1 then the point is in 2 segments 


	return cnt  

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
#    cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
