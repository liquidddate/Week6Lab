def is_valid_part(part):
    try:
        int_part = int(part)
        if part[0] == "0" and not int_part == 0: return False
        return 0 <= int_part < 256
    except ValueError as ve:
        return False

def is_valid_ip(ip:str):
        cnt = 0
        for part in ip.split('.'):
            if not is_valid_part(part): return False
            cnt += 1
        return True and (cnt == 4)

#print(is_valid_part("224"),is_valid_part("300"),is_valid_part("0"),is_valid_part("01"),)

#print(
#    is_valid_ip('192.168.49.1')
#)

#print(is_valid_ip("192.168.1.1"))  # True
#print(is_valid_ip("192.168.256.1"))  # False
#print(is_valid_ip("192.168.1"))  # False
#print(is_valid_ip("192.168.01.1"))  # False