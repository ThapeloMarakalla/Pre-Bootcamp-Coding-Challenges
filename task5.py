def calclate_area(side1, side2, side3):
    """Calulate the area of a triangle with side1, side2 and side3
    as the sides of the triangle
    """
    semi_perimeter = (side1 + side2 + side3) / 2
    area = (semi_perimeter * (semi_perimeter - side1) *
            (semi_perimeter - side2) * (semi_perimeter - side3))**.5
    return area


if __name__ == '__main__':
    side1 = 3
    side2 = 4
    side3 = 5
    print(f'The area of the triangle is {calclate_area(side1, side2, side3)}')
