class MyStr(str):
    def __str__(self):
        return self.upper()


my_str = MyStr('test')
print(my_str)


class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        try:
            if self.name.lower() == other.name.lower():
                return True
            else:
                return False
        except AttributeError as exc:
            print(f'{exc}')


first_user = User('andrII')
second_user = User('Andrii')
print(first_user == second_user)
