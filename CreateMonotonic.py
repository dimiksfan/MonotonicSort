import random as r

lst = list(range(20000))


def CreateLst():
    r.shuffle(lst)
    print(lst[:10])
    print(MonotonicSort(lst[1: 10]))
    return MonotonicSort(lst)


def MonotonicSort(lst):
    for i in range(1, (len(lst))):
         tmp = lst[i]
         while (i > 0) and (tmp <= lst[i - 1]):
             lst[i] = lst[i-1]
             i -= 1
         else:
            lst[i] = tmp
    return(lst)


#CreateLst()
