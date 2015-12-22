#Count Words in a String
#counts the words in a string

print("This program counts the words in a string")

user = input("submit string: ")

notaword = ".:-_,;'*¨^~`´'+?=)(/&%%¤##""!@£$€6{[]}|<>§½1234567890"
stri = ""
for char in user:
    if char in notaword:
        stri += ""
    else:
        stri += char
user = stri.split()


counter = 0

for x in user:
    print(x)
    counter += 1
print(counter, "words")


wordlist = []
for x in user:
    if not x in wordlist:
        wordlist.append(x)
#wordlist = wordlist.sort()
print(wordlist)
for x in wordlist:
    print(x, ":", user.count(x))


input("type anything to quit")