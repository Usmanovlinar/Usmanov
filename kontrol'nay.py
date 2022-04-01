class ListNode:
    def init(self, value):
        self.key = value
        self.next_node = None

class Queue:
    def init(self):
        self.length = 0
        self.head = None
        self.tail = None

    def append(self, key):
        self.length += 1
        if self.tail:
            self.tail.next_node = ListNode(key)
            self.tail = self.tail.next_node

        else:
            self.head = ListNode(key)
            self.tail = self.head

    def enqueue(self):
        if self.length == 0:
            return None
        if self.length == 1:
            value = self.head.key
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        value = self.head.key
        self.head = self.head.next_node
        self.length -= 1
        return value

class Rivet:
    def init(self, height, width, lengh, mass, color=None):
        self.height = height
        self.width = width
        self.lengh = lengh
        self.mass = mass
        self.color = color

    def repr(self):
        return f'Деталь 1: {self.height}, {self.width}, {self.lengh},{self.mass},{self.color}'


class Painting_area:
    def init(self):
        self.store = Queue()

    def add_detail(self, item):
        self.store.append(item)

    def get_details(self):
        file = open('list.txt', 'w')
        file.write(f'В цеху {self.store.length} деталей \n')

        i = 0
        while True:
            i += 1
            item = self.store.enqueue()
            if item is None:
                break
            file.write(f'Деталь {i}: {item.height}, {item.width}, {item.lengh},{item.mass},{item.color} \n ')

paint = Painting_area()
riv1 = Rivet(20, 43, 270, 230, "Brown")
riv2 = Rivet(10,10 ,10, 10, "Rainbow")

paint.add_detail(riv1)
paint.add_detail(riv2)

paint.get_details()