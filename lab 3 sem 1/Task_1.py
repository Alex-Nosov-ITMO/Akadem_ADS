from random import randint

N = int(input("Введите размер массива: "))
s1 = []
for i in range(N):
    s1.append(randint(10, 1000))
print(s1)

for i in range(N-1):
    for j in range(N - i - 1):
        if s1[j] > s1[j+1]:
            s1[j], s1[j+1] = s1[j+1], s1[j]
print(s1)

s2 = []
for i in range(N):
    s2.append(randint(10, 1000))
print(s2)
s2.sort()
print(s2)



