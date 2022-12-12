print('I love Python ' * 42)


age_in_month = 274
age_in_years = age_in_month // 12

my_age = f'My name is Andrii, I’m {age_in_years} years old'

some_var = 1
print(
    some_var < age_in_month,
    some_var > age_in_years,
    some_var != my_age,
    some_var == age_in_month % age_in_years,
    some_var < age_in_years ** age_in_month
)

a, b, c = 2, 5, 6
abc = int(str(a) + str(b) + str(c))
print(abc)
