def commom_characters(string1, string2):
    """Prints commint characters that common in string1 and string2
    """

    # 1. coverts string1 and string2 to two sets of characters,
    #  to remove duplicates.
    # 2. use set operator & to find common elements in both sets.
    print('Common letters:', *(set(string1) & set(string2)))

if __name__ == '__main__':
    commom_characters('house', 'computers')