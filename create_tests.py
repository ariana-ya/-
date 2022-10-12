string_10 = ''
string_100 = ''
string_1000 = ''
string_10000 = ''
string_100000 = ''
string_1000000 = ''
string_10000000 = ''
for i in range(1, 10):
    string_10 += str(i) + " "
string_10 += '7'
file = open("test_time_1.txt", "w", encoding="utf-8")
file.write(string_10)
file.close()
for i in range(1, 100):
    string_100 += str(i) + " "
string_100 += '7'
file = open("test_time_2.txt", "w", encoding="utf-8")
file.write(string_100)
file.close()
for i in range(1, 1000):
    string_1000 += str(i) + " "
string_1000 += '7'
file = open("test_time_3.txt", "w", encoding="utf-8")
file.write(string_1000)
file.close()
for i in range(1, 10000):
    string_10000 += str(i) + " "
string_10000 += '7'
file = open("test_time_4.txt", "w", encoding="utf-8")
file.write(string_10000)
file.close()
for i in range(1, 100000):
    string_100000 += str(i) + " "
string_100000 += '7'
file = open("test_time_5.txt", "w", encoding="utf-8")
file.write(string_100000)
file.close()
for i in range(1, 1000000):
    string_1000000 += str(i) + " "
string_1000000 += '7'
file = open("test_time_6.txt", "w", encoding="utf-8")
file.write(string_1000000)
file.close()
for i in range(1, 10000000):
    string_10000000 += str(i) + " "
string_10000000 += '7'
file = open("test_time_7.txt", "w", encoding="utf-8")
file.write(string_10000000)
file.close()
print("complete")