class doublyLL:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev= None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mydict = {}
        self.left = doublyLL(0,0)
        self.right = doublyLL(0,0)
        self.left.next = self.right
        self.right.prev= self.left

#   Insert before the right pointer
    def add(self,Node): 
        # 3 -> right : 3 -> 4 - > right
        prev,nxt = self.right.prev, self.right
        prev.next = nxt.prev = Node
        Node.prev, Node.next = prev,nxt

    def remove(self,doublyLL):
        prev,nxt = doublyLL.prev, doublyLL.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.mydict:
            self.remove(self.mydict[key])
            self.add(self.mydict[key])
            return self.mydict[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mydict:
            self.remove(self.mydict[key])
        newNode = doublyLL(key,value)
        self.mydict[key] = newNode
        self.add(newNode)

        if len(self.mydict) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.mydict[lru.key]















            

        





        



        

