import re
import nltk
import sys
import os.path
import getopt

SIZE_NGRAM = 4
START_TOKEN = "START_TOKEN_CHAR"
END_TOKEN = "END_TOKEN_CHAR"

# method to add padding
def maxxi_padding(list, ngram_size = SIZE_NGRAM):
	for counter in range (1, SIZE_NGRAM):
		list.insert(0, START_TOKEN)
		list.append(END_TOKEN)

# method to get ngrams from the sentence 
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
	
def test_ngram_printer(thing):
	for gram in thing:
		print(gram)

def exit():
	sys.exit(0)

langDict = {}
	
def dict_update(line):
	split_line = line.split(' ')
	language = split_line[0]
	if (not language in langDict):
		word_list = []
		for count in range (1, len(split_line)):
			word_list.append(split_line[count])
		langDict[language] = word_list
	else :
		current_list = langDict.get(language)
		for count in range (1, len(split_line)):
			current_list.append(split_line[count])
		langDict[language] = current_list
		
def dict_printer(dict):
	for keys, values in dict.items():
		print(keys)
		print(values)

TEST_LINE_1 = "language1 put me in here"
TEST_LINE_2 = "language2 asdfgh"
TEST_LINE_3 = "language1 here too"
dict_update(TEST_LINE_1)
dict_update(TEST_LINE_2)
dict_update(TEST_LINE_3)
dict_printer(langDict)
exit()
