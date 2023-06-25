class Stack_implimentation:
  
    def __init__(self):
        self.stack_list= []
  
    def push(self, element):
        self.stack_list.append(element)
  
    def pop(self):
        return self.stack_list.pop()
  
    def isEmpty(self):
        if len(self.stack_list) == 0:
            return True
        else:
            return False
    def peek(self):
        return self.stack_list[-1]
