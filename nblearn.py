import sys
import json

def update_dict(dictionary, doc_class, doc):
    if doc_class not in dictionary:
        dictionary[doc_class] = {}
        dictionary[doc_class]['NUM_DOCS'] = 1
    else:
        dictionary[doc_class]['NUM_DOCS'] += 1

    for word in doc:
        if word not in dictionary[doc_class]:
            dictionary[doc_class][word] = 1
        else:
            dictionary[doc_class][word] += 1
    
def main():
    trainfile = open(sys.argv[1])
    modelfile = open(sys.argv[2], 'w')

    wc_dict = {}

    for line in trainfile:
        words = line.split()
        update_dict(wc_dict, words[0], words[1:])

    json.dump(wc_dict, modelfile)
    
    trainfile.close()
    modelfile.close()

if __name__ == '__main__':
    main()
