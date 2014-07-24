#variables are not a collection
#variables- you can't put more than one thing in it
#lists can be nested or contain multiple types of things 
print [ 1, [5,6], blue]
#looking inside lists
friends = ['stalin', 'john', 'ride']
print friends[1]
#john (remember "elevator rules")

#strings can't change, only be copied. 
#lists can change!

#len(variable) counts the number of items in list
#range(variable) creates and returns a list
print range(4)
#[0,1,2,3]

#you can put these together to run through a string

friends = ['stalin', 'john', 'ride']
    for friend in friends :
    print 'Happy Blast Off, ', friend
 #this is the same as above, but use this one below if you need the count variable later   
for i in range(len(friends)):
        friend =friends[i]
        print 'Happy Blast Off, ', friend
        
#you can build a list with append
#us "in" and "not in" to check if a value is in the list

#sort() is automatically alphabetical, or numeric

#to find in lists
nums = [3, 41, 12, 9, 74, 15]
#count
print len(nums)
#max/min
print max(nums)
print min(nums)
#total
print sum(nums)
#average
print sum(nums)/len(nums)

#calculateing an average, better for smaller amount of numbers (100s of thousands)
numlist = list()
while true:
    inp = raw_input('enter a number')
    if inp = = 'done':break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print 'Average:',average    

#split
abc = 'with three words'
stuff = abc.split()
print stuff
print len(stuff)
print stuff[0]
#split splits on spaces, but only counts all spaces as one space
#you can also define what to split by, thing = line.split(';')


