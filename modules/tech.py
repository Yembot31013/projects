# this a function that eat food

# loop
# for loop
# while loop

# indent

# from logging import shutdown
# from operator import index, indexOf


# lists = [1, 2, 3, 4, 5, 8, 9, 34, 6, 7]

# for i in lists:
#     if i < 8:
#         cont(inue
#     printi)

name = 'yemi'

# for i in name:
#     print(i)

# i = 0

# while i < 10:
#     print('hello world')
#     i = i + 1

# while True:
#     print(1)

max = int(
    input('enter the maximum value of your list, must be in range of [1-20]: '))
i = 1
sum = 0
arr = []
values = {
    1: 'first',
    2: 'second',
    3: 'third',
    4: 'fourth',
    5: 'fifth',
    6: 'sixth',
    7: 'seventh',
    8: 'eighth',
    9: 'ninth',
    10: 'tenth',
    11: 'eleventh',
    12: 'twelveth',
    13: 'thirteenth',
    14: 'fourteenth',
    15: 'fifteenth',
    16: 'sixteenth',
    17: 'seventeenth',
    18: 'eighteenth',
    19: 'ninteenth',
    20: 'twenth'
}
while i <= max:
    value = input(f'enter your {values[i]} value: ')
    arr.append(value)
    value = int(value)
    sum = sum + value
    i = i + 1

print(f'the sum of {arr} is {str(sum)}')
