n1, m1 = map(int, input().split())      # вводим данные матриц
a1 = [[int(i) for i in input().split()] for _ in range(n1)]
n2, m2 = map(int, input().split())
a2 = [[int(i) for i in input().split()] for _ in range(n2)]

def trans(n, m, arr): # функция трансформирования матрицы
    if n != m: # если размерности не совпадают, то выбрасываем ошибку
        print('Матрицу нельзя транспонировать')
    else: # иначе трансформируем матрицу.
        b = [[[] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                b[i][j] = arr[j][i]
        for x in b:
            print(*x)
    print()


def multi(n1, m1, arr1, n2, m2, arr2): # функция умножения матриц.
    if m1 != n1: #если размерности не совпадают, то выкидываем ошибку
        print('Матрици нельзя перемножить')
    else: # иначе перемножаем матрицы.
        ans = [[0 for _ in range(m2)] for _ in range(n1)]
        for i in range(n1):
            for j in range(m2):
                for q in range(n2):
                    ans[i][j] += arr1[i][q] * arr2[q][j]
        for i in ans:
            print(*i)
    print()




trans(n1, m1, a1)
trans(n2, m2, a2)
multi(n1, m1, a1, n2, m2, a2)