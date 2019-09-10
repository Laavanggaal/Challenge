#Рекурентная форма

def FibR(n):
    if n <= 1:
        return n
    else:
        return FibR(n-1) + FibR(n-2)

#Последовательная
        
def FibA(n):
    if n <= 1:
        return n
    else:
        F = [0 for i in range(n+1)]
        F[1] = 1
        for j in range(2, n+1):
            F[j] = F[j-1] + F[j-2]
        return(F[n])
        
print('Выбирите алгоритм:')
print('0 - Жадный, 1 - Быстрый')
k = int(input())

print('Какое число желаете получить?')
n = int(input())
if k:
    print(FibA(n))
else:
    print(FibR(n))