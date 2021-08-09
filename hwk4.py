##############################################################################
# CS 126 Hwk 4: Ciphers, take two                                            #
# Name: Asa Henry                                                            #
# Email: ajh728@nau.edu                                                      #
# Date: Fri. Nov. 20th, 2020                                                 #
##############################################################################


alphabet = "abcdefghijkl mnoprstvwxyz"


def main():
    x = int(input("Would you like to:\n\t(1) encrypt\n\t(2) decrypt\n"))

    key = input("\nPlease enter a key: ")

    key_no_duplicates = ""
    used_letters = ""

    # This loop removes all duplicate letters from the key
    # It also makes all 'u's to 'v's and 'q's to 'k's
    for letter in key:
        if (letter == "u" or letter == "v") and not ("v" in used_letters):
            key_no_duplicates += "v"
        if (letter == "q" or letter == "k") and not ("k" in used_letters):
            key_no_duplicates += "k"
        elif not (letter in used_letters):
            key_no_duplicates += letter

        used_letters += letter

    # If the user inputs a 1, the program will encrypt a message
    # If the user inputs a 2, the program decrypts a message
    if x == 1:
        message = input("\nPlease enter a message to encrypt: ")
        # Converts message to lowercase and turns any u or q
        # into v or k respectively. Also adds x when needed
        message = modify_message(message.lower())
        encrypted_message = encrypt(message, key_no_duplicates)
        print(f"\nHere is your encrypted message:\n{encrypted_message}")
    else:
        message = input("\nPlease enter a message to decrypt: ")
        if error_checker(message):
            decrypted_message = decrypt(message.lower(), key_no_duplicates)
            print(f"\nHere is your decrypted message:\n{decrypted_message}")


def encrypt(message, key):
    # Creates a 5 X 5 matrix from the key
    matrix = make_code(key)
    encrypted_message = ""
    split_message = []
    # This loop splits message into pairs of two characters
    for i in range(0, len(message), 2):
        split_message.append(message[i:i+2])

    for pair in split_message:
        letter_1 = pair[0]
        letter_2 = pair[1]
        letter_1_index = [0, 0]
        letter_2_index = [0, 0]

        # This loop finds the index of each letter in the matrix
        for y in range(5):
            for x in range(5):
                if matrix[y][x] == letter_1:
                    letter_1_index = [y, x]
                elif matrix[y][x] == letter_2:
                    letter_2_index = [y, x]

        encrypted_pair = ""
        encrypted_letter_1 = ""
        encrypted_letter_2 = ""

        # These if statements figure out whether the two given letters make a
        # rectangle, row, or column in that order
        # If the two letter make a rectangle == True
        if ((abs(letter_1_index[0] - letter_2_index[0]) > 0) and
                (abs(letter_1_index[1] - letter_2_index[1]) > 0)):
            new_matrix = make_new_matrix(
                matrix, letter_1_index, letter_2_index, "rectangle")

            # This series of if statements decide when the new encrypted
            # letters should be. It does this by choosing the letter
            # opposite of the current letter in the rectangle
            if letter_1_index[0] < letter_2_index[0]:
                if letter_1_index[1] < letter_2_index[1]:
                    encrypted_letter_1 = new_matrix[0][-1]
                    encrypted_letter_2 = new_matrix[-1][0]
                else:
                    encrypted_letter_1 = new_matrix[0][0]
                    encrypted_letter_2 = new_matrix[-1][-1]
            elif letter_1_index[0] > letter_2_index[0]:
                if letter_1_index[1] < letter_2_index[1]:
                    encrypted_letter_1 = new_matrix[-1][-1]
                    encrypted_letter_2 = new_matrix[0][0]
                else:
                    encrypted_letter_1 = new_matrix[-1][0]
                    encrypted_letter_2 = new_matrix[0][-1]

            encrypted_pair = encrypted_letter_1 + encrypted_letter_2

        # If the two letter make a column == True
        elif (abs(letter_1_index[0] - letter_2_index[0]) > 0):
            if letter_1_index[0] < letter_2_index[0]:
                letter_2_index[0] += 1
            else:
                letter_1_index[0] += 1
            new_matrix = make_new_matrix(
                matrix, letter_1_index, letter_2_index, "column")

            # This section of code first resets the indexs for letter 1 and 2
            # for the new matrix. It then chooses the encrypted letter to be
            # one down from the current letter.
            if letter_1_index[0] < letter_2_index[0]:
                new_letter_1_y = 0
                new_letter_2_y = letter_2_index[0] - letter_1_index[0]
            else:
                new_letter_2_y = 0
                new_letter_1_y = letter_1_index[0] - letter_2_index[0]

            if letter_1_index[0] < letter_2_index[0]:
                encrypted_letter_1 = new_matrix[new_letter_1_y+1]
                encrypted_letter_2 = new_matrix[new_letter_2_y]
            else:
                encrypted_letter_1 = new_matrix[new_letter_1_y]
                encrypted_letter_2 = new_matrix[new_letter_2_y+1]

            encrypted_pair = "".join(
                [encrypted_letter_1[0], encrypted_letter_2[0]])

        # If the two letter make a row == True
        elif (abs(letter_1_index[1] - letter_2_index[1]) > 0):
            if letter_1_index[1] < letter_2_index[1]:
                letter_2_index[1] += 1
            else:
                letter_1_index[1] += 1
            new_matrix = make_new_matrix(
                matrix, letter_1_index, letter_2_index, "row")

            # This section of code first resets the indexs for letter 1 and 2
            # for the new matrix. It then chooses the encrypted letter to be
            # one right from the current letter.
            if letter_1_index[1] < letter_2_index[1]:
                new_letter_1_x = 0
                new_letter_2_x = letter_2_index[1] - letter_1_index[1]
            else:
                new_letter_2_x = 0
                new_letter_1_x = letter_1_index[1] - letter_2_index[1]

            if letter_1_index[1] < letter_2_index[1]:
                encrypted_letter_1 = new_matrix[0][new_letter_1_x+1]
                encrypted_letter_2 = new_matrix[0][new_letter_2_x]
            else:
                encrypted_letter_1 = new_matrix[0][new_letter_1_x]
                encrypted_letter_2 = new_matrix[0][new_letter_2_x+1]

            encrypted_pair = "".join(
                [encrypted_letter_1[0], encrypted_letter_2[0]])

        encrypted_message += encrypted_pair

    return encrypted_message.upper()


def decrypt(message, key):
    # Creates a 5 X 5 matrix from the key
    matrix = make_code(key)
    decrypted_message = ""
    split_message = []
    for i in range(0, len(message), 2):
        split_message.append(message[i:i+2])

    for chunk in split_message:
        letter_1 = chunk[0]
        letter_2 = chunk[1]
        letter_1_index = [0, 0]
        letter_2_index = [0, 0]

        # This loop finds the index of each letter in the matrix
        for y in range(5):
            for x in range(5):
                if matrix[y][x] == letter_1:
                    letter_1_index = [y, x]
                elif matrix[y][x] == letter_2:
                    letter_2_index = [y, x]

        encrypted_pair = ""
        encrypted_letter_1 = ""
        encrypted_letter_2 = ""

        # These if statements figure out whether the two given letters make
        # a rectangle, row, or column in that order
        # If the two letters make a rectangle == True
        if ((abs(letter_1_index[0] - letter_2_index[0]) > 0)
           and (abs(letter_1_index[1] - letter_2_index[1]) > 0)):
            new_matrix = make_new_matrix(
                matrix, letter_1_index, letter_2_index, "rectangle")

            # This series of if statements decide when the new encrypted
            # letters should be. It does this by choosing the letter
            # opposite of the current letter in the rectangle
            if letter_1_index[0] < letter_2_index[0]:
                if letter_1_index[1] < letter_2_index[1]:
                    encrypted_letter_1 = new_matrix[0][-1]
                    encrypted_letter_2 = new_matrix[-1][0]
                else:
                    encrypted_letter_1 = new_matrix[0][0]
                    encrypted_letter_2 = new_matrix[-1][-1]
            elif letter_1_index[0] > letter_2_index[0]:
                if letter_1_index[1] < letter_2_index[1]:
                    encrypted_letter_1 = new_matrix[-1][-1]
                    encrypted_letter_2 = new_matrix[0][0]
                else:
                    encrypted_letter_1 = new_matrix[-1][0]
                    encrypted_letter_2 = new_matrix[0][-1]

            encrypted_pair = encrypted_letter_1 + encrypted_letter_2

        # If the two letters make a column == True
        elif (abs(letter_1_index[0] - letter_2_index[0]) > 0):
            if letter_1_index[0] < letter_2_index[0]:
                letter_1_index[0] -= 1
            else:
                letter_2_index[0] -= 1
            new_matrix = make_new_matrix(
                matrix, letter_1_index, letter_2_index, "column")

            # This section of code first resets the indexs for letter 1 and 2
            # for the new matrix. It then chooses the encrypted letter to be
            # one up from the current letter.
            if letter_1_index[0] < letter_2_index[0]:
                new_letter_1_y = 0
                new_letter_2_y = letter_2_index[0] - letter_1_index[0]
            else:
                new_letter_2_y = 0
                new_letter_1_y = letter_1_index[0] - letter_2_index[0]

            if letter_1_index[0] < letter_2_index[0]:
                encrypted_letter_1 = new_matrix[new_letter_1_y]
                encrypted_letter_2 = new_matrix[new_letter_2_y-1]
            else:
                encrypted_letter_1 = new_matrix[new_letter_1_y-1]
                encrypted_letter_2 = new_matrix[new_letter_2_y]

            encrypted_pair = "".join(
                [encrypted_letter_1[0], encrypted_letter_2[0]])

        # If the two letters make a row == True
        elif (abs(letter_1_index[1] - letter_2_index[1]) > 0):
            if letter_1_index[1] < letter_2_index[1]:
                letter_1_index[1] -= 1
            else:
                letter_2_index[1] -= 1
            new_matrix = make_new_matrix(
                matrix, letter_1_index, letter_2_index, "row")

            # This section of code first resets the indexs for letter 1 and 2
            # for the new matrix. It then chooses the encrypted letter to be
            # one right from the current letter.
            if letter_1_index[1] < letter_2_index[1]:
                new_letter_1_x = 0
                new_letter_2_x = letter_2_index[1] - letter_1_index[1]
            else:
                new_letter_2_x = 0
                new_letter_1_x = letter_1_index[1] - letter_2_index[1]

            if letter_1_index[1] < letter_2_index[1]:
                encrypted_letter_1 = new_matrix[0][new_letter_1_x]
                encrypted_letter_2 = new_matrix[0][new_letter_2_x-1]
            else:
                encrypted_letter_1 = new_matrix[0][new_letter_1_x-1]
                encrypted_letter_2 = new_matrix[0][new_letter_2_x]

            encrypted_pair = "".join(
                [encrypted_letter_1[0], encrypted_letter_2[0]])

        decrypted_message += encrypted_pair

    cleaned_decrypted_message = ""

    # This loop removes all necessary "x"s
    for i in range(len(decrypted_message)):
        if (decrypted_message[i] == "x"
                and i < (len(decrypted_message) - 1)
                and i > 0):
            if decrypted_message[i-1] == decrypted_message[i+1]:
                pass
            else:
                cleaned_decrypted_message += decrypted_message[i]
        elif decrypted_message[i] == "x" and i == (len(decrypted_message)-1):
            pass
        else:
            cleaned_decrypted_message += decrypted_message[i]

    return cleaned_decrypted_message.upper()


# This function returns a 5 X 5 matrix based on the key given
def make_code(key):
    matrix = [[0] * 5 for i in range(5)]
    code = key

    # This loop makes the code to have 25 characters with the key first
    # and then the alphabet with no duplicates
    accumulator = 0
    while len(code) < 25:
        if accumulator > 24:
            accumulator = 0
        if not alphabet[accumulator] in code:
            code += alphabet[accumulator]
        accumulator += 1
    # This loop fills the matrix one by one with the string 'code'
    accumulator = 0
    for y in range(5):
        for x in range(5):
            matrix[y][x] = code[accumulator]
            accumulator += 1
    return matrix


# This function returns a string with 'x' in between duplicate letters
# This function also adds 'x' to end of the string
# if the amount of characters are odd
def modify_message(message):
    modified_message = ""
    for letter in message:
        if len(modified_message) == 0:
            if letter == "u":
                modified_message += "v"
            elif letter == "q":
                modified_message += "k"
            else:
                modified_message += letter
        else:
            if letter != modified_message[-1]:
                if letter == "u":
                    modified_message += "v"
                elif letter == "q":
                    modified_message += "k"
                else:
                    modified_message += letter
            else:
                modified_message += "x"+letter

    if not (len(modified_message) % 2 == 0):
        modified_message += "x"

    return modified_message


# This function returns a new matrix of the characters
# between and including letter 1 and letter 2
# Takes "rectangle", "column", or "row" in order
# to specify which shape should be made by the matrix
def make_new_matrix(matrix, index_1, index_2, classifier):
    y_length = abs(index_1[0] - index_2[0]) + 1
    x_length = abs(index_1[1] - index_2[1]) + 1
    new_matrix = [[0] * x_length for i in range(y_length)]

    # Creates a list of the indexes letter 1 and 2 surround
    # including their own indexes
    y_range = (range(index_1[0], index_2[0]+1) if index_1[0] < index_2[0]
               else range(index_2[0], index_1[0]+1))
    x_range = (range(index_1[1], index_2[1]+1) if index_1[1] <
               index_2[1] else range(index_2[1], index_1[1]+1))

    # Prevents errors by checking whether the last value is 5
    # and if so it will correct it by not adding 1
    if y_range[-1] == 5:
        y_range = (range(index_1[0], index_2[0]) if index_1[0] < index_2[0]
                   else range(index_2[0], index_1[0]))
    if x_range[-1] == 5:
        x_range = (range(index_1[1], index_2[1]) if index_1[1] < index_2[1]
                   else range(index_2[1], index_1[1]))

    # Creates a string of every character letter 1 and 2
    # surround including themselves
    string = ""
    for x in x_range:
        for y in y_range:
            string += matrix[y][x]

    # Creates a variable that holds a letter to wrap around to
    if classifier == "column":
        wrapped_letter = matrix[0][x_range[-1]]
    elif classifier == "row":
        wrapped_letter = matrix[y_range[-1]][0]
    else:
        wrapped_letter = string[0]

    # Fills in new matrix given the string in the previous for loop
    accumulator = 0
    for x in range(x_length):
        for y in range(y_length):
            if accumulator < len(string):
                new_matrix[y][x] = string[accumulator]
                accumulator += 1
            else:
                new_matrix[y][x] = wrapped_letter
    return new_matrix


def error_checker(message):
    for letter in message:
        if letter == "u":
            print("Invalid character: u")
            return False
        if letter == "q":
            print("Invalid character: q")
            return False
        if not (len(message) % 2 == 0):
            print("Invalid input: String not even amount of characters")
            return False

    return True


main()
