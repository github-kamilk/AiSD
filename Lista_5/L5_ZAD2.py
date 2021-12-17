class Tower_Stack:
    '''Represents a tower'''
    def __init__(self, name, n_disks = 0):
        self.name = name
        self.disks = []
        for i in range(n_disks, 0, -1):
            self.push(str(i))
    def __str__(self): 
        disks = ''.join('{:<2}'.format(d) for d in self.disks)
        return '{}[ {}]'.format(self.name, disks)
    def is_empty(self):
        return self.disks == []
    def push(self, disk):
        self.disks.append(disk)
    def pop(self):
        return self.disks.pop()
    def peek(self):
        return self.disks[len(self.disks) - 1]
    def size(self):
        return len(self.items)

move = 0

def hanoi_stack(n, source, helper, target):
    global move
    if not isinstance(n, int):
        raise TypeError('The amount of dics has to be an integer')
    if n < 0:
        raise ValueError('The amount of discs has to be positive')
    if n >= 1:
        hanoi_stack(n - 1, source, target, helper)
        move += 1
        print('Move disk-{} from {} to {} (count of moves:{}).'.format(str(n), source.name, target.name, move))
        target.push(source.pop())
        print_hanoi(source, helper, target)
        hanoi_stack(n - 1, helper, source, target)

def print_hanoi(A, B, C):
     for t in [A, B, C]: 
            print(t)

if __name__ == '__main__':
    number = 5
    a = Tower_Stack("Source-A", number)
    b = Tower_Stack("Helper-B")
    c = Tower_Stack("Target-C")
    print_hanoi(a, b, c)
    hanoi_stack(number, a, b, c)