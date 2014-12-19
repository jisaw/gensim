from gensim.corpora import Dictionary
from gensim import corpora, models, similarities
import sys, os
from lxml import etree
import argparse


def parse_args():
    """
    This class handles all of the command line parsing.
    :return: results object containing all of the args
    """
    print("[+] Parsing arguments")
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', action="store", dest='text', help="The name of the run directory you wish to use")
    parser.add_argument('--fname', action="store", dest="fname", help="The filename of the dictionary and corpus")
    results = parser.parse_args()
    print("[+] Arguments Parsed")
    return results


def generate_text(run_number):
    car_makes = []
    for (dirpath, dirnames, filenames) in os.walk('../../edmunds/data/%s' % run_number):
        car_makes.append(str(dirpath))
    count = 0
    print("[+] Creating generator")
    for car in car_makes[1:]:
        print("[+]", car)
        files = os.listdir(car)
        for fl in files:
            tree = etree.iterparse(open(str(car + "/" + fl), 'r'))
            for action, elem in tree:
                if elem.tag == "body":
                    yield elem.text.encode('utf-8')
    print("[+] Documents generator complete\n[+] Number of documents: %s" % count)


def build_dict(filen, generator):
    print("[+] Starting Dictionary Creation")
    dictionary = corpora.Dictionary(line.lower().split() for line in generator)
    print("[+] Compacting Dictionary")
    dictionary.compactify()
    print("[+] Saving Dictionary")
    dictionary.save(filen + ".dict")
    print(dictionary)
    return dictionary

def build_corpus(filen, generator, dictionary):
	print("[+] Starting Corpus Creation")
	corpus = (dictionary.doc2bow(text.lower().split()) for text in generator)
	print("[+] Saving Corpus")
	corpora.MmCorpus.serialize('%s.mm' % filen, corpus)
	print("[+] Corpus Saved Comeplete")

def main():
	parse = parse_args()

	if parse.text:
		text_gen = generate_text(parse.text)
		dictionary = build_dict(parse.fname, text_gen)

		text_gen = generate_text(parse.text)
		build_corpus(parse.fname, text_gen, dictionary)
		print("*"*15 + "\n[+] Dictionary File Name: %s\n[+] Corpus File Name: %s\n[+] Script Complete")


if __name__ == "__main__":
	main()