
#26 54 17 77 93 31 44 55 20

def print_array(a, low, high):
    print(a[low:high+1])
    
def read_array():
    s = input("Enter a list of integers: ")
    a = list(map(int, s.split()))

    return a, len(a)

def minimum(a, low, high):
    minn = a[low]
    for i in range(low, high+1):
        if(minn > a[i]):
            minn = a[i]
                        
    return a.index(minn)

def selsort():
    a = []
    new = []
    a, n = read_array()
    print("Old: ",a)
    
    for i in range(0, n-1):
        index = minimum(a, i+1, n-1)
        if a[index] < a[i]:
            a[i], a[index] = a[index], a[i]
        
    print("Sorted: ",a)

    
selsort()