# поиск в глубину
square1 = {
    1: [2, 8],
    2: [1, 3, 8],
    3: [2, 4, 8],
    4: [3, 7, 9],
    5: [6, 7],
    6: [5],
    7: [4, 5, 8],
    8: [1, 2, 3, 7],
    9: [4],
}

visit = set() #проверяем, посещена ли площадь?

def dfs(v):
    if v in visit: # если площадь уже посещене - выходим.
        return
    visit.add(v) # посетили площадь
    for i in square1[v]: # площади которые можно посетить через порталы.
        if not i in visit:
            dfs(i)

start = 1
dfs(start) # начальная вершина.
print(visit)





# поиск в ширину

square2 = {
    1: [2, 8],
    2: [1, 3, 8],
    3: [2, 4, 8],
    4: [3, 7, 9],
    5: [6, 7],
    6: [5],
    7: [4, 5, 8],
    8: [1, 2, 3, 7],
    9: [4],
}
start = 1
pathes = [None] * len(square2)
pathes[start - 1] = 0
queue = [start]
while len(square2) != 0:
    sq = queue.pop(0)
    for i in square2[sq]:
        if pathes[i-1] is None:
            pathes[i-1] = pathes[sq-1] + 1
            queue += [i]
print(f'Самые короткие пути из площади {start} к другим площадям: ')
for i in range(len(square2)):
    print(f'Площадь {i+1} - {pathes[i]}')




