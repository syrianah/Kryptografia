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


def generate_prime_number(length=256):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    flag = False
    # keep generating while the primality test fail
    while flag != True:
        q = generate_prime_candidate(length)
        if fermat_test(q):
            p = 2 * q + 1
            if fermat_test(p):
                flag = True
    return (q, p)


def find_generator(q, p):
    flag = False
    while flag != True:
        g = randint(2, p-1)
        if binpow(g, q, p) != 1:
            flag = True
    return g

def encode_msg(M):
    mybytes = M.encode('utf-8')
    myint = int.from_bytes(mybytes, 'little')
    return myint

def decode_msg(myint):
    recoveredbytes = myint.to_bytes((myint.bit_length() + 7) // 8, 'little')
    recoveredstring = recoveredbytes.decode('utf-8')
    return recoveredstring


# ALICE: (GENERATE KEYS)
print("GENERATE KEYS")
# first step: (generate prime number)
# Tested for 2048 but on such big number my rnwd dont work
q, p = generate_prime_number(128)
print("q =", q)
print("p =", p)

# # second step: (find generotor g in group Φ(p) )
g = find_generator(q, p)
print("g =", g)

# # third step: (random int from set 1<x<p-1)
x = randint(2, p-1)
print("x =", x)

# # fourth step: (calculate y = g^x (mod p))
y = binpow(g, x, p)
print("y =", y)

# fifth step: (public key)
public_key = (p, g, y)
# print("public_key(p, g, y) =", public_key)

# sixth setp: (secret key)
secret_key = (p, x)
# print("secret_key(p, x) =", secret_key)

# q = 171918138062919341097818716480985477201
# p = 343836276125838682195637432961970954403
# g = 22917347527634472474800209226765895314
# x = 303854515363691106028318602112927752384
# y = 248523585035908345222158887885946108283

# BOB: (ENCRIPTION)
print("ENCRIPTION")
# first step: (download Alice public key)
# alice_key = public_key
# print("alice_key =", alice_key)
# second step: (establishes M, 0 <= M < p)
# M = randint(0, p)
# M = randint(2, p - 1)
# M = 34567845433453453245645676453745645362345623453453426345623456235623656245363452341234564745678567
# print("M =", M)
msg = "Wojtek"
print("msg =", msg)
M = encode_msg(msg)
print("M =", M)

# decode test
# decode_M = decode_msg(M)
# print("decode_M =", decode_M)

# print("M % p =", M % p)
# third step: (random int 1 < z < p-1)
z = randint(2, p-1)
print("z =", z)

# fourth step: (calculate c1 = g^z(mod p))
c1 = binpow(g, z, p)
print("c1 =", c1)

# fifth step: (calculate c2 = My^z(mod p))
c2 = (M * binpow(y, z, p)) % p
print("c2 =", c2)

# sixth step: (Send cryptogram)
cryptogram = (c1, c2)
# print("cryptogram =", cryptogram)

# ALICE: (DECRIPTION)
print("DECRIPTION")
d, u, v = rnwd(binpow(c1, x, p), p)
print("u =", u)
alice_M = (c2 * u) % p
# alice_M = (c2 * c1 ** -x) % p
print("M =", alice_M)
decode_M = decode_msg(alice_M)
print("decode_M =", decode_M)
