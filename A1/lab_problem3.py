# reads the variables from the keyboard
n = int(input("input n: "))
k = int(input("input k: "))

# checks every number of 'n' digits if the
# product of it's digits multiplied by 'k'
# is equal to the number itself
for i in range(10**(n-1), 10**n) :
    a = i
    copy_a = a
    product = 1
    while copy_a != 0 :
        product = product * (copy_a%10)
        copy_a = copy_a//10
    if product * k == a :
        print(a)