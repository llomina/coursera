#week 5
n = 5
while n > 0:
    print n
    n = n-1
print 'Blastoff!'
# In English, While n is greater than 0, display the value of n and then reduce the value of n by 1. When you get to 0, exit the while statement and display the word Blastoff!

#while statement is "if statement is true", If the condition is true, execute the body and then go back to step 1.
#the second print statement would happen regardless (when you change the initial settin gof the variable to n = 0, it still prints blastoff.

#above has 5 "interations" in the loop

#For example, suppose you want to take input from the user until they type done. You could write:

#indefinite loop with stop command
while True:
    line = raw_input('> ')
    if line == 'done':
        break
    print line
print 'Done!'

#definite loop
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print 'Happy New Year:', friend
print 'Done!'


#to find the largest value in this list or sequence
largest = None
print 'Before:', largest
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print 'Loop:', itervar, largest
print 'Largest:', largest

#smallest is very similar
smallest = None
print 'Before:', smallest
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print 'Loop:', itervar, smallest
print 'Smallest:', smallest

#above is how to calculate it the hard way. 
#here is a function which uses the built in function min() 
#you can also do this with max()
def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest
    
    
    #count
count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print 'Count: ', count

#total
total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print 'Total: ', total