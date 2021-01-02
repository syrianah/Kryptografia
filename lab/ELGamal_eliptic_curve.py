from eliptic_curve import Eliptic_Curve, Point
from random import randint
from krypto_utils import encode_msg, decode_msg


# Zad 1
# ALICE: (GENERATE KEYS)
print("ALICE: (GENERATE KEYS)")
"""Zaimplementuj algorytm generowania kluczy kryptosystemu ElGamala na krzywej elip-tycznej."""
print("Przykład 1 - k = 100 #liczba bitów - mniejsza od 300")
print("Wyjście: ")

p = 20769187434139310514121985316880223 #liczba pierwsza p = 3 (mod 4) mająca min. k bitów
A = 17364248047998077729699720348015610
B = 18961004445282423322533381916488735
a1 = 2320240021928709874194025995780592
a2 = 14799265073943436805126565754994838
b1 = 12269447532190809160065009894517400
b2 = 9983858041819674032650867073682761
x = 18626391864564730346582943572556977
P = Point(a1, a2)
# Q = Point(b1, b2)

# p = 20769187434139310514121985316880223
# A = 17364248047998077729699720348015610
# B = 18961004445282423322533381916488735
# M = 8250681875682716001970051

# P = Point(x, y)

k = 400
Alice_E = Eliptic_Curve(k)
# Alice_E.change_parameters(A, B, p)
print(Alice_E)
P = Alice_E.random_point()
print("P =", P)

# # P1 = Point(17697479122247354229660308415633294, 17218480641539757828321077779303303)
# # P2 = Point(2320240021928709874194025995780592, 14799265073943436805126565754994838)

# # print(Alice_E.add(P1, P2))
x = randint(2, Alice_E.p + 1 - (2 * Alice_E.p **(1/2)))
# # x = randint(2, Alice_E.p)
# # print("x =", x)
Q = Alice_E.calculate_nP(x, P)
print("Q =", Q)

print("-------------------------")

# x1 = Alice_E.add(Point(float('inf'), float('inf')) , P)
# print(x1)
# x2 = Alice_E.add(x1, P)
# print(x2)
# x3 = Alice_E.add(x2, P)
# print(x3)

# xd = Alice_E.check_point(Q)
# print(xd)

# # BOB: (ENCRIPTION)
# # first step: # second step: (encode msg to int)
# # print("BOB: (ENCRIPTION)")
# send = "Wojtek"
# print("msg =", send)
# M = encode_msg(send)
# print("M =", M)
M = 123123762487612745612734563441234234

# # second step: (Download Alicia public key)
# # third step: (coding message M on point PM in eliptic curve)
Bob_E = Eliptic_Curve()
Bob_E.change_parameters(Alice_E.A, Alice_E.B, Alice_E.p)
# # Bob_E.change_parameters(A, B, p)
PM = Bob_E.find_point_for_msg(M)
print("PM =", PM)

# # fourth step: (random y in N,  y < #E(Fp)=> #E(Fp) >= p + 1 - 2sqrt(p))
y = randint(2, Alice_E.p + 1 - (2 * Alice_E.p**(1/2)))
print("y =", y)

# # fifth step: (calculate C_1 = yP)
C1 = Bob_E.calculate_nP(y, P)
print("C_1 =", C1)

# # sixth step: (calculate C_2 = PM xor yQ)
yQ = Bob_E.calculate_nP(y, Q)
print("yQ =", yQ)
C2 = Bob_E.add(PM, yQ)
print("C2 =", C2)

# # seventh step: (send C = (C_1, C_2) to Alice)
# # C = (C1, C2)

# # # ALICE (DECRIPTION)
# # # first step: (calculate PM = C_2 + xC1 -> przeciwny)

# p = 20769187434139310514121985316880223
# A = 17364248047998077729699720348015610
# B = 18961004445282423322533381916488735
# PM1 = 165013637513654320039401020
# PM2 = 5273216427742214302796987051820376

Alice_E.change_parameters(A, B, p)
xC1 = Alice_E.calculate_nP(x, C1)
flip_xC1 = Alice_E.opposite_point(C1)
Alice_PM = Alice_E.add(C2, flip_xC1)
print("Alice_PM =", Alice_PM)
Alice_M = Alice_PM.x // 20
print("Alice_M =", Alice_M)
# recive = decode_msg(Alice_M)
