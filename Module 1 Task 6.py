password = input()
while len(password) < 8:
    print("Too short")
    break
else: print("Accepted")