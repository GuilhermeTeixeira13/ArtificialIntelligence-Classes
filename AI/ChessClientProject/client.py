import socket, sys

from collections import Counter  # Added by me
import re  # Added by me

board = ""  # Added by me
interactive_flag = False


def pos2_to_pos1(x2):
    return x2[0] * 8 + x2[1]


# Added by me (copy from RandomPlays.py)
def pos1_to_pos2(x):
    row = x // 8
    col = x % 8
    return [row, col]


# Added by me (copy from RandomPlays.py)
def get_positions_directions(state, piece, p2, directions):
    ret = []
    for d in directions:
        for r in range(1, d[1] + 1):
            if d[0] == 'N':
                if p2[0] - r < 0:
                    break
                if state[pos2_to_pos1([p2[0] - r, p2[1]])] == 'z':
                    ret.append([p2[0] - r, p2[1]])
                    continue

                if abs(ord(state[pos2_to_pos1([p2[0] - r, p2[1]])]) - ord(piece)) > 16:
                    ret.append([p2[0] - r, p2[1]])
                break
            if d[0] == 'S':
                if p2[0] + r > 7:
                    break
                if state[pos2_to_pos1([p2[0] + r, p2[1]])] == 'z':
                    ret.append([p2[0] + r, p2[1]])
                    continue

                if abs(ord(state[pos2_to_pos1([p2[0] + r, p2[1]])]) - ord(piece)) > 16:
                    ret.append([p2[0] + r, p2[1]])
                break
            if d[0] == 'W':
                if p2[1] - r < 0:
                    break
                if state[pos2_to_pos1([p2[0], p2[1] - r])] == 'z':
                    ret.append([p2[0], p2[1] - r])
                    continue

                if abs(ord(state[pos2_to_pos1([p2[0], p2[1] - r])]) - ord(piece)) > 16:
                    ret.append([p2[0], p2[1] - r])
                break
            if d[0] == 'E':
                if p2[1] + r > 7:
                    break
                if state[pos2_to_pos1([p2[0], p2[1] + r])] == 'z':
                    ret.append([p2[0], p2[1] + r])
                    continue

                if abs(ord(state[pos2_to_pos1([p2[0], p2[1] + r])]) - ord(piece)) > 16:
                    ret.append([p2[0], p2[1] + r])
                break
            if d[0] == 'NE':
                if p2[0] - r < 0 or p2[1] + r > 7:
                    break
                if state[pos2_to_pos1([p2[0] - r, p2[1] + r])] == 'z':
                    ret.append([p2[0] - r, p2[1] + r])
                    continue

                if abs(ord(state[pos2_to_pos1([p2[0] - r, p2[1] + r])]) - ord(piece)) > 16:
                    ret.append([p2[0] - r, p2[1] + r])
                break
            if d[0] == 'SW':
                if p2[0] + r > 7 or p2[1] - r < 0:
                    break
                if state[pos2_to_pos1([p2[0] + r, p2[1] - r])] == 'z':
                    ret.append([p2[0] + r, p2[1] - r])
                    continue

                if abs(ord(state[pos2_to_pos1([p2[0] + r, p2[1] - r])]) - ord(piece)) > 16:
                    ret.append([p2[0] + r, p2[1] - r])
                break
            if d[0] == 'NW':
                if p2[0] - r < 0 or p2[1] - r < 0:
                    break
                if state[pos2_to_pos1([p2[0] - r, p2[1] - r])] == 'z':
                    ret.append([p2[0] - r, p2[1] - r])
                    continue

                if abs(ord(state[pos2_to_pos1([p2[0] - r, p2[1] - r])]) - ord(piece)) > 16:
                    ret.append([p2[0] - r, p2[1] - r])
                break
            if d[0] == 'SE':
                if p2[0] + r > 7 or p2[1] + r > 7:
                    break
                if state[pos2_to_pos1([p2[0] + r, p2[1] + r])] == 'z':
                    ret.append([p2[0] + r, p2[1] + r])
                    continue

                if abs(ord(state[pos2_to_pos1([p2[0] + r, p2[1] + r])]) - ord(piece)) > 16:
                    ret.append([p2[0] + r, p2[1] + r])
                break
            if d[0] == 'PS':
                if p2[0] + r > 7:
                    break
                if state[pos2_to_pos1([p2[0] + r, p2[1]])] == 'z':
                    ret.append([p2[0] + r, p2[1]])
                continue
            if d[0] == 'PN':
                if p2[0] - r < 0:
                    break
                if state[pos2_to_pos1([p2[0] - r, p2[1]])] == 'z':
                    ret.append([p2[0] - r, p2[1]])
                continue
            if d[0] == 'PS2':
                if p2[0] + r <= 7 or p2[1] + 1 <= 7:
                    if state[pos2_to_pos1([p2[0] + r, p2[1] + 1])] != 'z':
                        if abs(ord(state[pos2_to_pos1([p2[0] + r, p2[1] + 1])]) - ord(piece)) > 16:
                            ret.append([p2[0] + r, p2[1] + 1])

                if p2[0] + r <= 7 or p2[1] - 1 >= 0:
                    if state[pos2_to_pos1([p2[0] + r, p2[1] - 1])] != 'z':
                        if abs(ord(state[pos2_to_pos1([p2[0] + r, p2[1] - 1])]) - ord(piece)) > 16:
                            ret.append([p2[0] + r, p2[1] - 1])
                continue
            if d[0] == 'PN2':
                if p2[0] - r >= 0 or p2[1] + 1 <= 7:
                    if state[pos2_to_pos1([p2[0] - r, p2[1] + 1])] != 'z':
                        if abs(ord(state[pos2_to_pos1([p2[0] - r, p2[1] + 1])]) - ord(piece)) > 16:
                            ret.append([p2[0] - r, p2[1] + 1])

                if p2[0] - r >= 0 or p2[1] - 1 >= 0:
                    if state[pos2_to_pos1([p2[0] - r, p2[1] - 1])] != 'z':
                        if abs(ord(state[pos2_to_pos1([p2[0] - r, p2[1] - 1])]) - ord(piece)) > 16:
                            ret.append([p2[0] - r, p2[1] - 1])
                continue
            if d[0] == 'H':
                if p2[0] - 2 >= 0 and p2[1] - 1 >= 0:
                    if state[pos2_to_pos1([p2[0] - 2, p2[1] - 1])] == 'z' or abs(
                            ord(state[pos2_to_pos1([p2[0] - 2, p2[1] - 1])]) - ord(piece)) > 16:
                        ret.append([p2[0] - 2, p2[1] - 1])

                if p2[0] - 2 >= 0 and p2[1] + 1 <= 7:
                    if state[pos2_to_pos1([p2[0] - 2, p2[1] + 1])] == 'z' or abs(
                            ord(state[pos2_to_pos1([p2[0] - 2, p2[1] + 1])]) - ord(piece)) > 16:
                        ret.append([p2[0] - 2, p2[1] + 1])

                if p2[0] - 1 >= 0 and p2[1] + 2 <= 7:
                    if state[pos2_to_pos1([p2[0] - 1, p2[1] + 2])] == 'z' or abs(
                            ord(state[pos2_to_pos1([p2[0] - 1, p2[1] + 2])]) - ord(piece)) > 16:
                        ret.append([p2[0] - 1, p2[1] + 2])

                if p2[0] + 1 <= 7 and p2[1] + 2 <= 7:
                    if state[pos2_to_pos1([p2[0] + 1, p2[1] + 2])] == 'z' or abs(
                            ord(state[pos2_to_pos1([p2[0] + 1, p2[1] + 2])]) - ord(piece)) > 16:
                        ret.append([p2[0] + 1, p2[1] + 2])

                if p2[0] + 2 <= 7 and p2[1] + 1 <= 7:
                    if state[pos2_to_pos1([p2[0] + 2, p2[1] + 1])] == 'z' or abs(
                            ord(state[pos2_to_pos1([p2[0] + 2, p2[1] + 1])]) - ord(piece)) > 16:
                        ret.append([p2[0] + 2, p2[1] + 1])

                if p2[0] + 2 <= 7 and p2[1] - 1 >= 0:
                    if state[pos2_to_pos1([p2[0] + 2, p2[1] - 1])] == 'z' or abs(
                            ord(state[pos2_to_pos1([p2[0] + 2, p2[1] - 1])]) - ord(piece)) > 16:
                        ret.append([p2[0] + 2, p2[1] - 1])

                if p2[0] + 1 <= 7 and p2[1] - 2 >= 0:
                    if state[pos2_to_pos1([p2[0] + 1, p2[1] - 2])] == 'z' or abs(
                            ord(state[pos2_to_pos1([p2[0] + 1, p2[1] - 2])]) - ord(piece)) > 16:
                        ret.append([p2[0] + 1, p2[1] - 2])

                if p2[0] - 1 >= 0 and p2[1] - 2 >= 0:
                    if state[pos2_to_pos1([p2[0] - 1, p2[1] - 2])] == 'z' or abs(
                            ord(state[pos2_to_pos1([p2[0] - 1, p2[1] - 2])]) - ord(piece)) > 16:
                        ret.append([p2[0] - 1, p2[1] - 2])
    return ret


# Added by me (copy from RandomPlays.py)
def get_available_positions(state, p2, piece):
    ret = []
    if piece in ('a', 'h', 'A', 'H'):  # Tower
        aux = get_positions_directions(state, piece, p2, [['N', 7], ['S', 7], ['W', 7], ['E', 7]])
        if len(aux) > 0:
            ret.extend(aux)
        return ret

    if piece in ('c', 'f', 'C', 'F'):  # Bishop
        aux = get_positions_directions(state, piece, p2, [['NE', 7], ['SE', 7], ['NW', 7], ['SW', 7]])
        if len(aux) > 0:
            ret.extend(aux)
        return ret

    if piece in ('d', 'D'):  # Queen
        aux = get_positions_directions(state, piece, p2,
                                       [['N', 7], ['S', 7], ['W', 7], ['E', 7], ['NE', 7], ['SE', 7], ['NW', 7],
                                        ['SW', 7]])
        if len(aux) > 0:
            ret.extend(aux)
        return ret

    if piece in ('e', 'E'):  # King
        aux = get_positions_directions(state, piece, p2,
                                       [['N', 1], ['S', 1], ['W', 1], ['E', 1], ['NE', 1], ['SE', 1], ['NW', 1],
                                        ['SW', 1]])
        if len(aux) > 0:
            ret.extend(aux)
        return ret

    if piece in ('b', 'g', 'B', 'G'):  # Horse
        aux = get_positions_directions(state, piece, p2, [['H', 1]])
        if len(aux) > 0:
            ret.extend(aux)
        return ret

    # Pawn
    if ord('i') <= ord(piece) <= ord('p'):
        if p2[0] == 1:
            aux = get_positions_directions(state, piece, p2, [['PS', 2]])
            if len(aux) > 0:
                ret.extend(aux)
        else:
            aux = get_positions_directions(state, piece, p2, [['PS', 1]])
            if len(aux) > 0:
                ret.extend(aux)
        aux = get_positions_directions(state, piece, p2, [['PS2', 1]])
        if len(aux) > 0:
            ret.extend(aux)
        return ret

    if ord('I') <= ord(piece) <= ord('P'):
        if p2[0] == 6:
            aux = get_positions_directions(state, piece, p2, [['PN', 2]])
            if len(aux) > 0:
                ret.extend(aux)
        else:
            aux = get_positions_directions(state, piece, p2, [['PN', 1]])
            if len(aux) > 0:
                ret.extend(aux)
        aux = get_positions_directions(state, piece, p2, [['PN2', 1]])
        if len(aux) > 0:
            ret.extend(aux)
    return ret


# Added by me (copy from RandomPlays.py)
def sucessor_states(state, player):
    ret = []

    for x in range(ord('a') - player * 32, ord('p') - player * 32 + 1):

        p = state.find(chr(x))
        if p < 0:
            continue
        p2 = pos1_to_pos2(p)

        pos_available = get_available_positions(state, p2, chr(x))
        # print('%c - Tot %d' % (chr(x), len(pos_available)))

        for a in pos_available:
            state_aux = list('%s' % state)
            state_aux[p] = 'z'
            if ord('i') <= x <= ord('p') and a[0] == 7:
                state_aux[pos2_to_pos1(a)] = 'd'
            elif ord('I') <= x <= ord('P') and a[0] == 0:
                state_aux[pos2_to_pos1(a)] = 'D'
            else:
                state_aux[pos2_to_pos1(a)] = chr(x)
            ret.append(''.join(state_aux))

    return ret


# Added by me (copy from RandomPlays.py)
def check_win(cur_state):
    # If the black king is not on the boar, then the white player wins
    if cur_state.find('e') < 0:
        return 1
    # Vice versa
    if cur_state.find('E') < 0:
        return 0
    return 2


# Function that reverse a list
def reverse(lst):
    new_lst = lst[::-1]
    return new_lst


#   Square tables that will help us evaluate our board pieces and the values will
# be set in a 8x8 matrix such as in chess such that it must have a higher
# value at favorable positions and a lower value at a non-favorable place

pawntablewhite = [
    0, 0, 0, 0, 0, 0, 0, 0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5, 5, 10, 27, 27, 10, 5, 5,
    0, 0, 0, 25, 25, 0, 0, 0,
    5, -5, -10, 0, 0, -10, -5, 5,
    5, 10, 10, -25, -25, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]

pawntableblack = reverse(pawntablewhite)

knighttablewhite = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -20, -30, -30, -20, -40, -50]

knighttableblack = reverse(knighttablewhite)

bishopstablewhite = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -20, -10, -40, -10, -10, -40, -10, -20]

bishopstableblack = reverse(bishopstablewhite)

rookstablewhite = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20]

rookstableblack = reverse(rookstablewhite)

queentablewhite = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20]

queentableblack = reverse(queentablewhite)

kingtablewhite = [
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, 20, 0, 0, 0, 0, 20, 20,
    20, 30, 10, 0, 0, 10, 30, 20]

kingtableblack = reverse(kingtablewhite)

kingtablewhiteEND = [
    -50, -40, -30, -20, -20, -30, -40, -50,
    -30, -20, -10, 0, 0, -10, -20, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -30, 0, 0, 0, 0, -30, -30,
    -50, -30, -30, -30, -30, -30, -30, -50]

kingtableblackEND = reverse(kingtablewhiteEND)


# Build a list with the positions of the given "pieces" on the "board"
def positions_of_pieces(pieces, board):
    result = []
    lst = list(pieces)
    for piece in lst:
        for pos in re.finditer(piece, board):
            result.append(pos.start())
    result.sort()
    return result


# Analyses 2 states of the board ("board" and "move") and checks if the "player" made a capture
def is_capture(board, move, player):
    if player == 0:
        oppontent_pieces_before = positions_of_pieces("abcdefghijklmnop", board)
        oppontent_pieces_after = positions_of_pieces("abcdefghijklmnop", move)
    else:
        oppontent_pieces_before = positions_of_pieces("IJKLMNOPABCDEFGH", board)
        oppontent_pieces_after = positions_of_pieces("IJKLMNOPABCDEFGH", move)

    if oppontent_pieces_after < oppontent_pieces_before:
        return True
    else:
        return False


def evaluate_board():
    global board, player

    # Counts how many of each piece the player has
    counter = Counter(board)
    wp = counter["I"] + counter["J"] + counter["K"] + counter["L"] + counter["M"] + counter["N"] + counter["O"] + \
         counter["P"]
    bp = counter["i"] + counter["j"] + counter["k"] + counter["l"] + counter["m"] + counter["n"] + counter["o"] + \
         counter["p"]
    wk = counter["B"] + counter["G"]
    bk = counter["b"] + counter["g"]
    wb = counter["C"] + counter["F"]
    bb = counter["c"] + counter["f"]
    wr = counter["A"] + counter["H"]
    br = counter["a"] + counter["h"]
    wq = counter["D"]
    bq = counter["d"]

    #   The material score is calculated by the summation of all respective piece’s weights multiplied
    # by the difference between the number of that respective piece between white and black.
    material = 100 * (wp - bp) + 320 * (wk - bk) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)

    #   The individual pieces score is the sum of piece-square values of positions where the respective
    # piece is present at that instance of the game.

    pawnsq = sum([pawntablewhite[pos] for pos in positions_of_pieces("IJKLMNOP", board)])
    pawnsq = pawnsq + sum([-pawntableblack[pos] for pos in positions_of_pieces("ijklmnop", board)])

    knightsq = sum([knighttablewhite[pos] for pos in positions_of_pieces("BG", board)])
    knightsq = knightsq + sum([-knighttableblack[pos] for pos in positions_of_pieces("bg", board)])

    bishopsq = sum([bishopstablewhite[pos] for pos in positions_of_pieces("CF", board)])
    bishopsq = bishopsq + sum([-bishopstableblack[pos] for pos in positions_of_pieces("cf", board)])

    rooksq = sum([rookstablewhite[pos] for pos in positions_of_pieces("AH", board)])
    rooksq = rooksq + sum([-rookstableblack[pos] for pos in positions_of_pieces("aH", board)])

    queensq = sum([queentablewhite[pos] for pos in positions_of_pieces("D", board)])
    queensq = queensq + sum([-queentableblack[pos] for pos in positions_of_pieces("d", board)])

    # In case of end game, we use a different piece-square table for the king (else case):
    if wp + (wk * 3) + (wb * 3) + (wr * 5) + (wq * 9) <= 13 and bp + (bk * 3) + (bb * 3) + (br * 5) + (bq * 9) <= 13:
        kingsq = sum([kingtablewhiteEND[pos] for pos in positions_of_pieces("E", board)])
        kingsq = kingsq + sum([-kingtableblackEND[pos] for pos in positions_of_pieces("e", board)])
    else:
        kingsq = sum([kingtablewhite[pos] for pos in positions_of_pieces("E", board)])
        kingsq = kingsq + sum([-kingtableblack[pos] for pos in positions_of_pieces("e", board)])

    #   It will return the summation of the material scores and the individual scores for white and when
    # it comes for black, let’s negate it.

    eval = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq

    if player == 0:
        return eval
    else:
        return -eval


#   Quiescence search, the purpose of this search is to only evaluate the positions where there are no winning
# tactical moves to be made.
#   This search is needed to avoid the horizon effect which is caused by the depth limitation of the search algorithm.
def quiesce(alpha, beta):
    global board, player

    stand_pat = evaluate_board()
    if stand_pat >= beta:
        return beta
    if alpha < stand_pat:
        alpha = stand_pat

    for move in sucessor_states(board, player):
        if is_capture(board, move, player):
            board = move
            score = -quiesce(-beta, -alpha)
            board = ""

            if score >= beta:
                return beta
            if score > alpha:
                alpha = score
    return alpha


#   Alpha-beta pruning for the optimization of our execution speed
# It eliminates most of the unnecessary iterations
def alphabeta(alpha, beta, depthleft):
    global board, player

    bestscore = -9999
    if depthleft == 0:
        return quiesce(alpha, beta)
    for move in sucessor_states(board, player):
        board = move
        score = -alphabeta(-beta, -alpha, depthleft - 1)
        board = ""
        if score >= beta:
            return score
        if score > bestscore:
            bestscore = score
        if score > alpha:
            alpha = score

    return bestscore

# Searches for the best move in a certain depth
def selectmove(depth):
    global board, player

    bestMove = ""
    bestValue = -99999
    alpha = -100000
    beta = 100000
    for move in sucessor_states(board, player):
        board = move
        boardValue = -alphabeta(-beta, -alpha, depth - 1)
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        if boardValue > alpha:
            alpha = boardValue
        board = ""
    return bestMove

# Given a board "state", it will calculate the best move possible for the "player"
def decide_move(state, player):
    global board
    board = state
    win_in_next_play = False
    depth = 3

    # If one of the next moves ends up in a win for me, then choose that move.
    moves = sucessor_states(board, player)
    for m in moves:
        if check_win(m) == player:
            win_in_next_play = True
            decided_move = m
            break

    # Else, search for the best move possible.
    if not win_in_next_play:
        decided_move = selectmove(depth)

    return decided_move


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # socket initialization
client.connect((sys.argv[1], int(sys.argv[2])))                 # connecting client to server

client.send(sys.argv[3].encode('ascii'))

player = int(sys.argv[4])

while True:                                                     # making valid connection
    while True:
        message = client.recv(1024).decode('ascii')
        if len(message) > 0:
            break

    if interactive_flag:
        row_from = int(input('Row from > '))
        col_from = int(input('Col from > '))
        row_to = int(input('Row to > '))
        col_to = int(input('Col to > '))

        p_from = pos2_to_pos1([row_from, col_from])
        p_to = pos2_to_pos1([row_to, col_to])

        if (0 <= p_from <= 63) and (0 <= p_to <= 63):
            message = list(message)
            aux = message[p_from]
            message[p_from] = 'z'
            message[p_to] = aux
            message = ''.join(message)
    else:
        message = decide_move(message, player)

    client.send(message.encode('ascii'))
