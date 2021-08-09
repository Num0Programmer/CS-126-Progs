# !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!!
# You should not use the print() or input() functions anywhere in this file!
# !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!!

##############################################################################
# Name: Asa Henry                                                            #
# Email: ajh728@nau.edu                                                      #
# Date: Fri. Nov. 20th, 2020                                                 #
##############################################################################

# Function 1: Same First Digit
#
# Define a function called same_first_digit() that takes in three numbers and
# returns True if they all have the same first digit and False otherwise.
#
# Hint: Mold data according to the way you are going to use it: it's a shame
#       you can't index into a number...

def same_first_digit(number_1, number_2, number_3):
    num_1_str = str(number_1)
    num_2_str = str(number_2)
    num_3_str = str(number_3)

    if (num_1_str[0] == num_2_str[0]) and (num_2_str[0] == num_3_str[0]):
        return True

    return False


# Function 2: String Reversal
#
# Write a function called reverse() that takes in a string and gives back the
# the string with its characters in inverted order.
#
# Don't be a tool and just call the built-in function reversed()

def reverse(string):
    acc = -1
    reversed_string = ''

    for _ in range(len(string)):
        reversed_string += string[acc]
        acc -= 1
    
    return reversed_string


# Function 3: Palindrome Detection
#
# Write a function called is_palindrome() which takes in a single string
# parameter.  The function should return True if the string is a palindrome and
# False otherwise.  A palindrome is a string which can be read in the same way
# both forward and backward, "mom" for example.  The case of the string should
# not affect correctly detecting a palindrome; neither should any spaces,
# commas, or apostrophes in the string.
#
# HINT: If only you could get rid of all the characters you don't care about
# some how.
#
# HINT: If only there was some way to obtain a backwards version of a string...

def is_palindrome(string):
    lowered_string = string.lower()

    purge_chars = [' ', ',', "'"]
    purged_string = ''

    for char in lowered_string:
        if char in purge_chars:
            purged_string += ''
        else:
            purged_string += char


    if reverse(purged_string) == purged_string:
        return True

    return False


# Function 4: String to ASCII Codes
#
# Write a function called str_to_ascii() that takes in a string and returns a
# list of integers where each integer is the ASCII code for the corresponding
# character in the string at that position.
#
# EX: str_to_ascii('abc') --> [97, 98, 99]
#
# HINT: If you dont know what ASCII is, Google "ASCII table"
#
# HINT: There is a built in function that can do the char --> ASCII code
#       conversion for you; you just have to find it.

def str_to_ascii(string):
    ascii_list = []

    for letter in string:
        ascii_list.append(ord(letter))

    return ascii_list


# Function 5: Get Piece Value
#
# Write a function called get_piece_value() which takes in the name of a chess
# piece as a string and returns a numeric value corresponding to the piece
# after this scheme:
#
# | piece  | value |
# |--------+-------|
# | pawn   |     1 |
# | bishop |     3 |
# | knight |     3 |
# | rook   |     5 |
# | queen  |     9 |
#
# If a string is given as input which is not the name of a valid piece, your
# function should return None.  Make sure this function works for strings with
# any combination of letter case as long as they are spelled right.
#
# To get the intended practice for this problem, don't use *any* if statements

def get_piece_value(piece):
    piece_values = {'pawn': 1, 'bishop': 3, 'knight': 3, 'rook': 5, 'queen': 9}

    return piece_values.get(piece.lower())


# Function 6: Formatting Dates
#
# Write a function called format_date() which takes in a single parameter which
# is a string of the format yyyymmdd (like 20190209) and returns a string of
# the format "February 9th, 2019"
#
# Hint: One part of the date string is really easy, and one part has a
#       surprising number of edge cases

def format_date(date):
    leap_year = False

    months = {
        '01': 'January', '02': 'February', '03': 'March', '04': 'April', 
        '05': 'May', '06': 'June', '07': 'July', '08': 'August', 
        '09': 'September', '10': 'October', '11': 'November', 
        '12': 'December'
    }

    day_maxes = {'January': 31, 'February': 28, 'March': 31, 'April': 30,
                 'May': 31, 'June': 30, 'July': 31, 'August': 31,
                 'September': 30, 'October': 31, 'November': 30, 
                 'December': 31
    }

    day_suffixes = {'1': 'st', '2': 'nd', '3': 'rd'}

    year = date[:4]

    if int(year) % 4 == 0:
        day_maxes['February'] = 29
        leap_year = True

    month = date[4:6]
    month_format = months[month]

    day = date[6:8]
    day_ending = ''

    if (leap_year == False) and (month == '02') and (day == '29'):
        return False

    if day[0] == '0':
        day = day[1]
        if (day == '1') or (day == '2') or (day == '3'):
            day_ending = day_suffixes[day]
            return f"{month_format} {day}{day_ending}, {year}"
        else:
            day_ending = 'th'
            return f"{month_format} {day}{day_ending}, {year}"
    elif int(day) >= 11 and int(day)  <= 19:
        return f"{month_format} {day}th, {year}"
    elif (day[1] == '1') or (day[1] == '2') or (day[1] == '3'):
        day_ending = day_suffixes[day[1]]
        return f"{month_format} {day}{day_ending}, {year}"
    else:
        day_ending = 'th'
        return f"{month_format} {day}{day_ending}, {year}"
    
