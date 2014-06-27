# Info to make ISBN Hyphenator

#add emprt convert isbn
convertisbn = 0
#get isbn from user
isbn1 = raw_input("Enter ISBN-13: ")

#INFO 1. prefix, always 3

#TO DO
#change variable convertisbn to first three numbers, - , last 7 numbers
#convertisbn = 





#INFO 2. The allocated group IDs are: 0–5, 600–621, 7, 80–94, 950–989, 9927–9989, and 99901–99972

#TO DO
#add elif statements to separate based on if the strings match these codes
#if [2] in string (# after -) is 0–5, add hyphen after 1 digit, else go on
#if [2] in string (# after -) is 7, add hyphen after 1 digit, else go on
#if [2][3] in string (2#s after -) are in the range 80-94, add hyphen after 2 digits, else go on
#if [2][3][4] in string (3#s after -) are in the range 600–621, add hyphen after 3 digits, else go on
#if [2][3][4] in string (3#s after -) are in the range 950–989, add hyphen after 3 digits, else go on
#if [2][3][4][5] in string (4#s after -) are in the range 9927–9989, add hyphen after 4 digits, else go on
#if [2][3][4][5][6] in string (5#s after -) are in the range 99901–99972, add hyphen after 5 digits
#error checking?






#INFO 3.
#English-language publisher codes follow a systematic pattern, which allows their length to be easily determined, as follows:[28]
#Item number length 	

#0- group identifier 	
#           From 	        To 	            	
#6 digits 	0-00-xxxxxx-x 	0-19-xxxxxx-x 	 	
#5 digits 	0-200-xxxxx-x 	0-699-xxxxx-x 		
#4 digits 	0-7000-xxxx-x 	0-8499-xxxx-x 		
#3 digits 	0-85000-xxx-x 	0-89999-xxx-x 		
#2 digits 	0-900000-xx-x 	0-949999-xx-x 		
#1 digit 	0-9500000-x-x 	0-9999999-x-x 		
                                   	


#1- group identifier 	Total
#           From 	        To 	            
#6 digits 	1-00-xxxxxx-x 	1-09-xxxxxx-x 	 	
#5 digits 	1-100-xxxxx-x 	1-399-xxxxx-x 	 	
#4 digits 	1-4000-xxxx-x 	1-5499-xxxx-x 	 	
#3 digits 	1-55000-xxx-x 	1-86979-xxx-x 		
#2 digits 	1-869800-xx-x 	1-998999-xx-x 	
#1 digit 	1-9990000-x-x 	1-9999999-x-x 	


#TO DO
#add elif statements to separate based on if the strings match these codes
#error checking?




#INFO 4.something
#Actually, don't do anything here. Move on to the end.




#INFO 5. check digit, always 1
#TO DO
#change variable convertisbn to existing number 9 numbers, - , last digit
#convertisbn = 








#sample elif statement
#score = raw_input("Enter score: ")
#if score > 1.0:
#	print  "Your score is out of range. Please enter a numeric value for your score between 0.0 and 1.0"

#elif score < 0.0:
#	print  "Your score is out of range. Please enter a numeric value for your score between 0.0 and 1.0"
    
#elif score >= 0.9:
#	print "A"

#elif score >= 0.8:
#	print "B"

#elif score >= 0.7:
#	print "C"

#elif score >= 0.6:
#	print "D"	
    
#elif score < 0.6:
#	print "F"