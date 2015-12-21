#Count Vowels
print("### Count Vowels ###")
print("this program will count the vowels in whatever you input")


#func with vowels string that contains all vowels
#compares it with the string provided by the user and returns the count
def vowel_count(arg):
    vowels = "aeioyu"
    count = 0
    for x in arg:
        if x in vowels:
            count += 1
    return count

user = input("please write a sentence: ")
print("there are ", vowel_count(user), " vowels in your input")
input("type anything to quit")