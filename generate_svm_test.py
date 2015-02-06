import sys

def convert_line(line, vdict):
    result  = ""
    words = line.split()
    counts = {}

    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    for word in sorted(counts):
        if word in vdict:
            result += str(vdict[word]) + ':' + str(counts[word]) + ' '

    return result
        
def main():
    trainfile = open(sys.argv[1])
    vocabfile = open(sys.argv[2])
    svminfile = open(sys.argv[3], 'w')

    vocab = [line.strip() for line in vocabfile]
    vdict = {vocab[i]:i+1 for i in range(len(vocab))}

    for line in trainfile:
        svminfile.write('0 ' + convert_line(line, vdict) + '\n')

if __name__ == '__main__':
    main()
