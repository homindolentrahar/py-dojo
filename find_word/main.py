from helpers import *
import sys

if __name__ == '__main__':
    try:
        query = sys.argv[1]
        find_word(query=query)
    except IndexError:
        print("Provide an argument in the execution (python main.py joe")
