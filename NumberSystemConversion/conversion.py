from helperFunction import split_whole_to_fractional, twos_complement, pad_binary_octal, pad_binary_hexadecimal, apply_padding_signed_binary, apply_padding_unsigned_binary, apply_padding_signed_octal,apply_padding_unsigned_octal, apply_padding_signed_hexadecimal, apply_padding_unsigned_hexadecimal

def binary_to_decimal(binary):
    if binary[0] == '1':
        binary_complement = twos_complement(binary)
        whole, fractional = split_whole_to_fractional(binary_complement)
    else: 
        whole, fractional = split_whole_to_fractional(binary)
    
    decimal_whole = 0
    power = len(whole) - 1
    for digit in whole:
        decimal_whole += int(digit) * (2 ** power)
        power -= 1

    decimal_fractional = 0 
    power = -1
    for digit in fractional:
        decimal_fractional += int(digit) * (2 ** power)
        power -= 1
    
    decimal_representation = decimal_whole + decimal_fractional

    if binary[0] == '1':
        return -1 * decimal_representation
    else:
        return decimal_representation



def binary_to_octal(binary):
    if binary[0] == '1':
        binary = pad_binary_octal(binary)
        whole, fractional = split_whole_to_fractional(binary)
    else:
        binary = pad_binary_octal(binary)
        whole, fractional = split_whole_to_fractional(binary)  

    octal_whole = ''
    for i in range(0, len(whole), 3):
        group = whole[i:i+3]
        octal_whole += str(int(group, 2))

    octal_fractional = ''
    for i in range(0, len(fractional), 3):
        group = fractional[i:i+3]
        octal_fractional += str(int(group, 2))


    if octal_fractional:
        octal_representation = octal_whole + '.' + octal_fractional

    else:
        octal_representation = octal_whole

    if binary[0] == '1':
        octal_representation = apply_padding_signed_octal(octal_representation)
    
    else:
        octal_representation = octal_representation.lstrip('0')

    return octal_representation

 

def binary_to_hexadecimal(binary):
    if binary[0] == '1':
        binary = pad_binary_hexadecimal(binary)
        whole, fractional = split_whole_to_fractional(binary)
    else:
        binary = pad_binary_hexadecimal(binary)
        whole, fractional = split_whole_to_fractional(binary)

    hexadecimal_whole = ''
    for i in range(0, len(whole), 4):
        group = whole[i:i+4]
        hexadecimal_whole += hex(int(group, 2))[2:].upper()
  
    hexadecimal_fractional = ''
    for i in range(0, len(fractional), 4):
        group = fractional[i:i+4]
        hexadecimal_fractional += hex(int(group, 2))[2:].upper()

    if hexadecimal_fractional:
        hexadecimal_representation = hexadecimal_whole + '.' + hexadecimal_fractional
    else:
        hexadecimal_representation = hexadecimal_whole

    if binary[0] == '1':
        hexadecimal_representation = apply_padding_signed_hexadecimal(hexadecimal_representation)
    
    else:
        hexadecimal_representation = hexadecimal_representation.lstrip('0')

    return hexadecimal_representation



def decimal_to_binary(decimal):
    sign_indicator = False
    if decimal[0] == '-':
        sign_indicator = True
        decimal = decimal[1:]

    whole, fractional = split_whole_to_fractional(decimal)

    binary_whole = ''
    whole_int = int(whole)
    while whole_int > 0:
        remainder = whole_int % 2  
        binary_whole = str(remainder) + binary_whole  
        whole_int //= 2 

    if binary_whole == '':
        binary_whole = '0'

    binary_fractional = ''
    if fractional:
        fractional = '0.' + fractional
        fractional_float = float(fractional)

        precision = 10 

        while precision > 0 and fractional_float != 0:
            fractional_float *= 2  
            if fractional_float >= 1:
                binary_fractional += '1'  
                fractional_float -= 1  
            else:
                binary_fractional += '0' 
            precision -= 1 

    if binary_fractional:
        binary_value = binary_whole + '.' + binary_fractional
    else: 
        binary_value = binary_whole

    if sign_indicator:
        binary_representation = twos_complement(binary_value)
        binary_representation = apply_padding_signed_binary(binary_representation)
    else:
        binary_representation = apply_padding_unsigned_binary(binary_value)

    return binary_representation


def decimal_to_octal(decimal):
    decimal = decimal_to_binary(decimal)

    whole, fractional = split_whole_to_fractional(decimal)

    octal_whole = ''
    while len(whole) % 3 != 0:
        whole = '0' + whole
    for i in range(0, len(whole), 3):
        group = whole[i:i + 3]
        octal_whole += str(int(group, 2))

    octal_fractional = ''
    if fractional:
        while len(fractional) % 3 != 0:
            fractional += '0'
        for i in range(0, len(fractional), 3):
            group = fractional[i:i + 3]
            octal_fractional += str(int(group, 2))

    if octal_fractional:
        octal_representation = octal_whole + '.' + octal_fractional
    else:
        octal_representation = octal_whole

    octal_representation = octal_representation.lstrip('0')
    return octal_representation



def decimal_to_hexadecimal(decimal):
    decimal = decimal_to_binary(decimal)

    whole, fractional = split_whole_to_fractional(decimal)

    hexadecimal_whole = ''
    while len(whole) % 4 != 0:
        whole = '0' + whole
    for i in range(0, len(whole), 4):
        group = whole[i:i + 4]
        hexadecimal_whole += hex(int(group, 2))[2:].upper()

    hexadecimal_fractional = ''
    if fractional:
        while len(fractional) % 4 != 0:
            fractional += '0'
        for i in range(0, len(fractional), 4):
            group = fractional[i:i + 4]
            hexadecimal_fractional += hex(int(group, 2))[2:].upper()


    if hexadecimal_fractional:
        hexadecimal_representation = hexadecimal_whole + '.' + hexadecimal_fractional
    else:
        hexadecimal_representation = hexadecimal_whole

    hexadecimal_representation = hexadecimal_representation.lstrip('0')
    return hexadecimal_representation




def octal_to_binary(octal):
    oct_to_bin_map = {
        '0': '000', '1': '001', '2': '010', '3': '011',
        '4': '100', '5': '101', '6': '110', '7': '111'
    }

    sign_indicator = False
    if octal[0] == '-':
        sign_indicator = True
        octal = octal[1:]

    whole, fractional = split_whole_to_fractional(octal)

    binary_whole = ''
    if whole:
        for digit in whole:
            binary_whole += oct_to_bin_map[digit]

    binary_fractional = ''
    if fractional:
        for digit in fractional:
            binary_fractional += oct_to_bin_map[digit]

    binary_value = binary_whole
    if binary_fractional:
        binary_value += '.' + binary_fractional
        binary_value = apply_padding_unsigned_binary(binary_value)

    if sign_indicator:
        binary_value = twos_complement(binary_value)
        binary_value = apply_padding_signed_binary(binary_value)

    return binary_value


def octal_to_decimal(octal):
    sign_indicator = False
    if octal[0] == '-':
        sign_indicator = True
        octal = octal.lstrip('-')

    octal = octal_to_binary(octal)

    whole, fractional = split_whole_to_fractional(octal)

    decimal_whole = 0
    for digit in whole:
        decimal_whole = decimal_whole * 2 + int(digit)

    decimal_fractional = 0
    if fractional:
        for i, digit in enumerate(fractional):
            decimal_fractional += int(digit) * (2 ** -(i + 1))  

    decimal_value = decimal_whole + decimal_fractional 

    if sign_indicator == True:
        decimal_representation = -1 * (decimal_value)

    else:
        decimal_representation = decimal_value
    
    return decimal_representation



def octal_to_hexadecimal(octal):
    octal = octal_to_binary(octal)

    whole, fractional = split_whole_to_fractional(octal)

    hexadecimal_whole = ''
    while len(whole) % 4 != 0:
        whole = '0' + whole
    for i in range(0, len(whole), 4):
        group = whole[i:i + 4]
        hexadecimal_whole += hex(int(group, 2))[2:].upper()

    hexadecimal_fractional = ''
    if fractional:
        while len(fractional) % 4 != 0:
            fractional += '0'
        for i in range(0, len(fractional), 4):
            group = fractional[i:i + 4]
            hexadecimal_fractional += hex(int(group, 2))[2:].upper()

    if hexadecimal_fractional:
        hexadecimal_representation = hexadecimal_whole + '.' + hexadecimal_fractional
    else:
        hexadecimal_representation = hexadecimal_whole

    hexadecimal_representation = hexadecimal_representation.lstrip('0')
    return hexadecimal_representation



def hexadecimal_to_binary(hexadecimal):
    hex_to_bin_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    sign_indicator = False
    if hexadecimal[0] == '-':
        sign_indicator = True
        hexadecimal = hexadecimal[1:]

    whole, fractional = split_whole_to_fractional(hexadecimal)


    binary_whole = ''
    for hex_digit in whole:
        binary_whole += hex_to_bin_map[hex_digit]

    binary_fractional = ''
    if fractional:
        for hex_digit in fractional:
            binary_fractional += hex_to_bin_map[hex_digit]


    if binary_fractional:
        binary_value = binary_whole + '.' + binary_fractional
    else: 
        binary_value = binary_whole

    if sign_indicator:
        binary_representation = twos_complement(binary_value)
        binary_representation = apply_padding_signed_binary(binary_representation)
    else:
        binary_representation = apply_padding_unsigned_binary(binary_value)

    return binary_representation



def hexadecimal_to_decimal(hexadecimal):
    sign_indicator = False
    if hexadecimal[0] == '-':
        sign_indicator = True
        hexadecimal = hexadecimal[1:]

    hexadecimal = hexadecimal_to_binary(hexadecimal)

    whole, fractional = split_whole_to_fractional(hexadecimal)

    decimal_whole = 0
    for digit in whole:
        decimal_whole = decimal_whole * 2 + int(digit)

    decimal_fractional = 0
    if fractional:
        for i, digit in enumerate(fractional):
            decimal_fractional += int(digit) * (2 ** -(i + 1))

    decimal_representation = decimal_whole + decimal_fractional

    if sign_indicator:
        decimal_representation = -1 * decimal_representation

    else: 
        decimal_representation = decimal_representation

    return decimal_representation



def hexadecimal_to_octal(hexadecimal):
    hexadecimal = hexadecimal_to_binary(hexadecimal)

    whole, fractional = split_whole_to_fractional(hexadecimal)

    octal_whole = ''
    while len(whole) % 3 != 0:
        whole = '0' + whole
    for i in range(0, len(whole), 3):
        group = whole[i:i + 3]
        octal_whole += str(int(group, 2))

    octal_fractional = ''
    if fractional:
        while len(fractional) % 3 != 0:
            fractional += '0'
        for i in range(0, len(fractional), 3):
            group = fractional[i:i + 3]
            octal_fractional += str(int(group, 2))

    octal_representation = octal_whole
    if octal_fractional:
        octal_representation += '.' + octal_fractional

    else:
        octal_representation = octal_representation

    octal_representation = octal_representation.lstrip('0')
    return octal_representation




def menu():
    print("Menu-3 (Conversion)")
    print("[1] Binary to X")
    print("[2] Decimal to X")
    print("[3] Octal to X")
    print("[4] Hexadecimal to X")

def main_menu_for_number_system_conversion():
    menu()
    
    choice = input("Enter your choice: ")

    if choice == '1':
        binary = input("Enter a binary number: ")
        print("Decimal:", binary_to_decimal(binary))
        print("Octal:", binary_to_octal(binary))
        print("Hexadecimal:", binary_to_hexadecimal(binary))
        

    elif choice == '2':
        decimal = input("Enter a decimal number: ")
        print("Binary:", decimal_to_binary(decimal))
        print("Octal:", decimal_to_octal(decimal))
        print("Hexadecimal:", decimal_to_hexadecimal(decimal))

    elif choice == '3':
        octal = input("Enter an octal number: ")
        print("Binary:", octal_to_binary(octal))
        print("Decimal:", octal_to_decimal(octal))
        print("Hexadecimal:", octal_to_hexadecimal(octal))

    elif choice == '4':
        hexadecimal = input("Enter a hexadecimal number: ")
        print("Binary:", hexadecimal_to_binary(hexadecimal))
        print("Decimal:", hexadecimal_to_decimal(hexadecimal))
        print("Octal:", hexadecimal_to_octal(hexadecimal))

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main_menu_for_number_system_conversion()