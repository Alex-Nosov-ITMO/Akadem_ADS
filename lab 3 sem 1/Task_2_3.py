import numpy as np
from random import randint

n = int(input('Введите размерность массива: '))
s = []
mat = np.ones((n,n))
for i in range(n):
    s.append(randint(100,1000))
print(s)
x = len(s)
for i in range(len(s)):
    for j in range(len(s)):
        mat[i,j] = s[i] + s[j]
print(mat)