from random import randrange, getrandbits, randint


def rnwd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


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


def fermat_test(n, k=124):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    for _ in range(k):
        a = randint(1, n-1)
        if binpow(a, n-1, n) != 1:
            return False
    return True


def eulerTest(a, p): return True if binpow(a, (p-1)//2, p) == 1 else False


def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length=128):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    flag = False
    # keep generating while the primality test fail
    while flag != True:
        p = generate_prime_candidate(length)
        if fermat_test(p):
            if p % 4 == 3:
                flag = True
    return p


def generate_elliptic_curve(p):
    flag = False
    while (flag != True):
        A = randint(2, p)
        B = randint(2, p)
        delta = (4 * binpow(A, 3, p)) % p + (27 * binpow(B, 2, p)) % p
        if delta != 0:
            flag = True
    return A, B, delta


def random_point_elliptic_curve(A, B, p):
    flag = False
    while (flag != True):
        x = randint(2, p)
        xd = x**3 + A * x + B
        if eulerTest(xd, p):
            y = binpow(xd, (p+1)//4, p)
            flag = True
    return x, y


def check_point_in_elliptic_curve(A, B, p, x, y):
    if (y**2) % p == (x**3 + A * x + B) % p:
        return True
    else:
        return False


def opposite_point_in_elliptic_curve(x, y, p):
    return x, p - y


# def sum_points_in_elliptic_curve(A, B, p, x1, y1, x2, y2):
#     if x1 != x2:
#         print("x1 != x2")
#         d, u, v = rnwd(x1 - x2, p)
#         print("u =", u)
#         lambda_ = ((y1 - y2) % p) * u
#         print("lambda =", lambda_)
#         return (lambda_ ** 2 - x1 - x2) % p, (lambda_ * (x1 - (lambda_ ** 2 - x1 - x2) % p) - y1) % p
#     elif x1 == x2 and y1 == y2:
#         print("x1 == x2 and y1 == y2")
#         d, u, v = rnwd(2*y1, p)
#         lambda_ = (3*x1**2 + A) * u
#         return (lambda_ ** 2 - x1 - x2) % p, (lambda_ * (x1 - (lambda_ ** 2 - x1 - x2) % p) - y1) % p
#     elif x1 == x2 and y1 == p-y2:
#         print("x1 == x2 and y1 == -y2")
#         return float('inf'), float('inf')
#     elif x2 == float('inf') and y2 == float('inf'):
#         print("x2 == float('inf') and y2 == float('inf')")
#         return x1, y1
#     else:
#         return "Blad", "Blad"

def sum_points_in_elliptic_curve(A, B, p, P1, P2):
    x1 = P1[0]
    y1 = P1[1]
    x2 = P2[0]
    y2 = P2[1]
    if x1 != x2:
        # print("x1 != x2")
        d, u, v = rnwd(x1 - x2, p)
        # print("u =", u)
        lambda_ = ((y1 - y2) % p) * u
        print("lambda =", lambda_)
        return (lambda_ ** 2 - x1 - x2) % p, (lambda_ * (x1 - (lambda_ ** 2 - x1 - x2) % p) - y1) % p
    elif x1 == x2 and y1 == y2:
        # print("x1 == x2 and y1 == y2")
        d, u, v = rnwd(2*y1, p)
        lambda_ = (3*x1**2 + A) * u
        return (lambda_ ** 2 - x1 - x2) % p, (lambda_ * (x1 - (lambda_ ** 2 - x1 - x2) % p) - y1) % p
    elif x1 == x2 and y1 == p-y2:
        # print("x1 == x2 and y1 == -y2")
        return float('inf'), float('inf')
    elif x2 == float('inf') and y2 == float('inf'):
        # print("x2 == float('inf') and y2 == float('inf')")
        return x1, y1
    else:
        return "Blad", "Blad"

# Moduł drugi
# Zad1
print("#Zad 1")
"""Zaimplementuj algorytm (funkcję), która generuje losową krzywą eliptyczną nad F_p."""
# p = generate_prime_candidate(300)
p = 68719476731
print("Wejście:")
print("p =", p)
A, B, delta = generate_elliptic_curve(p)
print("Wyjście:")
print(f"y^2 = x^3 + Ax + B")
print("A =", A)
print("B =", B)
print("delta =", delta)

# Zad2
print("#Zad 2")
"""Zaimplementuj algorytm (funkcje), który znajduje losowy punkt na krzywej eliptycznej
nad Fp."""
p = 68719476731
A = 49710749469
B = 5286130045
print("Wejście:")
print("p =", p)
# A, B, delta = generate_elliptic_curve(p)
print("A =", A)
print("B =", B)
x, y = random_point_elliptic_curve(A, B, p)
print("Wyjście:")
print("x =", x)
print("y =", y)

# Zad3
print("#Zad 3")
"""Zaimplementuj algorytm (funkcje), który sprawdza czy punkt nalezy do krzywej."""
# p = generate_prime_candidate(300)
# A, B, delta = generate_elliptic_curve(p)
# x, y = random_point_elliptic_curve(A, B, p)
# print("Wejście:")
# print("p =", p)
# print("A =", A)
# print("B =", B)
# print("x =", x)
# print("y =", y)
# print("Wyjście:")
# print(check_point_in_elliptic_curve(A, B, p, x, y))

print("Przykład 1")
p = 68719476731
A = 49710749469
B = 5286130045
x = 12520181851
y = 51057687062
print("Wejście:")
print("p =", p)
print("A =", A)
print("B =", B)
print("x =", x)
print("y =", y)
print("Wyjście:")
print(check_point_in_elliptic_curve(A, B, p, x, y))

print("Przykład 2")
p = 68719476731
A = 49710749469
B = 5286130045
x = 12520181851
y = 51057687000
print("Wejście:")
print("p =", p)
print("A =", A)
print("B =", B)
print("x =", x)
print("y =", y)
print("Wyjście:")
print(check_point_in_elliptic_curve(A, B, p, x, y))

print("Przykład 3")
p = 83076749736557242056487941267521467
A = 51966339240643817679159456819110758
B = 69222991666392733393816378184919461
x = 3907170373
y = 4656627897
print("Wejście:")
print("A =", A)
print("B =", B)
print("p =", p)
print("x =", x)
print("y =", y)
print("Wyjście:")
print(check_point_in_elliptic_curve(A, B, p, x, y))

# Zad4
print("#Zad 4")
"""Zaimplementuj algorytm (funkcje), który oblicza punkt przeciwny do danego punktu."""
print("Przykład 1")
x = 2
y = 3
p = 5
print("Wejście:")
print("x =", x)
print("y =", y)
print("p =", p)

print("Wyjście:")
x1, y1 = opposite_point_in_elliptic_curve(x, y, p)
print("x1 =", x1)
print("y1 =", y1)

# Zad5
print("#Zad 5")
"""Zaimplementuj algorytm (funkcje), która oblicza P  Q sume punktów krzywej eliptycznych.
Zaimplementuj wszystkie przypadki."""

print("Przykład 1")
p = 68719476731
A = 2645887931
B = 63508942644
x1 = 56174319723
y1 = 50334202836
x2 = 15593395299
y2 = 42666859491
print("Wejście:")
print("A =", A)
print("B =", B)
print("p =", p)
print("x1 =", x1)
print("y1 =", y1)
print("x2 =", x2)
print("y2 =", y2)
P1 = (x1, y1)
P2 = (x2, y2)
x3, y3 = sum_points_in_elliptic_curve(A, B, p, P1, P2)
# print(sum_points_in_elliptic_curve(A, B, p, x1, y1, x2, y2))
print("Wyjście:")
print("x3 =", x3)
print("y3 =", y3)

print("Przykład 2")
p = 68719476731
A = 20850939805
B = 59338401596
x1 = 3789244612
y1 = 16129056986
x2 = 3789244612
y2 = 52590419745
print("Wejście:")
print("A =", A)
print("B =", B)
print("p =", p)
print("x1 =", x1)
print("y1 =", y1)
print("x2 =", x2)
print("y2 =", y2)

P1 = (x1, y1)
P2 = (x2, y2)
x3, y3 = sum_points_in_elliptic_curve(A, B, p, P1, P2)
# x3, y3 = sum_points_in_elliptic_curve(A, B, p, x1, y1, x2, y2)
# print(sum_points_in_elliptic_curve(A, B, p, x1, y1, x2, y2))
print("Wyjście:")
print("x3 =", x3)
print("y3 =", y3)

print("Przykład 3")
p = 68719476731
A = 49710749469
B = 5286130045
x1 = 24069898531
y1 = 10203122697
x2 = 24069898531
y2 = 10203122697
print("Wejście:")
print("A =", A)
print("B =", B)
print("p =", p)
print("x1 =", x1)
print("y1 =", y1)
print("x2 =", x2)
print("y2 =", y2)

P1 = (x1, y1)
P2 = (x2, y2)
x3, y3 = sum_points_in_elliptic_curve(A, B, p, P1, P2)
# x3, y3 = sum_points_in_elliptic_curve(A, B, p, x1, y1, x2, y2)
# print(sum_points_in_elliptic_curve(A, B, p, x1, y1, x2, y2))
print("Wyjście:")
print("x3 =", x3)
print("y3 =", y3)
