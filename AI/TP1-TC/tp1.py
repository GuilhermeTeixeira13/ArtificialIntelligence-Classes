# The transactions will be stored in a 3D m
def read_transactions(lenTransactions, size):
    cubic_3d_matrix = [[[] for _ in range(size)] for _ in range(size)]
    for i in range(lenTransactions):
        transaction = list(str(input()).split(" "))
        cubic_3d_matrix[int(transaction[0]) - 1][int(transaction[2]) - 1].append(transaction[1])
    return cubic_3d_matrix


def ndfa_condition1(cubic_3d_matrix):
    line_content = []
    for line in range(len(cubic_3d_matrix)):
        for column in range(len(cubic_3d_matrix)):
            for char in cubic_3d_matrix[line][column]:
                if char in line_content:
                    return True
                else:
                    line_content.append(char)
        line_content.clear()
    return False


def ndfa_condition2(cubic_3d_matrix):
    for line in range(len(cubic_3d_matrix)):
        for column in range(len(cubic_3d_matrix)):
            if "_" in cubic_3d_matrix[line][column]:
                return True
    return False


def automata_ndfa(cubic_3d_matrix, lenS0):
    # Condition 1 -> For each input symbol, the transition can be to multiple next states.
    # Condition 2 -> There are empty string transitions
    # Condition 3 -> #S0 > 1

    condition_1 = ndfa_condition1(cubic_3d_matrix)
    condition_2 = ndfa_condition2(cubic_3d_matrix)
    condition_3 = True if lenS0 > 1 else False

    if condition_1 is True or condition_2 is True or condition_3 is True:
        print("NDFA")

    if condition_1 is False and condition_2 is False and condition_3 is False:
        print("DFA")


# Exists in line and not in visited
def goal_exists_in_line(cubic_3d_matrix, line, goal, visited):
    line_content = []
    for count, column in enumerate(cubic_3d_matrix[line - 1]):
        if goal in cubic_3d_matrix[line - 1][count]:
            if [line, count+1, cubic_3d_matrix[line - 1][count].index(goal)+1] not in visited:
                return True
    return False


def get_columns_of_goal(cubic_3d_matrix, line, goal, visited):
    columns_with_goals = []
    for count, column in enumerate(cubic_3d_matrix[line - 1]):
        if goal in column:
            if [line, count+1, column.index(goal)+1] not in visited:
                return count+1
    return -1


def recognizes_word(path, final):
    if path[-1] in final:
        print("YES")
    else:
        print("NO")


def print_path(path):
    for i in range(len(path_to_string)-1):
        print(path[i], end=" ")
    print(path[-1])


def find_path(cubic_3d_matrix, word, s0):
    string_path = [s0[0]]
    word_char_pos = 0
    current_goal = word[word_char_pos]
    current_node = s0[0]
    visited = []
    current_word = ""

    while True:
        line = current_node
        if goal_exists_in_line(cubic_3d_matrix, line, current_goal, visited):
            current_word += current_goal
            current_node = get_columns_of_goal(cubic_3d_matrix, line, current_goal, visited)
            string_path.append(current_node)
            if current_word == word:
                break
            else:
                word_char_pos += 1
                if current_goal != word[word_char_pos]:
                    visited = []
                    current_goal = word[word_char_pos]
                else:
                    visited.append([line, current_node, cubic_3d_matrix[line-1][current_node-1].index(current_goal)+1])
        else:
            if goal_exists_in_line(cubic_3d_matrix, line, "_", visited):
                current_node = get_columns_of_goal(cubic_3d_matrix, line, "_", visited)
                string_path.append(current_node)
                visited.append([line, current_node, cubic_3d_matrix[line-1][current_node-1].index("_")+1])
            else:
                string_path = []
                break

    return string_path


# Main

# Read Input
S = int(input())
lenS0 = int(input())
S0 = list(map(int, str(input()).split(" ")))
lenF = int(input())
F = list(map(int, str(input()).split(" ")))
lenTransactions = int(input())
mtx = read_transactions(lenTransactions, S)
word = str(input())

automata_ndfa(mtx, lenS0) # Output 1
path_to_string = find_path(mtx, word, S0)
recognizes_word(path_to_string, F)  # Output 2
print_path(path_to_string)

