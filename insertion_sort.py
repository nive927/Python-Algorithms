#1
def linear_locate(target, a_sorted):
    if len(a_sorted) == 0 or target <= a_sorted[0]:
        return 0
    
    return linear_locate(target, a_sorted[1:]) + 1
    
print(linear_locate(25, []))

#2
def linear_locate(target, a_sorted, accumulator=0):
    if len(a_sorted) == 0 or target <= a_sorted[0]:
        return accumulator
    
    return linear_locate(target, a_sorted[1:], accumulator+1)
    
print(linear_locate(25, []))

#3

def linear_locate(target, a_sorted):
    index=0
    for i in range(len(a_sorted)):
        if a_sorted[i] < target:
            index = i+1
        
    return index
        
print(linear_locate(25, []))

#4

def linear_search(target, a_sorted):
    for i in range(len(a_sorted)):
        if a_sorted[i] == target:
            return i
    return -1
        
print(linear_search(2, [5, 10, 20, 35, 50]))

#5

def ordered_insert(u, v):
    if len(v) == 0 or u <= v[0]:
        return [u] + v
    
    return v[0:1] + ordered_insert(u, v[1:])
    
a = [5, 10, 20, 35, 50]
print(ordered_insert(15, a))
print(a)

#6

def ordered_insert(u, v):
    for i in range(len(v)):
        if u <= v[i]:
            return v[:i] + [u] + v[i:]
    
a = [5, 10, 20, 35, 50]
print(ordered_insert(2, a))
print(a)

#7

