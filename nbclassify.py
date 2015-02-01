import sys
import json

def classify(dictionary, doc):
    classprobs = [compute_classprob(dictionary, key, doc) for key in dictionary]
    #need to get argmax

def compute_classprob(dictionary, docclass, doc):
    #compute prior
    #compute conditional probability for each of the words in the doc

def main():
    modelfile = open(sys.argv[1])
    testfile = open(sys.argv[2])

    wc_dict = json.load(modelfile)

    num_doc_vec = [d[key]['NUM_DOCS'] for key in d]
    num_docs = sum(num_doc_vec)

    for line in testfile:
        pred = classify(wc_dict, line)
        print(pred)
    
if __name__ == '__main__':
    main()
