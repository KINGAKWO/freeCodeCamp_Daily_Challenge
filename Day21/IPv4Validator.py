def is_valid_ipv4(ipv4):
    integer_numbers = ipv4.split(".")
    valid_address = []

    if len(integer_numbers) != 4:
        return False

    for i in integer_numbers:
        if i.isdigit():
            if len(i) > 1 and i[0]=="0":
                return False
            num = int(i)
            if 0 <= num <= 255:
                valid_address.append(num)
            else:
                return False
        else:
            return False
    return True

is_valid_ipv4("192.168.1.1")