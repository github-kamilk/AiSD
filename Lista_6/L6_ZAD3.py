class BinHeap:
    def __init__(self, max_size):
        self.heap_list = [0]
        self.current_size = 0
        self.max_size = max_size

    def percUp(self,index):
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                tmp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = tmp
            index = index // 2      
        
    def insert(self,value):
        if self.current_size == self.max_size:
            if value > self.findMin():
                self.heap_list.append(value)
                self.delMin()
                self.current_size += 1
            else:
                raise ValueError("The value is too small to put on the Binary Heap")
        else: 
            self.heap_list.append(value)
            self.current_size += 1
            self.percUp(self.current_size)        
        
    def findMin(self):
        return self.heap_list[1]

    def percDown(self,index):
        while (index * 2) <= self.current_size:
            mc = self.minChild(index)
            if self.heap_list[index] > self.heap_list[mc]:
                tmp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            index = mc

    def minChild(self,index):
        if index * 2 + 1 > self.current_size:
            return index * 2
        else:
            if self.heap_list[index*2] < self.heap_list[index*2+1]:
                return index * 2
            else:
                return index * 2 + 1    
            
    def delMin(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.percDown(1)
        return retval           
    
    def buildHeap(self,alist):
        index = len(alist) // 2
        try:
            if len(alist) > self.max_size:
                raise IndexError
            else:
                self.current_size = len(alist)
                self.heap_list = [0] + alist[:]
                while (index > 0):
                    self.percDown(index)
                    index = index - 1    
        except IndexError:
            return("It is impossible to have more than " + str(self.max_size) + (" elements"))
            
    def size(self):
        return self.current_size
     
    def isEmpty(self):
        return self.current_size == 0
    
    def __str__(self):
        txt = "{}".format(self.heap_list[1:])
        return txt