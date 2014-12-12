__author__ = 'jakesawyer'

from gensim import corpora, models, similarities
import sys, os

class MyCorpus(object):
    def __init__(self, fn):
        self.fn = fn

    def __iter__(self, fn):
        for line in open('%s'%self.fn):
            yield dictionary.doc2bow(line.lower().split())

def stream_dict(filen):
    dictionary = corpora.Dictionary(line.lower().split() for line in open('%s'%filen))
    dictionary.compactify()
    dictionary.save('/dictionary/%s_dict'%filen)
    print(dictionary)

def main():
    print "hello"
    current_dir = os.getcwd()
    car_makes = []
    for (dirpath, dirnames, filenames, filepath) in os.walk('../../edmunds/data/run001/'):
        car_makes.append(str(filepath))
    print(car_makes)


if __name__ == "__main__":
    main()