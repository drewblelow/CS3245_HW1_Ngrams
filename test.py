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
	
def test_printer(thing):
	for gram in thing:
		print(gram)

def exit():
	sys.exit(0)

TEST_LINE = "asdfghjk lqw ertyu iop"
process = ngram_from_line(TEST_LINE)
test_printer(process)
exit()

"""
# this method builds n grams from a string input line by iterating through the list
def ngram_from_line1(line, ngram_size = SIZE_NGRAM):
	line_list = list(line)
	# loop - to attach start tokens to the first few ngrams
	fourgrams = []
	for counter in range(1, ngram_size):
		gram = []
		for counter_2 in range(counter, ngram_size):
			gram.append(START_TOKEN)
		for counter_3 in range(0, counter):
			gram.append(line_list[counter_3])
		fourgrams.append(gram)
	# loop - process all the fourgrams that contain characters in the line
	for counter in range (0, len(line_list) - ngram_size + 1):
		gram = []
		for counter_2 in range(0, ngram_size):
			gram.append(line_list[counter + counter_2])
		fourgrams.append(gram)
	# loop - attach end tokens to the last few ngrams	
	for counter in range(len(line_list) - ngram_size + 1, len(line_list)):
		gram = []
		
		for counter_4 in range(len(line_list) - counter, ngram_size):
			gram.append(END_TOKEN)
		fourgrams.append(gram)
	return fourgrams
"""