import os

filenames = os.listdir('data/SPAM_training')
outfile = open('spam_input.txt', 'w')

for filename in filenames:
    if filename[0] == 'H':
        outfile.write('HAM ')
    elif filename[0] == 'S':
        outfile.write('SPAM ')
    infile = open('data/SPAM_training/' + filename, errors='ignore')
    infiletext = infile.read()
    outfile.write(infiletext.replace('\n', ' ') + '\n')
    infile.close()

outfile.close()
