def istriangle(sides):
    verdict = True
    for i in range(len(sides)):
        if (sides[i] <= 0):
            verdict = False
            pass

    if((sides[0] + sides[1] < sides[2]) or (sides[1] + sides[2] < sides[0]) or (sides[2] + sides[0] < sides[1])):
        verdict = False

    return(verdict)
    

def equilateral(sides):

    if not(istriangle(sides)):
        return False

    return sides[0] == sides[1] == sides[2]


def isosceles(sides):

    if not(istriangle(sides)):
        return False

    return sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]


def scalene(sides):
    if not(istriangle(sides)):
        return False

    return sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]

