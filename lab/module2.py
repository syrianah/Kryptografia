from eliptic_curve import Eliptic_Curve, Point


# Zad5
print("#Zad 5")
"""Zaimplementuj algorytm (funkcje), która oblicza P  Q sume punktów krzywej eliptycznych.
Zaimplementuj wszystkie przypadki."""

print("Przykład 1")
E = Eliptic_Curve(10)
p = 68719476731
A = 2645887931
B = 63508942644
x1 = 56174319723
y1 = 50334202836
x2 = 15593395299
y2 = 42666859491

E.change_parameters(A, B, p)

print("Wejście:")
print(E)
print("x1 =", x1)
print("y1 =", y1)
print("x2 =", x2)
print("y2 =", y2)
P1 = Point(x1, y1)
P2 = Point(x2, y2)
P = E.add(P1, P2)
# print(sum_points_in_elliptic_curve(A, B, p, x1, y1, x2, y2))
print("Wyjście:")
print(P)

# print("Przykład 2")
p = 68719476731
A = 20850939805
B = 59338401596
x1 = 3789244612
y1 = 16129056986
x2 = 3789244612
y2 = 52590419745

E.change_parameters(A, B, p)

print("Wejście:")
print(E)
print("x1 =", x1)
print("y1 =", y1)
print("x2 =", x2)
print("y2 =", y2)
P1 = Point(x1, y1)
P2 = Point(x2, y2)
P = E.add(P1, P2)
# print(sum_points_in_elliptic_curve(A, B, p, x1, y1, x2, y2))
print("Wyjście:")
print(P)


print("Przykład 3")
p = 68719476731
A = 49710749469
B = 5286130045
x1 = 24069898531
y1 = 10203122697
x2 = 24069898531
y2 = 10203122697
E.change_parameters(A, B, p)

print("Wejście:")
print(E)
print("x1 =", x1)
print("y1 =", y1)
print("x2 =", x2)
print("y2 =", y2)
P1 = Point(x1, y1)
P2 = Point(x2, y2)
P = E.add(P1, P2)
# print(sum_points_in_elliptic_curve(A, B, p, x1, y1, x2, y2))
print("Wyjście:")
print(P)
