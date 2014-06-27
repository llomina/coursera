#Exercise 1 and 2
hours = raw_input("Enter your hours: ")
rate = raw_input("Enter your pay rate: ")
try:
	hours = float(hours)
except: 
	print "Please enter a numeric value for your hours"
try:
	rate = float(rate)
except: 
	print "Please enter a numeric value for your rate"
if hours > 40.0:
	hours = float(hours)
	rate = float(rate)
	overtime = hours - 40
	overtime = float(overtime)
	overtime_rate = 1.5 * float(rate)
	pay = ((hours - overtime) * rate) + (overtime * float(overtime_rate))
	print pay
	
else:
#	hours <= 40.0
	rate = float(rate)
	pay = hours * float(rate)
	print pay

