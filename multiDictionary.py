import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        diz = d.Dictionary()
        self.en = diz.loadDictionary(".\\resources\\English.txt")
        self.it = diz.loadDictionary(".\\resources\\Italian.txt")
        self.sp = diz.loadDictionary(".\\resources\\Spanish.txt")

    def printDic(self, language):
        if language == "English":
            return self.en
        if language == "Italian":
            return self.it
        if language == "Spanish":
            return self.sp

    def searchWord(self, words, language):
        dictionary =  self.printDic(language)
        richWords = []

        for word in words:
            rich_word = rw.RichWord(word)

            if word in dictionary:
                rich_word.corretta = True
                richWords.append(rich_word)
            else:
                rich_word.corretta = False
                richWords.append(rich_word)
                print(word)
        return richWords




