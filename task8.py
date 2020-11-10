def to_standard_time(num):
    """Print num as hours and minutes
    """
    hr = num // 60
    num %= 60
    min = num % 60

    print(f'{hr} hours, {min} minutes')

if __name__ == '__main__':
    to_standard_time(71)
    to_standard_time(133)