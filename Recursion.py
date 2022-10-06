items = [8, 2, 3, 0, 7, 4, 6, 2]

c=0

def sum_list(items):
    x = list(items)
    global c
    if len(x) > (0):
        reml = x.pop(0)
        c = c + reml
        sum_list(x)
    else:
        print(c)


print(items)
(sum_list(items))