from random import randint


# лгоритм сложностью О(3n)
n1 = int(input("Введите размерность массива: "))
s = []
for i in range(n1):
    s.append(randint(100, 1000))
print(s)

length = 3
n = len(s) + 1
for i in range(length):
    B = [[] for k in range(n)]
    for x in s:
        figure = x // 10**i % 10
        B[figure].append(x)
    S = []
    for k in range(n):
        S = S + B[k]
print(S)


