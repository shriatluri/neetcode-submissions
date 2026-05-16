class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head



    def isEmpty(self) -> bool:
        return self.head.next == self.tail
            
        

    def append(self, value: int) -> None:
        new = Node(value)
        last_node = self.tail.prev
        
        last_node.next = new
        new.prev = last_node
        new.next = self.tail
        self.tail.prev = new
        

    def appendleft(self, value: int) -> None:
        new = Node(value)
        first = self.head.next

        
        self.head.next = new
        new.prev = self.head
        new.next = first
        first.prev = new
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        target = self.tail.prev
        value = target.value
        previous = target.prev
        previous.next = self.tail
        self.tail.prev = previous



        return value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        target = self.head.next
        value = target.value
        nexter = target.next

        self.head.next = nexter
        nexter.prev = self.head


        return value
        
