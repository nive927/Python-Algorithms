import timeit

code_to_test = '''
import random

def maxSubSeq(seq, N):
	MaxSum = ThisSum = 0 
	for j in range(0, N):
		ThisSum += seq[j] 
		
		if ThisSum > MaxSum:
			MaxSum = ThisSum
		elif ThisSum < 0:
			ThisSum = 0

	return MaxSum 

Start = -100
Stop = 100
N = 200

arr = random.sample(range(Start, Stop), N)
'''
    
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print("The execution time is:", elapsed_time)

'''estimated_time = N**3
print("The estimated time is:", estimated_time)

print("Ratio:", elapsed_time/estimated_time)'''
