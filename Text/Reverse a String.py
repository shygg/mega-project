#reverse string

myString = input()
#fast way
print(myString[::-1])

#slower way
i = len(myString)
newString = ""
while i > 0:
    i -= 1
    newString += myString[i]
print(newString)

#what way is faster?
myString = input()[::-1]
print(myString)
#both works

input()