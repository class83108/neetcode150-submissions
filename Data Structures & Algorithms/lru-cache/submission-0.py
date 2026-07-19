class DoubleLinkListed:
    def __init__(self, key:int, value: int):
        self.key = key
        self.value = value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = DoubleLinkListed(-1, -1)
        self.tail = DoubleLinkListed(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.hashMap = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        node = self.hashMap[key]
        self.remove_node(node)
        self.add_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.remove_node(self.hashMap[key])
        
        node = DoubleLinkListed(key, value)
        
        self.hashMap[key] = node
        if len(self.hashMap) > self.capacity:
            del self.hashMap[self.head.next.key]
            self.remove_node(self.head.next)
        self.add_to_tail(node)

    
    def remove_node(self, node: DoubleLinkListed) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_tail(self, node: DoubleLinkListed) -> None:
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        prev_node.next = node
        self.tail.prev = node
    
    
        

        
