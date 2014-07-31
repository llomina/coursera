#list is ordered, dictionary is bag of stuff
#otherwise very similar
#dictionary reads labels

#creates dicitonary
counts=dict()
#list of names
names = ['csev', 'cwen', 'zquan', 'cwen']
#look each of the items in the dictionary
for name in names:
#count how many times each one occurs by looking for each 
#one and adding one more to count each time it is found
    counts[name] = counts.get(name,0) +1
#print the     
print counts
    