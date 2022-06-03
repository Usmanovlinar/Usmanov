stuffdict = {'banan':(300,75),
             'piano':(500,80),
             'bed':(400,100),
             'phone':(200,50),
             'lounch':(200,40),
             'desk':(200,70),
             'charge':(300,80),
             'headphones':(200,30),
             'clotches':(100,30),
             'mouse':(200,60)
            }


def get_weight_and_value(stuffdict):

    area = [stuffdict[item][0] for item in stuffdict]
    value = [stuffdict[item][1] for item in stuffdict]
    return area, value


def get_memtable(stuffdict, A=1000):
    area, value = get_weight_and_value(stuffdict)
    n = len(value)  #находим размеры таблицы


    V = [[0 for a in range(A + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(A + 1):

            if i == 0 or a == 0:
                V[i][a] = 0


            elif area[i - 1] <= a:
                V[i][a] = max(value[i - 1] + V[i - 1][a - area[i - 1]], V[i - 1][a])


            else:
                V[i][a] = V[i - 1][a]
    return V, area, value

def get_selected_items_list(stuffdict, A=1000):
    V, area, value = get_memtable(stuffdict)
    n = len(value)
    res = V[n][A]
    a = A
    items_list = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == V[i - 1][a]:
            continue
        else:
            items_list.append((area[i - 1], value[i - 1]))
            res -= value[i - 1]
            a -= area[i - 1]

    selected_stuff = []


    for search in items_list:
        for key, value in stuffdict.items():
            if value == search:
                selected_stuff.append(key)

    return selected_stuff

stuff = get_selected_items_list(stuffdict)
print(stuff)
totarea = sum([stuffdict[item][0] for item in stuff])
totvalue = sum([stuffdict[item][1] for item in stuff])
print(totarea)
print(totvalue)