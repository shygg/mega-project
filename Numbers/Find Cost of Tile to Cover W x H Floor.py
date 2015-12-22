#Find Cost of Tile to Cover W x H Floor
print("Calculate cost from cost per squaremetre, use (m) and usd")
width = int(input("width: "))
height = int(input("height: "))
cost = int(input("cost per square metre: "))
total = cost * height * width
print("total cost: ", total, "usd")
input("type anything to quit")