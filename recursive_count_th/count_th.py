'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


''' With Recursion '''
def count_th(word):
    if len(word) < 2:
        return 0
    else:
        if word[0:2] == 'th':
            return 1 + count_th(word[2:])
        else:
            return count_th(word[1:])

''' Or theres this hacky way using python list method lol '''
def count_of_letters(word, search):
    return word.count(search)
    
    
