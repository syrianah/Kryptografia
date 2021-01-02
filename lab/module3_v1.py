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

def sqrtZn(a, p): return binpow(a, (p+1)//4, p) if eulerTest(a, p) else False


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


def sum_points_in_elliptic_curve(A, B, p, P1, P2):
    x1, y1 = P1
    x2, y2 = P2
    if x2 == float('inf') and y2 == float('inf'):
        # print("x2 == float('inf') and y2 == float('inf')")
        return x1, y1
    elif x1 == float('inf') and y1 == float('inf'):
        return x2, y2
    elif x1 != x2:
        # print("x1 != x2")
        # print("ADD")
        d, u, v = rnwd(x1 - x2, p)
        # print("u =", u)
        lambda_ = ((y1 - y2) % p) * u
        # print("lambda =", lambda_)
        return (lambda_ ** 2 - x1 - x2) % p, (lambda_ * (x1 - (lambda_ ** 2 - x1 - x2) % p) - y1) % p
    elif x1 == x2 and y1 == y2:
        # print("DOUBLE")
        # print("x1 == x2 and y1 == y2")
        d, u, v = rnwd(2*y1, p)
        lambda_ = (3*x1**2 + A) * u
        return (lambda_ ** 2 - x1 - x2) % p, (lambda_ * (x1 - (lambda_ ** 2 - x1 - x2) % p) - y1) % p
    elif x1 == x2 and y1 == p-y2:
        # print("x1 == x2 and y1 == -y2")
        return float('inf'), float('inf')
    else:
        return "Blad", "Blad"

# Zad 2
# wielokrotność punktu na krzywej eliptycznej
def calculate_nP(A, B, p, n, P):
    Q = P
    R = [0, 0]    
    while(n > 0):
        if n % 2 == 1:
             R = sum_points_in_elliptic_curve(A, B, p, R, Q)
             n -= 1
        Q = sum_points_in_elliptic_curve(A, B, p, Q, Q)
        n = n//2
    return R

def encode_msg(M):
    mybytes = M.encode('utf-8')
    myint = int.from_bytes(mybytes, 'little')
    return myint

def decode_msg(myint):
    recoveredbytes = myint.to_bytes((myint.bit_length() + 7) // 8, 'little')
    recoveredstring = recoveredbytes.decode('utf-8')
    return recoveredstring

def find_point_for_msg(A, B, p, M, k=20):
    flag = False
    x = k * M
    while (flag != True):
        # x = k * M
        y = sqrtZn(x**3 + A * x + B, p)
        if y != False:
            # print("y =", y)
            if check_point_in_elliptic_curve(A, B, p, x, y):
                flag = True
            else:
                x += 1
        else:
            x += 1
    return x, y



# def calculate_nP(A, B, p, n, P):
#     if n == 0: 
#         return float('inf'), float('inf')
#     elif n == 1: 
#         return P
#     elif n % 2 == 0:
#         return sum_points_in_elliptic_curve(A, B, p, calculate_nP(A, B, p, n/2, P), calculate_nP(A, B, p, n/2, P))
#     elif n % 2 != 0:
#         xd = sum_points_in_elliptic_curve(A, B, p, P, calculate_nP(A, B, p, n//2, P))
#         return sum_points_in_elliptic_curve(A, B, p, xd, calculate_nP(A, B, p, n//2, P))



# Kryptosystem ElGamala on eliptic curve E/Fp

"""Zaimplementuj algorytm generowania kluczy kryptosystemu ElGamala na krzywej elip-tycznej."""
# # ALICE: (GENERATE KEYS)
print("ALICE: (GENERATE KEYS)")
# # first step: (generate prime number and establishes Fp)
# p = generate_prime_number(128)
# # p = 20769187434139310514121985316880223
# print("p =", p)

# # second step (random eliptic curve)
# A, B, delta = generate_elliptic_curve(p)
# E = (A, B)
# print("E =", E)
# # print("A =", A)
# # print("B =", B)

# # third step: (random point on eliptic curve)
# P = random_point_elliptic_curve(A, B, p)
# print(f"P = ({P[0]},{P[1]})")

# # fourth step: (random x in N, x < #E(Fp)=> #E(Fp) >= p + 1 - 2sqrt(p))
# x = randint(2, p + 1 - (2 * p**(1/2)))
# print("x =", x)



# M = "Wojtek ążźćś∑ę∑ęń©†ķ†ī¨ī†ę®†īķę¨Ż® TO SUPER GOSC 19222007"
# mybytes = M.encode('utf-8')
# myint = int.from_bytes(mybytes, 'little')
# print(myint)

# recoveredbytes = myint.to_bytes((myint.bit_length() + 7) // 8, 'little')
# recoveredstring = recoveredbytes.decode('utf-8')
# print(recoveredstring)

p = 20769187434139310514121985316880223 #liczba pierwsza p = 3 (mod 4) mająca min. k bitów
A = 17364248047998077729699720348015610
B = 18961004445282423322533381916488735
a1 = 2320240021928709874194025995780592
a2 = 14799265073943436805126565754994838
b1 = 12269447532190809160065009894517400
b2 = 9983858041819674032650867073682761
x = 18626391864564730346582943572556977

p = 1019
A = 159
B = 342
a1 = 53
a2 = 635
b1 = 492
b2 = 941
x = 250

p = 11 #liczba na wejściu przystaje do 3 mod 4
A = 3
B = 5
x = 0
y = 4
x = 4

P = (a1, a2)
Q = (b1, b2)

# # """Zaimplementuj algorytm, który oblicza wielokrotność punktu na krzywej eliptycznej"""
# # # fifth step: (calculate Q = xP)
Q = calculate_nP(A, B, p, x, P)
print("Q =", Q)

# public_key = (E, p, P, Q)
# secret_key = (E, p, P, Q, x)


# BOB: (ENCRIPTION)
# print("BOB: (ENCRIPTION)")
# # first step: # second step: (encode msg to int)
# msg = "Wojtek"
# print("msg =", msg)
# M = encode_msg(msg)
# print("M =", M)

# # decode test
# # decode_M = decode_msg(M)
# # print("decode_M =", decode_M)


# # second step: (Download Alicia public key)
# # third step: (coding message M on point P_M in eliptic curve)
# k = 20
# P_M = find_point_for_msg(A, B, p, M, k)
# print("P_M =", P_M)

# # fourth step: (random y in N,  y < #E(Fp)=> #E(Fp) >= p + 1 - 2sqrt(p))
# y = randint(2, p + 1 - (2 * p**(1/2)))
# print("y =", y)

# # # fifth step: (calculate C_1 = yP)
# # # C1 = calculate_nP(y, P)
# C1 = calculate_nP(A, B, p, y, P)
# print("C_1 =", C1)

# # # sixth step: (calculate C_2 = P_M xor yQ)
# yQ = calculate_nP(A, B, p,y, Q)
# print("yQ =", yQ)
# C2 = sum_points_in_elliptic_curve(A, B, p, P_M, yQ)
# print("C2 =", C2)

# # # seventh step: (send C = (C_1, C_2) to Alice)
# # C = (C1, C2)

# # # ALICE (DECRIPTION)
# # # first step: (calculate P_M = C_2 + xC1 -> przeciwny)
# xC1 = calculate_nP(A, B, p,x, C1)
# flip_xC1 = opposite_point_in_elliptic_curve(xC1[0], xC1[1], p)
# Alice_P_M = sum_points_in_elliptic_curve(A, B, p, C2, flip_xC1)
# print("Alice_P_M =", Alice_P_M)
# Alice_M = Alice_P_M[0] // k
# print("Alice_M =", Alice_M)

