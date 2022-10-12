import time
from classes import DataClass
a = 1
if a==1:
#for i in range(1, 8):
    #file_name = "test_time_" + str(i) + ".txt"
    file_name = "test_time_7.txt"
    f = open(file_name, "r", encoding="utf-8")
    tic = time.perf_counter()
    array = DataClass(f.readline().split(' '))
    print(array._sum())
    toc = time.perf_counter()
    print(f"Вычисление файла {file_name} элементом заняло {toc - tic:0.10f} секунд")
    f.close()