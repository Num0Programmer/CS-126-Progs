###############################################################################
# Date: Fri. -- Oct. 23rd, 2020                                               #
# Contributor Name(s): Asa Henry | Zoe Allison | Joshua Heinz                 #
# Contributor Email(s): ajh728@nau.edu | zda23@nau.edu | [jah957@nau.edu]     #
###############################################################################

# Notes:
# * To solve the extra credit problem, and keep using the dictionary approach
#   could just go ahead and make a tuple which includes each layer of the lett-
#   er, then tell Python to print the lines of the respective letters. Might
#   need to restric the width of the window where the letters/banner phrase
#   is displayed for cutoff and displayment reasons. IDK I wanna be a Game
#   dev, not a Software dev. 



# Main
def main():
    # Setup var(s)
    ASCII_chars = {
        ' ' : ' '
              ' '
              ' '
              ' '
              ' ',
        'a' : ['    A     ',
               '   A A    ',
               '  AAAAA   ',
               ' A     A  ',
               'A       A '],
        'b' : ['BBBBBBBB  ',
               'BB     BB ',
               'BBBBBBBB  ',
               'BB     BB ',
               'BBBBBBBB  '],
        'c' : ['    CCCCC ',
               ' CCCC     ',
               'CC        ',
               ' CCCC     ',
               '    CCCCC '],
        'd' : ['DDDDDDD   ',
               'DD      DD',
               'DD      DD',
               'DD      DD',
               'DDDDDDD   '],
        'e' : ['EEEEEEE   ',
               'EE        ',
               'EEEEEE    ',
               'EE        ',
               'EEEEEEE   '],
        'f' : ['FFFFFFFF  ',
               'FF        ',
               'FFFFF     ',
               'FF        ',
               'FF        '],
        'g' : [' GGGGGG   ',
               'G         ',
               'G   GGGG  ',
               'G      G  ',
               ' GGGGGG   '],
        'h' : ['H     H   ',
               'H     H   ',
               'HHHHHHH   ',
               'H     H   ',
               'H     H   '],
        'i' : ['IIIIIIIIII',
               '    II    ',
               '    II    ',
               '    II    ',
               'IIIIIIIIII'],
        'j' : ['JJJJJJJ   ',
               '     JJ   ',
               '     JJ   ',
               '     JJ   ',
               ' JJJJ     '],
        'k' : ['K    K    ',
               'K  KK     ',
               'KKK       ',
               'K  KK     ',
               'K    K    '],
        'l' : ['LL        ',
               'LL        ',
               'LL        ',
               'LL        ',
               'LLLLLL    '],
        'm' : ['MMM   MMM ',
               'M  M M  M ',
               'M   M   M ',
               'M       M ',
               'M       M '],
        'n' : ['NN    N   ',
               'N N   N   ',
               'N  N  N   ',
               'N   N N   ',
               'N    NN   '],
        'o' : ['  OOOO    ',
               'OO    OO  ',
               'OO    OO  ',
               'OO    OO  ',
               '  OOOO    '],
        'p' : ['PPPPPPP   ',
               'PP   PP   ',
               'PPPPPPP   ',
               'PP        ',
               'PP        '],
        'q' : ['QQQQQQQQQ ',
               'QQ     QQ ',
               'QQ    QQQ ',
               'QQQQQQQQQ ',
               '        QQ'],
        'r' : ['RRRRRRRR  ',
               'RR   RR   ',
               'RR RR     ',
               'RR   RR   ',
               'RR     RR '],
        's' : [' SSSSS    ',
               'SS        ',
               '  SSSS    ',
               '      SS  ',
               ' SSSSSS   '],
        't' : ['TTTTTTTTT ',
               '   TT     ',
               '   TT     ',
               '   TT     ',
               '   TT     '],
        'u' : ['U       U ',
               'U       U ',
               'U       U ',
               ' U     U  ',
               '  U U U   '],
        'v' : ['V       V ',
               ' V     V  ',
               '  V   V   ',
               '   V V    ',
               '    V     '],
        'w' : ['W       W ',
               'W       W ',
               'W   W   W ',
               ' WW W WW  ',
               '  W   W   '],
        'x' : ['XX     XX ',
               ' XX   XX  ',
               '   XXX    ',
               '  XX  XX  ',
               'XX      XX'],
        'y' : ['YY    YY  ',
               ' YY  YY   ',
               '   YY     ',
               '   YY     ',
               '   YY     '],
        'z' : ['ZZZZZZZZ  ',
               '      Z   ',
               '    Z     ',
               '  Z       ',
               'ZZZZZZZZ  ']
    }


    phrase = input("Phrase you would like to 'bannerize': ")
    banner_format = input("Orientation of banner (h = horizontal, v = vertical): ")


    if banner_format == 'h':
           banner = horiz_find_banner_art(phrase.lower(), ASCII_chars)
           display_banner_horiz(phrase, banner)
    else:
           banner = vert_find_banner_art(phrase.lower(), ASCII_chars)
           display_banner_vert(banner)





# Function(s)
# Vertical Printing
def vert_find_banner_art(phrase, ASCII_chars):
    banner = []

    for char in phrase:
       if ASCII_chars[char]:
              for row in ASCII_chars[char]:
                     chars = ''
                     line = ''
                     for elem in row:
                            chars += elem

                     line += chars
                     banner.append(line)

    return banner


def display_banner_vert(banner):
    for elem in banner:
        print(elem)




# Horizontal Printing
def horiz_find_banner_art(phrase, ASCII_chars):
       banner = []

       for tracker in range(5):
              for char in phrase:

                     if ASCII_chars[char]:
                            line = ''
                            for elem in ASCII_chars[char][tracker]:
                                   line += elem
                                   
                            banner.append(line)
                            line = ''

       return banner


def display_banner_horiz(phrase, banner):
       step_amount = (1 / 5)
       
       line1 = [banner[:int((0 + step_amount) * len(banner))]]
       line2 = [banner[int(((1 / 5) * len(banner))):int(((1 / 5) + step_amount) * len(banner))]]
       line3 = [banner[int(((2 / 5) * len(banner))):int(((2 / 5) + step_amount) * len(banner))]]
       line4 = [banner[int(((3 / 5) * len(banner))):int(((3 / 5) + step_amount) * len(banner))]]
       line5 = [banner[int(((4 / 5) * len(banner))):int(((4 / 5) + step_amount) * len(banner))]]


       line = ''
       for elem in line1:
              for char in elem:
                     line += char
       print(line)

       line = ''
       for elem in line2:
              for char in elem:
                     line += char
       print(line)

       line = ''
       for elem in line3:
              for char in elem:
                     line += char
       print(line)

       line = ''
       for elem in line4:
              for char in elem:
                     line += char
       print(line)

       line = ''
       for elem in line5:
              for char in elem:
                     line += char
       print(line)





# Call(s)
if __name__ == '__main__':
    main()
