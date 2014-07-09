#watch out! the print statements are commented out!

#all the below things need this fruit variable
fruit = 'pineapple'
love = 'tea'
library = 'books'
name = library + 'and' + love
#print name
#output is booksandtea
number = 9
username = name + str(number)
#print username
#output is booksandtea9

#NOTE: All raw input is string! even if numbers, must be converted

#print len(fruit)
#output is 6

length = len(fruit)
last = fruit[length-1]
#print last
# output is a, you have to do length-1 because length doesn't start at 0 like string stuff does

#print every letter forward (loop through the string)
index = 0
while index < len(fruit):
    letter = fruit[index]
#    print letter
    index = index + 1
    
#or this does the same thing as above, but is more ELEGANT
#had to comment out entire block or else there was an empty for loop.
#uncomment out next two lines to see it work
#for char in fruit:
#    print char
    
#print every letter backward
index = len(fruit)
while index > 0:
    last = fruit[index-1]
#    print last
    index = index - 1
    
#looping and counting
word = 'banana'
count = 0
for letter in word : 
    if letter == 'a':
        count = count + 1
#print count

s = 'Monty Python'
#print s[0:4]
# output is mont

#the second number is "up to but not including". 
#print s[6:7]
# output is p

#if the second number is beyond the end of the string, it will only go to the end 
#print s[6:20]
# output is python

#if you eave off the first #, it thinks "beginning", 
#if you eave off the second, it thinks "end", 
#if you eave off the both [:], it thinks "entire string", 

#string concatenation does not add spaces

#"in" operator
#fruit = 'pineapple'
#if 'n' in fruit:
#    print 'Found an n!'
#output is Found an n!, because the statement "'n' in fruit" is True

#String comparison
#greater than sorts alphabetically
if fruit < 'banana':
    print 'your word, '+ fruit + ', comes before banana.' 
elif fruit > 'banana':
    print 'your word, '+ fruit + ', comes after banana.' 
else:
    print 'All right, bananas.' 
#output is after statement. If you change "fruit" in this to "word", it will be bananas

#string library
greet = 'Hello Bob'
#this gives a lower case copy, but doesn't change greet
zap = greet.lower()
#print zap
# output is 'hello bob'

#dir 
#means what is a list of things that you can do with this data type

#str.capitalize

pos = fruit.find('apple')
#print pos
#output is 4
unpos =  fruit.find('ban')
#print unpos
#output is -1 (unfound)


#str.replace('findthis','replacewiththis') - for all occurances
#lstrip() - from left
#rstrip() - from right
#strip() - on left and right side
#str.startswith('start') - true false

#assignment
#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
indexnumber =  text.find(':')
#print indexnumber
#18
indexnumber =  indexnumber + 1
#print indexnumber
#19
chunk =  text[indexnumber:]
#print chunk
#    0.8475"
stripchunk = chunk.strip()
#print stripchunk
result = float(stripchunk)
print result


#0.8475

stx = "hello there bob how are you"
wds = stx.split()
print wds[2]