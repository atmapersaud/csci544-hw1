import sys

def main():
    trainfile = open(sys.argv[1])
    vocabfile = open(sys.argv[2], 'w')

    vocab = set()

    for line in trainfile:
        for word in line.split():
            vocab.add(word)

    sortedvocab = sorted(vocab)

    for word in sortedvocab:
        vocabfile.write(word + '\n')

    trainfile.close()
    vocabfile.close()

if __name__ == '__main__':
    main()
