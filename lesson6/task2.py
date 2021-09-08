class Road:
    _length = None
    _width = None
    __weight_of_concrete = 25
    __thick_of_concrete = 5/ 1000
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def mass(self):
        return self._length * self._width * self.__weight_of_concrete * self.__thick_of_concrete

road= Road(5000, 20)
print(road.mass())
