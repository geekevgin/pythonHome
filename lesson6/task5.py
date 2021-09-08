class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return "Start drawing"

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return "You have taken a pen"

class Pencill(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return "You have taken a pencil"

class Hadle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return "You have taken a hadle"

pen = Pen('Pen')
pencill = Pencill('Pencill')
handle = Hadle('Handle')

print(pen.draw())
print(pencill.draw())
print(handle.draw())