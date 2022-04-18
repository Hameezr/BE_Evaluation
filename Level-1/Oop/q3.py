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
    
    def add(self, item):
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
    
    def add(self, item):
        self.dict.update({item: item})

    def empty(self):
        tempArr = self.dict.values()
        self.dict = {}
        return tempArr

    def count(self):
        return len(self.dict)

def repack_boxes(): 
    
