import re
import nltk
import sys
import os.path
import getopt

SIZE_NGRAM = 4
START_TOKEN = '+'
END_TOKEN = '-'

def test(in_file):
	"""
	build language models for each label
	each line in in_file contains a label and an URL separated by a tab(\t)
	"""
	print 'building language models...'
	file_contents = open(in_file).readlines()
	"""
	for each line in the file, read the language type
	then for character sequences in that line, add the ngrams to the LM
	"""
	for line in file_contents:
		language_type = line.partition(' ')[0]
		print language_type

input_file_t = 'D:\\ProgramFiles(x86)\\temp\\A0110649J\\input.train.txt'
test(input_file_t)