def task3(num1, num2):
    """Returns True if either num1 or num2 is 65 OR the sum of num1 and num2
    is 65, False otherwise.
    """
    if (65 in [num1, num2]) or ((num1 + num2) == 65):
        return True
    return False


if __name__ == '__main__':
    num1 = 23
    num2 = 41

    if task3(num1, num2):
        print('Either one of the numbers(or both) is 65 or the sum of the', end=' ')
        print('numbers is 65')
    else:
        print('None of the number is 65 and the sum of the', end=' ')
        print('numbers is not 65')
