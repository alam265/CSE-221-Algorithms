class Node:
    def __init__(self,elem,next):
        self.elem = elem 
        self.next = next 

class Singly_Linked_List:
    def __init__(self):
        self.head = None 
        
    def creation(self,arr):
        self.head = Node(arr[0],None)
        tail = self.head

        for i in range(1,len(arr)):
            newNode = Node(arr[i],None)
            tail.next = newNode
            tail = newNode 
        return self.head

def display(head):
    p = head 
    while p:
        print(p.elem,end=' ')
        p = p.next 
def SelectionSort(head):
    p = head 
    while p :
        q = p.next 
        minloc = p 
        while q:
            if q.elem < minloc.elem:
                minloc=q 
            q = q.next 
        p.elem , minloc.elem = minloc.elem ,p.elem 
        p = p.next 
    return head 




LL = Singly_Linked_List()
LL = LL.creation([1,6,3,9,2,0,12,67,43,2])

SorteLL = SelectionSort(LL)

display(SorteLL)