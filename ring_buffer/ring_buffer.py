class RingBuffer:
    def __init__(self, capacity):
        # capacity to check if we need to overwrite the oldest value when appending
        self.capacity = capacity
        # storage to hold the items
        self.storage = []
        # a specific position tracker in the list for items appended beginning at 0
        self.index = 0

    def append(self, item):
        # check if the items in storage are less than capacity
        if len(self.storage) == self.capacity:
            pass

    def get(self):
        # to get the list, return the array storing the values
        return self.storage