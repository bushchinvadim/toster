class User(object):

    _id = 0

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.id = User._id
        User._id += 1

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # def info(self):
    #     print(self.first_name, self.last_name)

user0 = User('Vasya', 'Pipkin', 34, 'M')
user1 = User('Masha', 'Svetlova', 23, 'W')
# user1.info()
# user0.info()
print(user0.id, user1.id)
print(user0._id, user1._id)