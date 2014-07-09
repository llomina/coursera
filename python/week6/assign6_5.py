text = "X-DSPAM-Confidence:    0.8475";
indexnumber =  text.find(':')
indexnumber =  indexnumber + 1
chunk =  text[indexnumber:]
stripchunk = chunk.strip()
result = float(stripchunk)
print result