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

def win(board):
    for num in range(1, 16):
        if board[num-1] != num:
            return False
    if board[15] != 0:
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
    nd = find_node(tree, father)

    # Se não se encontrar o pai, então retorna a árvore
    if nd is None:
        return tree
    # Se o pai encontrado não tiver filhos, o filho passa a ser "new"
    if len(nd[1]) == 0:
        nd[1] = [new]
        return tree

    # Se o pai tiver filhos, então insere na lista dos filhos o "new"
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
    if not win(tree[0]) and N > 0:
        for s in sucessors(tree[0], height, width):
            insertTree(tree, [s, []], tree[0])

        for f in tree[1]:
            expand_tree(f, N-1, height, width)
    else:
        if(win(tree[0])):
            show_state(tree[0], height, width)
        return tree


height = 4
width = 4
inicial_board = create_randomstate(height, width)
print("inicial:")
show_state(inicial_board , height, width)

#print(valid_state(l, height, width))

#suc = sucessors(inicial_board, height, width)
#print("sucessores:")
#for board in suc:
    #show_state(board, height, width)

tree = [inicial_board, []]
expand_tree(tree, 12, height, width)

#print(tree)
#show_tree(tree, height, width)
