from menus import binary_operations_menu

def binary_operations():
    binary_operations_menu()
    operation_choice = int(input("Enter your choice: "))
def binary_division(dividend, divisor):
    dividend_int = int(dividend, 2)
    divisor_int = int(divisor, 2)
    quotient_int = 0
    remainder_int = 0
    for i in range(len(dividend)):
        remainder_int = (remainder_int << 1) | int(dividend[i])
        if remainder_int >= divisor_int:
            remainder_int -= divisor_int
            quotient_int |= (1 << (len(dividend) - 1 - i))
    quotient_bin = format(quotient_int, 'b')
    remainder_bin = format(remainder_int, 'b')
    return quotient_bin, remainder_bin

def binary_multiplication(a, b):
    product = 0
    a_int = int(a, 2)
    b_int = int(b, 2)
    while b_int != 0:
        if b_int & 1:
            product += a_int
        a_int <<= 1
        b_int >>= 1
    return format(product, 'b')

def binary_subtraction(a, b):
    result_int = int(a, 2) - int(b, 2)
    if result_int == 0:
        return '0'
    elif result_int < 0:
        result_binary = decimal_to_binary(-result_int)
        return '-' + result_binary
    else:
        return decimal_to_binary(result_int)

def add_binary(a, b):
    max_length = max(len(a), len(b))
    a = '0' * (max_length - len(a)) + a
    b = '0' * (max_length - len(b)) + b

    result = ''
    carry = 0

    for i in range(max_length - 1, -1, -1):
        digit_sum = int(a[i]) + int(b[i]) + carry
        result = str(digit_sum % 2) + result
        carry = digit_sum // 2

    if carry:
        result = '1' + result

    return result

def twos_complement(binary):
    complement = ''.join('1' if bit == '0' else '0' for bit in binary)
    
    result = ''
    carry = 1
    for bit in complement[::-1]:
        if bit == '0' and carry == 1:
            result = '1' + result
            carry = 0
        elif bit == '1' and carry == 1:
            result = '0' + result
        else:
            result = bit + result
        
    return result
