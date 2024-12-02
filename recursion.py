#Assignment 13

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(5, 10))


def compareTo(s1, s2):
    if not s1 or not s2:
        return 0
    elif not s1:
        return -1
    elif not s2:
        return 1
    elif s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])

print(compareTo("dog", "cat"))

