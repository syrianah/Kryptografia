from eliptic_curve import Eliptic_Curve, Point
from random import randint
from krypto_utils import encode_msg, decode_msg

# Zad 1
print("Zad 1")
"""Zaimplementuj algorytm generowania kluczy kryptosystemu ElGamala na krzywej elip-tycznej."""
print("Przykład 1")
# p = 20769187434139310514121985316880223 #liczba pierwsza p = 3 (mod 4) mająca min. k bitów
# A = 17364248047998077729699720348015610
# B = 18961004445282423322533381916488735
# a1 = 2320240021928709874194025995780592
# a2 = 14799265073943436805126565754994838
# b1 = 12269447532190809160065009894517400
# b2 = 9983858041819674032650867073682761
# n = 18626391864564730346582943572556977

# P = Point(a1, a2)

Alice_E = Eliptic_Curve()
# Alice_E.change_parameters(A, B, p)
print(Alice_E)
P = Alice_E.random_point()
print("P =", P)

n = randint(2, Alice_E.p + 1 - (2 * Alice_E.p **(1/2)))

Q = Alice_E.calculate_nP(n, P)
print("Q =", Q)

print(Alice_E.check_point(Q))

print("Zad 2")
print("Przykład 1")
p = 1019
A = 159
B = 342
a1 = 53
a2 = 635
b1 = 492
b2 = 941
n = 250
P = Point(a1, a2)

Alice_E = Eliptic_Curve()
Alice_E.change_parameters(A, B, p)
print(Alice_E)
# P = Alice_E.random_point()
print("P =", P)

Q = Alice_E.calculate_nP(n, P)
print("Q =", Q)
print(Alice_E.check_point(Q))

# Zad 2
print("Przykład 2")
p = 11 #liczba na wejściu przystaje do 3 mod 4
A = 3
B = 5
x = 0
y = 4
n = 4

P = Point(x, y)

E = Eliptic_Curve()
E.change_parameters(A, B, p)
Q = E.calculate_nP(n, P)
print(E)
print(Q)

print("Przykład 3")
p = 251 
A = 61 
B = 81
x = 222 
y = 23
n = 81

P = Point(x, y)

E = Eliptic_Curve()
E.change_parameters(A, B, p)
Q = E.calculate_nP(n, P)
print(E)
print(Q)

print("Przykład 4")
p = 1298074214633706907132624082305003
A = 228534005990621198360294597781867
B = 569902189632523536847978118572132
x = 149381772199891494705202718572565
y = 409260229456564272828054179242535
n = 1298074214633706907132624082305000
P = Point(x, y)

E = Eliptic_Curve()
E.change_parameters(A, B, p)
Q = E.calculate_nP(n, P)
print(E)
print(Q)

# Zad 3
print("Zad 3")
print("Przykład 1")
p = 20769187434139310514121985316880223
A = 17364248047998077729699720348015610
B = 18961004445282423322533381916488735
m = 8250681875682716001970051

E = Eliptic_Curve()
E.change_parameters(A, B, p)
PM = E.find_point_for_msg(m)
print(PM)

print("Przykład 2")
p = 20769187434139310514121985316880223
A = 17364248047998077729699720348015610
B = 18961004445282423322533381916488735
m = 97

E = Eliptic_Curve()
E.change_parameters(A, B, p)
PM = E.find_point_for_msg(m)
print(PM)

print("Przykład 3")
p = 1019
A = 159
B = 342
m = 10

E = Eliptic_Curve()
E.change_parameters(A, B, p)
PM = E.find_point_for_msg(m)
print(PM)

print("Przykład 4")
E = Eliptic_Curve()
msg = "Wojciech Kubiak"
M = encode_msg(msg)
print(M)
PM = E.find_point_for_msg(M)
print(PM)

# # Zad 4
print("Zad 4")
print("Przykład 1")
p = 20769187434139310514121985316880223
A = 17364248047998077729699720348015610
B = 18961004445282423322533381916488735
a1 = 2320240021928709874194025995780592
a2 = 14799265073943436805126565754994838
b1 = 12269447532190809160065009894517400
b2 = 9983858041819674032650867073682761
PM1 = 165013637513654320039401020
PM2 = 5273216427742214302796987051820376
y = 18626391864564730346582943572556977

P = Point(a1, a2)
Q = Point(b1, b2)
PM = Point(PM1, PM2)
print("PM =", PM)

E.change_parameters(A, B, p)
C1 = E.calculate_nP(y, P)
print("C_1 =", C1)

# sixth step: (calculate C_2 = PM xor yQ)
yQ = E.calculate_nP(y, Q)
# print("yQ =", yQ)
C2 = E.add(PM, yQ)
print("C2 =", C2)


print("Przykład 2")
p = 1019
A = 159
B = 342
a1 = 53
a2 = 635
b1 = 492
b2 = 941
n = 126
PM1 = 201
PM2 = 135

P = Point(a1, a2)
Q = Point(b1, b2)
PM = Point(PM1, PM2)

E.change_parameters(A, B, p)
# y = randint(2, E.p + 1 - (2 * E.p**(1/2)))
# y = randint(2, p)
print("y =", n)
C1 = E.calculate_nP(n, P)
print("C_1 =", C1)

# # sixth step: (calculate C_2 = PM xor yQ)
yQ = E.calculate_nP(n, Q)
print("yQ =", yQ)
# C2 = E.add(yQ, PM)
print("C2 =", C2)

# # Zad 5
# print("Zad 5")
# print("Przykład 1")
# p = 20769187434139310514121985316880223
# A = 17364248047998077729699720348015610
# B = 18961004445282423322533381916488735
# a1 = 2320240021928709874194025995780592
# a2 = 14799265073943436805126565754994838
# n = 18626391864564730346582943572556977
# C1x = 7461171280232618252346248166047239
# C1y = 9848579285671294043158700804581973
# C2x = 20556666266534045717211983269903004
# C2y = 7124954620676015317017867433690102

# P = Point(a1, a2)
# Q = Point(b1, b2)
# C1 = Point(C1x, C1y)
# C2 = Point(C2x, C2y)

# E.change_parameters(A, B, p)
# print(E)

# xC1 = E.calculate_nP(n, C1)
# flip_xC1 = E.opposite_point(C1)
# Alice_PM = E.add(C2, flip_xC1)
# print("Alice_PM =", Alice_PM)
# Alice_M = Alice_PM.x // 20
# print("Alice_M =", Alice_M)

# print("Przykład 2")
# p = 1019
# A = 159
# B = 342
# a1 = 53
# a2 = 635
# n = 250
# C1x = 884
# C1y = 411
# C2x = 615
# C2y = 996

# P = Point(a1, a2)
# # Q = Point(b1, b2)
# C1 = Point(C1x, C1y)
# C2 = Point(C2x, C2y)

# E.change_parameters(A, B, p)

# xC1 = E.calculate_nP(n, C1)
# flip_xC1 = E.opposite_point(xC1)
# Alice_PM = E.add(C2, flip_xC1)
# print("Alice_PM =", Alice_PM)
# Alice_M = Alice_PM.x // 20
# print("Alice_M =", Alice_M)