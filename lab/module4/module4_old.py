# Zad 1 
print("Zad 1")
"""Zaimplementuj funkcje suma()"""


def suma(a, b):
    return hex(int(a, 16) ^ int(b, 16))

# Przykład 1

a = "0xa3"
b = "0xf2"
print("suma() =", suma(a, b))

# Przykład 2
a = "0x03"
b = "0x1f"
print("suma() =", suma(a, b))


# Zad 2
print("Zad 2")
"""Zaimplementuj funkcje xtime()"""

def xtime(a):
    a = int(a, 16)
    ans = int(bin(a << 1).replace('0b', '')[-8:], 2)
    if a & (1<<7):
        ans = ans ^ int('0x1B', 16)
    return hex(ans)


# Przykład 1
a = "0x32"
print("xtime() =", xtime(a))

# Przykład 2
a = "0xff"
print("xtime() =", xtime(a))

# Przykład 3
a = "0xbc"
print("xtime() =", xtime(a))

# Zad 3
print("Zad 3")
"""Zaimplementuj funkcje iloczyn()"""
        

def iloczyn(x, y):
    x_int = int(x, 16)
    y_int = int(y, 16)
    y_prim = y_int >> 1
    if not y_prim:
        return hex(x_int)
    if y_int & 1:
        return suma(iloczyn(xtime(hex(x_int)), hex(y_prim)), hex(x_int))
    else:
        return iloczyn(xtime(hex(x_int)), hex(y_prim))

# Przykład 1
a = "0xff"
b = "0xe1"
print("iloczyn() =", iloczyn(a, b))

# Przykład 2
a = "0x02"
b = "0x08"
print("iloczyn() =", iloczyn(a, b))

# Zad 4
print("Zad 4")
"""Zaimplementuj funkcje odwrotnosc()"""

def odwrotnosc(x):
    ans = x
    for _ in range(253):
        ans = iloczyn(x, ans)
    return ans

# Przykład 1
a = "0x03"
print("odwrotnosc() =", odwrotnosc(a))

a = "0xf0"
print("odwrotnosc() =", odwrotnosc(a))

a = "0x00"
print("odwrotnosc() =", odwrotnosc(a))




