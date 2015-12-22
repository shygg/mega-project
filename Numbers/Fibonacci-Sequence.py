#Fibonacci-Sequence
print("Fibonacci Sequence, how many numbers do you want generated?")

while True:
    try:
        user_input = int(input("n numbers: "))
        break
    except ValueError:
        print("you goofed somehow, please provide an integer")


def fibo(n):
    if n == 0:
        print("zero? really?")
        return 0
    a, b = 1, 1
    fibolist = []
    fibolist.append(a)
    if len(fibolist) == n:
        return fibolist
    fibolist.append(b)
    if len(fibolist) == n:
        return fibolist
    while True:
        a += b
        fibolist.append(a)
        if len(fibolist) == n:
            return fibolist

        b += a
        fibolist.append(b)
        if len(fibolist) == n:
            return fibolist
print("fibonacci-sequence you asked for: ", fibo(user_input))
e = input("type-anything-to-exit")

