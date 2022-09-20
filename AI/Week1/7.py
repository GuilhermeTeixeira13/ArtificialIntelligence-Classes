# The number of rabbits banded at a series of sampling sites has been counted and
# entered into the following list. The first item in each sublist is an alphanumeric
# code for the site and the second value is the number of rabbits banded. Cut and
# paste the list into your assignment and then answer the following questions by
# printing them to the screen.
# data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
#   ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
#   ['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
#   ['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
#   ['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
#   ['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
#   ['D5', 98], ['D6', 32]]

# a. How many sites are there?
# b. How many rabbits were counted at the 7th site?
# c. How many rabbits were counted at the last site?
# d. What is the total number of rabbits counted across all sites?
# e. What is the average number of rabbits seen on a site?
# f. What is the total number of rabbits counted on sites with codes beginning with ‘C’?


data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
['D5', 98], ['D6', 32]]

totalRabbits = 0
rabbitsInSitesWithC = 0

for i in range(data.__len__()-1):
    totalRabbits += data[i][1]

for i in range(data.__len__()-1):
    if(data[i][0][0] == "C"):
        rabbitsInSitesWithC += data[i][1]


print("a) There are " + str(data.__len__()) + " sites.")
print("b) In the 7th site " + str(data[6][1]) + " rabbits were counted.")
print("c) " + str(data[data.__len__()-1][1]) + " rabbits were counted at the last site.")
print("d) The total number of rabbits is " + str(totalRabbits) + ".")
print("e) The avg number of rabbits on a site is " + str(totalRabbits / data.__len__()) + ".")
print("f) The number of rabbits counted on sites with codes beginning with ‘C’ is " + str(rabbitsInSitesWithC) + ".")
