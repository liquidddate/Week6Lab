from ip_part1 import is_valid_part
from conversions import binary_to_decimal

def ip_to_binary(ip):
    if not is_valid_ip(ip):
        return "Invalid IP address"
    result = ''
    for part in ip.split('.'):
        bits = decimal_to_binary(int(part))
        while len(bits) < 8:
            bits = "0" + bits
        if result:
            result = result + "."
        result = result + bits
    return result

print(ip_to_binary('192.168.49.1'))
print(ip_to_binary("192.168.1.1"))  # "11000000.10101000.00000001.00000001"
print(ip_to_binary("255.255.255.0"))  # "11111111.11111111.11111111.00000000"
print(ip_to_binary("256.1.1.1"))  # "Invalid IP address"