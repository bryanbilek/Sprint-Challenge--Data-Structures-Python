class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

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
        # store previous for current node as None since it starts out at the front
        prev = None
        # while there is a head, run the loop
        while self.head is not None:
            # store the next node
            next_node = self.head.next_node
            # set the current node's next to previous which reverses the pointer
            self.head.next_node = prev
            # slide the previous & current node pointers over toward the new head
            prev = self.head
            self.head = next_node
        # where prev = self.head is moving a pointer, by calling self.head
        # it is formally setting the prev as the new head of the list
        self.head = prev
