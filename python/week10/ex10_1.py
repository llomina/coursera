#10.2 Write a program to read through the mbox-short.txt and 
#figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by 
#finding the time and 
#then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, 
#print out the counts, 
#sorted by hour as shown below. 
#Note that the autograder does not have support for the sorted() function.
#

#Desired Output
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1

#below is the text from assign 9

times = list()
counts=dict()
#get file
name = raw_input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
#find the From lines
for line in handle:
    if not line.startswith("From ") : continue
    #get second word
    wordgroup1 = line.split()
#    print wordgroup1
    wordgroup2 = wordgroup1[5].split(':') 
#    print wordgroup2
    times.append(wordgroup2[0])

for time in times:
#count how many times each one occurs by looking for each 
#one and adding one more to count each time it is found
    counts[time] = counts.get(time,0) +1
#sort the vales and keys    
sorted = counts.items()
sorted.sort()
#print the vales and keys    

for key, val in sorted :
    print key, val
