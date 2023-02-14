lists = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]

target = int(input("enter your target: "))


def first_search():
    first = -1
    count = 0
    for i in range(len(lists)):
        if target == lists[i] and count == 0:
            first = i
            count = 1
    return first


def second_search():
    counts = -1
    for j in range(len(lists)):
        count = j
        if target == lists[j]:
            counts = count
    return counts


print([first_search(), second_search()])
