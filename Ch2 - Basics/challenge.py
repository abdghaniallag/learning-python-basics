import string


def palindrome(str_in):
    lower = str_in.lower()
    str_alph_num = ""
    for char in lower:
        if char.isalnum():
            str_alph_num += char

    print(lower)
    return  True

# print(set_of_characters_is_reserved)

palindrome("Ghani . // l")
