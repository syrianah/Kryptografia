from eliptic_curve import Eliptic_Curve, Point
from random import randint
from krypto_utils import encode_msg, decode_msg


# Zad 1
# ALICE: (GENERATE KEYS)
print("ALICE: (GENERATE KEYS)")
Alice_E = Eliptic_Curve()
# Alice_E.change_parameters(A, B, p)
print(Alice_E)
P = Alice_E.random_point()
print("P =", P)

x = randint(2, Alice_E.p + 1 - (2 * Alice_E.p **(1/2)))
print("x =", x)
Q = Alice_E.calculate_nP(x, P)
print("Q =", Q)

print("-------------------------")


# BOB: (ENCRIPTION)
# first step: # second step: (encode msg to int)
print("BOB: (ENCRIPTION)")
send = "Wojtek Kubiak!"
print("msg =", send)
M = encode_msg(send)
print("M =", M)
# M = 123123762487612745612734563441234234

# second step: (Download Alicia public key)
# third step: (coding message M on point PM in eliptic curve)
Bob_E = Eliptic_Curve()
Bob_E.change_parameters(Alice_E.A, Alice_E.B, Alice_E.p)
PM = Bob_E.find_point_for_msg(M)
print("PM =", PM)

# fourth step: (random y in N,  y < #E(Fp)=> #E(Fp) >= p + 1 - 2sqrt(p))
y = randint(2, Alice_E.p + 1 - (2 * Alice_E.p**(1/2)))
print("y =", y)

# fifth step: (calculate C_1 = yP)
C1 = Bob_E.calculate_nP(y, P)
print("C_1 =", C1)

# sixth step: (calculate C_2 = PM xor yQ)
yQ = Bob_E.calculate_nP(y, Q)
print("yQ =", yQ)
C2 = Bob_E.add(PM, yQ)
print("C2 =", C2)
print("-------------------------")

# seventh step: (send C = (C_1, C_2) to Alice)
# C = (C1, C2)

# ALICE: (DECRIPTION)
# first step: (calculate PM = C_2 + xC1 -> przeciwny)

print("ALICE: (DECRIPTION)")
xC1 = Alice_E.calculate_nP(x, C1)
flip_xC1 = Alice_E.opposite_point(xC1)
Alice_PM = Alice_E.add(C2, flip_xC1)
print("Alice_PM =", Alice_PM)
print("k =", Alice_E.k)
Alice_M = Alice_PM.x // Alice_E.k
print("Alice_M =", Alice_M)
recive = decode_msg(Alice_M)
print(recive)
print("-------------------------")
