def rows(letter):
    n = ord(letter) - ord("A")
    m = 1
    l1 = []
    l1.append(" "*n + "A" + " "*n)
    if n > 0:
        for _ in range(n):
            l1.append(" "*(n-1) + chr(m + ord("A")) + " "*(2*m-1) + chr(m + ord("A")) + " "*(n-1))
            n -= 1
            m += 1
        m -= 1
        n += 1
        for _ in range(m-1):
            l1.append(" "*(n) + chr(m-1 + ord("A")) + " "*(2*m - 3) + chr(m-1 + ord("A")) + " "*(n))
            m -= 1
            n += 1
        l1.append(" "*n + "A" + " "*n)
    return l1
    
       
        
        
    