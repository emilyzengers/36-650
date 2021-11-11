class Queue:
    inner_list = []
    counter = 0
    
    def enqueue(self, value):
        self.inner_list.insert(self.counter, value)
        self.counter = self.counter + 1 
        # print(self.inner_list)
        
    def dequeue(self):
        value = self.inner_list.pop(0)
        self.counter = self.counter - 1
        return value
    
    def delete(self, input):
        for i in range(len(self.inner_list)):
            x = self.dequeue()
            if x != input:
                self.enqueue(x)
        # return self.inner_list