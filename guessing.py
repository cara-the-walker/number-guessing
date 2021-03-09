import pandas as pd
import numpy as np
import random

def display(input):
    print('The answer is ',answer,'!')

def guess(ans):
    guess = input('Please make you guess by entering an integral number : ').strip()
    dic = {'target' : ans,
    'user input' : guess,}

def main():
    print('Welcome to Number Guessing game!! \n\nThe target number is between 0 and 100.\n\n')
    answer = int(random.random()*100)
    while True:
        guess(answer)


main():
