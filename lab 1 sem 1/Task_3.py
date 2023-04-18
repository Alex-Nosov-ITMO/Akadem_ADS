import numpy as np

print("Введите число")
num = int(input())
m = list(np.arange(1, num+1, 1))
for i in range(len(m)):
    if m[i] % 5 == 0 and m[i] % 3 == 0:
        m[i] = str('FizzBuzz')
    elif m[i] % 5 == 0:
        m[i] = str('Fizz')
    elif m[i] % 3 == 0:
        m[i] = str('Buzz')
print(m)