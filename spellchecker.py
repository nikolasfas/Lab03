import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multy_dictionary = md.MultiDictionary()
        self.richWords = []

    def handleSentence(self, txtIn, language):
        words = txtIn.strip().split()
        correctWords = []
        for word in words:
            correctWord = replaceChars(word).lower()
            correctWords.append(correctWord)
        print("-"*40)
        print("Using CONTAINS")
        start = time.time()
        list = self.multy_dictionary.searchWord(correctWords, language)
        end = time.time()
        print(f"Time elapsed: {end - start:.6f}")

        print("-" * 40)
        print("Using LINEAR SEARCH")
        start = time.time()
        list1 = self.multy_dictionary.searchWordLinear(correctWords, language)
        end = time.time()
        print(f"Time elapsed: {end-start:.6f}")

        print("-" * 40)
        print("Using DICHOTOMIC SEARCH")
        start = time.time()
        list2 = self.multy_dictionary.searchWordDichotomic(correctWords, language)
        end = time.time()
        print(f"Time elapsed: {end-start:.6f}")



    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
