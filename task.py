def conv_endian(num, endian='big'):
    hex = len_str(dec_to_hex(num))
    if endian == 'big':
        out = ' '.join(hex[i:i + 2] for i in range(0, len(hex), 2))
        return sign_check(num, out)
    elif endian == 'little':
        out = ' '.join(reversed([hex[i:i + 2] for i in range(0, len(hex), 2)]))
        return sign_check(num, out)
    else:
        return None


def dec_to_hex(number):
    number = abs(number)
    table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
             5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
             10: 'A', 11: 'B', 12: 'C', 13: 'D',
             14:  'E', 15: 'F'}
    number = abs(number)
    hexdec = ''
    while number > 0:
        hexdec = table[number % 16] + hexdec
        number = number // 16
    return hexdec


def len_str(strng):
    if len(strng) % 2 == 1:
        strng = '0' + strng
        return strng
    return strng


def sign_check(number, strng):
    if (number) < 0:
        strng = '-' + strng
        return strng
    return strng
