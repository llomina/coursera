largest = 0
smallest = None
while True:
    line = raw_input('Enter a number: ')
    try:
        ival = int(line)
    except:
        ival = -1
    if ival > 0:
        if largest < ival:
            largest = ival
        if smallest is None or smallest > ival:
            smallest = ival
    elif line == 'done':
        break
    else:
        print 'Invalid input'
    if line == 'done':
        break
print "Maximum is", largest
print "Minimum is", smallest



#Enter a number: 4
#Enter a number: 5
#Enter a number: bad data
#Invalid input
#Enter a number: 7
#Enter a number: done