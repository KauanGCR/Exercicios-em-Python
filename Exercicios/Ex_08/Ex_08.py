# Write a program to read through the mail box data and when you find
# ...line that starts with “From”, you will split the line into words using the
# ...split function. We are interested in who sent the message, which is the
# ...second word on the From line.

han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])

