def conv_endian(num, endian='big'):
    '''Converts integer to hexadecimal.'''
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
    '''Converts decimal to hexadecimal.'''
    number = abs(number)
    hexDecNum = ['0'] * 100
    i = 0
    while number != 0:
        temp = 0
        temp = number % 16
        if temp == 1:
            hexDecNum[i] = '1'
        elif temp == 2:
            hexDecNum[i] = '2'
        elif temp == 3:
            hexDecNum[i] = '3'
        elif temp == 4:
            hexDecNum[i] = '4'
        elif temp == 5:
            hexDecNum[i] = '5'
        elif temp == 6:
            hexDecNum[i] = '6'
        elif temp == 7:
            hexDecNum[i] = '7'
        elif temp == 8:
            hexDecNum[i] = '8'
        elif temp == 9:
            hexDecNum[i] = '9'
        elif temp == 10:
            hexDecNum[i] = 'A'
        elif temp == 11:
            hexDecNum[i] = 'B'
        elif temp == 12:
            hexDecNum[i] = 'C'
        elif temp == 13:
            hexDecNum[i] = 'D'
        elif temp == 14:
            hexDecNum[i] = 'E'
        elif temp == 15:
            hexDecNum[i] = 'F'
        i = i + 1
        number = number // 16
    output = ''
    j = i - 1
    while j >= 0:
        output = output + hexDecNum[j]
        j = j - 1
    return output

def len_str(strng):
    '''Measures length of string.'''
    if len(strng) % 2 == 1:
        strng = '0' + strng
        return strng
    return strng

def sign_check(number, strng):
    '''Checks negative sign.'''
    if (number) < 0:
        strng = '-' + strng
        return strng
    return strng
