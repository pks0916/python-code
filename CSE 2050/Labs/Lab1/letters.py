import string

def count_letters(file):
   
    """make dict"""
    letter_count = {}
   
    """open file"""
    f = open(f'{file}')
    """assign file"""
    for line in f:  
        for char in line:
            """covert to lowercase and check"""
            char = char.lower()
            """check for lower"""
            if char in string.ascii_lowercase:
                """update the count"""
                letter_count[char] = letter_count.get(char, 0) + 1


    return letter_count







print(count_letters('frost.txt'))


