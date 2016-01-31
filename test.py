import re
import nltk
import sys
import os.path
import getopt

SIZE_NGRAM = 4

def ngram_from_line(line, ngram_size = SIZE_NGRAM):
	"""
	builds n grams from a string input line using regex
	"""
	fourgrams = re.findall(r'(?=(...))', line)
	return fourgrams

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
		#print text_line
	
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
"""
for o, a in opts:
    if o == '-b':
        input_file_b = a
    elif o == '-t':
        input_file_t = a
    elif o == '-o':
        output_file = a
    else:
        assert False, "unhandled option"
"""
"""
if input_file_b == None or input_file_t == None or output_file == None:
    usage()
    sys.exit(2)
"""
LM = build_LM(input_file_b)
#test_LM(input_file_t, output_file, LM)