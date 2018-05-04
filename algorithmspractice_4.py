spaces = int(8)
stars = int(1)

while spaces > 0:
    print(" " * spaces + "*" * stars)
    spaces-=1
    stars+=2
