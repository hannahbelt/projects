with open('iliad.txt') as iliad:
    # a dictionary to collect words as keys and number of occurrences as the value
    most_common_words = {}
    for line in iliad:
        # print(line)
        # break
        # make a list of words out of each line
        word_list = line.split()
        # print(word_list)
        # break
        for word in word_list:
            # if a word is not yet in the most_common_words dictionary, add it
            # if the word is there already, increase the count by 1
            most_common_words[word] = most_common_words.get(word, 0) + 1
            
    most_common_word = None
    highest_count = None
    for word, count in most_common_words.items():
        # as we go through the most_common_words dictionary,
        # set the word and the count that's the biggest we've seen so far
        if highest_count is None or count > highest_count:
            most_common_word = word
            highest_count = count

    print(f'The most common word in The Iliad is: {most_common_word}')
    print(f'It is in The Iliad {highest_count} times')

            