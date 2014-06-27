#indefinite loop with stop command
count = 0
total = 0
while True:
    line = raw_input('Enter a number: ')
    #added debug secton if not number
    try:
        ival = int(line)
    except:
        ival = -1
    if ival > 0:
        ival = float(ival)
#        print line
        #ival = ival
        #calculate count:
        count = count + 1
#        print 'Count: ', count
        
        #calculate total        
        total = total + ival
#        print 'Total: ', total
        
        #calculate average
        average = total / count
#        print 'Average: ', average
    elif line == 'done':
        break
    else:
        print 'Invalid Input'
    #end debug section
    if line == 'done':
        break
 #   print line
print 'Done!'
#print total, count, average
print total, count, average