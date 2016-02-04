#A0110649J
#!/usr/bin/python
import re
import nltk
import sys
import os.path
import getopt
from collections import Counter

SIZE_NGRAM = 4
START_TOKEN = "START_TOKEN_CHAR"
END_TOKEN = "END_TOKEN_CHAR"
LANGUAGE_MODEL = {}
UNIQUE_GRAMS = []

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

# method checks the dictionary for the language, then adds ngrams to it if it exists. Creates a key otherwise
def dict_update(language, ngrams):
	gram_list = list(ngrams)
	if (not language in LANGUAGE_MODEL):
		LANGUAGE_MODEL[language] = gram_list
		for gram in gram_list:
			if (not gram in UNIQUE_GRAMS):
				UNIQUE_GRAMS.append(gram)
	else :
		current_list = LANGUAGE_MODEL.get(language)
		for gram in gram_list:
			current_list.append(gram)
			if (not gram in UNIQUE_GRAMS):
				UNIQUE_GRAMS.append(gram)
		LANGUAGE_MODEL[language] = current_list
	
# method does smootihng for the ngrams
def smooth_dict():
	for key in LANGUAGE_MODEL:
		ngram_set = LANGUAGE_MODEL.get(key)
		ngram_set.extend(UNIQUE_GRAMS)
	
def build_probability_model():
	PM = {}
	for key in LANGUAGE_MODEL:
		probability_language = {}
		values = LANGUAGE_MODEL.get(key)
		num_grams = len(values)
		counter = Counter(values)
		for gram, occurences in counter.iteritems():
			probability = occurences / float(num_grams)
			probability_language[gram] = probability
		PM[key] = probability_language
	return PM
	
def build_LM(in_file):
	"""
	build language models for each label
	each line in in_file contains a label and an URL separated by a tab(\t)
	"""
	print 'building language models...'
	file_contents = open(in_file).readlines()
	#for each line in the file, split the language type away from the text line
	#split the text line into n grams and add it to the correct language type
	#apply smoothing to the final dictionary
	for line in file_contents:
		split_line = line.split(' ', 1)
		language_type = split_line[0]
		text_line = split_line[1]
		line_fourgram = ngram_from_line(text_line)
		dict_update(language_type, line_fourgram)
	smooth_dict()
	print("models built")
	return build_probability_model

def calculate_probability(ngrams, probability_model):
	current_highest = 0
	for key in probability_model:
		probability = 1
		probability_language = probability_model[key]
		for gram in ngrams:
			gram_prob = probability_language[gram]
			if (gram_prob != 0):
				probability *= gram_prob
		if (probability > current_highest and probability != 1):
			label = key
	if (current_highest == 0):
		label = "others"
	return label
	
def test_LM(in_file, out_file, LM):
	"""
	test the language models on new URLs
	each line of in_file contains an URL
	you should print the most probable label for each URL into out_file
	"""
	print "testing language models..."
    # for each input line, break string into ngrams, then check it against each probability model
	test_contents = open(in_file).readlines()
	for line in test_contents:
		fourgrams = ngram_from_line(line)
		print(calculate_probability(fourgrams, LM))
		#write label to file
	
def usage():
	print "usage: " + sys.argv[0] + " -b input-file-for-building-LM -t input-file-for-testing-LM -o output-file"
	
input_file_b = "input.train.txt"
input_file_t = "input.test.txt"
output_file = "output.txt"
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