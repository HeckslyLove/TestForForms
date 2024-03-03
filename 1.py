def merge_sorted_lists(list1, list2):
    res = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1

    while i < len(list1):
        res.append(list1[i])
        i += 1

    while j < len(list2):
        res.append(list2[j])
        j += 1

    return res

list1 = [1, 3, 5, 7, 9, 11, 12]
list2 = [2, 4, 6, 8, 10]

res = merge_sorted_lists(list1, list2)
res.reverse()
print(res)

