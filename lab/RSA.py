from random import randrange, getrandbits, randint


def rnwd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def nwd(a, b):
    while b != 0:
        gcd = b
        b = a % b
        a = gcd
    return gcd


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
            flag = True
    return p


def rsa_generate_primes(lenght=128):
    p = generate_prime_number(lenght)
    flag = False
    while flag != True:
        q = generate_prime_number(lenght)
        if p != q:
            flag = True
    return p, q


def find_e(n):
    flag = False
    while flag != True:
        e = randint(2, n-1)
        if nwd(e, n) == 1:
            flag = True
    return e

def encode_msg(M):
    mybytes = M.encode('utf-8')
    myint = int.from_bytes(mybytes, 'little')
    return myint

def decode_msg(myint):
    recoveredbytes = myint.to_bytes((myint.bit_length() + 7) // 8, 'little')
    recoveredstring = recoveredbytes.decode('utf-8')
    return recoveredstring


# Alice: (GENERATE KEYS)
print("GENERATE KEYS")
# first step (generate prime numbers p, q, p != q)
p, q = rsa_generate_primes(128)
print("q =", q)
print("p =", p)

# second step: (Calculate n = pq oraz φ(n) = (p - 1)(q - 1))
n = p * q
phi = (p - 1) * (q - 1)
print("n =", n)
print("phi =", phi)

# third step: (random int e < φ(n), (e, φ(n)) = 1)
e = find_e(phi)
print("e =", e)

# fourth step: (Calculate d, ed = 1 (mod φ(n)))
x, d, v = rnwd(e, phi)
print("d =", d)

# fifth step: (public key)
public_key = (n, e)
# print("public_key(p, g, y) =", public_key)

# sixth setp: (secret key)
secret_key = (n, d)
# print("secret_key(p, x) =", secret_key)


# BOB: (ENCRIPTION)
print("ENCRIPTION")
# first step: (Download Alicia public key)
# second step: (establishes M, 0 <= M < n)
M = 12341242353465
# M = randint(2, n - 1)
# print("M =", M)
# msg = "Wojtek ążźćś∑ę∑ęń©†ķ†ī¨ī†ę®†īķę¨Ż® TO SUPER GOSC 19222007"
# print("msg =", msg)
# M = encode_msg(msg)
# print("M =", M)

# decode test
# decode_M = decode_msg(M)
# print("decode_M =", decode_M)

# third step: (C = M^e (mod n))
C = binpow(M, e, n)
print("C =", C)

# ALICE: (DECRIPTION)
print("DECRIPTION")
alice_M = binpow(C, d, n)
print("alice decripted", alice_M)
