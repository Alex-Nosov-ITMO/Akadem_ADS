from random import randint
import math
N = int(input('Введите размерность массива: '))
s = []
n = []
for i in range(N):
    s.append(randint(100,1000))
print(s)

for i in range(3*int(math.log(len(s)))):
    n.append(s[i])
print(n)