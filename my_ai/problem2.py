def multiply_nums(first, second):
    return first*second


def sum_nums(first, second):
    return first + second


first = int(input('first number: '))
second = int(input('second number: '))

product = multiply_nums(first, second)
sum = sum_nums(first, second)

print(f'sum of {first} & {second} is {sum}')
print(f'product of {first} & {second} is {product}')
