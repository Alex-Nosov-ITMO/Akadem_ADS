import sort_task_1, random

def block(arr):
    max_value = max(arr)
    size = max_value/len(arr)

    buckets_list = []
    for x in range(len(arr)):
        buckets_list.append([])

    for i in range(len(arr)):
        j = int(arr[i] / size)
        if j != len(arr):
            buckets_list[j].append(arr[i])
        else:
            buckets_list[len(arr) - 1].append(arr[i])

    for z in range(len(arr)):
        sort_task_1.quick(buckets_list[z])


    final = []
    for x in range(len(arr)):
        final = final + buckets_list[x]
    return final



def pyramid(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        pyramidify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        pyramidify(arr, i, 0)
    return arr

def pyramidify(arr, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        pyramidify(arr, heap_size, largest)