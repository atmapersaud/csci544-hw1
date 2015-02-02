import os
import string

filenames = os.listdir('data/SPAM_test')
outfile = open('spam_test.txt', 'w')

remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

for filename in filenames:
    infile = open('data/SPAM_test/' + filename, errors='ignore')
    infiletext = infile.read()
    infiletext = infiletext.replace('\n', ' ')
    infiletext = infiletext.translate(remove_punctuation_map)
    outfile.write(infiletext + '\n')
    infile.close()

outfile.close()
