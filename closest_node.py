class Node(object):

    __slots__ = ['_itemNode', '_nextNode']

    def __init__(self, itemNode=None, nextNode=None):
        self._itemNode = itemNode
        self._nextNode = nextNode

    def __str__(self):
        return str(self._itemNode)

    def setItem(self, itemNode=None):
        self._itemNode = itemNode

    def setNext(self, nextNode=None):
        self._nextNode = nextNode

    def getItem(self):
        return self._itemNode

    def getNext(self):
        return self._nextNode
    
class Point(object):

    __slots__ = ['_x', '_y']

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return "(" + str(self._x) + "," + str(self._y) + ")"

    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        return Point(self._x - other._x, self._y - other._y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def distance(self, other):
        x_diff = (self._x - other._x) ** 2
        y_diff = (self._y - other._y) ** 2
        return (x_diff + y_diff) ** 0.5

    def translate(self, x=0, y=0):
        self._x += x
        self._y += y
        
class Empty(Exception):
    pass


class LinkedQueue(object):

    __slots__ = ['_front', '_rear', '_size']

    def __init__(self):
        self._front = Node()
        self._rear = self._front
        self._size = 0

    def __str__(self):
        pos = self._front
        res = '<'
        while pos._nextNode is not None:
            res = res + str(pos._nextNode._itemNode) + ', '
            pos = pos._nextNode
        res = res + '>'
        return res

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._front._nextNode is None

    def front(self):
        if self._front._nextNode is None:
            raise Empty("Queue is empty!")
        return self._front._nextNode._itemNode

    def dequeue(self):
        if self._front._nextNode is None:
            raise Empty("Queue is empty!")
        item = self._front._nextNode._itemNode
        self._front = self._front._nextNode
        self._size -= 1
        return item

    def enqueue(self, item):
        self._rear._nextNode = Node(item, None)
        self._rear = self._rear._nextNode
        self._size += 1
        return
    
def merge(lst1, lst2):
        i = j = 0
        res = []
        
        while ( (i < len(lst1)) and (j < len(lst2))):
            if( lst1[i][2] < lst2[j][2]):
                res.append( lst1[i] )
                i += 1
            else:
                res.append( lst2[j] )
                j += 1
        if(i<len(lst1)):
            res.extend(lst1[i:])
        elif(j<len(lst2)):
            res.extend(lst2[j:])
        return res
    
def msort(lst):
    length = len(lst)
    if(length < 2):
        return lst[:]
    else:
        mid = length // 2
    return merge( msort(lst[:mid]), msort(lst[mid:]))

def qinsert(l,pt):
    lst=[]
    for i in range(len(l)):
        t=l.dequeue()
        temp=[]
        temp.append(t.get_x())
        temp.append(t.get_y())
        temp.append(t.distance(pt))
        lst.append(temp)
    lst=msort(lst)
    l.enqueue(pt)
    #print(lst)
    for i in lst:
        l.enqueue(Point(i[0],i[1]))
        
l = LinkedQueue()

n = int(input("Enter n : "))

for i in range(n):
    print("\nEnter Co-ordinate ", i+1)
    x = int(input("Enter x : "))
    y = int(input("Enter y : "))
    temp = Point(x,y)
    if(l.isEmpty()):
        l.enqueue(temp)
    else:
        qinsert(l,temp)
    print()
    print("LinkedQueue : ",l)
