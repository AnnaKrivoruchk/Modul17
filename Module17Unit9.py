array = input("Введите через пробел последовательность положительных чисел:")
array = list(array.split(" "))
array = list(map(int, array))

def all(array):
    for i in (array):
        if i < 0:
            raise ValueError("Вы ввели последовательность чисел, не соответствующую условиям")
        else:
            pass
    return array

user_number = int(input("Введите, пожалуйста, положительное целое число:"))
if user_number < 0:
    raise ValueError("Вы ввели число, не соответствующее условиям")

array = sorted(array)

def binary_search(array, user_number):
    left = 0
    right = len(array)-1
    index = -1
    while (left <= right) and (index == -1):
        middle = (left+right)//2
        if array[middle] == user_number:
            index = middle
        else:
            if user_number<array[middle]:
                right = middle -1
            else:
                left = middle +1
    return index

index = binary_search(array, user_number)

if index == -1:
    print("Индекс числа введенного пользователем {}, индекс числа меньше введенного {}, "
          "числа больше введенного нет, оно максимально для данной последовательности."
          .format(array.index(user_number), array.index(user_number - 1)))
if index == 0:
    print("Индекс числа введенного пользователем {}, числа меньше введенного нет, введенное число минимально для данной "
          "последовательности. Индекс числа больше введенного {}."
          .format(array.index(user_number), array.index(user_number + 1)))
else:
    print("Индекс числа введенного пользователем {}, индекс числа меньше введенного {}, индекс числа больше введенного {}."
          .format(array.index(user_number), array.index(user_number - 1), array.index(user_number + 1)))
