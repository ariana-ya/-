def _min(array):
    if len(array) == 1 and array[0] =='':
        return "array is empty"
    else:
        min_element = int(array[0])
        for i in range(1, len(array)):
            if min_element > int(array[i]):
                min_element = int(array[i])
        return min_element


def _max(array):
    if len(array) == 1 and array[0] =='':
        return "array is empty"
    else:
        max_element = int(array[0])
        for i in range(1, len(array)):
            if max_element < int(array[i]):
                max_element = int(array[i])
        return max_element

def _sum(array):
    if len(array) == 1 and array[0] =='':
        return "array is empty"
    else:
        sum_of_elements = 0
        for i in range(len(array)):
            sum_of_elements += int(array[i])
        return sum_of_elements


def _mult(array):
    mult_of_elements = 1
    if len(array) == 1 and array[0] =='':
        return "array is empty"
    else:
        for i in range(len(array)):
            mult_of_elements *= int(array[i])
        return mult_of_elements


print("Введите название файла")
file = open(input())
array = file.readline().split(' ')
print("Команды:", "1 - найти минимум", "2 - найти максимум", "3 - найти сумму", "4 - найти произведение", sep = "\n")
command = int(input())
if command == 1:
    print(_min(array))
if command == 2:
    print(_max(array))
if command == 3:
    print(_sum(array))
if command == 4:
    print(_mult(array))