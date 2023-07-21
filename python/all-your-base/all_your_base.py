def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    base10 = 0
    #translate to base 10
    for i, digit in enumerate(digits[::-1]):
        if not 0 <= digit < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        base10 += input_base ** i * digit

    if base10 == 0:
        return [0]
    #find highest place in output base
    highest_place = 0
    while output_base ** highest_place < base10:
        highest_place += 1
    
    output_digits = []
    while highest_place >= 0:
        output_digits.append(base10//(output_base ** highest_place))
        base10 = base10 % output_base ** highest_place
        highest_place -= 1

    if len(output_digits) > 1 and output_digits[0] == 0:
        output_digits.remove(0)

    return output_digits

