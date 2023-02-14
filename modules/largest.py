lists = [4, 2, 9, 7, 5, 6, 7, 1, 3]
print(
    f"enter the maximum position you want to check from {lists}. for (example, if you want to check the fourth largest you will enter \"4\" as an input.")

k = int(input("enter your max position: "))


def maxs(k, lists):
    if len(lists) < 4:
        return False
    elif len(lists) == 4:
        return lists[4]
    else:
        for i in range(k-1):
            maxe = max(lists)
            lists.remove(maxe)
        print(max(lists))


maxs(k, lists)
