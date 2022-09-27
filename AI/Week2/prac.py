import random
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
        if((pos+1) % height == 0):
            table.append(table_line)
            table_line = []

    print(tabulate(table))

def valid_state(state, height, width):
    if(len(state) != height * width):
        return False

    for i in range(height * width):
        if i not in state:
            return False

    return True


def sucessors(state, height, width):
    # encontrar o zero, transformar em pos 2D
    # ou esta no canto e tem 2 suc
    # ou esta nas bordas e tem 3
    # ou está no resto e tem 4

    if 0 in state:
        pos_0_1D = state.index(0)

    pos_0_2D = pos1D_to_pos2D(pos_0_1D)
    suc = []

    # 1 - Este, 2 - Sul, 3 - Oeste, 0 - Norte
    for i in range(4):
        # mover peça para norte
        if pos_0_2D[0] != 0:
            # nv = novo
            nv = state.copy()
            aux = state.index(pos2D_to_pos1D([pos_0_2D[0]-1, pos_0_2D[1]]))
            nv[pos_0_1D] = aux
            nv[pos2D_to_pos1D([pos_0_2D[0]-1, pos_0_2D[1]])] = 0
            suc.append(nv)
        # mover peça para sul
        if pos_0_2D[0] != height:
            # nv = novo
            nv = state.copy()
            aux = state.index(pos2D_to_pos1D([pos_0_2D[height]-1, pos_0_2D[1]]))
            nv[pos_0_1D] = aux
            nv[pos2D_to_pos1D([pos_0_2D[height]-1, pos_0_2D[1]])] = 0
            suc.append(nv)
        # mover peça para oeste
        if pos_0_2D[1] != 0:
            # nv = novo
            nv = state.copy()
            aux = state.index(pos2D_to_pos1D([pos_0_2D[0], pos_0_2D[0]-1]))
            nv[pos_0_1D] = aux
            nv[pos2D_to_pos1D([pos_0_2D[0], pos_0_2D[0]-1])] = 0
            suc.append(nv)
        # mover peça para este
        if pos_0_2D[1] != width:
            # nv = novo
            nv = state.copy()
            aux = state.index(pos2D_to_pos1D([pos_0_2D[0], pos_0_2D[width]-1]))
            nv[pos_0_1D] = aux
            nv[pos2D_to_pos1D([pos_0_2D[0], pos_0_2D[width]-1])] = 0
            suc.append(nv)




# [Estado, [E1, E2, E3]]

# def show_tree(state)

# find_state(tree, state)

def pos2D_to_pos1D(p, height, width):
    return (p[0] * width + p[1])

def pos1D_to_pos2D(p, height, width):
    return([p // width, p / width])

height = 4
width = 4
l = create_randomstate(height, width)
show_state(l, height, width)
print(valid_state(l, height, width))
sucessors(l, height, width)
