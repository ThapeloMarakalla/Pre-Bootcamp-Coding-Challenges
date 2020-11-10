def calclate_area(side1, side2, side3):
    """Calulate the area of a triangle with side1, side2 and side3
    as the sides of the triangle
    """
    s = (side1+side2+side3) / 2 # semi perimeter
    return (s*(s-side1)*(s-side2)*(s-side3))**.5

if __name__ == '__main__':
    side1 = 3
    side2 = 4
    side3 = 5
    print(f'The area of the triangle is {calclate_area(side1, side2, side3)}')