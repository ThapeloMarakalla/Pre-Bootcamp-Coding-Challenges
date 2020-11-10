def maximum(num1, num2, num3):
    """Return the maximum number between num1, num2 and num3
    """
    max = num1

    if num2 > max:
        max = num2
    if num3 > max:
        max = num3

    return max

if __name__ == '__main__':
    print(f'The maximum between -1 ,99, 6 is {maximum(-1 ,99, 6)}')