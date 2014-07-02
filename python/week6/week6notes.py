#watch out! the print statements are commented out!

#all the below things need this fruit variable
fruit = 'pineapple'


#len(fruit)
#output is 6

length = len(fruit)
last = fruit[length-1]
#print last
# output is a, you have to do length-1 because length doesn't start at 0 like string stuff does

#print every letter forward
index = 0
while index < len(fruit):
    letter = fruit[index]
#    print letter
    index = index + 1
    
#or this does the same thing as above.
#had to comment out entire block or else there was an empty for loop.
#for char in fruit:
#    print char
    
#print every letter backward
index = len(fruit)
while index > 0:
    last = fruit[index-1]
#    print last
    index = index - 1
