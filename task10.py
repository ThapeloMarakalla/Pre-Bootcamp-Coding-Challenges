def print_vowels(string):
    """Prints all the vowels in string.
    """
    vowels = 'aeiou'
    print(f"vowels in {string}:", end=' ')
    for letter in string:
        if letter.lower() in vowels:
            print(letter, end=' ')
    print()

if __name__ == '__main__':
    print_vowels('ThapElo')