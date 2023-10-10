# Exercise 5: Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence: 0.8475'
# Use find and string slicing to extract the portion of the string after the
# ...colon character and then use the float function to convert the extracted
# ...string into a floating point number.

str = 'X-DSPAM-Confidence: 0.8475'
print(str)

ipos = str.find(':')
#print('A posição dos dois pontos', ipos)

piece = str[ipos+1:]
#print('A parte a ser convertida é', piece)

value = float(piece)
print('O valor final é', value)