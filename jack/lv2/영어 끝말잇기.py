from collections import defaultdict
from math import ceil

class WordsDict :
    def __init__(self) :
        self.wd = set()
        self.last = ""
    
    def check(self, word) :
        if self.last == "" :
            return True
        if word[0] != self.last or word in self.wd:
            return False
        return True
    
    def tell(self, word) :
        if self.check(word) :
            self.wd.add(word)
            self.last = word[-1]
            return True
        else :
            return False

def solution(n, words):
    wd = WordsDict()
    for order, word in enumerate(words, 1) :
        if not wd.tell(word) :
            return [order%n if order%n else n, ceil(order/n)]
    else :
        return [0,0]
            
        
