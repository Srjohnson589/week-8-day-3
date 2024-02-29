# ---------Description---------
# Nickname Generator
# Write a function, nicknameGenerator that takes a string name as an argument 
# and returns the first 3 or 4 letters as a nickname.
# If the 3rd letter is a consonant, return the first 3 letters.
# Notes:
# Vowels are "aeiou", so discount the letter "y".
# Input will always be a string.
# Input will always have the first letter capitalised and the rest lowercase (e.g. Sam).
# ----------EXAMPLES----------
# nickname("Robert") //=> "Rob"
# nickname("Kimberly") //=> "Kim"
# nickname("Samantha") //=> "Sam"
# If the 3rd letter is a vowel, return the first 4 letters.
# nickname("Jeannie") //=> "Jean"
# nickname("Douglas") //=> "Doug"
# nickname("Gregory") //=> "Greg"
# If the string is less than 4 characters, return "Error: Name too short"

# take in a string
# if len < 4: return Error
# check character at str[2], if in [a, e, i, o ,u]
    # return slice.str[:4]
# else return slice.str[:3]


def nickname(str1):
    if len(str1) < 4:
        return "Error: Name too short"
    if str1[2] in ['a', 'e', 'i', 'o', 'u']:
        return str1[:4]
    else:
        return str1[:3]
    
print(nickname('Jeannie'))
print(nickname("Robert"))
print(nickname('Douglas'))
print(nickname('Robert'))