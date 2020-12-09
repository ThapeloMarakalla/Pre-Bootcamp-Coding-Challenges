def commom_characters(string1, string2):
    """Prints commint characters that common in string1 and string2
    """
    print('Common letters:', *(set(string1) & set(string2)))

if __name__ == '__main__':
    commom_characters('house', 'computers')