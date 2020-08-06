import random

def countOutOfOrderPairs(arr, N):
	count = 0

	for i in range(0, N):
		for j in range(i+1, N):
			if arr[i] > arr[j]:
				count += 1
	return count

Start = 1
Stop = 11
N = 5

arr = random.sample(range(Start, Stop), N)
#arr = [5, 4, 3, 2, 1]

print(arr)
print("Unordered Pairs Count: ", countOutOfOrderPairs(arr, N))

'''
ALGORITHM ANALYSIS:

The outer loop executes N times - O(N).
The inner loop executes N-i-1 times - O(N).
So, by Rule Of Products, the time complexity of the brute force approach is O(N^2).

Using polynomials, Big-Theta(N^2)
'''
