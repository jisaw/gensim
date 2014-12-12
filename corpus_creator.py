__author__ = 'jakesawyer'

from gensim import corpora, models, similarities
import sys, os
from lxml import etree

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
    for (dirpath, dirnames, filenames) in os.walk('../../edmunds/data/run001'):
        car_makes.append(str(dirpath))
    count =0
    # f = open("cars.txt", "a")
    for car in car_makes[1:]:
        print(car)
        files = os.listdir(car)
        for f in files:
            tree = etree.parse(open(str(car +"/" + f), 'r'))
            root = tree.getroot()
            print root.children()
            count += 1
    print(count)
        #for thread in files:
            #df = pd.read_json(car+thread)
            #for i in df['body']:
            #    f.write(str(i))




if __name__ == "__main__":
    main()