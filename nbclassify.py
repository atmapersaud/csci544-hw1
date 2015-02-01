import sys
import json

def classify(dictionary, doc):
    classprobs = [compute_classprob(dictionary, key, doc) for key in dictionary]
    #need to get argmax

def compute_classprob(dictionary, docclass, doc):
    classdict = dictionary[docclass]
    condprobs = [compute_wordprob(classdict,word) for word in doc]
    return log(classdict['PRIOR']) + sum(condprobs)

def compute_wordprob(classdict, word):
    if word in classdict:
        log((classdict[word]+1)/classdict['N+k'])
    else:
        log(1/classdict['N+k'])

def compute_class_statistics(dictionary):
    num_doc_vec = [dictionary[key]['NUM_DOCS'] for key in dictionary]
    num_docs = sum(num_doc_vec)

    for key in dictionary:
        classdict = dictionary[key]
        classdict['PRIOR'] = classdict['NUM_DOCS'] / num_docs
        classdict['VOCAB'] = len(classdict)-3 # don't want to count NUM_DOCS, NUM_WORDS or PRIOR
        classdict['N+k'] = classdict['NUM_WORDS']+classdict['VOCAB']

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
