# Uses python3
# There are two ways of running this program:
# 1. Run
#     python3 APlusB.py
# then enter two numbers and press ctrl-d/ctrl-z
# 2. Save two numbers to a file -- say, dataset.txt.
# Then run
#     python3 APlusB.py < dataset.txt

a, b = input().split()
a = int(a)
b = int(b) 

if(a >= 0 and b<=9):
	print(a+b)
else:
	print("Error in inputs")

