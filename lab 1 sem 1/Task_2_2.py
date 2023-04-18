from itertools import *

n, m = map(int, input().split()) # ввод данных матрицы
a = [[int(i) for i in input().split()] for _ in range(n)]

def determinant(n, arr): #функция определителя
    ans = 0 # алгоритм определения определителя через алг. дополнения.
    al = [s for s in permutations(range(1, n+1), n)]
    for q in range(len(al)):
        c = 0
        for i in range(n-1):
            for j in range(i+1, n):
                c += al[q][i] > al[q][j]
        k = (-1) ** c
        for t in range(n):
            k *= arr[t][al[q][t] - 1]
        ans += k
    return ans # возвращение результата.


def rank(n, m, arr): # функция определения ранга
    for r in range(min(n, m), 0, -1):
        for i in range(m-r+1):
            for j in range(n-r+1):
                b = [[[] for _ in range(r)] for _ in range(r)]
                for q in range(i, i + r):
                    for t in range(j, j + r):
                        b[t-j][q-i] = arr[t][q]
                if determinant(len(b), b) != 0:
                    return r
print(rank(n, m, a))
