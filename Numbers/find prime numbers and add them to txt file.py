from time import time
#find prime numbers and add them to txt file
working_number = 8
prime_numbers = [2, 3, 5, 7]
f = open("prime_numbers.txt", 'w')


def isPrime(wn, prime_numbers):
    potential_prime = False
    #original_number = wn
    #print("working with:", wn)
    while wn > 1:
        potential_prime = True
        for x in prime_numbers:
            if 0 == wn % x:
                #print(wn, x)
                wn /= x
                potential_prime = False
                break
        if potential_prime:
            #print(original_number, "is a prime?")

            break
    if wn == 1:
        #print("not prime", wn)
        return False
    else:
        #print("maybe??", wn)
        return True
start = time()
for x in range(5, 1000000):
    if(isPrime(x, prime_numbers)):
        prime_numbers.append(x)
        f.write(str(x) + " ")
f.close()
finish = time()
totaltime = finish - start
print("operation took ", totaltime, "sec to complete, results: ")
print(prime_numbers)

input()
