from tabulate import tabulate

def pos1_to_pos2(x, n):
    row = x // n
    col = x % n
    return [row, col]


def pos2_to_pos1(x2, n):
    return x2[0] * n + x2[1]

def show_board(board, n):
    table = []
    table_line = []
    for pos in range(n*n):
        table_line.append(board[pos])
        if (pos + 1) % n == 0:
            table.append(table_line)
            table_line = []

    print(tabulate(table))


def diagonalPri(pos2D, n):
    pos2Dx = pos2D[0]
    pos2Dy = pos2D[1]
    diagonal_pri = []

    # up
    new2Dx = pos2Dx
    new2Dy = pos2Dy
    while (new2Dx + 1 < n and new2Dy + 1 < n):
        diagonal_pri.append([new2Dx + 1, new2Dy + 1])
        new2Dx += 1
        new2Dy += 1

    # down
    new2Dx = pos2Dx
    new2Dy = pos2Dy
    while (new2Dx - 1 >= 0 and new2Dy - 1 >= 0):
        diagonal_pri.append([new2Dx - 1, new2Dy - 1])
        new2Dx -= 1
        new2Dy -= 1

    return diagonal_pri

def diagonalSec(pos2D, n):
    pos2Dx = pos2D[0]
    pos2Dy = pos2D[1]
    diagonal_sec = []

    # up
    new2Dx = pos2Dx
    new2Dy = pos2Dy
    while(new2Dx + 1 < n and new2Dy - 1 >= 0):
        diagonal_sec.append([new2Dx + 1, new2Dy - 1])
        new2Dx += 1
        new2Dy -= 1

    # down
    new2Dx = pos2Dx
    new2Dy = pos2Dy
    while (new2Dx - 1 >= 0 and new2Dy + 1 < n):
        diagonal_sec.append([new2Dx - 1, new2Dy + 1])
        new2Dx -= 1
        new2Dy += 1

    return diagonal_sec

def diagonals(pos2D, n):
    return diagonalSec(pos2D, n) + diagonalPri(pos2D, n)


def is_attacking(pos, board, n):
    posAnalysed2D = pos1_to_pos2(pos, n)
    is_attacking = False

    for posBoard1D in range(n*n):
        posBoard2D = pos1_to_pos2(posBoard1D, n);
        if posBoard2D != posAnalysed2D and board[posBoard1D] == 1:
            # Row verification
            if posBoard2D[0] == posAnalysed2D[0]:
                is_attacking = True
            # Column verification
            if posBoard2D[1] == posAnalysed2D[1]:
                is_attacking = True

    for pos2D in diagonals(posAnalysed2D, n):
        if board[pos2_to_pos1(pos2D, n)] == 1:
            is_attacking = True

    return is_attacking


def is_final_board(board, n):
    # The final board is a board where there is no empty spaces in what the queen not attacking other pieces
    final_board = True

    for pos in range(n*n):
        if board[pos] != 1:
            if not is_attacking(pos, board, n):
                final_board = False

    return final_board


def get_successors(board, n):
    sucs = []

    for posBoard1D in range(n*n):
        if board[posBoard1D] != 1 and not is_attacking(posBoard1D, board, n):
            nv = board.copy()
            nv[posBoard1D] = 1
            sucs.append(nv)

    return sucs

def find_node(tr, id):
    if len(tr) == 0:
        return None
    if tr[0] == id:
        return tr
    for t in tr[-1]:
        aux = find_node(t, id)
        if aux is not None:
            return aux
    return None

def successors(tr, st, n):
    suc = get_successors(st[0], n)
    for b in suc:
        aux = find_node(tr, b)
        if aux is None:
            st[-1].append([b, []])
    return st


def board_in_list(b, lst):
    return b in lst


def insert_sorted(lst, nv):
    index = len(lst)
    for i in range(len(lst)):
        if lst[i][2] > nv[2]:
            index = i
            break

    if index == len(lst):
        return lst[:index] + [nv]
    return lst[:index] + [nv] + lst[index:]


# depth first
def search(st, n, type_search):
    # type_search: 1=breadth first; 2=depth first; 3=A*
    done = []
    todo = [st]
    while len(todo) > 0:
        cur = todo.pop(0)
        if is_final_board(cur[0], n):
            return st, cur

        cur = successors(st, cur, n)
        for s in cur[-1]:
            if board_in_list(s[0], done):
                continue
            if type_search == 1:
                todo.append(s) # Queue push to end
            elif type_search == 2:
                todo.insert(0, s) # Stack push to beginning

        done.insert(-1, cur[0])
    return st, None



n = 4
initial_board = [0] * (n * n)
initial_state = [initial_board, []]
initial_state, result = search(initial_state, n, 1)
print(result)
show_board(result[0], n)
