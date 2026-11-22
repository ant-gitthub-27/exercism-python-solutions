def commands(binary_str):
    l1 = []
    b = binary_str
    if b[-1] == "1":
            l1.append('wink')
    if b[-2] == "1":
            l1.append('double blink')
    if b[-3] == "1":
            l1.append('close your eyes') 
    if b[-4] == "1":
            l1.append('jump')
    if int(b) > 9999 :
        return l1[::-1]
    else:
        return l1