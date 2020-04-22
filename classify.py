# -*- coding: utf-8 -*-
"""
Siddharth Dekhane

NLP Spam Filtering using Naive Bayes
"""

import glob
import sys

## Set path to argument value
path = sys.argv[1]

## Define the output model file
output_file_name = "nboutput.txt"

## Initialize and fill it with model data
word_probability = {}
total_keyword = "uniquee_total_probabilities"

model_file = open("nbmodel.txt", "r", encoding="latin1")
for line in model_file:
    temp = line.split()
    word_probability[ temp[0] ] = [ float(temp[1]) , float(temp[2]) ]
model_file.close()

## Extract P(Spam) & P(Ham) from the model contents
total_spam_probability = word_probability[total_keyword][0]
total_ham_probability = word_probability[total_keyword][1]

## Search recursively through the entire directory
test_list = glob.glob(path + '/**/*.txt', recursive=True)

## Classify and write to output.txt
## Format : { LABEL <\t> PATH }
output_file = open(output_file_name, "w+", encoding="latin1")
for test_file_path in test_list:
    file_ham_probability = total_ham_probability
    file_spam_probability = total_spam_probability
    test_file = open(test_file_path, "r", encoding="latin1")
    for line in test_file:
        for word in line.split():
            if word in word_probability:
                file_spam_probability += word_probability[word][0]
                file_ham_probability += word_probability[word][1]

    ## Classify as spam/ham and write to output file
    if file_ham_probability >= file_spam_probability:
        output_file.writelines("ham\t"+test_file_path+"\n")
    else:
        output_file.writelines("spam\t"+test_file_path+"\n")
output_file.close()