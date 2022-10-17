from tabulate import tabulate
from datetime import datetime


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
        table_line.append(board[pos]+1)
        if (pos + 1) % n == 0:
            table.append(table_line)
            table_line = []

    print(tabulate(table))


def negative_diagonal(pos2D, n):
    nd = []

    # up
    x = pos2D[0]
    y = pos2D[1]
    while x + 1 < n and y + 1 < n:
        nd.append([x + 1, y + 1])
        x += 1
        y += 1

    # down
    x = pos2D[0]
    y = pos2D[1]
    while x - 1 >= 0 and y - 1 >= 0:
        nd.append([x - 1, y - 1])
        x -= 1
        y -= 1

    return nd


def positive_diagonal(pos2D, n):
    pd = []

    # up
    x = pos2D[0]
    y = pos2D[1]
    while x + 1 < n and y - 1 >= 0:
        pd.append([x + 1, y - 1])
        x += 1
        y -= 1

    # down
    x = pos2D[0]
    y = pos2D[1]
    while x - 1 >= 0 and y + 1 < n:
        pd.append([x - 1, y + 1])
        x -= 1
        y += 1

    return pd


def diagonals(pos2D, n):
    return positive_diagonal(pos2D, n) + negative_diagonal(pos2D, n)


def vertical(pos2D, n):
    v = []

    x_lower = pos2D[0] - 1
    while x_lower >= 0:
        v.append([x_lower, pos2D[1]])
        x_lower -= 1

    x_upper = pos2D[0] + 1
    while x_upper < n:
        v.append([x_upper, pos2D[1]])
        x_upper += 1

    return v


def block_arround(pos2D, board, n):
    to_block = vertical(pos2D, n) + diagonals(pos2D, n)
    board[pos2_to_pos1(pos2D, n)] = 1

    for item2D in to_block:
        if board[pos2_to_pos1(item2D, n)] != -1:
            board[pos2_to_pos1(item2D, n)] = -1


def is_final_board(board, n):
    # If the number of queens equals n, then the board is final
    if board.count(1) == n:
        return True

    return False


def first_row_with_pos_available(board, n):
    table_line = []
    line = -1
    for pos in range(n * n):
        table_line.append(board[pos])
        if (pos + 1) % n == 0:
            line += 1
            if table_line.count(1) == 0:
                return line + 1
            table_line = []

    return -1


def get_successors(board, n, row_tested):
    sucs = []
    row_tested_beginning = n*(row_tested-1)
    row_tested_end = n * row_tested

    if row_tested != -1:
        for posBoard1D in range(row_tested_beginning, row_tested_end):
            if board[posBoard1D] == 0:
                nv = board.copy()
                block_arround(pos1_to_pos2(posBoard1D, n), nv, n)
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


def successors(tr, st, n, row_tested):
    suc = get_successors(st[0], n, row_tested)
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


def search(st, n, type_search):
    # type_search: 1=breadth first; 2=depth first; 3=A*
    done = []
    todo = [st]
    num_sol = 0
    sol_leet = []
    while len(todo) > 0:
        cur = todo.pop(0)
        if is_final_board(cur[0], n):
            #  show_board(cur[0], n)
            num_sol += 1

        cur = successors(st, cur, n, first_row_with_pos_available(cur[0], n))
        for s in cur[-1]:
            if board_in_list(s[0], done):
                continue
            if type_search == 1:
                todo.append(s)  # Queue push to end
            elif type_search == 2:
                todo.insert(0, s)  # Stack push to beginning

        done.insert(-1, cur[0])

    return num_sol

###################################


start_time = datetime.now()

n = 8
initial_board = [0] * (n * n)
initial_state = [initial_board, []]
num_solutions = search(initial_state, n, 2)
print(num_solutions)

end_time = datetime.now()
print(end_time-start_time)
