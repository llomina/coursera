#9.4 Write a program to read through the mbox-short.txt and 
#figure out who has the sent the greatest number of mail messages. 
#The program looks for 'From ' lines and 
#takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary 
#that maps the sender's mail address to a count of the number of times 
#they appear in the file. After the dictionary is produced, 
#the program reads through the dictionary using a maximum loop to 
#find the most prolific committer.
#
#cwen@iupui.edu 5
#

addresses = list()
name = raw_input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = 0
for line in handle:
    if not line.startswith("From ") : continue
    #count
    count = count + 1
    #get second word
    wordgroup = line.split()   
    addresses.append(wordgroup[1])
for x in range(len(addresses)):
    address =addresses[x]

#make the dictionary    
d = dict()
#add addresse
for at in addresses:
    d[at] = d.get(at,0) + 1

#counting    
bigcount = None
chatty = None
for word,count in d.items():
	if bigcount is None or count > bigcount:
		chatty = word
		bigcount = count
print chatty, bigcount