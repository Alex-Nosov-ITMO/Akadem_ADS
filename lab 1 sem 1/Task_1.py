n = int(input())
for i in range(1, n+1):
    if i % 15 == 0:
        print('FizzBuzz', end=' ')
    if i % 3 == 0:
        print('Fizz', end=' ')
    if i % 5 == 0:
        print('Buzz', end=' ')
    else:
        print(str(i), end=' ')
