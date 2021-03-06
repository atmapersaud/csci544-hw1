import os
import string

filenames = os.listdir('data/SPAM_training')
outfile = open('spam_training.txt', 'w')

remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

for filename in filenames:
    if filename[0] == 'H':
        outfile.write('HAM ')
    elif filename[0] == 'S':
        outfile.write('SPAM ')
    infile = open('data/SPAM_training/' + filename, errors='ignore')
    infiletext = infile.read()
    infiletext = infiletext.replace('\n', ' ')
    infiletext = infiletext.translate(remove_punctuation_map)
    outfile.write(infiletext + '\n')
    infile.close()

outfile.close()
