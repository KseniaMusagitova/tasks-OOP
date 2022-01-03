# 1 задача
class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.lower().capitalize()
        self.last_name = last_name.title() # or last_name.lower().capitalize()
        self.full_name = self.first_name + ' ' + self.last_name
        self.initials = self.first_name[0] + '.' + self.last_name[0]


n = Name('jOHN', 'sIlVeR')
print(n.first_name)
print(n.last_name)
print(n.full_name)
print(n.initials)


# 2 задача
class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


c = Calculator()
print(c.add(1, 2))


# 3 задача
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def from_string(cls, str_to_parse):
        # data = str_to_parse.split('-')
        # return cls(data[0], data[1], data[2])

        first_name, last_name, salary = str_to_parse.split('-')
        return cls(first_name, last_name, salary)


emp = Employee.from_string('John-Smith-55000')
print(emp.first_name)
print(emp.last_name)
print(emp.salary)


# 4 задача
class Pizza:
    order = 0 # статический счетчик

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.order += 1
        self.order_number = Pizza.order

    @classmethod
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])

    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])

    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushroom'])


p1 = Pizza(['ham', 'bacon'])
p2 = Pizza.garden_feast()
p3 = Pizza.hawaiian()
p4 = Pizza(['beef', 'olives'])

print(Pizza.order)
print(p1.order_number)
print(p2.order_number)
print(p3.order_number)
print(p4.order_number)


# 5 задача
import math


class Circle:
    def __init__(self, r=0):
        self.r = r

    def get_area(self):
        return math.pi * self.r ** 2

    def get_perimetr(self):
        return 2 * math.pi * self.r


c = Circle(4.44)
print(c.get_perimetr())
print(c.get_area())


# 6 задача
prices = {'strawberries': 1.5, 'banana': 0.5, 'mango': 2.5}

class Beverage:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cost = sum([prices[fruit] for fruit in self.ingredients])
        self.price = self.cost * 2.5

    def get_cost(self):
        return f'${self.cost:.2f}'

    def get_price(self):
        return f'${self.price:.2f}'

    def get_name(self):
        lst = sorted([i.replace('ies', 'y') for i in self.ingredients])
        return f'{" ".join(lst)} {"Fusion" if len(lst) > 1 else "Smoothie"}'


b1 = Beverage(['mango', 'strawberries'])
print(b1.ingredients)
print(b1.get_cost())
print(b1.get_price())
print(b1.get_name())

b1 = Beverage(['mango'])
print(b1.ingredients)
print(b1.get_cost())
print(b1.get_price())
print(b1.get_name())


# 7 задача, крестики-нолики
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def print_state(state):
    for i, c in enumerate(state):
        if (i+1) % 3 == 0:
            print(f'{c}')
        else:
            print(f'{c}', end='')


winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                        (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def get_winner(state, combinations):
    for (x,y,z) in combinations:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == 'O'):
            return state[x]
    return ''


def play_game(board):
    current_sign = 'X'
    while get_winner(board, winning_combinations) == '':
        index = int(input(f'Where do you want to draw {current_sign}?'))
        board[index] = current_sign

        print_state(board)

        winner_sign = get_winner(board, winning_combinations)
        if winner_sign != '':
            print(f'We have a winner:{winner_sign}')

        current_sign = 'X' if current_sign == 'O' else 'O'


play_game(board)

