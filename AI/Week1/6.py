# In mathematics, primorial, denoted by “#”, is a function from natural numbers to
# natural numbers similar to the factorial function, but rather than successively
# multiplying positive integers, the function only multiplies prime numbers. Create
# a function that takes an integer n and returns its primorial.
# Example: primordial(2) = 6 (the product of the first two prime numbers)


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def primordial(n):
    p = 1
    for i in range(1, n + 1):
        if is_prime(i):
            p *= i
    return p


i = input("Number: ")
print("The primordial of " + i + " is " + str(primordial(int(i))))





