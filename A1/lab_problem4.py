# inputs the variables from the keyboard
n = int(input("n = "))
k = int(input("k = "))

# checks if wether the powers of 'n' are
# lower than 'k' and if it's true prints
# the number
for i in range(0, k) :
    if n**i < k :
        print(n**i)
    else :
        break
