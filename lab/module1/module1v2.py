# Zadania z Kryptografi i algebry
# Wojciech Kubiak
import random


def nwd(a, b): return nwd(b, a % b) if b else a


def rnwd(a, b):
    if a == 0:
        return (b, 0, 1)
    d, u, v = rnwd(b % a, a)
    return (d, v - (b//a) * u, u)

def binpow(x, k, n):
    k_binary = f"{k:b}"
    length = len(k_binary) - 1
    index = 0
    tmp = 1

    while length >= 0:
        tmp = tmp * tmp % n
        if str(k_binary)[index] == str(1):
            tmp = (tmp*x) % n
        index += 1
        length = length - 1

    return tmp


def power(x, y, n):
    number = 1
    while y > 0:
        if y & 1:
            number = number * x % n
        x = x * x % n
        y >>= 1
    return number


def eulerTest(a, p): return True if binpow(a, (p-1)//2, p) == 1 else False
def eulerPrinter(b): return "b jest resztą kwadratową" if b == True else "b nie jest resztą kwadratową"

def sqrtZn(a, p): return binpow(a, (p+1)//4, p) if eulerTest(a, p) else "b nie jest resztą kwadratową"


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

b = 646364623469634716329421551581459444393459634563465364563456387456873465873645876345876345876345876345876345863458763458763485763485763487563845638465837465834658765735646345645856346875
k = 7268263486823646238468236462384682364586385634856834658634586348658365873645874658734658736458763875638475683765834658346586856348756873465863456
n = 943923749729479745795479759798579759734597345979578937597359739587398573985793875983759834759735973459873459734985739857359793573598734975983745983745973495734957394579347593847593759734597345973497349857394759347593745934793475973459734957394759374597349573457934759347597345973459734957394579379579579374597359735975173



print("****************************MODUŁ Iv2***************************")
# Moduł pierwszy
# Zad1
print("#Zad 1")
"""Zaimplementuj algorytm (funkcje), która generuje losowy element zbioru Zn."""
# k = 4
# z = random.getrandbits(k)
# print(f"random int DEC: {z}\nrandom int BIN: {bin(z)}")


# Zad 2
print("#Zad 2")
"""Zaimplementuj algorytm (funkcje) obliczania odwrotnosci w grupie (n). Wykorzystaj
Rozszerzony Algorytm Euklidesa."""
# b = 10
# n = 13
d, u, v = rnwd(b, n)
# print(f"{b} * u + {n} * v = {d}")
# print(f"{b} * {u} + {n} * {v} = {d}")
print(u)
# if d == 1:
#     z = d * 1/b % n
#     print(f"d / b % n = z")
#     print(f"{d} / {b} % {n} = {z}")

# Zad 3
print("#Zad 3")
"""Zaimplementuj algorytm (funkcje) efektywnego potegowania w zbiorze Zn. Wykorzystaj
algorytm iterowanego podnoszenia do kwadratu."""
print(f"x^y % n")
# print(f"{b}^{k} % {n} = {binpow(b, k, n)}")
print(binpow(b, k, n))

# Zad 4
print("#Zad 4")
"""Zaimplementuj test (funkcje), który sprawdza czy element zbioru Zn jest reszta kwadratowa
w Zn. Wykorzystaj twierdzenie Eulera."""
print("(a/p)")
print(f"({n}/{b})")
print(eulerPrinter(eulerTest(n, b)))

# Zad 5
print("#Zad 5")
"""Zaimplementuj algorytm (funkcje), który oblicza pierwiastek kwadratowy w ciele Fp, gdzie
p = 3 (mod 4) jest liczba pierwsza. Wykorzystaj twierdzenie Eulera."""
a = k
p = n
print(sqrtZn(a, p))
# if eulerTest(a, p):
#     print(f"sqrt({a}) = {binpow(a, (p+1)//4, p)}")

# Zad 6
print("#Zad 6")
"""Zaimplementuj test (funkcje), który sprawdza liczba naturalna n jest liczba pierwsza.
Wykorzystaj test Fermata"""
# is_prime = 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151
# is_prime = 2**201 - 381
is_prime = 133444136156678048003218652526286524805322674621386947435537173756495733557013079001888514670571159376826503948779174849325928635423621116645450612116058736061371074003956266893556385889746286979961099241372058781936649225181224643221184156022909004513659896344970075206959029524174675524137348380879567794107
# is_prime = n
print(f"fermat_test({is_prime})")
print(fermat_test(is_prime))

print("****************************MODUŁ Iv2***************************")