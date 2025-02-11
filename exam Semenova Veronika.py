#1
with open('test.txt') as file:
    text = file.read().strip()

def replace_char(text):

    x = 0
    res = []

    while x < len(text) - 1:
        ch1 = ord(text[x])
        ch2 = ord(text[x+1])
        sr_znach = (ch1 + ch2) / 2
        res.append(sr_znach)
        x += 2

    if len(text) % 2 != 0:
        res.append(ord(text[-1]))
    else:
        pass

    return sum(res)

res_hesh = replace_char(text)
print(res_hesh)

#2

def matrixtuple(matrix):
    return tuple(min(x) for x in matrix)

def vvod():
    matrix = []
    for i in range(3):
        ress = [int(x) for x in input(f"строка {i + 1}:").split()]
        if len(ress) != 3:
            raise ValueError
        matrix.append(ress)
    return matrix


def ttuple(matrix):
    el = set()
    for x in matrix:
        for i in x:
            el.add(i)
    return tuple(el)

def print_m(matrix):
    for x in matrix:
        print(x)

matrix = vvod()

ttuple(matrix)
res_tuple = matrixtuple(matrix)

result_ttuple = ttuple(matrix)
print(result_ttuple)
print_m(matrix)

#3
import random
from datetime import datetime

class Stage:
    def __init__(self, cost, start, end, desc):
        self.cost = cost
        self.start_date = self.validate_date(start)
        self.end_date = self.validate_date(end)
        self.description = desc
        self.status = "запланирован"

    def validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%d.%m.%Y")
            return date_str
        except ValueError:
            raise ValueError('неверный формат даты')

    def next(self):
        if self.status == "запланирован":
            self.status = "осуществляется"
        elif self.status == "осуществляется":
            self.status = "выполнен"

    def prev(self):
        if self.status == "осуществляется":
            self.status = "запланирован"
        elif self.status == "выполнен":
            self.status = "осуществляется"

    def start(self):
        self.status = "осуществляется"

    def stop(self):
        self.status = "выполнен"

    def reject(self):
        self.status = "забракован"

class Project(Stage):
    pass

class Fund(Stage):
    pass

class Walls(Stage):
    pass

class Roof(Stage):
    pass

class Electric(Stage):
    pass

class Finish(Stage):
    pass

class Building:
    def __init__(self):
        self.stages = []
        self.current_stage = 0

    def add_stage(self, stage):
        self.stages.append(stage)

    def run(self):
        for i in range(len(self.stages)):
            self.current_stage = i
            stage = self.stages[i]
            stage.start()
            if random.random() < 0.1:
                stage.reject()
                if i == 0:
                    return False
                else:
                    self.stages[i - 1].prev()
                    i -= 1
            else:
                stage.stop()
        return True

count = 0
for x in range(1000):
    construction = Building()
    construction.add_stage(Project(1000, "01.01.2023", "31.12.2023", 'проектирование'))
    construction.add_stage(Fund(1000, "01.01.2024", "31.12.2024", 'фундамент'))
    construction.add_stage(Walls(1000, "01.01.2024", "31.12.2024", 'стены'))
    construction.add_stage(Roof(1000, "01.01.2024", "31.12.2024", 'крыша'))
    construction.add_stage(Electric(1000, "01.01.2025", "31.12.2025", 'электрика'))
    construction.add_stage(Finish(1000, "01.01.2025", "31.12.2025", 'отделка'))
    if construction.run():
        count += 1

print(f"{count/1000 * 100}%")

class TestStage:
    def invalid_date(self):
