#  Create a function that takes two numbers as arguments (num, length) and returns an
#  array of multiples of num until the array length reaches length.
#  Example: (7, 5) ➞ [7, 14, 21, 28, 35].

def multiples(num, length):
    multiples = []
    for i in range(length):
        multiples.append(num * (i+1));
    return multiples


n, l = input("num, lenght: ").split()
print(multiples(int(n), int(l)))
