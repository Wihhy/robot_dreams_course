class MyStr(str):
    def __init__(self, string):
        super().__init__()
        self.string = string

    def __str__(self):
        return self.string.upper()


my_str = MyStr('test')
print(my_str)


class User:
    def __init__(self, name):
        self.name = name.lower()

    def __eq__(self, other):
        try:
            if self.name == other.name:
                return True
            else:
                return False
        except AttributeError as exc:
            print(f'{exc}')


first_user = User('andrII')
second_user = User('Andrii')
print(first_user == second_user)
