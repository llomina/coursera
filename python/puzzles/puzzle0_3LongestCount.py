import re
words = open('words.txt')
for line in words:
    line = line.rstrip()
    results = re.findall('[^qjx]+?', line)
    if len(results) > 23 :
       print line
 #results are 
 #pathologicopsychological
 #scientificophilosophical
 #tetraiodophenolphthalein
 #thyroparathyroidectomize