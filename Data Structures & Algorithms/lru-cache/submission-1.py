class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def add(self, Node):
        prev, next = self.right.prev, self.right
        Node.next = next
        Node.prev = prev
        prev.next = self.right.prev = Node
    
    def remove(self, Node):
        prev, next = Node.prev, Node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            value = node.value
            self.remove(node)
            self.add(node)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newnode = Node(key, value)
        self.cache[key] = newnode
        self.add(newnode)

        if len(self.cache) > self.cap:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]

        
