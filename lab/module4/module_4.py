class F_256:
    def __init__(self, x):
        self.x_hex = x
        self.x_int = int(x, 16)

    def __repr__(self):
        return self.x_hex

    def __add__(self, other):
        return F_256(hex(self.x_int ^ other.x_int))

    def xtime(self):
        ans = int(bin(self.x_int << 1).replace('0b', '')[-8:], 2)
        if self.x_int & (1<<7):
            ans = ans ^ int('0x1B', 16)
        return F_256(hex(ans))

    def __mul__(self, other):
        y_prim = other.x_int >> 1
        if not y_prim:
            return F_256(hex(self.x_int))
        if other.x_int & 1:
            return self.xtime() * F_256(hex(y_prim)) + self 
        else:
            return self.xtime() * F_256(hex(y_prim))

    def inverse(self):
        ans = self
        for _ in range(253):
            ans = self * ans
        return ans


# Zad 1 
print("Zad 1")

# Przykład 1
a = F_256("0xa3")
b = F_256("0xf2")
suma = a + b
print(f"{a} + {b} = {suma}")

# Przykład 2
a = F_256("0x03")
b = F_256("0x1f")
suma = a + b
print(f"{a} + {b} = {suma}")

print("-----------------")
# Zad 2
print("Zad 2")

# Przykład 1
a = F_256("0x32")
x_time = a.xtime()
print(f"{a} * {a} = {x_time}")

# Przykład 2
a = F_256("0xff")
x_time = a.xtime()
print(f"{a} * {a} = {x_time}")

# Przykład 3
a = F_256("0xbc")
x_time = a.xtime()
print(f"{a} * {a} = {x_time}")

print("-----------------")
# Zad 3
print("Zad 3")

# Przykład 1
a = F_256("0xff")
b = F_256("0xe1")
ab = a * b
print(f"{a} * {b} = {ab}")

# Przykład 2
a = F_256("0x02")
b = F_256("0x08")
ab = a * b
print(f"{a} * {b} = {ab}")

print("-----------------")
# Zad 4
print("Zad 4")

# Przykład 1
a = F_256("0x03")
print(f"inv({a}) = {a.inverse()}")

# Przykład 2
a = F_256("0xf0")
print(f"inv({a}) = {a.inverse()}")

# Przykład 3
a = F_256("0x00")
print(f"inv({a}) = {a.inverse()}")

print("-----------------")

