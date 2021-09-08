class Workers:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {wage: "wage", bonus: "bonus"}

class Position(Workers):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]
worker = Position('Luka', 'Lukovich', 'bookkeeper', 1000, 100)
print(worker.name)
print(worker.surname)
print(worker.position)
print(worker._income)
print(worker.get_full_name())
print(worker.get_total_income())