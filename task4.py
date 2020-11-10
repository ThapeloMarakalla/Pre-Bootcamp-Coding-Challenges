def task4(num1, num2):
    """Returns True if either num1 or num2 is 3, AND the sum of num1 and num2 contains 
    a 3, False otherwise.
    """
    if (3 in [num1, num2]) and ('3' in str(num1 + num2)):
        return True
    return False

if __name__ == '__main__':
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if task4(num1, num2):
        print('Either one of the numbers(or both) is 3 and the sum of the', end=' ')
        print('numbers contains a 3')
    else:
        print('Either one of the number is not 3 or the sum of the', end=' ')
        print('numbers does not contain a 3')