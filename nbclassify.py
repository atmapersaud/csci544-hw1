import sys
import json
import math

def classify(dictionary, doc):
    classprobs = [compute_classprob(dictionary, key, doc) for key in dictionary]
    return max(classprobs, key=lambda x: x[1])[0]
    #return classprobs

def compute_classprob(dictionary, docclass, doc):
    classdict = dictionary[docclass]
    condprobs = [compute_wordprob(classdict,word) for word in doc.split()]
    return docclass, math.log(classdict['PRIOR']) + sum(condprobs)

def compute_wordprob(classdict, word):
    if word in classdict:
        return math.log((classdict[word]+1)/classdict['N+k'])
    else:
        return math.log(1/classdict['N+k'])

def compute_class_statistics(dictionary):
    num_doc_vec = [dictionary[key]['NUM_DOCS'] for key in dictionary]
    num_docs = sum(num_doc_vec)

    totalvocab = 0

    for key in dictionary:
        classdict = dictionary[key]
        classdict['PRIOR'] = classdict['NUM_DOCS'] / num_docs
        totalvocab += len(classdict)-3 # don't want to count NUM_DOCS, NUM_WORDS or PRIOR

    for key in dictionary:
        classdict = dictionary[key]
        classdict['N+k'] = classdict['NUM_WORDS']+totalvocab+1 # the +1 is for the unknown word

def main():
    modelfile = open(sys.argv[1])
    testfile = open(sys.argv[2])

    wc_dict = json.load(modelfile)

    compute_class_statistics(wc_dict)

    for line in testfile:
        pred = classify(wc_dict, line)
        print(pred)
    
if __name__ == '__main__':
    main()
