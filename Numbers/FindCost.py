def costF(w,h,cost):
    return w*h*cost
print('Приступим к расчётам')
print('Введите ширину:', end = ' ')
w = int(input())
print('Введите длину:', end = ' ')
h = int(input())
print('Введите стоимость одной плитки', end = ' ')
cost = int(input())
print('Плитка будет стоить:', end = ' ')
print(costF(w,h,cost))