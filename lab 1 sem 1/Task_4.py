a = [[int(i) for i in input().split()] for _ in range(3)] # входные данные матрицы.

def det3(a): # определитель матрицы 3х3.
    A = a[0][0] * a[1][1] * a[2][2] * a[1][0] * a[2][1] * a[0][2] * a[0][1] * a[1][2] * a[2][0]
    B = a[0][2] * a[1][1] * a[2][0] * a[0][0] * a[1][2] * a[2][1] * a[0][1] * a[1][0] * a[2][2]
    return A - B

def algdop(a, x, y): # функция поиска алгебраических дополнений.
    res = []
    for i in range(len(a)):
        for j in range(len(a)):
            if i != x and j != y:
                res += [a[i][j]]
    opred2 = res[0] * res[3] - res[1] * res[2]
    return opred2 * (-1) ** (x+y)

def obrat(arr): # функция поиска обратной матрицы.
    if det3(arr) == 0: # если определитель равен 0, то обратной матрицы нет.
        print('Нет обратной матрицы')

    else: # создаем еще одну матрицу и будем ее заполнять
      #  методом алгебраических дополнений.
        ans = [[[] for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                t = 1 / det3(arr) * algdop(arr, i, j)
                if int(t) == t:
                    ans[j][i] = int(t)
                else:
                    ans[j][i] = t
        for x in ans:
            print(*x)

obrat(a)