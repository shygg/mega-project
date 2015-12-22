#Fizz Buzz
print("### Fizz Buzz ###")
print("rules: enter a number between 0 and 100")
print("if the number can be a product of 3 then you will get a FIZZ")
print("if the number can be a product of 5 then you will get a BUZZ")
print("FIZZBUZZ is printed when all conditions are met")

#checking data provided by user
while True:
    try:
        user_number = int(input("Please enter a number between 0 and 100:  "))
        if user_number >= 0 and user_number <= 100:
            break
        else:
            print("the number you have entered isn't within the scope")
    except:
        print("you goofed, try again...")

#fizz, check if product of 3

if user_number % 3 == 0 and user_number % 5 == 0:
    print("FIZZBUZZ")
elif user_number % 3 == 0:
    print("FIZZ")
elif user_number % 5 == 0:
    print("BUZZ")


input("type anything to quit")