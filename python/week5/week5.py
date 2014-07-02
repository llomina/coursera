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

while True:
    line = raw_input('> ')
    if line == 'done':
        break
    print line
print 'Done!'