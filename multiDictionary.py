import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        diz = d.Dictionary()
        self.en = sorted(diz.loadDictionary(".\\resources\\English.txt"))
        self.it = sorted(diz.loadDictionary(".\\resources\\Italian.txt"))
        self.sp = sorted(diz.loadDictionary(".\\resources\\Spanish.txt"))

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

    def searchWordLinear(self, words, language):
        dictionary =  self.printDic(language)
        richWords = []

        for word in words:
            rich_word = rw.RichWord(word)

            for vocab in dictionary:
                if word == vocab:
                    rich_word.corretta = True
                    richWords.append(rich_word)
            if not rich_word.corretta:
                print(word)

        return richWords

    def searchWordDichotomic (self, words, language):
        dictionary = self.printDic(language)
        richWords = []

        for word in words:
            rich_word = rw.RichWord(word)

            left = 0
            right = len(dictionary) -1
            trovata = False

            while left <= right:

                mid = (left + right) // 2

                if word == dictionary[mid]:
                    trovata = True
                    break
                elif word < dictionary[mid]:
                    right = mid - 1
                else:
                    left = mid +1
            rich_word.corretta = trovata
            richWords.append(rich_word)


            if not trovata:
                print(word)
        return richWords




