import sort_task_1, random, time

arr = [random.randint(1, 1000) for i in range(30)]
print(arr)
print()


st_qk = time.time()
print(sort_task_1.quick(arr))
fn_qk = time.time()
print('Время выполнения быстрой сортировки: ', fn_qk - st_qk)

st_br = time.time()
print(sort_task_1.hairbrush(arr))
fn_br = time.time()
print('Времы выполнения сортировки расческой: ', fn_br - st_br)

