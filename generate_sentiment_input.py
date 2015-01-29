import os
import string

filenames = os.listdir('data/SENTIMENT_training')
outfile = open('sentiment_training.txt', 'w')

remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

for filename in filenames:
    if filename[0] == 'P':
        outfile.write('POS ')
    elif filename[0] == 'N':
        outfile.write('NEG ')
    infile = open('data/SENTIMENT_training/' + filename, errors='ignore')
    infiletext = infile.read()
    infiletext = infiletext.replace('\n', ' ')
    infiletext = infiletext.translate(remove_punctuation_map)
    outfile.write(infiletext + '\n')
    infile.close()

outfile.close()
