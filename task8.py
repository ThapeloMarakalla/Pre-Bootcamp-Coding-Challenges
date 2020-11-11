def to_standard_time(num):
    """Print num as hours and minutes
    """
    hours = num // 60
    num %= 60
    minutes = num % 60

    if hours == 0:
        print(f'{minutes} minutes')
    else:
        print(f'{hours} hour(s), {minutes} minutes')

if __name__ == '__main__':
    to_standard_time(71)
    to_standard_time(133)