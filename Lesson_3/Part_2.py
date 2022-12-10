akinator = input('Hi, just write something here pls:)\n')
if akinator.isdigit():
    if int(akinator) % 2 == 0:
        print(f'It’s a number! I know it)\nIt’s Even!')
    else:
        print(f'It’s a number! I know it)\nIt’s Odd!')
else:
    print(f'It’s word! I know it)\nHis length is:{len(akinator)}!')

