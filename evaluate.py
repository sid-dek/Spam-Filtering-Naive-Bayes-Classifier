"""
Siddharth Dekhane

NLP Spam Filtering using Naive Bayes
"""

import sys

## Set path to argument value
path = sys.argv[1]

## Initialize counter variables
true_spam, false_spam = 0, 0
true_ham, false_ham = 0, 0

## Compute the count for true/false positives/negatives
output_file = open(path, "r", encoding="latin1")
for line in output_file:
    temp = line.split()
    file_label = temp[0]
    path_to_file = temp[1]
    if "ham" in path_to_file and file_label == "ham":
        true_ham += 1
    if "ham" in path_to_file and file_label == "spam":
        false_spam += 1
    if "spam" in path_to_file and file_label == "spam":
        true_spam += 1
    if "spam" in path_to_file and file_label == "ham": 
        false_ham += 1
output_file.close()

## Evaluate Accuracy, Precision, Recall, F1 and print it
def evaluate_metrics(true_positive, false_positive, true_negative, false_negative):
    accuracy_denominator = true_positive + true_negative + false_positive + false_negative
    precision_denominiator = true_positive + false_positive
    recall_denominator = true_positive + false_negative

    accuracy, precision, recall = 0.5, 0.5, 0.5
    
    if accuracy_denominator != 0:
        accuracy = (true_positive + true_negative) / accuracy_denominator
    
    if precision_denominiator != 0:
        precision = true_positive / precision_denominiator
    
    if recall_denominator != 0:
        recall = true_positive / recall_denominator
    
    f1_score = 2* ( (precision * recall) / (precision + recall) )
    
    print("Precision : ", precision)
    print("Recall : ", recall)
    print("F1 : ",f1_score)
    print()
    return accuracy


print("Metrics for SPAM :")
accuracy = evaluate_metrics(true_spam, false_spam, true_ham, false_ham)

print("Metrics for HAM :")
accuracy = evaluate_metrics(true_ham, false_ham, true_spam, false_spam)

print("Accuracy : ", accuracy)