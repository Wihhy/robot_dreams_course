from time import sleep

analyzer = input('Hi, just write something here pls:)\n')
for char in analyzer:
    if char.isdigit():
        if int(char) % 2 == 0:
            print(f'It’s a even number!')
        else:
            print(f'It’s a odd number!')
    elif char.isalnum():
        if char.isupper():
            print(f'It’s a upper letter!')
        else:
            print(f'It’s a lower letter!')
    else:
        print(f'It’s a symbol!')


while True:
    print('I love Python')
    sleep(4.2)
