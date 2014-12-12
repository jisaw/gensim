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
    print("\n\n\n\n\n STARTING \n\n\n\n\n")
    dictionary = corpora.Dictionary(line.lower().split("/*/*/") for line in open(filen))
    print("\n\n\n\n\n COMAPCTING \n\n\n\n\n")
    dictionary.compactify()
    print("\n\n\n\n\n SAVING \n\n\n\n\n\n")
    dictionary.save('cars.dict')
    print(dictionary)

def main():
    #print "hello"
    #current_dir = os.getcwd()
    #car_makes = []
    #for (dirpath, dirnames, filenames) in os.walk('../../edmunds/data/run001'):
    #    car_makes.append(str(dirpath))
    #count =0
    #f = open("cars.txt", "a")
    #for car in car_makes[1:]:
    #    print(car)
    #    files = os.listdir(car)
    #    for fl in files:
    #        tree = etree.iterparse(open(str(car +"/" + fl), 'r'))
    #        for action, elem in tree:
    #            if elem.tag == "body":
    #                f.write(elem.text.encode('utf-8'))
    #                f.write("/*/*/")
    #                count += 1
#
    #print(count)
    #f.close()
    stream_dict('cars.txt')
        #for thread in files:
            #df = pd.read_json(car+thread)
            #for i in df['body']:
            #    f.write(str(i))




if __name__ == "__main__":
    main()