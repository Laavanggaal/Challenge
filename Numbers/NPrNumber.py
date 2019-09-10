def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n
a = ''
n = 2
print('Я буду печатать простые числа, пока не получу на вход stop')
while a != 'stop':
    if isPrime(n):
        print(n, end = ' ')
        n += 1
        a = input()
    else:
        n += 1   