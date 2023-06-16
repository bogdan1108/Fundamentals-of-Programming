# the "prime" function checks if a number is prime or not
def prime(a) :
    ok = 1
    for i in range(2, int(a/2)+1) :
        if a % i == 0 :
            ok = 0
            break
    if a == 2 :
        ok = 1
    if a == 1 :
        ok = 0
    if ok == 1 :
        return 1
    else :
        return 0

# the "prime_prefix" function gets a as argument and
# checks if the prefix of the number (first digit) is
# prime or not
def prime_prefix(a) :
    copy_a = a
    while copy_a >= 10 :
        copy_a = copy_a // 10
    if prime(copy_a) == 1 :
        return 1
    else :
        return 0

# a is number of digits that the generated number must have
a = input("enter your number: ")
a = int(a)

# the lines below generates all the numbers of the specific
# 'a' digits and checks with the help of the functions above
# if the number is prime and it's prefix is prime
for i in range(10**(a-1), 10**a) :
    if prime(i) == 1 :
        if prime_prefix(i) == 1 :
            print(i)
