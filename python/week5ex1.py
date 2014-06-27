count = 0
total = 0
while True:
    line = raw_input('Enter a number: ')
    try:
        ival = int(line)
    except:
        ival = -1
    if ival > 0:
        ival = float(ival)
        count = count + 1
        total = total + ival
        average = total / count
    elif line == 'done':
        break
    else:
        print 'Invalid Input'
    if line == 'done':
        break
print total, count, average