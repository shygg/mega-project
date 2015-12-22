#Check-if-Palindrome
print("### Check if Palindrome ###")
print("type a word or sentence to see if its a palidrome")


def isPalindrome(arg):
    if arg == arg[::-1]:
        return True
    else:
        return False

while True:
    user = input("submit a palindrome: ")
    if isPalindrome(user):
        print("this is a palindrome")
        break
    else:
        print("this isnt a palindrome, keep trying!")
input("type anything to exit")

