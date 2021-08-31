with open('words.txt', 'r+') as read_file, open('words_filtered.txt', 'w+') as file_write_to:
    for line in read_file.readlines():
        line = line.lower()
        file_write_to.write(line)