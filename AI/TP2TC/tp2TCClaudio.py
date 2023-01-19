def read_rules(num_rules):
    rules_mtx = []
    for i in range(num_rules):
        line = list(str(input()).split(" "))
        line.remove("->")
        rules_mtx.append([line[0], ''.join(line[1::])])
    return rules_mtx


def create_triangular_mtx(size):
    return [[[] for _ in range(i+1)] for i in range(size)]


def fill_cell(mtx, l, c, production_result, rules):
    for rule in rules:
        if production_result in rule[1] and rule[0] not in mtx[l][c]:
            mtx[l][c].append(rule[0])


def cartesian_product(l1, l2):
    return [i+str(j) for i in l1 for j in l2]


def get_submatrix(matrix, line, column):
    return [row[column:column+i+1] for i,row in enumerate(matrix[line:])]


def solve(w, rules):
    mtx = create_triangular_mtx(len(w))
    n = len(w)

    # Resolve a primeira linha
    for c in range(0, n):
        fill_cell(mtx, n-1, c, w[c], rules)

    # Line --> Mtx.len() - 1 até 0
    for line in range(n-2, -1, -1):
        # Column --> 0 até line-1
        for col in range(0, line+1):
            submatrix = get_submatrix(mtx, line, col)
            #print("Submatrix -> "+str(submatrix))
            for k in range(1, len(submatrix)):
                #print(mtx)
                #print("Prod -> "+str(submatrix[k][0]) + " X " + str(submatrix[len(submatrix)-k][len(submatrix)-k]))
                prod = cartesian_product(submatrix[k][0], submatrix[len(submatrix)-k][len(submatrix)-k])
                for element in prod:
                    fill_cell(mtx, line, col, element, rules)

    # Print mtx
    #print(mtx)


word_to_recognize = str(input())
m = int(input())
r = read_rules(m)
solve(word_to_recognize, r)

