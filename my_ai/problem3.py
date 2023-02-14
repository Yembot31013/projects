
def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum


num = int(input('enter the number range: '))

sums = sum(num)

print(sums)
