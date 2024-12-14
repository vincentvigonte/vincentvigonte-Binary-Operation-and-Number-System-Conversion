from menus import number_sysytem_conversion_menu

def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_hexadecimal(decimal)

def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_octal(decimal)

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def decimal_to_hexadecimal(decimal):
    hexadecimal = ""
    hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while decimal > 0:
        remainder = decimal % 16
        if remainder >= 10:
            hexadecimal = hex_map[remainder] + hexadecimal
        else:
            hexadecimal = str(remainder) + hexadecimal
        decimal //= 16
    return hexadecimal

def decimal_to_octal(decimal):
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal

def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return decimal_to_binary(decimal)

def hexadecimal_to_decimal(hexadecimal):
    decimal = 0
    power = len(hexadecimal) - 1
    hex_map = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for digit in hexadecimal:
        if digit in hex_map:
            decimal += hex_map[digit] * (16 ** power)
        else:
            decimal += int(digit) * (16 ** power)
        power -= 1
    return decimal

def hexadecimal_to_octal(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return decimal_to_octal(decimal)

def octal_to_binary(octal):
    decimal = octal_to_decimal(octal)
    return decimal_to_binary(decimal)

def octal_to_decimal(octal):
    decimal = 0
    power = len(octal) - 1
    for digit in octal:
        decimal += int(digit) * (8 ** power)
        power -= 1
    return decimal

def octal_to_hexadecimal(octal):
    decimal = octal_to_decimal(octal)
    return decimal_to_hexadecimal(decimal)

def number_system_conversion():
    number_sysytem_conversion_menu()