import time
import matplotlib.pyplot as plt
from L4_ZAD5 import UnorderedList

def compare_lists(n):
### CREATING LISTS ###
    start_create_own_list = time.time()

    own_list = UnorderedList()

    end_create_own_list = time.time()
    total_create_own_list = end_create_own_list - start_create_own_list
    
    start_create_py_list = time.time()

    python_list = []

    end_create_py_list = time.time()
    total_create_py_list = end_create_py_list - start_create_py_list

### APPENDING DATA ###
    time_append_own=[]
    time_append_py_list=[]
    x = range(100, n+100, 100)

    for i in x:
        start_append_own = time.time()
        for k in range(i):
            own_list.append(k)

        end_append_own = time.time()
        total_append_own = end_append_own - start_append_own
        time_append_own.append(total_append_own)

    for i in x:
        start_append_py = time.time()
        for k in range(i):
            python_list.append(k)

        end_append_py = time.time()
        total_append_py = end_append_py - start_append_py
        time_append_py_list.append(total_append_py)

### INSERT OPERATION ###
    time_insert_own=[]
    time_insert_py_list=[]

    for i in x:
        start_insert_own = time.time()
        for k in range(i):
            own_list.insert(k,10)

        end_insert_own = time.time()
        total_insert_own = end_insert_own - start_insert_own
        time_insert_own.append(total_insert_own)
    
    for i in x:
        start_insert_py = time.time()
        for k in range(i):
            python_list.insert(i,10)

        end_insert_py = time.time()
        total_insert_py = end_insert_py - start_insert_py
        time_insert_py_list.append(total_insert_py)

### INDEX METHOD ###
    start_own_index = time.time()

    own_list.index(n/2)

    end_own_index = time.time()
    total_own_index = end_own_index - start_own_index
        
    start_py_index = time.time()

    python_list.index(n/2)

    end_py_index = time.time()
    total_py_index = end_py_index - start_py_index
    
### SIZE METHOD ###
    start_own_size = time.time()

    own_list.size()

    end_own_size = time.time()
    total_own_size = end_own_size - start_own_size
        
    start_py_size = time.time()

    python_list.__sizeof__()

    end_py_size = time.time()
    total_py_size = end_py_size - start_py_size
    
    
### POP METHOD ###
    time_pop_own=[]
    time_pop_py_list=[]
    for i in x:
        start_pop_own = time.time()
        for k in range(i):
            own_list.pop()

        end_pop_own = time.time()
        total_pop_own = end_pop_own - start_pop_own 
        time_pop_own.append(total_pop_own)

    for i in x:
        start_pop_py = time.time()
        for k in range(i):
            python_list.pop()

        end_pop_py = time.time()
        total_pop_py = end_pop_py - start_pop_py
        time_pop_py_list.append(total_pop_py)
    

    print("Amount of elements: " + str(n))
    print("Time of creating own list: {0:02f}s".format(total_create_own_list))
    print("Time of creating Python list: {0:02f}s".format(total_create_py_list))
    print("----")
    print("Time of appending data for own list: {0:02f}s".format(total_append_own))
    print("Time of appending data for Python list: {0:02f}s".format(total_append_py))
    print("----")
    print("Time of insert operation  for own list: {0:02f}s".format(total_insert_own))
    print("Time of insert operation for Python list: {0:02f}s".format(total_insert_py))
    print("----")
    print("Search time for the own index method: {0:02f}s".format(total_own_index))
    print("Search time for the Python index method: {0:02f}s".format(total_py_index))
    print("----")
    print("Search time for the own size method: {0:02f}s".format(total_own_size))
    print("Search time for the Python size method: {0:02f}s".format(total_py_size))
    print("----")
    print("Time of erase of data from own list: {0:02f}s".format(total_pop_own))
    print("Time of erase of data from Python list: {0:02f}s".format(total_pop_py))

    
    plt.figure(1)
    plt.subplot(2, 1, 1)
    plt.scatter(x, time_append_own)
    plt.grid()
    plt.ylim(0, 2)
    plt.title('Appending operations for own list')
    plt.xlabel('Amount of elements')
    plt.ylabel('Time')

    plt.subplot(2, 1, 2)
    plt.scatter(x, time_append_py_list)
    plt.grid()
    plt.ylim(0, 2)
    plt.title('Appending operations for Python list')
    plt.xlabel('Amount of elements')
    plt.ylabel('Time')
    plt.tight_layout()
    plt.show()

    plt.figure(2)
    plt.subplot(2, 1, 1)
    plt.scatter(x, time_insert_own)
    plt.grid()
    plt.ylim(0, 0.2)
    plt.title('Insert operation for own list')
    plt.xlabel('Amount of elements')
    plt.ylabel('Time')

    plt.subplot(2, 1, 2)
    plt.scatter(x, time_insert_py_list)
    plt.grid()
    plt.ylim(0, 0.2)
    plt.title('Insert operation for Python list')
    plt.xlabel('Amount of elements')
    plt.ylabel('Time')
    plt.tight_layout()
    plt.show()

    plt.figure(3)
    plt.subplot(2, 1, 1)
    plt.scatter(x, time_pop_own)
    plt.grid()
    plt.title('Pop operations for own list')
    plt.xlabel('Amount of elements')
    plt.ylabel('Time')

    plt.subplot(2, 1, 2)
    plt.scatter(x, time_pop_py_list)
    plt.grid()
    plt.ylim(0, 0.1)
    plt.title('Pop operations for Python list')
    plt.xlabel('Amount of elements')
    plt.ylabel('Time')
    plt.tight_layout()
    plt.show()

def main():
    compare_lists(1000)

if __name__ == "__main__":
    main()