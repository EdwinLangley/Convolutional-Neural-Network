import bs4
from urllib.request import urlopen as UrReq
from bs4 import BeautifulSoup as soup
import sqlite3
import texttable as tt
import math
import requests
import time
from random import randint
import nltk


class Tagger:

    def __init__(self, text):
        self.passage = text
        print("Entered passage: " + self.passage)

    def tokenise_text(self):
        self.passage = nltk.word_tokenize(self.passage)
    
    def tag_text(self):
        self.tags = nltk.pos_tag(self.passage)
    
    def identify_uses(self):
        nounssize = len(self.tags)
        nnsjjpairs = []
        for i in range(0,nounssize - 1):
            current_word_pos = self.tags[i]
            next_word_pos = self.tags[i+1]

            if current_word_pos[1] == 'JJ' and next_word_pos[1] == 'NNS':
                nnsjjpairs.append(current_word_pos[0] + ' ' + next_word_pos[0])

        print(nnsjjpairs)

        return nnsjjpairs
        

if __name__ == '__main__':
    newtagger = Tagger("This type of butterfly holds blue spots and white wings")
    newtagger.tokenise_text()
    newtagger.tag_text()
    newtagger.identify_uses()