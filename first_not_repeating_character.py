'''Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.'''

def firstNotRepeatingCharacter(s):
    
    letters_list=[]
    other_list=[]
    for letter in s:
        if letter in other_list:
            continue
            
        if letter not in letters_list:
            letters_list.append(letter)
        else:
            other_list.append(letter)
            letters_list.remove(letter)
    if len(letters_list)==0:
        return '_'
    else:
        return letters_list[0]
