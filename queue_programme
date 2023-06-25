class Queue_implementation:
    def __init__(self) -> None:
        self.queue_list = []
    
    def peek(self):
        if self.isEmpty():
            return False
        return self.queue_list[-1]
    
    def enqueue(self, value):
        self.queue_list.append(value)

    def dequeue(self):
        if self.isEmpty():
            return False
        return self.queue_list.pop(1)
    
    def isEmpty(self):
        if len(self.queue_list == 0):
            return True
        else:
            return False
    
