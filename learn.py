# -*- coding: utf-8 -*-
"""
Siddharth Dekhane

NLP Spam Filtering using Naive Bayes
"""

import glob
import math
import sys

## Set path to argument value
path = sys.argv[1]

## Define the output model file
output_file_name = "nbmodel.txt"

## Look up for all available HAM and SPAM training data
ham_file_list = glob.glob(path + '/**/ham/*.txt', recursive=True)
spam_file_list = glob.glob(path + '/**/spam/*.txt', recursive=True)

## Initialize empty data structures
ham_words = {}
ham_words_count = 0
spam_words = {}
spam_words_count = 0
unique_words = set()

## Fill in ham_words with corresponding counts
for files in ham_file_list:
    current_file = open(files, "r", encoding="latin1")
    for line in current_file:
        ## Iterate through every word of each file
        for word in line.split():
            ## Convert all words to lower case
            word = word.lower()
            if word in ham_words:
                ham_words[word] += 1
            else:
                ham_words[word] = 1
            ham_words_count += 1
            unique_words.add(word)
    current_file.close()

## Fill in spam_words with corresponding counts
for files in spam_file_list:
    current_file = open(files, "r", encoding="latin1")
    for line in current_file:
        ## Iterate through every word of each file
        for word in line.split():
            ## Convert all words to lower case
            word = word.lower()
            if word in spam_words:
                spam_words[word] += 1
            else:
                spam_words[word] = 1
            spam_words_count += 1
            unique_words.add(word)
    current_file.close()

## Evaluate the total word count/ unique word count
total_words_count = ham_words_count + spam_words_count
unique_words_count = len(unique_words)

## Evaluate smoothing denominators
spam_smoothing_denominator = spam_words_count + unique_words_count 
ham_smoothing_denominator = ham_words_count + unique_words_count
total_smoothing_denominator = total_words_count + unique_words_count

## P(Spam) & P(Ham) calculations
denominator = unique_words_count + len(ham_file_list) + len(spam_file_list)
total_spam_probability = math.log( (len(spam_file_list)+1) / denominator )
total_ham_probability = math.log( (len(ham_file_list)+1) / denominator )

## Generate model with pre-calculated probabilities
output_file = open(output_file_name , "w+", encoding="latin1")
output_file.writelines("uniquee_total_probabilities" + " " + str(total_spam_probability) + " " + str(total_ham_probability) + "\n")

for word in unique_words:
    if word in spam_words:
        spam_probability = math.log((spam_words[word]+1) / spam_smoothing_denominator)
    else:
        spam_probability = math.log(1 / spam_smoothing_denominator)

    if word in ham_words:
        ham_probability =  math.log((ham_words[word]+1) / ham_smoothing_denominator)
    else:
        ham_probability =  math.log(1 / ham_smoothing_denominator)

    output_file.writelines(word+" "+str(spam_probability)+" "+str(ham_probability)+"\n")
output_file.close()