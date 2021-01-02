from random import randrange, getrandbits, randint


def nwd(a, b): return nwd(b, a % b) if b else a

def rnwd(a, b):
    # print(a)
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return x


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

def encode_msg(M):
    mybytes = M.encode('utf-8')
    myint = int.from_bytes(mybytes, 'little')
    return myint

def decode_msg(myint):
    recoveredbytes = myint.to_bytes((myint.bit_length() + 7) // 8, 'little')
    recoveredstring = recoveredbytes.decode('utf-8')
    return recoveredstring

