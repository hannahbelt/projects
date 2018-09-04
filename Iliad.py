with open('Iliad.txt') as iliad:
    term_count = 0
    mult_term_line = 0
    for line in iliad:
        # line = line.lower()
        if 'Achilles' in line:
            term_count += line.count('Achilles')
            if line.count('Achilles') > 1:
                # print(line)
                mult_term_line += 1

    print(term_count)
    print(mult_term_line)