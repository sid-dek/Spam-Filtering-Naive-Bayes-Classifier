# -*- coding: utf-8 -*-
"""
Siddharth Dekhane
NLP Spam Filtering using Naive Bayes

Note : This code requires a pre-existing directory named "mini_train"
and sub-folders "spam" and "ham" to compute the mini dataset.
"""

import glob
import math
import shutil

## Source dataset
path = 'train'

## Existing Mini dataset location
output_path = 'mini_train'

## Extract all spam and ham data
ham_dataset = glob.glob(path + '/**/ham/*.txt', recursive=True)
spam_dataset = glob.glob(path + '/**/spam/*.txt', recursive=True)

counter = 0

## Evaluation of aplit points to form mini dataset
total_count = min(len(ham_dataset), len(spam_dataset))
target_elements = math.ceil(total_count * 0.1)
gap = total_count//target_elements

## Copy every 1/10th file number to new location
for i in range(0, total_count-1, gap):
    ham_path = output_path+"/ham/"+str(counter)+".ham.txt"
    spam_path = output_path+"/spam/"+str(counter)+".spam.txt"
    shutil.copy2(ham_dataset[i], ham_path)
    shutil.copy2(spam_dataset[i], spam_path)
    counter += 1