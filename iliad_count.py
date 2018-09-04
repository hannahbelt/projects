with open('iliad.txt') as iliad:
    most_common_word = {}
    for line in iliad:
        # print(line)
        # break
        word_list = line.split()
        # print(word_list)
        # break
        for word in word_list:
            most_common_word[word] = most_common_word.get(word, 0) + 1

            