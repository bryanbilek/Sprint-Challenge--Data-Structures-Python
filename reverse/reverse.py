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

    # def reverse_list(self, node, prev):
    #     # store previous for current node as None since it starts out at the front
    #     prev = None
    #     # while there is a head, run the loop
    #     while self.head is not None:
    #         # store the next node
    #         next_node = self.head.next_node
    #         # set the current node's next to previous which reverses the pointer
    #         self.head.next_node = prev
    #         # slide the previous & current node pointers over toward the new head
    #         prev = self.head
    #         self.head = next_node
    #     # where prev = self.head is moving a pointer, by calling self.head
    #     # it is formally setting the prev as the new head of the list
    #     self.head = prev

    ## come up with a recursive solution for reverse_list
    def reverse_list(self, node, prev):
        # if node is None, means there is an empty list
        if node is None:
            return None
        # if next node is None, we put the head on the current node
        # and point the next node to the prev
        if node.next_node is None:
            self.head = node
            node.next_node = prev
            return
        # now we swap the pointers as the end of the orignal list is the new
        # head & call recursion repeating the process til list is reversed
        current = node.next_node
        node.next_node = prev
        self.reverse_list(current, node)
        
    
