import pandas as pd
import numpy as np
import random

#def display(input):
#    print('The answer is ',answer,'!')




def guess(ans):

    dic = {'target' : ans}
    r   = range(1,100)

    while True:
        while True:

            guess = input('Please make you guess by entering an integral number between 0 and 100: ').strip()

            try:
                int(guess)
                break
            except ValueError:
                print('\n\nYour input is not recoginizable. \nWe\'ll need to ask you for ONLY integral number.\n\n')

        guess = int(guess)
    #    print(type(guess),'  ',guess,'  ',dic['target'], '  ',isinstance(ans,int), '  ',guess in r)

        if guess in r:
            dic['user input'] = guess
            break;
        else: print('\n\nYour input is not recoginizable. \nWe\'ll need to ask you for that number BETWEEN 0 AND 100.\n\n')

    return dic


def main():
    print('Welcome to Number Guessing game!! \n\nThe target number is between 0 and 100.\n\n')
    answer = int(random.random()*100)
    while True:
        num = guess(answer)
        print(num)
#        print(guess(answer))
        print('break')
        break


if __name__ == "__main__":
	main()
