import random

extended_ascii_list_beggining = [chr(i) for i in range(256)]
bad_chars = ['', ' ', ',', ', ', '\\', '\`', '\"', '\b', '\f', '\n', '', '', '\r', '\t', '\t', 'uxxxx', 'Uxxxxxxxx', '\ooo', 'xhh', '\ ','\\ ', '\` ', '\" ', '\b ', '\f ', '\n ', ' ', ' ', '\r ', '\t ', '\t ', 'uxxxx ', 'Uxxxxxxxx ', '\ooo ', 'xhh ', '\ ' ]
extended_ascii_list = [x for x in extended_ascii_list_beggining if str(x) not in bad_chars]

while True:
    char_from_list = str(extended_ascii_list[random.randint(0, 246)])
    print(char_from_list, end = ' ')

    
