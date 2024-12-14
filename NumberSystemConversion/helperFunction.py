def split_whole_to_fractional(number_str):
    number_str = str(number_str)
    if '.' in number_str:
        components = number_str.split('.')
        whole = components[0]
        fractional = components[1] if len(components) > 1 else ''
    else:
        whole = number_str
        fractional = ''
    return whole, fractional


def twos_complement(binary):
    dot_index = binary.find('.')

    binary = binary[::-1]
    
    encountered_one = False
   
    for i in range(len(binary)):
        if binary[i] == '.':
            continue 
        if not encountered_one:
            if binary[i] == '1':
                encountered_one = True
        else:
            binary = binary[:i] + ('0' if binary[i] == '1' else '1') + binary[i+1:]

    binary = binary[::-1]

    if dot_index != -1:
        dot_index = len(binary) - dot_index - 1
    return binary


def pad_binary_octal(binary):
    whole, fractional = binary.split('.')
    if binary[0] == '1':
        while len(whole) % 3 != 0:
            whole = '1' + whole
        while len(fractional) % 3 != 0:
            fractional += '0'
    else:  
        while len(whole) % 3 != 0:
            whole = '0' + whole
        while len(fractional) % 3 != 0:
            fractional += '0'
    return f"{whole}.{fractional}"


def pad_binary_hexadecimal(binary):
    whole, fractional = binary.split('.')
    if binary[0] == '1':
        while len(whole) % 4 != 0:
            whole = '1' + whole
        while len(fractional) % 4 != 0:
            fractional += '0'
    else:  
        while len(whole) % 4 != 0:
            whole = '0' + whole
        while len(fractional) % 4 != 0:
            fractional += '0'
    return f"{whole}.{fractional}"


def apply_padding_signed_binary(binary):
    padding_needed = 36 - len(binary)
  
    binary = '1' * padding_needed + binary
    
    return binary

def apply_padding_unsigned_binary(binary):
    padding_needed = 36 - len(binary)
    
    binary = '0' * padding_needed + binary

    return binary

def apply_padding_signed_octal(octal):
    padding_needed = 36 - len(octal)
  
    octal = '7' * padding_needed + octal
    
    return octal

def apply_padding_unsigned_octal(octal):
    padding_needed = 36 - len(octal)
  
    octal = '0' * padding_needed + octal
    
    return octal

def apply_padding_signed_hexadecimal(hexadecimal):
    padding_needed = 36 - len(hexadecimal)
  
    hexadecimal = 'F' * padding_needed + hexadecimal
    
    return hexadecimal

def apply_padding_unsigned_hexadecimal(hexadecimal):
    padding_needed = 36 - len(hexadecimal)
  
    hexadecimal = '0' * padding_needed + hexadecimal
    
    return hexadecimal
