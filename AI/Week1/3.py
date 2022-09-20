# Create a function that takes a string and returns a string in which each character is
# repeated once (example: "String" ➞ "SSttrriinngg")

def x2(quote):
    for c in quote:
        print(c+c, end="")


q = input("Quote: ")
x2(q)
