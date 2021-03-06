class LinkedList:
    def __init__(self):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is not None:
            if node.get_next() == None:
                self.head = node
                self.head.next_node = prev
                return
            self.reverse_list(node.get_next(), node)
            node.next_node = prev
