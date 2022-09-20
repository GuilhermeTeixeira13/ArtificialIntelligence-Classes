from tabulate import tabulate


def readFile(fileName):
    fileObj = open(fileName, "r")
    data = []
    lines = fileObj.readlines()
    for line in lines:
        data.append(line.split(", "))
    fileObj.close()
    return data


data = readFile("data.txt")
table = []
sum = 0

for animal in data:
    id = animal[0]
    GCContent = (animal[2].count("C") + animal[2].count("G")) / animal[2].__len__() * 100
    sum += GCContent
    if float(animal[1]) > 10:
        size = "large"
    else:
        size = "small"
    table.append([id, size, str(round(GCContent, 2))+"%"])

print(tabulate(table))
print("The average GC Content is -> " + str(round(sum/data.__len__(), 2))+ "%.")