def sum_of_multiples():
    """Finds the sum of all the multiples of 3 and 5 
    below 1000
    """
    total = 0
    for num in range(1, 1000):
        if (num % 3 == 0) or (num % 5 == 0):
            total += num

    print(f'The sum of all the multiples of 3 or 5 below 1000 is {total}')

if __name__ == '__main__':
    sum_of_multiples()
    