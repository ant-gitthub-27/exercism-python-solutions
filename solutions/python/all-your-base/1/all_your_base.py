def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if any(i >= input_base or i < 0 for i in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    l1 = []
    m = 0
    for i in digits[::-1]:
        l1.append(i*(input_base**m))
        m += 1
    deci = sum(l1)
    check = 1
    ans = []
    
    
    while check:
        if deci // output_base == 0:
            check = 0
        ans.append(deci % output_base)
        deci = deci // output_base
        
    return ans[::-1]
        
    
    
        
        
