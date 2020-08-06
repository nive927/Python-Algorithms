
from heapq import heappush, heappop, heapify 
 
class MinHeap: 
	
	def __init__(self): 
		self.heap = []

	def buildHeap(self, dic):
		self.heap =  [[wt, [sym, ""]] for sym, wt in dic.items()]
		heapify(self.heap)		
	 
	def insert(self, k): 
		heappush(self.heap, k) 
			
	def deleteMin(self): 
		return heappop(self.heap)

	def parent(self, i): 
        	return (i-1)/2

	def isLeaf(self, i):
		return (2*i+1) > len(self.heap)

	def decreaseKey(self, i, new_val): 
		self.heap[i] = new_val 
		while(i != 0 and self.heap[self.parent(i)] > self.heap[i]): 

			self.heap[i] , self.heap[self.parent(i)] = (self.heap[self.parent(i)], self.heap[i])

	def increaseKey(self, i, new_val): 
		self.heap[i] = new_val
		heapify(self.heap, i)

	def length(self):
		return len(self.heap)
		 
	def display(self):
		print(self.heap)

def huffman(heapObj):

    while heapObj.length() > 1:
        
        lo = heapObj.deleteMin()
        hi = heapObj.deleteMin()

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        heapObj.insert([lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heapObj.deleteMin()[1:], key=lambda p: (len(p[-1]), p))

def printHuffCodes(huff, symProb):
	print("Symbol Prob  Huffman Code")
	for p in huff:
		print("%s\t%s\t%s" % (p[0], symProb[p[0]], p[1]))

# Driver program 

heapObj = MinHeap()

symProb = {'a':0.24, 'b':0.16, 'c':0.11, 'd':0.09, 'e':0.40}

heapObj.buildHeap(symProb)

huff = huffman(heapObj)

printHuffCodes(huff, symProb)





