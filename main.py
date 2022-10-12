from classes import DataClass
print("Введите название файла")
file = open(input())
array = DataClass(file.readline().split(' '))
print("Команды:", "1 - найти минимум", "2 - найти максимум", "3 - найти сумму", "4 - найти произведение", "5 - найти все", sep = "\n")
command = int(input())
if command == 1:
    print(array._min())
if command == 2:
    print(array._max())
if command == 3:
    print(array._sum())
if command == 4:
    print(array._mult)
if command == 5:
    print(array._min())
    print(array._max())
    print(array._sum())
    print(array._mult())
