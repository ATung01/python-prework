value = 9.22 - 1.1 # value is 8.12, or is it?
d = 3.32
result = value - d # result is 4.8, or is it?
print(result)
print(value)

a_int = 200             # this is an int
b_int = 2               # this is an int
sum = a_int / b_int     # sum is a float
print(sum)              # 100.0
print(type(sum))        # <class `float`>

a_float = 200.0         # this is an float
b_float = 2.0           # this is an float
sum = a_float / b_float # sum is a float
print(sum)              # 100.0
print(type(sum))        # <class `float`>

# all integers
a_int = 200
b_int = 3
sum = a_int // b_int
print(sum)       # 66
print(type(sum)) # <class 'int'>

# all floats
a_float = 200.0
b_float = 3.0
sum = a_float // b_float
print(sum)       # 66.0
print(type(sum)) # <class 'float'>

# mix of int and float
sum = a_int // b_float
print(sum)       # 66.0
print(type(sum)) # <class 'float'>
