brackets = str(input('Введите структуру из скобок: '))
br_index = 0
check = 0
for i in range(len(brackets)):
    if brackets[i] == '(':
        check += 1
        if check == 1:
            br_index = i
    else:
        check -= 1

    if check == -1:
        print('Встречена лишняя закрытая скобка под индексом ' + str(i))
        break
if check == 0:
    print('Структура верная!')
if check > 0:
    print('Встречена лишняя открытая скобка под индексом ' + str(br_index))

