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
        if self.current_size == self.max_size:
            if value > self.find_min():
                self.heap_list.append(value)
                self.del_min()
                self.current_size += 1
            else:
                raise ValueError("The value is too small to put on the Binary Heap")
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
        index = len(alist) // 2
        try:
            if len(alist) > self.max_size:
                raise IndexError
            else:
                self.current_size = len(alist)
                self.heap_list = [0] + alist[:]
                while (index > 0):
                    self.perc_down(index)
                    index = index - 1    
        except IndexError:
            return("It is impossible to have more than " + str(self.max_size) + (" elements"))
            
    def size(self):
        return self.current_size
     
    def is_empty(self):
        return self.current_size == 0
    
    def __str__(self):
        txt = "{}".format(self.heap_list[1:])
        return txt