from abc import ABC, abstractmethod

class Items:
    def __init__(self, name, value):
        self.name = name
        self.value = value

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

class DictBox(Box):
    def __init__(self):
        self.dict = {}
    
    def add(self, key, value):
        self.dict.update({key: value})

    def empty(self):
        tempArr = self.dict.items()
        self.dict = {}
        return tempArr

    def count(self):
        return len(self.dict)

box = ListBox()
box.add(1)
print(box.arr)
before_empty = box.empty()
print('list before empty', before_empty)
print(box.arr)
box.add(1)
box.add(2)
box.add(3)
count = box.count()
print(box.arr, 'count:', count)

dict_box = DictBox()
dict_box.add('test', 'value')
print(dict_box.dict)
t = dict_box.empty()
print(t)
dict_box.add('a', 1)
dict_box.add('b', 2)
dict_box.add('c', 3)
count = dict_box.count()
print(dict_box.dict, 'count:', count)




