my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = 0
print(my_list)
print('Положительные числа из списка:')
while number < len(my_list):
    num = my_list[number]
    number = number + 1
    if num == 0:
        continue
    elif num < 0:
        print('Отрицательные числа из списка:', num)
        break
    elif number == len(my_list):
        print(num)
    else:
        print(num)