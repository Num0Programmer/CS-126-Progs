##############################################################################
# CS 126 Hwk5: And yet more functions                                        #
# Name: Asa Henry                                                            #
# Email: ajh728@nau.edu                                                      #
# Date: Fri. Nov. 20th, 2020                                                 #
##############################################################################

# Function 1: Select a field
#
# Write a function called select_field() that takes in two parameters.  The
# first parameter should be a string of comma separated fields.  The second
# parameter should be a number designating which field to select.  The first
# field should be designated by the number 0 (just like indexing).
#
# The function should return the designated field from the string with any
# leading and/or trailing whitespace removed.
#
# EX: select_field('AL, AK, AZ, AR, CA, CO', 2) --> "AZ"
#
# If a field index is provided which designates a non-existent field of the
# string (e.g. it's too big), the function should return None.  Use a
# try-except structure to make this happen.
#
# EX: select_field('AL, AK, AZ, AR, CA, CO', 750) --> None

def select_field(csf_string, field_selection):
    try:
        return csf_string.split(',')[field_selection].strip()
    except IndexError:
        return None

# Function 2: Find all vowel indices
#
# Write a function called find_vowel_indexes() that takes in a string and
# returns a list containing the indexes of all the vowels in the string.  The
# letter 'y' should count as a vowel unless it is the first character of the
# word.
#
# The input string may be in upper, lower, or mixed case.
#
# Don't forget that you can write helper functions
#
# EX: find_vowel_indexes("hello") --> [1, 4]
#     find_vowel_indexes("yellow") --> [1, 4]
#     find_vowel_indexes("the sky is falling") --> [2, 6, 8, 12, 15]

def find_vowel_indexes(string):
    vowel_indecies = []

    index = 0
    for char in string:
        if is_vowel(string, char, index):
            # True, the index of char should get added
            vowel_indecies.append(index)
        index += 1

    return vowel_indecies

def is_vowel(string, char, index):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if char.lower() == 'y' and index == 0:
        return False
    elif char.lower() == 'y':
        # True, and the current char is y
        if not y_begins_word(string, index):
            # True, and y does not appear at the beginning of the word
            return True

    return char.lower() in vowels

def y_begins_word(string, index):
    # if index == 0: # If y is the first letter in a word
    #     # Y is not a vowel
    #     return False

    return string[index - 1] == ' ' # True if y is the first letter in a word
                                    # False if y is not the first letter in a word

# Function 3: Finding the First Factor
#
# Write a function called first_factor() which takes in a number and returns
# the first number larger than one which evenly divides that number.
#
# EX: first_factor(55) --> 5
#     first_factor(19) --> 19
#     first_factor(6)  --> 2

def first_factor(number):
    for possible_factor in range(2, number + 1):
        if is_even(number, possible_factor):
            return possible_factor

def is_even(number, possible_factor):
    return number % possible_factor == 0

# Function 4: Dete 1cting Primes
#
# Write a function called is_prime() that takes in an integer and returns True
# if it is prime and False otherwise.
#
# HINT: Remind yourself of what it means for a number to be prime by looking
#       it up
#
# HINT: *DON'T* look up how to decide if a number is prime on the
#       internet, you will almost certainly find a bunch of really complicated
#       code that is overkill for this problem
#
# HINT: You have already implemented another function that you could call to
#       make this problem easier (assuming you are doing these in order)

def is_prime(integer):
    return first_factor(integer) == integer and integer % 1 == 0

# Function 5: Roman Numerals
#
# Write a function called romanize() that takes in one number as an argument.
# The number is guaranteed to be in the range [1, 100].  The function should
# return a string containing the Roman Numeral representation of the number.
#
# SUGGESTION: If you don't know/remember how Roman Numerals work, Wikipedia has
#             a good set of explanations
#
# FOOD FOR THOUGHT: It is possible to create a solution to this problem that
#                   uses no loops!  That solution is also not one that is easy
#                   to come up with (in my opinion)

def romanize(number):
    first_ten_numerals = {
        0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII',
        8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX', 30: 'XXX', 50: 'L', 90: 'XC'
    }

    if len(str(number)) == 3:  # If True, number is equal to 100
        return 'C'
    elif len(str(number)) == 2:  # If True, number is between 10 and 99 
                                 # including both
        if number >= 10 and number <= 39: # Covers 10 to 39
            tens_form = number - int(str(number)[1]) 
            int_ver_ones = int(str(number)[1])
            return f'{first_ten_numerals[tens_form]}{first_ten_numerals[int_ver_ones]}'
        elif number >= 40 and number <= 89: # Covers 40 to 89
            tens_form = number - int(str(number)[1])
            if number >= 40 and number < 50:  # covers 40 and 40s
                int_ver_ones = int(str(number)[1])
                return f'XL{first_ten_numerals[int_ver_ones]}'
            elif number >= 50 and number < 60: # Covers 50 and 50s
                int_ver_ones = int(str(number)[1])
                return f'L{first_ten_numerals[int_ver_ones]}'
            else: # Covers everything above 50s to 89
                tens_form = number - int(str(number)[1])
                int_ver_ones = int(str(number)[1])
                return f'L{first_ten_numerals[tens_form - 50]}{first_ten_numerals[int_ver_ones]}'
        elif number == 90: # Covers 90
            return 'XC'
        elif number > 90: # Covers 90s
            int_ver_ones = int(str(number)[1])
            return f'XC{first_ten_numerals[int_ver_ones]}'
    else:
        return first_ten_numerals[number]

# EXTRA CREDIT! EXTRA CREDIT! EXTRA CREDIT! EXTRA CREDIT! EXTRA CREDIT!
#
# Matching Parentheses
#
# Define a function called all_parens_matched() that takes in a string and
# returns True if the string contains properly matched parenthesis pairs.
#
# Ex: all_parens_matched("(this (string) is) (fine)") --> True
#     all_parens_matched(")uh (oh) (doomed from (the start))") --> False
#     all_parens_matched("(everything (is (fine until the end)))(") --> False
#
# HINT: Order matters! You can't simply count the number of open parentheses
#       and compare to the number of close parentheses
#
# HINT: This problem is hard!

def all_parens_matched(string):
    parens = ''
    for char in string:
        if char == '(' or char == ')':
            parens += char

    open_parens = ''
    close_parens = ''
    for paren in parens:
        if paren == '(':
            open_parens += paren
        if paren == ')':
            close_parens += paren
    
    if len(open_parens) == len(close_parens):
        pairs = 0
        for i in range(len(open_parens)):
            if open_parens[i] == '(' and close_parens[i] == ')':
                pairs += 1



        matches = []
        for paren in parens:
            index = 1 # should alwasy be ahead of the index paren would be at
            if paren == '(' and parens[index] == ')':
                matches.append([paren, parens[index]])

    return False


