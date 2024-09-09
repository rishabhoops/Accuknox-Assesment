class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __iter__(self):
        return iter([{'length': self.length}, {'width': self.width}])

rectangle = Rectangle(10, 5)
for dimension in rectangle:
    print(dimension)
