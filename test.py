import re
import nltk
import sys
import os.path
import getopt

SIZE_NGRAM = 4
START_TOKEN = '+'
END_TOKEN = '-'

def ngram_from_line(line, ngram_size = SIZE_NGRAM):
	"""
	builds n grams from a string input line
	"""
	fourgrams = re.findall(r'(?=(...))', line)
	for grams in fourgrams:
		print grams
	print "done"

def test(in_file):
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
		print language_type
		print text_line
		break

input_file_t = 'D:\\ProgramFiles(x86)\\temp\\A0110649J\\input.train.txt'
test(input_file_t)
ngram_from_line('hello asdfgh')