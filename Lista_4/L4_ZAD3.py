import random


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Kayak:
    def __init__(self):
        self.in_use = False
        self.down = False
        self.time_remaining = 0

    def set_time(self, time):
        self.time_remaining = time

    def set_position(self):
        self.down = False

    def set_in_use(self):
        self.in_use = True

    def if_down(self):
        return self.down

    def tick(self):
        if self.in_use == True:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.in_use = False
                self.down = True


class Client:
    def __init__(self, time):
        self.time_stamp = time
        self.ride_time = random.randrange(1800, 3601)

    def get_stamp(self):
        return self.time_stamp

    def get_ride_time(self):
        return self.ride_time

    def wait_time(self, current_time):
        return current_time - self.time_stamp


def new_client():
    return random.randint(1, 901) == 900


def simulation(number_of_kayaks, time):
    kayaks_up = Stack()
    kayaks_down = Stack()
    clients_queue = Queue()
    kayaks_on_river = []
    waiting_times = []

    for i in range(number_of_kayaks):
        kayaks_up.push(Kayak())

    for current_second in range(time):
        if new_client():
            client = Client(current_second)
            clients_queue.enqueue(client)

        if (not kayaks_up.is_empty()) and (not clients_queue.is_empty()):
            next_client = clients_queue.dequeue()
            next_kayak = kayaks_up.pop()
            next_kayak.set_time(next_client.get_ride_time())
            next_kayak.set_in_use()

            kayaks_on_river.append(next_kayak)
            waiting_times.append(next_client.wait_time(current_second))

        kayaks_on_river_copy = kayaks_on_river.copy()
        for kayak in kayaks_on_river_copy:
            kayak.tick()
            if kayak.if_down():
                kayaks_down.push(kayak)
                kayaks_on_river.remove(kayak)

        if kayaks_down.size() == number_of_kayaks:
            while not kayaks_down.is_empty():
                kayak_go_up = kayaks_down.pop()
                kayaks_up.push(kayak_go_up)
                kayak_go_up.set_position()

    for client in clients_queue.items:
        waiting_times.append(client.wait_time(time))

    average_wait = sum(waiting_times) / len(waiting_times)
    # print("Average Wait %6.2f min, %3d clients remaining."%(average_wait/60,clients_queue.size()))
    return round(average_wait / 60, 2)


if __name__ == "__main__":
    waiting_times = []
    for i in range(10):
        waiting_times.append(simulation(10, 28800))

    average_wait = sum(waiting_times) / len(waiting_times)
    print(average_wait)
