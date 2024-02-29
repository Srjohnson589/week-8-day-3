# ----------Description----------
# Mary brought home a "spot the differences" book.
# The book is full of a bunch of problems, and each problem consists of two strings that are similar.
# However, in each string there are a few characters that are different. An example puzzle from her book is:
# String 1: "abcdefg"
# String 2: "abcqetg"
# Notice how the "d" from String 1 has become a "q" in String 2, and "f" from String 1 has become a "t" in String 2.
# It's your job to help Mary solve the puzzles. Write a program spot_diff/Spot
# that will compare the two strings and return a list with the positions where the two strings differ.
# In the example above, your program should return [3, 5] because String 1 is different from String 2 at positions 3 and 5.
# NOTE
# • If both strings are the same, return []
# • Both strings will always be the same length
# • Capitalization and punctuation matter
# ----------Examples----------
# solution( "racecar","RaceCar" ) => [0, 4]
# solution("Cat","Dog") => [0, 1, 2]
# solution("same","same") => []
# solution("broke","break") => [2, 3, 4]

# takes 2 strings
# loop through both strings together? compare values at each index O(n)
# if they are different add the index to the list
# return indexes where they differ

def solution(str1, str2):
    output = []
    for index in range(0, len(str1)):
        if str1[index] != str2[index]:
            output.append(index)
    return output

print(solution("racecar","RaceCar"))
print(solution("Cat","Dog"))
print(solution("same","same"))
print(solution("broke","break"))

