class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

class UnorderedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:  # jeśli usuwamy pierwszy element
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __str__(self):
        current = self.head
        li = []
        while current != None:
            li.append(current.get_data())
            current = current.get_next()
        s = ("Elements in the list are [" + ', '.join(['{}'] * len(li)) + "]")
        return s.format(*li)

    def append(self, item):
        temp = Node(item)
        if self.is_empty():
            self.head = temp
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(temp)

    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.get_data() == item:
                return index
            else:
                current = current.get_next()
                index += 1
        return None

    def insert(self, pos, item):
        current = self.head
        previous = None
        temp = Node(item)
        found = False
        index = 0
        if pos != 0:
            while current != None and not found:
                if index == pos:
                    previous.set_next(temp)
                    temp.set_next(current)
                    found = True
                else:
                    previous = current
                    current = current.get_next()
                    if current == None and index < pos:
                        raise IndexError
                index += 1
        else:
            temp.set_next(self.head)
            self.head = temp

    def pop(self, pos=-1):
        current = self.head
        previous = None
        size = self.size()
        if size == 0:
            raise IndexError
        elif size == pos+1:
            pos = -1
        elif size == 1 and (pos == 1 or pos == -1):
            self.head = None
            return current.get_data()
        else:
            pass

        if pos == -1:
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            previous.set_next(None)
            return current.get_data()
        elif pos == 0:
            temp = current.get_data()
            self.head = current.get_next()
            return temp
        else:
            index = 0
            while current != None:
                if index != pos:
                    previous = current
                    current = current.get_next()
                    if current == None:
                        raise IndexError
                else:
                    current = current.get_next()
                    previous.set_next(current)
                    return current.get_data()
                index += 1
                
    def peek(self):
        current = self.head
        previous = None

        if self.is_empty():
            raise IndexError("Object is empty")

        while current != None:
            previous = current
            current = current.get_next()
        return previous.get_data()

class StackUsingUL(object):
  def __init__(self):
    self.items = UnorderedList()

  def __str__(self):
        return self.items.__str__()

  def is_empty(self):
    """
    Metoda sprawdzajacą, czy stos jest pusty.
    Nie pobiera argumentów.
    Zwraca True lub False.
    """
    return self.items.is_empty()
  
  def push(self, item):
    """
    Metoda umieszcza nowy element na stosie.
    Pobiera element, który ma zostać umieszczony.
    Niczego nie zwraca.
    """
    self.items.append(item)

  def pop(self):
    """
    Metoda ściąga element ze stosu.
    Nie przyjmuje żadnych argumentów.
    Zwraca ściągnięty element.
    Jeśli stos jest pusty, rzuca wyjątkiem IndexError.
    """
    if self.is_empty():
      raise IndexError('The stack is empty')
    else:
      return self.items.pop()

  def peek(self):
    """
    Metoda podaje wartość elementu na wierzchu stosu
    nie ściągajac go.
    Nie pobiera argumentów.
    Zwraca wierzchni element stosu.
    Jeśli stos jest pusty, rzuca wyjątkiem IndexError.
    """
    if self.is_empty():
      raise IndexError("The stack is empty")
    else:
      return self.items.peek()

  def size(self):
    """
    Metoda zwraca liczę elementów na stosie.
    Nie pobiera argumentów.
    Zwraca liczbę elementów na stosie.
    """
    return self.items.size()