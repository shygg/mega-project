#Pig Latin

print("#### PIG LATIN ####")
print("Rules are simple: type a sentence, see it translated into pig latin!")


def word_transform(word):
    vowels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    if word[0] in vowels:
        #print("vowel")
        new_word = word + "way"

    if word[0] in consonants:
        #print("consonant")
        new_word = word[1:] + word[0] + "ay"

    return new_word


def fix_sentence(sentence):
    words = sentence.split()
    new_sentence = ""
    for x in words:
        new_sentence += word_transform(x) + " "
    return new_sentence

sentence = fix_sentence(input())

print(sentence)
sentence = input()

