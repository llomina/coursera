#Exercise 1
hours = raw_input("Enter your hours: ")
rate = raw_input("Enter your pay rate: ")
hours = float(hours)
print type(hours)
if hours <= 40.0:
	pay = float(hours) * float(rate)
if hours > 40.0:
	overtime = hours - 40
	print overtime
	overtime_rate = 1.5 * float(rate)
	print overtime_rate
	print overtime_rate * overtime
	print hours
	pay = ((float(hours) - float(overtime)) * float(rate)) + (float(overtime) * float(overtime_rate))
print pay