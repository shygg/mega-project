class wordcount():
    words = {}
    def __init__(self):
        pass
    def count_words_in_string(self, string):
        for word in string.split(" "):
            if word in self.words:
                print("yes")
            try:
                self.words[word] += 1
            except:
                self.words[word] = 1
        return self.words

article = wordcount()
article.count_words_in_string("ett ord i ett ord som inte är ett ord men egentligen heter oden")
print(article.words)
input()
