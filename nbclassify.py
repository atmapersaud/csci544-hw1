import sys
import json

def main():
    modelfile = open(sys.argv[1])
    testfile = open(sys.argv[2])

    wc_dict = json.load(modelfile)

    num_doc_vec = [d[key]['NUM_DOCS'] for key in d]
    num_docs = sum(num_doc_vec)
    
if __name__ == '__main__':
    main()
