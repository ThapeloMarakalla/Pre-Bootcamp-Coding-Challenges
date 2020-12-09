def maximum(*args):
    """Return the maximum number in args
    """
    if args:
        max = args[0]

        for num in args[1:]:
            if num > max:
                max = num
        return max
    else:
        raise TypeError('maximum expected at least 1 arguments, got 0')


if __name__ == '__main__':
    print(f'The maximum between -1 ,5, 12, 4, 11, 81, 6 is {maximum(-1 ,5, 12, 4, 11, 81, 6)}')
