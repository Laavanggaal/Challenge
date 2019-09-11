#Скучноватая задача, но потом попробую переделать без стороних функций и с обработччиком ввода

def DtB(number):
    return bin(int(number))
    
def BtD(number):
    return int(number, 2)
    
print('Введите конвертор. 0 - из двочиной в десятичную, 1 - из десятичнйо в двоичную:')
k = int(input())

print('Введите число:')
number = input()

if k:
    print(DtB(number))
else:
    print(BtD(number))