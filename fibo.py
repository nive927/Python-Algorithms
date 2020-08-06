#cd ../../mnt/d/work/nive/SSN\ College\ Of\ Engineering/all\ SEMESTERS/SEM4/UCS1403\ Design\ And\ Analysis\ Of\ Algorithms/Lab/S1

def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]
        
def max_mult(a, b):
    res = [[0 for x in range(len(a))] for y in range(len(b[0]))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k] * b[k][j]
    return res

def fib(n):
    
    if n == 0:
        return 0
    elif n < 3:
        return 1
    
    bin_str = toStr(n-1, 2)
    
    M = [[1, 1],[1, 0]]

    term = M
    
    if bin_str[-1] == '1':
        result = M
    else:
        result = [[1, 0], [0, 1]]
        
    for i in range(len(bin_str)-2, -1, -1):
        term = max_mult(term, term)
        if bin_str[i] == '1':
            result = max_mult(result, term)
            
    return result[0][0]
    
n = int(input("Which fibonacci term do you want?: "))
print("Ans:",fib(n))
#print("The",n,"th term is",fib(n),"!")