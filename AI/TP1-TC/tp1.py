# The transactions will be stored in a 3D m
def read_transactions(size):
    cubic_3d_matrix = [[[] for _ in range(S)] for _ in range(S)]
    for i in range(lenTransactions):
        transaction = list(str(input()).split(" "))
        cubic_3d_matrix[int(transaction[0]) - 1][int(transaction[2]) - 1].append(transaction[1])
    return cubic_3d_matrix


def automata_ndfa(cubic_3d_matrix):
    line_content = []
    ndfa = False

    for line in range(len(cubic_3d_matrix)):
        for column in range(len(cubic_3d_matrix)):
            for char in cubic_3d_matrix[line][column]:
                if char in line_content:
                    ndfa = True
                else:
                    line_content.append(char)
        line_content.clear()

    print("NDFA") if ndfa else print("DFA")


def goal_exists_in_line(cubic_3d_matrix, line, goal):
    line_content = []
    for column in range(len(cubic_3d_matrix)):
        for char in cubic_3d_matrix[line - 1][column]:
            line_content.append(char)

    if goal in line_content:
        return True
    else:
        return False


def get_columns_of_goal(cubic_3d_matrix, line, goal, visited):
    columns_with_goals = []
    for count, column in enumerate(cubic_3d_matrix[line - 1]):
        if goal in column:
            if [line, column, column.index(goal)] not in visited:
                columns_with_goals.append(count)
    return columns_with_goals


def find_path(cubic_3d_matrix, word, s0):
    path_to_string = [s0[0]]
    word_char_pos = 0
    current_goal = word[word_char_pos]
    current_node = s0[0]
    visited = []
    current_word = ""
    goal_columns = []

    while True:
        line = current_node
        if goal_exists_in_line(cubic_3d_matrix, line, current_goal):
            current_word += current_goal
            goal_columns = get_columns_of_goal(cubic_3d_matrix, line, current_node, visited)


# Main

# Read Input
S = int(input())
lenS0 = int(input())
S0 = list(map(int, str(input()).split(" ")))
lenF = int(input())
F = list(map(int, str(input()).split(" ")))
lenTransactions = int(input())
mtx = read_transactions(S)
word = str(input())

# Checks if automata is NDFA or DFA and prints it
automata_ndfa(mtx)

# path = path()
# reconhcepath() - print YES or NO
# print(path)
