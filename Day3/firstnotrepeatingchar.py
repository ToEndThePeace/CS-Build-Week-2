from collections import OrderedDict
def first_not_repeating_character(s):
    res = "_"
    seen = OrderedDict()
    for i in range(len(s)):
        char = s[i]
        if char not in seen:
            seen[char] = 0
        seen[char] += 1
    for x in seen:
        if seen[x] == 1:
            res = x
            break
    return res


"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
first_not_repeating_character(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
first_not_repeating_character(s) = '_'.

There are no characters in this string that do not repeat.


Input:
s: "vbijvdpmxfztmlgieywuloeaudyokfjcoriqfwxuwdfxrllddihadvaeohgkjxiepvzmzhmpnuvgchqgabimpekppnewthrrbpvtfc"
Expected Output:
"_"

Input:
s: "bcccccccccccccyb"
Expected Output:
"y"

Input:
s: "abcdefghijklmnopqrstuvwxyziflskecznslkjfabe"
Expected Output:
"d"


Input:
s: "bcb"
Expected Output:
"c"


nput:
s: "z"
Expected Output:
"z"


Input:
s: "abacabad"
Expected Output:
"c"

"""