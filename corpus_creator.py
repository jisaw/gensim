__author__ = 'jakesawyer'

from gensim.corpora import dictionary
from gensim import corpora, models, similarities
import sys, os
from lxml import etree
import argparse

#DICTIONARY = corpora.Dictionary.load('cars.dict')

class MyCorpus(object):
    def __init__(self, fn):
        self.fn = fn

    def __iter__(self):
        for line in open(self.fn):
            yield dictionary.doc2bow(line.lower().split())

def stream_dict(filen):
    print("\n\n\n\n\n STARTING \n\n\n\n\n")
    dictionary = corpora.Dictionary(line.lower().split("/*/*/") for line in open(filen))
    print("\n\n\n\n\n COMAPCTING \n\n\n\n\n")
    dictionary.compactify()
    print("\n\n\n\n\n SAVING \n\n\n\n\n\n")
    dictionary.save(filen[0:-4] + '.dict')
    print(dictionary)
    return dictionary


def create_text(name):
    #current_dir = os.getcwd()
    car_makes = []
    for (dirpath, dirnames, filenames) in os.walk('../../edmunds/data/run001'):
        car_makes.append(str(dirpath))
    count = 0
    f = open(str(name), "a")
    for car in car_makes[1:]:
        print(car)
        files = os.listdir(car)
        for fl in files:
            tree = etree.iterparse(open(str(car + "/" + fl), 'r'))
            for action, elem in tree:
                if elem.tag == "body":
                    f.write(elem.text.encode('utf-8'))
                    f.write("/*/*/")
                    count += 1
    print(count)
    f.close()


def corpi():
    mem_friendly_corpus = MyCorpus('cars.txt')
    for vector in mem_friendly_corpus:
        print(vector)

        # f = open("cars.txt", 'r')
        #corpus = [dictionary.doc2bow(line.lower().split("/*/*/")) for line in open("cars.txt")]
        #corpora.MmCorpus.serialize(args.corp, corpus)
        #for thread in files:
        #df = pd.read_json(car+thread)
        #for i in df['body']:
        #    f.write(str(i))


def main():
    args = parse_args()
    if args.text:
        print('Creating text')
        create_text(args.text_file_name)
    elif args.dict:
        print('Creating dict')
        stream_dict(args.dict)
    elif args.corp:
        print('Creating corpi')
        corpi()


def parse_args():
    """
    This class handles all of the command line parsing.
    :return: results object containing all of the args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', action="store", dest='text')
    parser.add_argument('--dict', action="store", dest="dict")
    parser.add_argument('--corpus', action='store', dest='corp')
    results = parser.parse_args()
    return results

if __name__ == "__main__":
    main()