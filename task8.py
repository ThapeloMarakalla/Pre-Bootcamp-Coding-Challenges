def to_standard_time(num):
    """Print num as hours and minutes
    """
    hours = num // 60
    num %= 60
    minutes = num % 60

    if hours == 1:
        print(f'{hours} hour, ', end="")
    elif hours > 1:
        print(f'{hours} hours, ', end="")

    if minutes == 1:
        print(f'{minutes} minute', end="")
    elif minutes > 1:
        print(f'{minutes} minutes', end="")

    print()


if __name__ == '__main__':
    to_standard_time(71)
    to_standard_time(133)
