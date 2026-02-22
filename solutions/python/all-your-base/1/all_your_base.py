def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    elif output_base < 2:
        raise ValueError("output base must be >= 2")
    
    for dig in digits:
        if dig < 0 or dig >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    zero_count = 0
    output_10 = 0
    for ind, dig in enumerate(digits):
        output_10 += pow(input_base, len(digits) - ind - 1) * dig
        if dig == 0:
            zero_count += 1

    if zero_count == len(digits) or len(digits) == 0:
        return [0]
        

    output = []
    temp = 0
    while output_10 != 0:
        temp = output_10%output_base
        output.insert(0, temp)
        output_10 = output_10 // output_base

    return output