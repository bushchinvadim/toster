class User(object):

    _id = 0

    def __init__(self, first_name, last_name, age, gender, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.id = User._id
        self.balance = balance
        User._id += 1

    def __repr__(self):
        return f'User object - {self.first_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def birthday(self):
        self.age += 1

    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.balance += other
            return self.balance
        elif isinstance(other, User):
            return self.balance + other.balance
        else:
            raise ValueError('Не число')

    def __radd__(self, other):
        self.__add__(other)
        return self.balance

    def __sub__(self, other):
        self.__add__(-other)
        return self.balance

    def __rsub__(self, other):
        self.__add__(-other)
        return self.balance


    # def info(self):
    #     print(self.first_name, self.last_name)

user0 = User('Vasya', 'Pipkin', 34, 'M', 1000)
user1 = User('Masha', 'Svetlova', 23, 'W',2000)

print(user0 + 500 + user1)
