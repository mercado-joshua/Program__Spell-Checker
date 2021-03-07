letters = ['h', 'z', 'a', 'p', 'u', 'c', 't']
needed_letter = 't'

count = 1
four_word_list = []
five_word_list = []

for chars in letters:
    start = chars

    for second in letters:
        for third in letters:
            for fourth in letters:
                print(f'{start}{second}{third}{fourth}')
                four_word_list.append(f'{start}{second}{third}{fourth}')
                for fifth in letters:
                    print(f'{start}{second}{third}{fourth}{fifth}')
                    five_word_list.append(f'{start}{second}{third}{fourth}{fifth}')