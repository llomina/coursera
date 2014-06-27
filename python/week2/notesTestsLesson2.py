#Notes from Lesson 2
#constants are not variables, you can use single or double quotes.
#variable naming rules: start with underscores or letters, contains that or numbers, case sensitive

#reserved: and del for is raise assert elif from lambda return break else global not try class except if or while continue exec import pass yeild def finally in print

#operators are +(addition) -(subtract) *(multiplication) /(division) **(power) %(remainder)

yy = 5280
zz = yy / 1000
print zz
#5 is the integer answer of 5280/1000 (no remainder unless specified)
jj = 23
kk = jj % 5
print kk
#3 is the remainder of 23/5
print 4**3
#64 is 4 cubed

#Order of evaluation happens
#parenthesis, exponent, (mult, division, remainder), addition and subtraction, left to right

x = 1 + 2 ** 3 / 4 * 5

#1 + (8) / 4 * 5
#1 + (2) * 5
#1 + (10)
#11
print x
#Python Integer Division in weird. Integer division truncates (no remainder), and floating point division produces dloating point numbers
print 10/2
#5
print 10.0/2.0
#5.0
print 99.0/100
#0.99
xy = 97.0/100
print xy
#0.97

#2.2
#python understnads types (difference between strings, numbers, variables, literals)
#+ means addition and concatenate
# you can ask what type a variable is
print type("hello")
#<type 'str'>
print float(95)/100
#.95
# putting quotes around a number means convert integer to string
sval = '123'
print type(sval)
# "int()" means convert string to integer
# "float()" means convert string to decimal number
ival = int(sval)
print type(ival)
#you can't actually convert a string to an integer if it's not really a number

#you can create a prompt for something, this is a function
nam=raw_input('enter your name? ')
print 'welcome', nam

#numbers start at 0
#raw input is a string!



#starting word counting program
#get the name of the file and open it
name = raw_input("Enter file: ")
handle = open(name, "r")
text = handle.read()
words = text.split()

#count word frequency
counts = dict()
for word in words:
	counts[word] = counts.get(word,0)+1
	
#find the most common word
bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count
		
#all done
print bigword, bigcount

#guessing
#hours = raw_input("Enter file: ")
#rate = raw_input("Enter file: ")
#pay = float(hours) * float(rate)
#print "Your pay is $"pay




