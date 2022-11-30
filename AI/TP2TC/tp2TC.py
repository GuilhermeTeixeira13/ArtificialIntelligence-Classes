def read_rules(numRules):
    mtx = []
    for i in range(numRules):
        line = list(str(input()).split(" "))
        line.remove("->")
        mtx.append([line[0], line[1::]])
    return mtx


def create_matrix(size):
    return [[[] for _ in range(size)] for _ in range(size)]


def fill_cell(mtx, mtx_size, l, c, state_son, rules):
    for r in rules:
        #print("state_son -> "+str(state_son))

        #state_son_list = list(state_son)
        r1S = ''.join(r[1])

        print("state_son -> "+str(state_son))
        print("r[0] -> " + str(r[0]))
        print("r1S -> " + str(r1S))
        print(state_son in r1S)
        print(r[0] not in mtx[mtx_size-l-1][c])

        if state_son in r1S and r[0] not in mtx[mtx_size-l-1][c]:
            mtx[mtx_size - l - 1][c].append(r[0])

def extract_k_length_substrings(str, K):
    return [str[i: j] for i in range(len(str)) for j in range(i + 1, len(str) + 1) if len(str[i:j]) == K]


def cartesian_product(l1, l2):
    return [i+str(j) for i in l1 for j in l2]


def split_string(str):
    size = len(str)
    res = []
    for i in range(1, size):
        res.append([str[:i], str[i:]])

    return res

def search_for_str_generators(mtx, mtx_size, s, w):
    print("["+str((mtx_size-(len(s)-1))-1)+"]"+"["+str((extract_k_length_substrings(w, len(s)).index(s)))+"]")
    return mtx[mtx_size-(len(s)-1)-1][extract_k_length_substrings(w, len(s)).index(s)]


def solve(w, rules):
    mtx = create_matrix(len(w))
    n = len(w)

    print("regras-> "+str(rules))

    for c in range(0, n):
        fill_cell(mtx, n, 0, c, w[c], rules)

    for l in range(n-2, -1, -1):
        print("l = "+str(l))
        sub_words = extract_k_length_substrings(w, n-l)
        print("sub_words = "+str(sub_words))
        for pos, word in enumerate(sub_words):
            sub_sub_word = split_string(word)

            for sub_sub_sub_word in sub_sub_word:
                print("sub_sub_sub_word = " + str(sub_sub_sub_word))
                l1 = search_for_str_generators(mtx, n, sub_sub_sub_word[0], w)
                l2 = search_for_str_generators(mtx, n, sub_sub_sub_word[1], w)

                cart = cartesian_product(l1, l2)

                print("l1 = " + str(l1))
                print("l2 = " + str(l2))
                print("cart = " + str(cart))

                for element in cart:
                    print("inserir em ["+str(n - l - 1)+"]["+str(pos)+"]")
                    fill_cell(mtx, n, n - l - 1, pos, element, rules)
                    print(mtx)
        print("------------------")
    print(mtx)


print(split_string("ab"))
w = str(input())
m = int(input())
rules = read_rules(m)
solve(w, rules)

#print(rules)
#print(extract_k_length_substrings(w, 2))
#print(cartesian_product(["A","B"], ["C"]))
#print(split_every_k_char(w, 2))