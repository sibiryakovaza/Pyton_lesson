# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

from random import sample


def find_num(count, num):
    if count < 0:
        return "Negative value of the number of numbers!"
    # sample - неповторяющиеся значения
    list_nums = sample(range(1, (count + 1) * 2), k=count)
    print(list_nums)

    if num in list_nums:
        return f"The number - {num} is present in the list."
    return f"The number - {num} is not in the list."


print(find_num(int(input("Number of numbers: ")), int(input("Number: "))))

# -------------------------- вариант

from random import sample


def find_num(count, num):
    if count < 0:
        return "Negative value of the number of numbers!"

    list_nums = sample(range(1, (count + 1) * 2), k=count)
    print(list_nums)
    return "Yes" if num in list_nums else "No"


print(find_num(int(input("Number of numbers: ")), int(input("Number: "))))
