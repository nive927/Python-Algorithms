def matchingNutsBolts(nuts, bolts, low, high):
    
    if low < high:
        pivot = partition(nuts, low, high, bolts[high])
        partition(bolts, low, high, nuts[pivot])   
        
        matchingNutsBolts(nuts, bolts, low, pivot - 1)  
        matchingNutsBolts(nuts, bolts, pivot + 1, high)
        
def partition(lst, start, end, pivot):
    less, pivotList, more = [], [], []
    
    for e in lst:
    
        if e < pivot:
            less.append(e)
        
        elif e > pivot:
            more.append(e)
            
        else:
            pivotList.append(e)
            
    i = 0
    for e in less:
        lst[i] = e
        i += 1
        
    for e in pivotList:
        lst[i] = e
        i += 1
                    
    for e in more:
        lst[i] = e
        i += 1
                        
    return lst.index(pivot)
#Driver 

nuts = ['!', '@', '#', '$', '%', '^']
bolts = ['^', '%', '$', '#', '@', '!']

print("Nuts: ", nuts)
print("Bolts: ", bolts)
    
matchingNutsBolts(nuts, bolts, 0, len(nuts)-1)

print("After Matching:")
print(nuts)
print(bolts)
