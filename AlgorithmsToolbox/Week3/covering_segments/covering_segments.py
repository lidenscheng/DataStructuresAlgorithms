# Uses python3
import sys
#from collections import namedtuple
#from operator import attrgetter

#Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
	points = []
	segments = sorted(segments, key=lambda x: x[1]) 
#	segments = sorted(segments, key=attrgetter('end'))
#	print(segments) 
	min_rightend = int(segments[0][1]) 
	points.append(min_rightend) 
#	print(min_rightend) 


	for i in range(len(segments)):
		if(min_rightend < int(segments[i][0])):
			min_rightend = int(segments[i][1]) 
			points.append(min_rightend) 
#			print(points, segments[i][0], segments[i][1]) 

	return points 

'''	for i in range(len(segments)):
		if(min_rightend < segments[i].start):
			min_rightend = segments[i].end
			points.append(min_rightend)
'''

		
			


if __name__ == '__main__':
	inputs = sys.stdin.read()
	n, *data = map(int, inputs.split())
#	segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
	segments = list(zip(data[::2], data[1::2]))
#	print(segments) 
	points = optimal_points(segments)
	print(len(points))
	for p in points:
		print(p, end=' ')


