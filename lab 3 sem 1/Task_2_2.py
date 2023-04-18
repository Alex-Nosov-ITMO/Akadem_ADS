from random import randint

# алгоритм сложностью О(n log(n))

def merge(list1, left_index, right_index, middle):
    left_sublist = list1[left_index:middle + 1]
    right_sublist = list1[middle + 1:right_index + 1]
    left_sublist_index = 0
    right_sublist_index = 0
    sorted_index = left_index
    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:
            list1[sorted_index] = left_sublist[left_sublist_index]
            left_sublist_index += 1
        else:
            list1[sorted_index] = right_sublist[right_sublist_index]
            right_sublist_index += 1

        sorted_index += 1

    while left_sublist_index < len(left_sublist):
        list1[sorted_index] = left_sublist[left_sublist_index]
        left_sublist_index += 1
        sorted_index += 1
    while right_sublist_index < len(right_sublist):
        list1[sorted_index] = right_sublist[right_sublist_index]
        right_sublist_index += 1
        sorted_index += 1

def merge_sort(list1, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    merge_sort(list1, left_index, middle)
    merge_sort(list1, middle + 1, right_index)
    merge(list1, left_index, right_index, middle)



n2 = int(input("Введите размерность массива: "))
s = []
for i in range(n2):
    s.append(randint(100, 1000))
print(s)
merge_sort(s, 0, len(s) - 1)
print(s)


