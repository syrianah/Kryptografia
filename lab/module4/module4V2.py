from bitarray import bitarray

def hex_to_bin(my_hex):

    scale = 16 ## equals to hexadecimal

    num_of_bits = 8

    return bin(int(my_hex, scale))[2:].zfill(num_of_bits)

def bin_to_hex(my_bin):
    return hex(int(my_bin, 2))[2:]

test = "e5"
test_bin = hex_to_bin(test)
test_hex = bin_to_hex(test_bin)
print("test_bin =", test_bin)
print("test_hex =", test_hex)



# Zad 1 
print("Zad 1")
"""Zaimplementuj funkcje suma()"""
# def suma(a, b):
#     return hex(a ^ b)

# def suma1(a, b):
#     return hex(int(hex_to_bin(a), 2) ^ int(hex_to_bin(b), 2))

# def suma(a, b):
    # return hex(int(xor(hex_to_bin(a), hex_to_bin(b), len(hex_to_bin(a))), 2))[2:]

# def suma(a, b):
    # return bin_to_hex(xor(hex_to_bin(a), hex_to_bin(b), len(hex_to_bin(a))))

def suma(a, b):
    a_bin = bitarray.util.hex2ba(a)
    print(a_bin)
    # a_bin = bitarray(hex_to_bin(a))
    # b_bin = bitarray(hex_to_bin(b))
    # return ba2hex(a_bin ^ b_bin)
    # return bin_to_hex(xor(hex_to_bin(a), hex_to_bin(b), len(hex_to_bin(a))))
# Przykład 1

a = "a3"
b = "f2"
print("a ^ b =", suma(a, b))

# # Przykład 2
a = "03"
b = "1f"
print("a ^ b =", suma(a, b))


# # Zad 2
print("Zad 2")
"""Zaimplementuj funkcje xtime()"""

# def xtime(a):
#     a = hex_to_bin(a)
    
#     if (a[0] == "0"):
#         return hex(int(a, 2)<<1)[2:]
#     elif (a[0] != 0):
#         xd = hex_to_bin(hex(int(a, 2)<<1))[1:9]
#         print(xd)
#         print(a)
#         # return hex(int(xor(xd, hex_to_bin("1B"), len(xd)), 2))[2:]
#         return bin_to_hex(xor(xd, hex_to_bin("1B"), len(xd)))
        


# # Przykład 1
# a = "32"
# print("xa =", xtime(a))

# # Przykład 2
# a = "ff"
# print("xa =", xtime(a))

# # Przykład 3
# a = "bc"
# print("xa =", xtime(a))

# # Zad 3
# print("Zad 3")
# """Zaimplementuj funkcje iloczyn()"""

# def iloczyn(x, y):
#     y_bin = hex_to_bin(y)
#     y_prim = hex_to_bin(hex(int(y_bin, 2)<<1))[1:9]
#     print(x, y, bin_to_hex(y_prim))
#     # y_prim = "00000001"
#     if y_prim == "00000000" or y_prim == "00000001":
#         return hex(x)[2:] 
#     if (y_bin[0] == "0"):
#         print(xtime(x))
#         iloczyn(xtime(x), bin_to_hex(y_prim))
#         # return hex(iloczyn(xtime(x), hex(y_prim)[2:]))[2:]
#     elif (y_bin[0] == "1"):
#         print(xtime(x))
#         return suma(iloczyn(xtime(x), bin_to_hex(y_prim)), x)
#         # return int(xtime(x), 16) * int(y_prim, 2)
#         # print(hex_to_bin(hex(xd)))
#         # return xor(hex_to_bin(xd), y_prim, len(hex_to_bin(hex(xd))))
#         # return hex(suma(iloczyn(xtime(x), hex(y_prim)[2:]), x))[2:]

# # Przykład 1
# a = "ff"
# b = "e1"
# print("a * b =", iloczyn(a, b))



