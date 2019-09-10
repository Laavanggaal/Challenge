from math import pi

print('До какого знака вывести число Пи?')
n = int(input())
print("%.{}f".format(n) % (pi))