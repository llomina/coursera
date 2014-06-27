import re
words = open('words.txt')
for line in words:
    line = line.rstrip()
    if re.search('[^qjx]+?', line) :
        print line