#Comparison Operators
# < less than
# <= less than or equal to
# >= greater than or equal to
# == equal to
# != not equal to
# = is used only for assignment (for variables, etc.)

#One way decisions
#Conditional steps Program
x=5
if x < 10:
    print 'Smaller'
if x > 10:
    print 'Bigger'
print 'Finis'
# comments don't matter, blank linkes don't matter, tab vs spaces do matter

#Two way decisions
x=4
if x > 2:
    print 'Bigger'
else :
    print 'Smaller'
print 'All Done'

#Multi way if
x=4
if x < 2:
    print 'Small'
elif x < 10:
    print 'Medium'
else :
    print 'LARGE'
print 'All Done'

#in a multiway you don't actually need an "else"


#try and except
#$ cat notry.py
astr = 'Hello Bob'
try: 
    istr = int(astr)
except:
    istr=-1
print 'First', istr

astr = '123'
try:
    istr = int(astr)
except:
    istr=-1
print 'Second', istr


#sample try/ except
rawstr = raw_input('Enter a number:')

try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print 'Nice work'
else:
    print 'Not a number'
    
