from urllib.request import urlopen


print("n digits of pi 0<99999: ")
n = input()
if n.isdigit():
    n = int(n) + 2

if n < 999999 and n > 0:
    data = urlopen("http://www.angio.net/pi/digits/100000.txt").read(n)
    pi = data

print(pi.decode('utf-8'))
input()