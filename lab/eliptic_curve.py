from random import randrange, getrandbits, randint
from krypto_utils import generate_prime_number, binpow, eulerTest, rnwd, sqrtZn
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

class Eliptic_Curve:
    def __init__(self, lenght=128):
        self.p = generate_prime_number(lenght)
        self.A, self.B = self.generate(self.p)
        self.k = 20
        
    def generate(self, p):
        flag = False
        while (flag != True):
            A = randint(2, p)
            B = randint(2, p)
            delta = (4 * binpow(A, 3, p)) % p + (27 * binpow(B, 2, p)) % p
            if delta != 0:
                flag = True
        return A, B
    
    def change_parameters(self, A, B, p):
        self.A = A
        self.B = B
        self.p = p
    
    def random_point(self):
        flag = False
        while (flag != True):
            x = randint(2, self.p)
            xd = x**3 + self.A * x + self.B
            if eulerTest(xd, self.p):
                y = binpow(xd, (self.p+1)//4, self.p)
                flag = True
        return Point(x, y)
    
    def check_point(self, P):
        if (P.y**2) % self.p == (P.x**3 + self.A * P.x + self.B) % self.p:
            return True
        else:
            return False
    
    def opposite_point(self, P):
        return Point(P.x, self.p - P.y)

    def add(self, P1, P2):
        if P2.x == float('inf') and P2.y == float('inf'):
            return Point(P1.x, P1.y)
        elif P1.x == float('inf') and P1.y == float('inf'):
            return Point(P2.x, P2.y)
        elif P1.x != P2.x:
            # u = rnwd(P1.x - P2.x, self.p)
            u = rnwd((P1.x - P2.x) % self.p, self.p)
            lambda_ = ((P1.y - P2.y) % self.p) * u
            # print(lambda_)
            xr = (lambda_ ** 2 - P1.x - P2.x) % self.p
            yr = (lambda_ * (P1.x - xr) - P1.y) % self.p
            return Point(xr, yr)
        elif P1.x == P2.x and P1.y == P2.y:
            u = rnwd(2*P1.y, self.p)
            lambda_ = (3*P1.x**2 + self.A) * u
            # print(lambda_)
            xr = (lambda_ ** 2 - P1.x - P2.x) % self.p
            return Point(xr, (lambda_ * (P1.x - (lambda_ ** 2 - P1.x - P2.x) % self.p) - P1.y) % self.p)
        else:
            return "Blad", "Blad"

    def calculate_nP(self, n, P):
        Q = P
        R = Point(float('inf'), float('inf'))   
        while(n > 0):
            if n % 2 == 1:
                # print("R", R)
                R = self.add(R, Q)
                n -= 1
            # print("Q", Q)
            Q = self.add(Q, Q)
            n = n//2
        return R
    
    def find_point_for_msg(self, M):
        flag = False
        x = self.k * M
        while (flag != True):
            # x = k * M
            y = sqrtZn(x**3 + self.A * x + self.B, self.p)
            if y != False:
                # print("y =", y)
                if self.check_point(Point(x, y)):
                    flag = True
                else:
                    x += 1
            else:
                x += 1
        return Point(x, y)

    
    def __repr__(self):
        return "A = {}\nB = {}\np = {}".format(self.A, self.B, self.p)

# print("Przykład 1")
# p = 68719476731
# A = 2645887931
# B = 63508942644
# x1 = 56174319723
# y1 = 50334202836
# x2 = 15593395299
# y2 = 42666859491
# P1 = Point(x1, y1)
# P2 = Point(x2, y2)

# E = Eliptic_Curve(128)
# E.change_parameters(A, B, p)
# print(E)

# P = E.add(P1, P2)
# print("P =", P)

# P = E.random_point()
# print("P =", P)

# P1 = E.random_point()
# print("P1 =", P1)

# check = E.check_point(P)
# print("check =", check)

# flip_P1 = E.opposite_point(P1)
# print("flip_P1 =", flip_P1)

# x = randint(2, p)
# print("x =", x)

# Q = E.calculate_nP(x, P)
# print("Q =", Q)

# p = 20769187434139310514121985316880223 #liczba pierwsza p = 3 (mod 4) mająca min. k bitów
# A = 17364248047998077729699720348015610
# B = 18961004445282423322533381916488735
# a1 = 2320240021928709874194025995780592
# a2 = 14799265073943436805126565754994838
# b1 = 12269447532190809160065009894517400
# b2 = 9983858041819674032650867073682761
# x = 18626391864564730346582943572556977
# P = Point(a1, a2)
# Q = Point(b1, b2)

# E = Eliptic_Curve(128)
# E.change_parameters(A, B, p)
# print(E)
# # print("P =", P)
# # print("Q =", Q)

# # # """Zaimplementuj algorytm, który oblicza wielokrotność punktu na krzywej eliptycznej"""
# # # # fifth step: (calculate Q = xP)
# Q = E.calculate_nP(x, P)
# print("Q =", Q)

# # public_key = (E, p, P, Q)
# # secret_key = (E, p, P, Q, x)


# # BOB: (ENCRIPTION)
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
# P_M = E.find_point_for_msg(M, k)
# print("P_M =", P_M)

