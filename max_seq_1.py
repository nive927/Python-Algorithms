import timeit

code_to_test = '''
import random
def maxSubSeq(seq, N):
	MaxSum = 0 
	for i in range(0, N):
		for j in range(i, N):
			ThisSum = 0 
			for k in range(i, j+1):
				ThisSum += seq[k]

			if ThisSum > MaxSum:
				MaxSum = ThisSum

	return MaxSum 

Start = -100
Stop = 100
N = 115

arr = random.sample(range(Start, Stop), N)
'''

'''
timeit runs the code segment multiple times(passed) to obtain the execution time.
I have specified this as number=100.
So, it executes 100 times and after that an average is taken.
'''
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print("The execution time is:", elapsed_time)

