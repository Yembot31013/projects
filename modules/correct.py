maximum = int(input('enter the maximum input for your list: '))

i = 1
yem = []
while i <= maximum:
    value = input(f'enter your {i} value: ')
    yem.append(value)
    print(yem)
    i = i+1

print(yem)
