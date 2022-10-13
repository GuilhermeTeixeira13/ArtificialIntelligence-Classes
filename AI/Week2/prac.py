import random
import math
import trees
from tabulate import tabulate


def create_randomstate(height, width):
    state = list(range(0, height * width))
    random.shuffle(state)
    return state


def show_state(state, height, width):
    table = []
    table_line = []
    for pos in range(height * width):
        table_line.append(state[pos])
        if ((pos + 1) % height == 0):
            table.append(table_line)
            table_line = []

    print(tabulate(table))


def valid_state(state, height, width):
    if (len(state) != height * width):
        return False

    for i in range(height * width):
        if i not in state:
            return False

    return True

def pos2D_to_pos1D(p, height, width):
    return (p[0] * width + p[1])


def pos1D_to_pos2D(p, height, width):
    return ([p // width, p % height ])


def sucessors(state, height, width):
    # Encontrar o zero, transformar em pos 2D
    # ou esta no canto e tem 2 suc
    # ou esta nas bordas e tem 3
    # ou está no resto e tem 4

    if 0 in state:
        pos_0_1D = state.index(0)

    pos_0_2D = pos1D_to_pos2D(pos_0_1D, height, width)
    suc = []

    # Mover zero para norte
    if pos_0_2D[0] != 0:
        norte = pos2D_to_pos1D([pos_0_2D[0] - 1, pos_0_2D[1]], height, width)
        nv = state.copy()
        aux = state[norte]  # Pegar na peça por cima do zero e guardar
        nv[pos_0_1D] = aux  # Colocar a peça por cima do zero no lugar do zero
        nv[norte] = 0  # A posição onde estava a peça q substitui o zero, passa a ser zero
        suc.append(nv)
    # Mover zero para sul
    if pos_0_2D[0] != height-1:
        sul = pos2D_to_pos1D([pos_0_2D[0] + 1, pos_0_2D[1]], height, width)
        nv = state.copy()
        aux = state[sul]
        nv[pos_0_1D] = aux
        nv[sul] = 0
        suc.append(nv)
    # Mover zero para oeste
    if pos_0_2D[1] != 0:
        oeste = pos2D_to_pos1D([pos_0_2D[0], pos_0_2D[1] - 1], height, width)
        nv = state.copy()
        aux = state[oeste]
        nv[pos_0_1D] = aux
        nv[oeste] = 0
        suc.append(nv)
    # Mover zero para este
    if pos_0_2D[1] != width-1:
        este = pos2D_to_pos1D([pos_0_2D[0], pos_0_2D[1] + 1], height, width)
        nv = state.copy()
        aux = state[este]
        nv[pos_0_1D] = aux
        nv[este] = 0
        suc.append(nv)

    return suc

def win(board, height, width):
    for num in range(1, height*width):
        if board[num-1] != num:
            return False
    if board[height*width - 1] != 0:
        return False
    return True

# [Estado, [E1, ...]]

def find_node(tree, state):
    if len(tree) == 0:
        return None
    if tree[0] == state:
        return tree
    for t in tree[1]:
        aux = find_node(t, state)
        if aux is not None:
            return aux
    return None

def insertTree(tree, new, father):
    nd = find_node(tree, father[0])

    if nd is None:
        return None
    nd[1].append(new)
    return tree

def show_tree(tree, height, width):
    if len(tree) == 0:
        return
    show_state(tree[0], height, width)
    for t in tree[1]:
        show_tree(t, height, width)


def count_tree(tree):
    if len(tree) == 0:
        return 0
    lev = [0]
    for t in tree[1]:
        lev.extend([count_tree(t)])
    return max(lev) + 1

def expand_tree(tree, N, height, width):
    if N == 0:
        return tree
    suc = sucessors(tree[0], height, width)
    for s in suc:
        tree = insertTree(tree, expand_tree([s, []], N - 1, height, width), tree)
    return tree

def show_tree(tr, cur_d, h, w):
    if len(tr) == 0:
        return
    print('[%d]-------------------------------------' % cur_d)
    for ih in range(h):
        for iw in range(w):
            print('%d\t' % tr[0][ih * w + iw], end='')
        print('')
    print('-------------------------------------')
    for t in tr[1]:
        show_tree(t, cur_d +1, h, w)


'''def minimal(tree, steps, depth, height, width):
    minimal_steps = steps
    if len(tree) == 0 or (steps == depth and win(tree[0], height, width) is False):
        minimal_steps = -1
    elif win(tree[0], height, width):
        minimal_steps = steps
    else:
        for t in tree[1]:
            minimal_steps = minimal(t, steps+1, depth, height, width)

    return minimal_steps

def minimal_number_steps(inicial_state, depth, height, width):
    tree = [inicial_state, []]
    tree = expand_tree(tree, depth, height, width)

    return minimal(tree, 0, depth, height, width)'''



# Fila
def BFS(inicial_state, height, width):
    done = []
    todo = [inicial_state]

    while len(todo) > 0:
        x = todo.pop(0)
        if win(x, height, width):
            return x
        suc = sucessors(x, height, width)
        for s in suc:
            if s in done:
                continue
            todo.append(s)
        done.append(x)

    return None

# Pilha
def DFS(inicial_state, height, width):
    done = []
    todo = [inicial_state]

    while len(todo) > 0:
        x = todo.pop()
        if win(x, height, width):
            return x
        suc = sucessors(x, height, width)
        for s in suc:
            if s in done:
                continue
            todo.append(s)
        done.append(x)

    return None

def ObjectiveFunction(board, height, width):
    count_erradas = 0

    # 1 a 15
    for i in range(1, height * width):
        if(board[i-1] != i):
            count_erradas += 1

    if(board[height * width -1] != 0):
        count_erradas += 1

    return count_erradas

def AASTERISCO(inicial_state, height, width):
    done = []
    todo = [inicial_state]
    count_steps = 0

    while len(todo) > 0:
        x = todo.pop()
        if win(x, height, width):
            return x
        suc = sucessors(x, height, width)
        count_steps += 1
        for s in suc:
            if (s not in done) and (s not in todo):
                # Na função f, mais pontos é mau, menos é bom
                #print(ObjectiveFunction(s, height, width)+count_steps)
                todo.insert(ObjectiveFunction(s, height, width) + count_steps, s)
        done.append(x)

    return None


height = 3
width = 3

#inicial_board = create_randomstate(height, width)
almost_win = [1, 2, 3, 4, 5, 0, 6, 7, 8]

print("Estado inicial:")
show_state(almost_win, height, width)

#tree = expand_tree([almost_win,[]], 2, height, width)
#print("\n\nÁrvore:\n")
#show_tree(tree, 0, height, width)

show_state(BFS(almost_win, height, width), height, width)

show_state(DFS(almost_win, height, width), height, width)

show_state(AASTERISCO(almost_win, height, width), height, width)