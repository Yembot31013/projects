print('compare multiply numbers')
print('you must input from 1 and above')
high = 1
many = int(input('how many numbers did you want to compare? '))

for i in range(many):
    nums = int(input(f'no {i+1} number to compare: '))
    if nums > high:
        high = nums

    elif nums < 1:
        print(f'your are not allow to input {nums} as a value')
        break

    else:
        high = high

print(f'the highest number is {high}')
