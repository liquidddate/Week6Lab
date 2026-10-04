
def decimal_to_binary(num):
    if num == 0: return '0'
    if num == 1: return '1'
    next, digit = divmod(num, 2)
    return decimal_to_binary(next) + str(digit)

def binary_to_decimal(bum:str):
    if bum == '': return 0
    place = len(bum) - 1
    return 2**place * int(bum[0]) + binary_to_decimal(bum.removeprefix(bum[0]))

# print(decimal_to_binary(10))

# Test cases
# print(decimal_to_binary(10))   # "1010"
# print(decimal_to_binary(255))  # "11111111"
# print(decimal_to_binary(1))    # "1"

#print(binary_to_decimal("1010"))      # 10
#print(binary_to_decimal("11111111"))  # 255
#print(binary_to_decimal("1"))         # 1