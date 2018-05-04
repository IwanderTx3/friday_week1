spaces = int(input("How tall do you want the tree? "))
stars = int(1)

while spaces > 80:
    print("Lets be resonable.  Keep the number under 80")
    spaces = int(input("How tall do you want the tree? "))



while spaces > 0:
    print(" " * spaces + "*" * stars)
    spaces-=1
    stars+=2
