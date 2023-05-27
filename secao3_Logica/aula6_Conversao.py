# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
#    str, int, float, bool
print(int('1'), type(int('1'))) # 1, <class 'int'>
print(type(float('1') +1)) # <class 'float'>

print(bool('')) # False
print(str(11) + 'b') # 11b

print(float("1") + 1) # 2.0
print(int("1") + 1) # 2
print(type(int('1'))) # <class 'int'>

# python só concatena valores do mesmo tipo.