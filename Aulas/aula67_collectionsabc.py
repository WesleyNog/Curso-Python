class MyList:
    def __init__(self):
        self._data = {}
        self._index = 0

    def append(self, value):
        self._data[self._index] = value
        self._index += 1

if __name__ == '__main__':
    lista = MyList()
    lista.append('Wsley')
    lista.append('Helloa')
    print(lista._data)