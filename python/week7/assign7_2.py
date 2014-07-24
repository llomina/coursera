#7.2 Write a program that prompts for a file name, then opens that file and 
#reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines 
#and compute the average of those values and produce an output as shown below.
#when you are testing below enter mbox-short.txt as the file name.


# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
average = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #count
    count = count + 1
    #get the total
    indexnumber =  line.find(':')
    indexnumber =  indexnumber + 1
    chunk =  line[indexnumber:]
    stripchunk = chunk.strip()
    result = float(stripchunk)
    total = result + total
    #get the average
    average = total/count
print "Average spam confidence: ", average