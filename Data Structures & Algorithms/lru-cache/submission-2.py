class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        #tail -> head
        self.tail.next = self.head
        self.head.prev = self.tail

    def add(self, Node):
        prev, next = self.head.prev, self.head
        Node.prev, Node.next = prev, next
        prev.next, next.prev = Node, Node


    def remove(self, Node):
        node_prev, node_next = Node.prev, Node.next
        node_prev.next = node_next
        node_next.prev = node_prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newnode = Node(key, value)
        self.cache[key] = newnode
        self.add(newnode)

        if len(self.cache) > self.capacity:
            remove_node = self.tail.next
            self.remove(remove_node)
            del self.cache[remove_node.key]




        
