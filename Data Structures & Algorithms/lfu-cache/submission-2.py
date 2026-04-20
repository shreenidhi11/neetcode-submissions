class ListNode:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:

    def __init__(self):
        # Left -><- Right
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        # to store the capacity of the cache
        self.map = {}

    def length(self):
        return len(self.map)

    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        # val will point to the node directly
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node

    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            next, prev = node.next, node.prev
            next.prev = prev
            prev.next = next
            self.map.pop(val, None)
    
    def popLeft(self):
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res
    
    # def update(self, val):
    #     self.pop(val)
    #     self.pushRight(val)


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfucnt = 0
        self.valMap = {} # Map the key to the value, this is where we will immediately cehck for the key
        self.countMap = defaultdict(int) #Map the key to count
        # Map count of key -> linkedlist
        self.listMap = defaultdict(LinkedList)

    def counter(self, key):
        # storing the previous count to remove from the old location
        cnt = self.countMap[key]
        self.countMap[key] += 1
        # count of the key has changed so now you need to move this key to another list
        self.listMap[cnt].pop(key) #remove from old
        self.listMap[cnt + 1].pushRight(key) # add to new

        if cnt == self.lfucnt and self.listMap[cnt].length() == 0:
            self.lfucnt += 1

    def get(self, key: int) -> int:
        # if the key is not in the valMap return -1
        if key not in self.valMap:
            return -1
        # else increase the counter and return the key value
        self.counter(key)
        return self.valMap[key]
        

    def put(self, key: int, value: int) -> None:
        # handling the edge case
        if self.cap == 0:
            return
        
        # if the new key to be added is not in the valMap and at the same time the valMap has reached capacity
        if key not in self.valMap and len(self.valMap) == self.cap:
            # you need to pop the first element from the left of the listMap because the list map stores the count and then linked list
            res = self.listMap[self.lfucnt].popLeft()
            # remove this resultant node from valMap
            self.valMap.pop(res)
            # remove this resultant node from countMap
            self.countMap.pop(res)


        self.valMap[key] = value
        self.counter(key)
        # this is to maintain the current Least frequenct count so that we know where to remove the item from
        self.lfucnt = min(self.lfucnt, self.countMap[key])
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)