"""
Siddharth Dekhane

NLP Spam Filtering using Naive Bayes

runner.py runs nblearn.py, nbclassify.py, ndevaluate.py sequentially with arguments
"""

import subprocess

print("Model Learning Started . . . . . . .")
step1 = subprocess.Popen(['python' , 'nblearn.py', 'train'])
step1.wait()
print("Model Learning Completed\n")

print("Classification Ongoing . . . . . . \n")
step2 = subprocess.Popen(['python' , 'nbclassify.py', 'dev'])
step2.wait()

step3 = subprocess.Popen(['python' , 'nbevaluate.py', 'nboutput.txt'])
step3.wait()