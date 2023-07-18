import numpy as np


def math():
    a = int(input("Enter 1st integer for arithmetic results: "))
    b = int(input("Enter 2nd integer for arithmetic results: "))

    c = a + b
    d = a - b
    e = a * b
    f = a / b
    g = a % b
    h = np.log(a**a)
    i = a**b

    print(f"The sum of the 2 numbers is: {c}")
    print(f"The result of subtracting a from b is: {d}")
    print(f"The product of the two integers is: {e}")
    print(f"The result of dividing a by b is: {f}")
    print(f"The remainder of a divided by b is: {g}")
    print(f"The base 10 logarithm of a is :{h}")
    print(f"The result of integer a raised to b is: {i}")


math()
