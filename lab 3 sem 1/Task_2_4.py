from random import randint

n = int(input('Введите размерность массива: '))
s = []
a, b, c = 0, 0, 0
for i in range(n):
    s.append(randint(10,100))
print(s)

for i in range(len(s)):
    a = s[i]
    for j in range(len(s)):
        b = s[j]
        for z in range(len(s)):
            c = s[z]
            if a<50 and b%10==4 and c%10==2:
                print(a,b,c)