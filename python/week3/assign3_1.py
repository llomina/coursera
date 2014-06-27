#Exercise 1
hours = raw_input("Enter Hours: ")
rate = raw_input("Enter Pay Rate: ")
hours = float(hours)

if hours > 40.0:
	overtime = hours - 40
	overtime_rate = 1.5 * float(rate)
	pay = ((float(hours) - float(overtime)) * float(rate)) + (float(overtime) * float(overtime_rate))
    
else:
	pay = float(hours) * float(rate)
print pay