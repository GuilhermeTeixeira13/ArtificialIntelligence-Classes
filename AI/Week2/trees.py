tree = [5, [[3, [[1, []], [4, []]]], [8, [[7, []], [10, [[9, []], [11, []]]]]]]]

#                                       5
#                       /                           \
#                       3                           8
#                   /       \               /             \
#                   1       4               7             10
#                                                   /           \
#                                                   9           11
#



# [9, []]


def insert_node_tree(tr, nv, parent):
    nd = find_node(tr, parent)
    if nd is None:
        return tr
    if len(nd[1]) == 0:
        nd[1] = [nv]
        return tr
    for pos, el in enumerate(nd[1]):
        #if el[0] > nv[0]:
            nd[1].append(nv)
            return tr

    nd[1].append(nv, -1)
    return tr



def count_nodes(tr):
    ret = 0
    if len(tr) > 0:
        for t in tr[1]:
            ret += count_nodes(t)
        return(1 + ret)
    return ret


def DF_traverse(tr):
    if len(tr) == 0:
        return
    print(tr[0])
    for t in tr[1]:
        DF_traverse(t)

def BF_traverse(tr):
    tr_aux = tr.copy()

    while len(tr_aux) > 0:
        t = tr_aux.pop(0)
        print('%d' % t[0])
        for s in t[1]:
            tr_aux.append(s)
    return


def count_levels(tr):
    if len(tr) == 0:
        return 0
    lev = [0]
    for t in tr[1]:
        lev.extend([count_levels(t)])
    return max(lev) + 1


def find_node(tr, id):
    if len(tr) == 0:
        return None
    if tr[0] == id:
        return tr
    for t in tr[1]:
        aux = find_node(t, id)
        if aux is not None:
            return aux
    return None


def find_depth_node_aux(tr, id, aux):
    if len(tr) == 0:
        return -1
    if tr[0] == id:
        return aux
    for t in tr[1]:
        a = find_depth_node_aux(t, id, aux + 1)
        if a >= 0:
            return a
    return -1


def find_depth_node(tr, id):
    return find_depth_node_aux(tr, id, 0)





print('Total nodes = %d' % count_nodes(tree))

print('Total levels = %d' % count_levels(tree))

print('Depth-First Traverse')
DF_traverse(tree)

print('Breadth-First Traverse')
BF_traverse([tree])


fd = 4
nd = find_node(tree, fd)

if nd is None:
    print('%d Not exist' % fd)
else:
    print('Exist %d' % nd[0])


d = find_depth_node(tree, fd)

print('%d is at depth %d' % (fd, d))

tree = insert_node_tree(tree, [6, []], 11)

print('Total nodes = %d' % count_nodes(tree))


