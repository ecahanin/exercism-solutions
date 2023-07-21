def equilateral(sides):
    return len(set(sides)) == 1 and is_triangle(sides)

def isosceles(sides):
    return len(set(sides)) <= 2 and is_triangle(sides)

def scalene(sides):
    return len(set(sides)) == 3 and is_triangle(sides)

def is_triangle(sides):
    if 0 in sides or len(sides) != 3:
        return False
    sides.sort()
    return sides[0] + sides[1] > sides[2]


