import sys

def main():
    infile = open(sys.argv[1])
    outfile = open(sys.argv[2], 'w')
    spamsent = sys.argv[3]

    if spamsent == 'SPAM':
        s1 = 'SPAM'
        s2 = 'HAM'
    elif spamsent == 'SENT':
        s1 = 'NEG'
        s2 = 'POS'

    for line in infile:
        if line[0] == '-':
            outfile.write(s1 + '\n')
        else:
            outfile.write(s2 + '\n')

if __name__ == '__main__':
    main()
