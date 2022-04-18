from abc import ABC, abstractmethod
import math

class Box(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def empty(self):
        pass
    @abstractmethod
    def count(self):
        pass

class Items:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class ListBox(Box):
    def __init__(self):
        self.arr = []
    
    def add(self, *item):
        self.arr.append(item)

    def empty(self):
        tempArr = self.arr
        self.arr = []
        return tempArr

    def count(self):
        return len(self.arr)
    
    def display(self):
        print(self.arr)

class DictBox(Box):
    def __init__(self):
        self.dict = {}
    
    def add(self, item):
        self.dict.update({item: item})

    def empty(self):
        tempArr = self.dict.values()
        self.dict = {}
        return tempArr

    def count(self):
        return len(self.dict)

def repack_boxes(*boxes):
    it = 0
    counter = 0
    for i in boxes:
        print ('Box {}:'.format(it+1), i.count())
        it+=1
        counter += i.count()
        i.empty()
    avg = math.floor(counter/it)
    it = 0
    print ('after packing evenly')
    for i in boxes:
        for j in range(avg):
            i.add(Items(str(j),j))
        print ('Box {}:'.format(it+1), i.count())
        it+=1
    remaining = counter - (avg*3)

first_box = ListBox()
second_box = ListBox()
third_box = DictBox()

for i in range(20):
    first_box.add(Items(str(i), i))
for i in range(9):
    second_box.add(Items(str(i), i))
for i in range(5):
    third_box.add(Items(str(i), i))

repack_boxes(first_box, second_box, third_box)