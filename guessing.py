import pandas as pd
import numpy as np
import random

#def display(input):
#    print('The answer is ',answer,'!')

def guess(ans):

    dic = {'target' : ans}
    r   = range(1,100)

    while True:

        guess = int(input('Please make you guess by entering an integral number between 0 and 100: ').strip())
        print(type(guess),'  ',guess,'  ',dic['target'], '  ',isinstance(ans,int), '  ',guess in r)

        if isinstance(guess,int) and guess in r:
            dic['user input'] = guess
            break

        print('Your input is not recoginizable. We\'ll need to ask you for another input. ')

    return dic


def main():
    print('Welcome to Number Guessing game!! \n\nThe target number is between 0 and 100.\n\n')
    answer = int(random.random()*100)
    while True:
        guess(answer)
#        print(guess(answer))
        print('break')
        break


if __name__ == "__main__":
	main()
