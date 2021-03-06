class Tower_Stack:
    '''Represents a tower'''
    def __init__(self, name, num_disks = 0):
        self.name = name
        self.disks = []
        for i in range(num_disks, 0, -1):
            self.push(str(i))
    def __str__(self): 
        disks = ''.join('{:<2}'.format(d) for d in self.disks)
        return '{}[ {}]'.format(self.name, disks)
    def push(self, disk):
        self.disks.append(disk)
    def pop(self):
        return self.disks.pop()

move = 0

def hanoi_tower(n, source, helper, target):
    global move
    if n < 0:
        raise ValueError('The amount of discs has to be positive')
    if n >= 1:
        hanoi_tower(n - 1, source, target, helper)
        move += 1
        print('Move disk - {} from {} to {} (count of moves: {}).'.format(str(n), source.name, target.name, move))
        target.push(source.pop())
        show_hanoi(source, helper, target)
        hanoi_tower(n - 1, helper, source, target)

def show_hanoi(A, B, C):
     for t in [A, B, C]: 
            print(t)

def main():
    number = 3
    if type(number) != int:
        raise TypeError('The amount of discs has to be an integer')
    a = Tower_Stack("Source-A ", number)
    b = Tower_Stack("Helper-B ")
    c = Tower_Stack("Target-C ")
    show_hanoi(a, b, c)
    hanoi_tower(number, a, b, c)

if __name__ == '__main__':
    main()