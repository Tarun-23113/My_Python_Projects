from math import e, factorial
import numpy as np

fac = np.vectorize(factorial)

def mac(x, terms):
    n = np.arange(terms)
    return np.sum((x ** n) / fac(n))

e_x = e ** 5

print("Maclaurin Terms Summation \t\t Error")

for i in range(1, 20):
    maclaurin = mac(5, i)
    error = e_x - maclaurin
    print(f"{maclaurin:.5f} \t\t\t\t {error:.4f}")