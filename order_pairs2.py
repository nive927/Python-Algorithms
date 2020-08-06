import random

def mergeSort1(arr, n): 
	
	temp = [0]*n 
	return mergeSort2(arr, temp, 0, n-1) 


def mergeSort2(arr, temp, left, right): 

	inv_count = 0

	if left < right: 

		mid = (left + right)//2

		inv_count += mergeSort2(arr, temp, left, mid) 
		inv_count += mergeSort2(arr, temp, mid + 1, right) 
		inv_count += merge(arr, temp, left, mid, right) 

	return inv_count 

def merge(arr, temp_arr, left, mid, right): 
	
	i = left	 
	j = mid + 1 
	k = left	  
	inv_count = 0 

	while i <= mid and j <= right: 

		if arr[i] <= arr[j]: 
			temp_arr[k] = arr[i] 
			k += 1
			i += 1
		else: 
			temp_arr[k] = arr[j] 
			inv_count += (mid-i + 1) 
			k += 1
			j += 1

	while i <= mid: 
		temp_arr[k] = arr[i] 
		k += 1
		i += 1

	while j <= right: 
		temp_arr[k] = arr[j] 
		k += 1
		j += 1

	for loop_var in range(left, right + 1): 
		arr[loop_var] = temp_arr[loop_var] 
		
	return inv_count 

Start = 1
Stop = 11
N = 5

arr = random.sample(range(Start, Stop), N)
#arr = [5, 4, 3, 2, 1]

print(arr)

result = mergeSort1(arr, N) 

print("Unordered pairs count: ", result) 

'''
ALGORITHM ANALYSIS:

Method: Enhanced Merge Sort
Design Technique: Divide & Conquer
Asymptotic Notation Run-time Complexity: Big-Theta(NlogN)
This holds good for worst, average and best case.

T(N) = 2T(N/2) + Big-Theta(N)
The above recurrence can be solved by Master method. 
It falls under case II of Master Method:

CASE  I: T(N) = aT(N/b) + f(N) a >= 1 & b > 1
CASE II: When a = b,
	 if f(N) is sub-linear time then, T(N) is Big-Theta(N)
'''

