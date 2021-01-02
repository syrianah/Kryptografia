# Zadania z Kryptografi i algebry moduł1
# Wojciech Kubiak
import random


def nwd(a, b): return nwd(b, a % b) if b else a


def rnwd(a, b):
    if a == 0:
        return (b, 0, 1)
    d, u, v = rnwd(b % a, a)
    return (d, v - (b//a) * u, u)


def binpow(a, b, n):
    if (b == 0):
        return 1
    res = binpow(a, b // 2, n)
    if (b % 2):
        return res * res * a % n
    else:
        return res * res % n


def eulerTest(a, p): return True if binpow(a, (p-1)//2, p) == 1 else False


def eulerPrinter(
    b): return "b jest resztą kwadratową" if b == True else "b nie jest resztą kwadratową"


def sqrtZn(a, p): return binpow(a, (p+1)//4, p) if eulerTest(a,
                                                             p) else "b nie jest resztą kwadratową"


def fermat_test(n):
    k = 1000

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(1, n-1)
        if binpow(a, n-1, n) != 1:
            return False
    return True


print("****************************MODUŁ Iv3***************************")
# Moduł pierwszy
# Zad1
print("#Zad 1")
"""Zaimplementuj algorytm (funkcje), która generuje losowy element zbioru Zn."""
# k = 4
z = random.getrandbits(10)
print(f"random int DEC: {z}\nrandom int BIN: {bin(z)}")
z = random.getrandbits(20)
print(f"random int DEC: {z}\nrandom int BIN: {bin(z)}")


# Zad 2
print("#Zad 2")
"""Zaimplementuj algorytm (funkcje) obliczania odwrotnosci w grupie (n). Wykorzystaj
Rozszerzony Algorytm Euklidesa."""
n = 2**30 - 5
b = 3
d, u, v = rnwd(b, n)
print(u)
n = 54321
b = 100
d, u, v = rnwd(b, n)
print(u)

# Zad 3
print("#Zad 3")
"""Zaimplementuj algorytm (funkcje) efektywnego potegowania w zbiorze Zn. Wykorzystaj
algorytm iterowanego podnoszenia do kwadratu."""
b = 3
k = 2**30
n = 2**100 - 1
print(f"x^y % n")
print(f"{b}^{k} % {n} = {binpow(b, k, n)}")
b = 10
k = 3**39 + 1
n = 2**62 + 10
print(f"x^y % n")
print(f"{b}^{k} % {n} = {binpow(b, k, n)}")
n = 186**58
b = 229


# Zad 4
print("#Zad 4")
"""Zaimplementuj test (funkcje), który sprawdza czy element zbioru Zn jest reszta kwadratowa
w Zn. Wykorzystaj twierdzenie Eulera."""
n = 2**(201) - 313
b = 2
print(eulerPrinter(eulerTest(b, n)))
n = 2**(201) - 313
b = 3
print(eulerPrinter(eulerTest(b, n)))
n = 2**33 - 9
b = 11
print(eulerPrinter(eulerTest(b, n)))
n = 2**33 - 9
b = 10
print(eulerPrinter(eulerTest(b, n)))
n = 132**58
b = 10
print(eulerPrinter(eulerTest(b, n)))

# Zad 5
print("#Zad 5")
"""Zaimplementuj algorytm (funkcje), który oblicza pierwiastek kwadratowy w ciele Fp, gdzie
p = 3 (mod 4) jest liczba pierwsza. Wykorzystaj twierdzenie Eulera."""
a = 2
p = 2**(201) - 313
print(sqrtZn(a, p))
a = 3
p = 2**(201) - 313
print(sqrtZn(a, p))
a = 11
p = 2**33 - 9
print(sqrtZn(a, p))
a = 10
p = 2**33 - 9
print(sqrtZn(a, p))

# Zad 6
print("#Zad 6")
"""Zaimplementuj test (funkcje), który sprawdza liczba naturalna n jest liczba pierwsza.
Wykorzystaj test Fermata"""
is_prime = 2**201 - 313
print(fermat_test(is_prime))
is_prime = 2**201 - 323
print(fermat_test(is_prime))
is_prime = 2**33 - 9
print(fermat_test(is_prime))
is_prime = 2**33 - 21
print(fermat_test(is_prime))

print("****************************MODUŁ Iv3***************************")


# print(binpow(176, 104, 229))

# print(binpow(218, -58, 229))
print(176*104 % 229)
d, u, v = rnwd(218, 229)
print(u)

print(binpow(3, 990, 101))
# print(176*104%229)
d, u, v = rnwd(3, 101)
print(u)

print(2*13 % 13)
