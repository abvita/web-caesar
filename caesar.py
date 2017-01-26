def alphabet_position(letter):
    lwr_let = letter.lower()
    pos = ord(lwr_let) - 97
    return pos

def rotate_character(char, rot):
    if not char.isalpha():
        return char
    else:
        rotated = chr(alphabet_position(char) + rot + 97)
        if not rotated.isalpha():
            rotated = chr(ord(rotated) - 26)
    if char.isupper():
        rotated = rotated.upper()
    return rotated

def encrypt(text,rot):
    result = ""
    for i in text:
        result += rotate_character(i, rot)
    return result
