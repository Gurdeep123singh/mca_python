import pickle
def readFile(fname):
    with open (fname,'rb') as f:
        for x in f:
            g=pickle.load(x)
            print(g)

fname="b.txt"
readFile(fname)