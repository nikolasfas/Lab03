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
        lista = self.multy_dictionary.searchWord(correctWords, language)



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
