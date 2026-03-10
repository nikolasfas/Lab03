class Dictionary:
    def __init__(self):
        self._dict = []


    def loadDictionary(self,path):
        with open(path,'r', encoding="utf8") as f:
            for line in f:
                fields = line.strip().split()
                word = fields[0]
                self._dict.append(word)
        return self._dict

    def printAll(self):
        for word  in self._dict:
            print(word)

    def __contains__(self,word):
        return word in self._dict

    @property
    def dict(self):
        return self._dict