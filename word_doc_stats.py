# a script that gives word count, char count and frequencies of
# the most frequent words
# run with "python3 word_doc_stats.py filename length_of_word frequency"

import sys
import re
import itertools

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

# command line args
filename = sys.argv[1]
length_of_word = int(sys.argv[2])
frequency = int(sys.argv[3])

# cleaning words
lines = [x.strip('\n').split(' ') for x in lines]
raw_words = list(itertools.chain(*lines))
words = [re.sub('[\.,-]', "", word.lower()) for word in raw_words]

# clean out hyphens
words = list(filter(None, words))

# word frequency
word_dict = {}
for word in words:
    if word in word_dict.keys():
        word_dict[word] += 1
    else:
        word_dict[word] = 1

# stats
word_count = len(words)
char_count = sum([len(word) for word in words])

most_freq_words = []
for word, freq in word_dict.items():
    if freq > frequency and len(word) > length_of_word:
        most_freq_words.append((word, freq))
most_freq_words.sort(key = lambda tup: tup[1], reverse = True)

print("Word count: {0}".format(word_count))
print("Character count: {0}".format(char_count))
print("---------------------")
for pair in most_freq_words:
    print("{0}: {1}".format(pair[0], pair[1]))
