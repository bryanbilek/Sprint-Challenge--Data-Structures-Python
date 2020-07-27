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
            # check if the index equals the capacity
            if self.index == self.capacity:
                # the index is set to 0
                self.index = 0
            # append item into storage at the index of 0
            self.storage[self.index] = item
            # as items gets appended, increment the index to 1
            self.index += 1
        # if storage isn't at capacity, just add the item   
        else:
            self.storage.append(item)

    def get(self):
        # to get the list, return the array storing the values
        return self.storage