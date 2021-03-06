import os
import string

filenames = os.listdir('data/SENTIMENT_test')
filenames.sort()
outfile = open('sentiment_test.txt', 'w')

remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

for filename in filenames:
    infile = open('data/SENTIMENT_test/' + filename, errors='ignore')
    infiletext = infile.read()
    infiletext = infiletext.replace('\n', ' ')
    infiletext = infiletext.translate(remove_punctuation_map)
    outfile.write(infiletext + '\n')
    infile.close()

outfile.close()
