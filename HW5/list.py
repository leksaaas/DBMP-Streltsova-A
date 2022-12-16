class Node:
    def __init__(self, value,
                 prev_pointer=None, next_pointer=None):
        self.set_value(value)
        self.set_prev(prev_pointer)
        self.set_next(next_pointer)

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_pointer

    def get_prev(self):
        return self._prev_pointer

    def set_value(self, value):
        self._value = value

    def set_prev(self, prev_pointer):
        self._prev_pointer = prev_pointer

    def set_next(self, next_pointer):
        self._next_pointer = next_pointer

    def __str__(self):
        return str(self.get_value())

class Itlist:
    def __init__(self, list):
        self._list = list
        self._index = -1
        self._length = len(list)

    def __next__(self):
        self._index += 1
        if self._index > self._length - 1:
            raise StopIteration
        return self._list[self._index]

class List:
    def __init__(self, collections = None):
        self._start_pointer = None
        self._finish_pointer = None
        self._length = 0
        if isinstance(collections, int):
            self.append(collections)
        elif isinstance(collections, list):
            for i in collections:
                self.append(i)

    def __len__(self):
        return self._length

    def append(self, value):
        if self._length == 0:
            self._start_pointer = Node(value)
            self._finish_pointer = self._start_pointer
            self._length = 1
        else:
            self._finish_pointer.set_next(Node(value,
                                               self._finish_pointer))
            self._finish_pointer = self._finish_pointer.get_next()
            self._length += 1

    def __getitem__(self, i):
        if i < 0 or i >= self._length:
            return False
        curr_pointer = self._start_pointer
        for j in range(i):
            curr_pointer = curr_pointer.get_next()
        return curr_pointer.get_value()

    def __str__(self):
        arr = []
        for i in range(self._length):
            arr.append(str(self[i]))
        return "[" + ", ".join(arr) + "]"

    def __add__(self, other):
        for i in range(len(other)):
            self.append(other[i])
        return self

    def __radd__(self, other):
        for i in range(len(self)):
            other.append(self[i])
        return other

    def __eq__(self, other):
        for i in range(len(self)):
            self[i] = other[i]
        return self

    def pop(self, i):
        l = List()
        result = self[i]
        for j in range(len(self)-1):
            if j < i:
                l.append(self[j])
            if j >= i:
                l.append(self[j+1])
        self = l
        return result
    def __iter__(self):
        return Itlist(self)
A=List()
for j in range(10):
    A.append(j)
for j in A:
    print(j)
B=[1,2]
A.__add__(B)
print(A)