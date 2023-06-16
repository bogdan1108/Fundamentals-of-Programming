# inputs n from the keyboard
n = int(input("n = "))

# creating the list with the only element being '1'
l = [1]

# makes the list of numbers with the properties that
# '2n+1' and '3n+1' appends to the list
for i in range(0, n) :
    l.append(2*l[i] + 1)
    l.append(3*l[i] + 1)

# sorts the list
for i in range(0, len(l)-1) :
    for j in range(0, len(l)-1) :
        if l[j] > l[j+1] :
            a = l[j]
            l[j] = l[j+1]
            l[j+1] = a

# prints the list
for i in range(0, n) :
    print(l[i])