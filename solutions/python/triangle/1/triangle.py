
def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    zero = a>0 and b>0 and c>0
    inequality = a + b > c and b + c > a and c + a > b
    
    return (a == b == c) and zero and inequality

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    zero = a>0 and b>0 and c>0
    inequality = a + b > c and b + c > a and c + a > b
    two_equal = a == b or b == c or c == a
    
    return two_equal and zero and inequality

def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    zero = a>0 and b>0 and c>0
    inequality = a + b > c and b + c > a and c + a > b
    no_equal = a != b and b != c and c != a

    return no_equal and zero and inequality
    
