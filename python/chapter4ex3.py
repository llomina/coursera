#Exercise 3
score = raw_input("Enter score: ")
try:
	score = float(score)
except: 
	print "Please enter a numeric value for your score"
#score = float(score)	
if score > 1.0:
	print  "Your score is out of range. Please enter a numeric value for your score between 0.0 and 1.0"

elif score >= 0.9:
	print "A"

elif score >= 0.8:
	print "B"

elif score >= 0.7:
	print "C"

elif score >= 0.6:
	print "D"	
	
else:
#	score >= 0.5
	print "F"

