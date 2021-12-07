#task 1
class QueueBaB(object):
  """
  Klasa implementująca kolejkę za pomocą pythonowej listy tak,
  że początek kolejki jest przechowywany na początku listy.
  """
  
  def __init__(self):
    self.list_of_items = []
    
  def enqueue(self, item):
    """
    Metoda służąca do dodawania obiektu do kolejki.
    Pobiera jako argument obiekt który ma być dodany.
    Niczego nie zwraca.
    """
    self.list_of_items.append(item)

  def dequeue(self):
    """
    Metoda służąca do ściągania obiektu do kolejki.
    Nie pobiera argumentów.
    Zwraca ściągnięty obiekt.
    """
    if self.is_empty():
      raise IndexError("The queue is empty")
    else:
      return self.list_of_items.pop(0)
  
  def is_empty(self):
    """
    Metoda służąca do sprawdzania, czy kolejka jest pusta.
    Nie pobiera argumentów.
    Zwraca True jeśli kolejka jest pusta lub False gdy nie jest.
    """
    return self.list_of_items == []
    
  def size(self):
    """
    Metoda służąca do określania wielkości kolejki.
    Nie pobiera argumentów.
    Zwraca liczbę obiektów w kolejce.
    """
    return len(self.list_of_items)
    
  
class QueueBaE(object):
  """
  Klasa implementująca kolejkę za pomocą pythonowej listy tak,
  że początek kolejki jest przechowywany na końcu listy.
  """
  
  def __init__(self):
    self.list_of_items = []
    
  def enqueue(self, item):
    """
    Metoda służąca do dodawania obiektu do kolejki.
    Pobiera jako argument obiekt który ma być dodany.
    Niczego nie zwraca.
    """
    self.list_of_items.insert(0, item)
    
  def dequeue(self):
    """
    Metoda służąca do ściągania obiektu do kolejki.
    Nie pobiera argumentów.
    Zwraca ściągnięty obiekt.
    """
    if self.is_empty():
      raise IndexError("The queue is empty")
    else:
      return self.list_of_items.pop()
  
  def is_empty(self):
    """
    Metoda służąca do sprawdzania, czy kolejka jest pusta.
    Nie pobiera argumentów.
    Zwraca True jeśli kolejka jest pusta lub False gdy nie jest.
    """
    return self.list_of_items == []
    
  def size(self):
    """
    Metoda służąca do określania wielkości kolejki.
    Nie pobiera argumentów.
    Zwraca liczbę obiektów w kolejce.
    """
    return len(self.list_of_items)

#task 2
import time    
import matplotlib.pyplot as plt     
import numpy as np

q_BaB = QueueBaB()
q_BaE = QueueBaE()

#enqueue 
def enqueue_BaB(n):
    start_BaB_en = time.time()
    for k in range(100):
        for i in range(n):
            q_BaB.enqueue(i)

    end_BaB_en = time.time()
    total_BaB_en = end_BaB_en - start_BaB_en
    total_BaB_en = total_BaB_en/100
    return total_BaB_en

def enqueue_BaE(n):
    start_BaE_en = time.time()
    for k in range(100):
        for i in range(n):
            q_BaE.enqueue(i)

    end_BaE_en = time.time()
    total_BaE_en = end_BaE_en - start_BaE_en
    total_BaE_en = total_BaE_en/100
    return total_BaE_en
    
#dequeue
def dequeue_BaB(n):
    start_BaB_deq = time.time()
    for k in range(100):
        for i in range(n):
            q_BaB.dequeue()

    end_BaB_deq = time.time()
    total_BaB_deq = end_BaB_deq - start_BaB_deq
    total_BaB_deq = total_BaB_deq/100
    return total_BaB_deq

def dequeue_BaE(n):
    start_BaE_deq = time.time()
    for k in range(100):
        for i in range(n):
            q_BaE.dequeue()

    end_BaE_deq = time.time()
    total_BaE_deq = end_BaE_deq - start_BaE_deq
    total_BaE_deq = total_BaE_deq/100
    return total_BaE_deq

def check_compability(n):
    """A function to compare the capability of both implementation"""

    print("Size of queue: " + str(n))
    print("Time of enqueue operation for QueueBaB: {0:.6f}s".format(enqueue_BaB(n)))
    print("Time of enqueue operation for QueueBaE: {0:.6f}s".format(enqueue_BaE(n)))
    print("Time of dequeue operation for QueueBaB: {0:.6f}s".format(dequeue_BaB(n)))
    print("Time of dequeue operation for QueueBaE: {0:.6f}s".format(dequeue_BaE(n)))

    x = range(100,n+100,100)
    y1= []
    y2= [] 
    y3 = []
    y4 = []
    for i in x:
        y_BaB_en = enqueue_BaB(i)
        y1.append(y_BaB_en)
        y_BaE_en = enqueue_BaE(i)
        y2.append(y_BaE_en)
        y_BaB_deq = dequeue_BaB(i)
        y3.append(y_BaB_deq)
        y_BaE_deq = dequeue_BaE(i)
        y4.append(y_BaE_deq)
    
    plt.figure(1)
    plt.subplot(2, 1, 1)

    plt.scatter(x, y1)
    plt.grid()
    plt.ylim(0, 0.05)
    plt.title('Enqueue operation on queue BaB')
    plt.xlabel('Size of queue')
    plt.ylabel('Time')

    plt.subplot(2, 1, 2)
    plt.scatter(x, y2)
    plt.grid()
    plt.ylim(0, 0.05)
    plt.title('Enqueue operation on queue BaE')
    plt.xlabel('Size of queue')
    plt.ylabel('Time')

    plt.tight_layout()
    plt.show()

    plt.figure(2)
    plt.subplot(2, 1, 1)

    plt.scatter(x, y3)
    plt.grid()
    plt.ylim(0, 0.05)
    plt.title('Dequeue operation on queue BaB')
    plt.xlabel('Size of queue')
    plt.ylabel('Time')

    plt.subplot(2, 1, 2)
    plt.scatter(x, y4)
    plt.grid()
    plt.ylim(0, 0.05)
    plt.title('Dequeue operation on queue BaE')
    plt.xlabel('Size of queue')
    plt.ylabel('Time')

    plt.tight_layout()
    plt.show()
    
def main():
    check_compability(1000)

if __name__ == '__main__':
    main()