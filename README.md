# Spam-Filtering-Naive-Bayes-Classifier
A Naive Bayes classifier to perform spam filtering. 


## Description
• learn : Trains the model using the "train" (Train) dataset
• classify : Classifies the "dev" (Test) emails as spam/ham
• evaluate : Calculates precision, recall, accuracy
• split_dataset : Script to split dataset for personal testing purposes
• runner : Script to do all learning, classifying and evaluation in a go
• Report : A small summarization of classification results
• spam_ham_dataset : "train" - Training Dataset , "dev" - Testing Dataset


## Usage
>python3 nblearn.py </path/to/input>

>python3 nbclassify.py </path/to/input>

>python3 nbevaluate.py <nboutput_filename>