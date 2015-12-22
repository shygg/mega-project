

user_input = int(input("enter number you want the prime factor thingy buildingblocks from: "))

f = open("prime_numbers.txt", 'r')
prime_numbers = []

string_list = f.read().split()
f.close()
for x in string_list:
    if int(x) > user_input:
        break
    prime_numbers.append(int(x))
print(prime_numbers)

wn = user_input
prime_factors = []

while True:
    if int(wn) in prime_numbers:
        prime_factors.append(wn)
        break
    else:
        for x in prime_numbers:
            if int(wn % x) == 0:
                prime_factors.append(x)
                wn = int(wn / x)
                break

print("answer: ", prime_factors)

input()