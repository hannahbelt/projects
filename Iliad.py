

def search(search_term, filename):
    with open(filename) as iliad:
         # how many times our search_term has occurred
        term_count = 0
        # how many lines contain at least two of our search_term
        mult_term_line = 0
        # lowercase because of line.lower() below -- we want to compare lowercase only against lowercase
        search_term = search_term.lower()
        for line in iliad:
            line = line.lower()
            if search_term in line:
                # however many times our search_term has already occurred, add the number that are in this line
                term_count += line.count(search_term)
                if line.count(search_term) > 1:
                    # print(line)
                    mult_term_line += 1

        return [search_term, mult_term_line, term_count]

def print_data(search_term, mult_term_line, term_count):
        if mult_term_line != 1:
            times = 'times'
        else:
            times = 'time'

        print(f'{search_term} was in The Iliad {term_count} times')
        print(f'It was on the same line multiple times {mult_term_line} {times}, which will have printed out above unless the answer was zero')

if __name__== '__main__':
    filename = 'iliad.txt'
    term_list = search('Ajax', filename)
    print_data(term_list[0], term_list[1],term_list[2])