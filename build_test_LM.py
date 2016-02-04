#A0110649J
#!/usr/bin/python
import re
import nltk
import sys
import os.path
import getopt

SIZE_NGRAM = 4
LANGUAGE_MODEL = {}

# method to add padding
def maxxi_padding(list, ngram_size = SIZE_NGRAM):
	for counter in range (1, SIZE_NGRAM):
		list.insert(0, START_TOKEN)
		list.append(END_TOKEN)

# method to get ngrams from the sentence, size of ngram can be changed in the global variable 
def ngram_from_line(line, ngram_size = SIZE_NGRAM):
	line_list = list(line)
	maxxi_padding(line_list)
	# loop - process all the fourgrams in the line
	fourgrams = []
	for counter in range (0, len(line_list) - ngram_size + 1):
		gram = []
		for counter_2 in range(0, ngram_size):
			gram.append(line_list[counter + counter_2])
		fourgrams.append(gram)
	return fourgrams

def dict_update(language, ngrams):
	gram_list = list(ngrams)
	if (not language in LANGUAGE_MODEL):
		LANGUAGE_MODEL[language] = gram_list
	else :
		current_list = LANGUAGE_MODEL.get(language)
		for gram in gram_list:
			current_list.append(gram)
		LANGUAGE_MODEL[language] = current_list
	
def build_LM(in_file):
	"""
	build language models for each label
	each line in in_file contains a label and an URL separated by a tab(\t)
	"""
	print 'building language models...'
	file_contents = open(in_file).readlines()
	"""
	for each line in the file, split the language type away from the text line
	split the text line into n grams and add it to the correct language type
	"""
	for line in file_contents:
		split_line = line.split(' ', 1)
		language_type = split_line[0]
		text_line = split_line[1]
		line_fourgram = ngram_from_line(text_line)
		dict_update(language_type, line_fourgram)
	print 'finished building'

def usage():
	print "usage: " + sys.argv[0] + " -b input-file-for-building-LM -t input-file-for-testing-LM -o output-file"
	
input_file_b = "input.train.txt"
input_file_t = output_file = None
try:
    opts, args = getopt.getopt(sys.argv[1:], 'b:t:o:')
except getopt.GetoptError, err:
    usage()
    sys.exit(2)

for o, a in opts:
    if o == '-b':
        input_file_b = a
    elif o == '-t':
        input_file_t = a
    elif o == '-o':
        output_file = a
    else:
        assert False, "unhandled option"

if input_file_b == None or input_file_t == None or output_file == None:
    usage()
    sys.exit(2)

LM = build_LM(input_file_b)
test_LM(input_file_t, output_file, LM)