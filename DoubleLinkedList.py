from Node import Node
class DoubledLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            new_node.prev = self.tail
            new_node.next = prev      
        self.head = new_node

    def append_tail(self, data):
        node = Node(data)
        if self.tail is None:  # lista vacía
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) + " -> None"
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -- ")
            current = current.next
        print("None")

    def _node_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("índice fuera de rango")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur  
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def pop_first(self):
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        return value
    
    def is_empty(self):
        if not self.head:
            return True
        return False
    
    def pop(self):  # eliminar cola
        if self.is_empty():
            raise IndexError("lista vacía")
        if self._size == 1:
            return self.pop_first()
        prev = self._node_at(self._size - 2)
        data = prev.next.data
        prev.next = None
        self.tail = prev
        self._size -= 1
        return data
    
    def find(self, target):
        current = self.head
        index = 0
        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1

    def set(self, index, data):
        self._node_at(index).data = data
    
    def insert(self, index, data):
        if index < 0 or index > self._size:
            raise IndexError("índice fuera de rango")
        if index == 0:
            return self.prepend(data)
        if index == self._size:
            return self.append(data)
        prev = self._node_at(index - 1)
        node = Node(data, prev.next)
        prev.next = node
        self._size += 1

    def sort_asc(self):
            prev_before = None
            current = self.head.next if self.head else None
            before = self.head
            while before and before.next is not None:
                while current is not None:
                    t_before = before
                    t_current = current
                    if before.data > current.data:
                        next_before = before.next
                        before.next = current.next
                        if next_before == current: # si el siguiente de b == c
                            current.next = before
                        else:
                            current.next = next_before
                            prev_current.next = t_before
                        if prev_before is not None: # si tiene anterior b
                            prev_before.next = current
                        else:
                            self.head = current
                        current = t_before
                        before = t_current
                        print(self)
                    prev_current = current
                    current = current.next
                prev_before = before
                before = before.next
                current = before.next

sll = DoubledLinkedList()
sll.append_tail(5)
sll.append_tail(3)
sll.append_tail(2)
sll.append_tail(1)
sll.append_tail(5)

sll.sort_asc()

#print(sll)