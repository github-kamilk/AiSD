class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
        
    def percUp(self,index):
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                tmp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = tmp
            index = index // 2      
        
    def insert(self,k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
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
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.percDown(1)
        return retval           
    
    def buildHeap(self,alist):
        index = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while (index > 0):
            self.percDown(index)
            index = index - 1    
            
    def size(self):
        return self.current_size
    
    def isEmpty(self):
        return self.current_size == 0
    
    def __str__(self):
        txt = "{}".format(self.heap_list[1:])
        return txt

def sortHeap(data_list):
    sorted_heap = []
    heap = BinHeap()
    heap.buildHeap(data_list)
    n = len(data_list)
    for i in range(n):
        temp = heap.delMin()
        sorted_heap.append(temp)
    return sorted_heap


if __name__ == "__main__":
    new_list = sortHeap([5,9,3,7,2,5,10,1,4])
    print(new_list)