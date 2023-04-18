import random

def quick(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
    less_arr = [n for n in arr if n < pivot]

    p_arr = [pivot] * arr.count(pivot)
    bigger_arr = [n for n in arr if n > pivot]
    return quick(less_arr) + p_arr + quick(bigger_arr)


def hairbrush(arr):
    gap = len(arr)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))
        swaps = False
        for i in range(len(arr) - gap):
            j = i + gap
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swaps = True
    return arr



