# Zadania z Kryptografi i algebry
# Wojciech Kubiak
import random


def nwd(a, b): return nwd(b, a % b) if b else a


def rnwd(a, b):
    if a == 0:
        return (b, 0, 1)
    d, u, v = rnwd(b % a, a)
    return (d, v - (b//a) * u, u)

# def binpow(x, k, n):
#     k_binary = f"{k:b}"
#     length = len(k_binary) - 1
#     index = 0
#     tmp = 1

#     while length >= 0:
#         tmp = tmp * tmp % n
#         if str(k_binary)[index] == str(1):
#             tmp = (tmp*x) % n
#         index += 1
#         length = length - 1

#     return tmp


def binpow(a, b, n):
    if (b == 0):
        return 1
    res = binpow(a, b // 2, n)
    if (b % 2):
        return res * res * a % n
    else:
        return res * res % n


def power(x, y, n):
    number = 1
    while y > 0:
        if y & 1:
            number = number * x % n
        x = x * x % n
        y >>= 1
    return number


def eulerTest(a, p): return True if binpow(a, (p-1)/2, p) == 1 else False
def eulerTest2(a, p): return True if power(a, (p-1)/2, p) == 1 else False


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


print("****************************MODUŁ I***************************")
# Moduł pierwszy
# Zad1
print("#Zad 1")
"""Zaimplementuj algorytm (funkcje), która generuje losowy element zbioru Zn."""
k = 4
z = random.getrandbits(k)
print(f"random int DEC: {z}\nrandom int BIN: {bin(z)}")


# Zad 2
print("#Zad 2")
"""Zaimplementuj algorytm (funkcje) obliczania odwrotnosci w grupie (n). Wykorzystaj
Rozszerzony Algorytm Euklidesa."""
b = 10
n = 13
d, u, v = rnwd(10, 13)
print(f"{b} * u + {n} * v = {d}")
print(f"{b} * {u} + {n} * {v} = {d}")
if d == 1:
    z = d / b % n
    print(f"d / b % n = z")
    print(f"{d} / {b} % {n} = {z}")

# Zad 3
print("#Zad 3")
"""Zaimplementuj algorytm (funkcje) efektywnego potegowania w zbiorze Zn. Wykorzystaj
algorytm iterowanego podnoszenia do kwadratu."""
x = 10
y = 23
n = 2345
# x = 73423553452345345423562562456345324
# y = 43534523542134
# n = 45362344234242344235223
print(f"x^y % n")
print(f"{x}^{y} % {n} = {binpow(x, y, n)}")
# print(f"{x}^{y} % {n} = {binpow2(x, y, n)}")
print(f"{x}^{y} % {n} = {power(x, y, n)}")

# Zad 4
print("#Zad 4")
"""Zaimplementuj test (funkcje), który sprawdza czy element zbioru Zn jest reszta kwadratowa
w Zn. Wykorzystaj twierdzenie Eulera."""
a = 3
p = 13
print("(a/p)")
print(f"({a}/{p})")
print(eulerTest(a, p))
# print(eulerTest2(a, p))

# Zad 5
print("#Zad 5")
"""Zaimplementuj algorytm (funkcje), który oblicza pierwiastek kwadratowy w ciele Fp, gdzie
p = 3 (mod 4) jest liczba pierwsza. Wykorzystaj twierdzenie Eulera."""
a = 81
p = 19
if eulerTest(a, p):
    print(f"sqrt({a}) = {binpow(a, (p+1)/4, p)}")

# Zad 6
print("#Zad 6")
"""Zaimplementuj test (funkcje), który sprawdza liczba naturalna n jest liczba pierwsza.
Wykorzystaj test Fermata"""
# is_prime = 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151
# is_prime = 943923749729479745795479759798579759734597345979578937597359739587398573985793875983759834759735973459873459734985739857359793573598734975983745983745973495734957394579347593847593759734597345973497349857394759347593745934793475973459734957394759374597349573457934759347597345973459734957394579379579579374597359735975173
# is_prime = 2**201 - 381
# is_prime = 13
# print(f"fermat_test({is_prime})")
# print(fermat_test(is_prime))

print("****************************MODUŁ I***************************")

# zadanie ćwiczenia
for i in range(2, 13):
    print(f"7^{i} mod 13 =", binpow(7, i, 13))
