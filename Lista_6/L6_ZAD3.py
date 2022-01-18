class BinHeap:
    def __init__(self, max_size):
        self.heap_list = [0]
        self.current_size = 0
        self.max_size = max_size

    def perc_up(self,index):
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                tmp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = tmp
            index = index // 2      
        
    def insert(self,value):
        if not isinstance(value, int):
            raise TypeError('Value should be an integer')
        if self.current_size >= self.max_size: 
            if value > self.find_min():
                self.del_min()
                self.insert(value)
            else:
                pass
        else: 
            self.heap_list.append(value)
            self.current_size += 1
            self.perc_up(self.current_size)        
        
    def find_min(self):
        return self.heap_list[1]

    def perc_down(self,index):
        while (index * 2) <= self.current_size:
            mc = self.min_child(index)
            if self.heap_list[index] > self.heap_list[mc]:
                tmp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            index = mc

    def min_child(self,index):
        if index * 2 + 1 > self.current_size:
            return index * 2
        else:
            if self.heap_list[index*2] < self.heap_list[index*2+1]:
                return index * 2
            else:
                return index * 2 + 1    
            
    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval           
    
    def build_heap(self,alist):
        if not isinstance(alist, list):
            raise TypeError('Value should be a list')
        index = len(alist) // 2
        if len(alist) > self.max_size:
            for i in range(0, len(alist)):
                self.insert(alist[i])  
        else:
            self.current_size = len(alist)
            self.heap_list = [0] + alist[:]
            while (index > 0):
                self.perc_down(index)
                index = index - 1
        
    def size(self):
        return self.current_size
     
    def is_empty(self):
        return self.current_size == 0
    
    def __str__(self):
        txt = "{}".format(self.heap_list[1:])
        return txt