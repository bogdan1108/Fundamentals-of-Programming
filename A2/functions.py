# this is the file that contains all the functions of the program

def add(my_list, value) :
    '''
    adds a value as the last element of the list
    '''
    my_list.append(value)

def add_index(my_list, index, value) :
    '''
    adds a value at a specific index of the list
    '''
    my_list.insert(index, value)

def remove(my_list, index) :
    '''
    removes a value at a specific index of the list
    '''
    my_list.pop(index)

def remove_between(my_list, from_index, to_index) :
    '''
    removes all the values between 2 specific indexes of the list
    '''
    for i in range (to_index, from_index - 1, -1) :
        del(my_list[i])

def is_prime(value) :
    '''
    checks if a number is prime or not
    '''
    ok = True
    if value > 0 :
        for i in range(2, value//2 + 1) :
            if value % i == 0 :
                ok = False
                break
        if value == 1 :
            ok = False
        if value == 2 :
            ok = True
        return ok
    return False

def prime_between(my_list, from_index, to_index) :
    '''
    returns all the prime numbers from a list
    '''
    final_list = []
    for i in range(from_index, to_index + 1) :
        if is_prime(my_list[i]) :
            final_list.append(my_list[i])
    return final_list

def odd_between(my_list, from_index, to_index) :
    '''
    returns all the odd numbers between 2 specific indexes
    '''
    final_list = []
    for i in range(from_index, to_index + 1) :
        if my_list[i] % 2 == 1 :
            final_list.append(my_list[i])
    return final_list

def sum(my_list, from_index, to_index) :
    '''
    returns the sum of all the elements between 2 specific indexes
    '''
    sum = 0
    for i in range(from_index, to_index + 1) :
        sum += my_list[i]
    return sum

def replace(my_list, old_value, new_value) :
    '''
    replaces all the sub lists which are 'old_value' from 'my_list'
    with 'new_value'
    '''
    for i in range(0, len(my_list)) :
        if i < len(my_list) :
            if len(old_value) > 0 and len(new_value) > 0 :
                if my_list[i] == old_value[0] and i + len(old_value) < len(my_list) :
                    ok = 1
                    for j in range(0, len(old_value)) :
                        if my_list[i+j] == old_value[j] :
                            ok = 1
                        else :
                            ok = 0
                            break
                    if ok == 1 :
                        my_list[i : i+len(old_value)] = new_value

def max_between(my_list, from_index, to_index) :
    '''
    get the max value between 2 specific indexes
    '''
    maxx = my_list[from_index]
    for i in range(from_index, to_index + 1) :
        if my_list[i] > maxx :
            maxx = my_list[i]
    return maxx

def filter_prime(my_list) :
    '''
    removes all the non prime elements from a list
    '''
    for i in range(len(my_list) - 1, -1, -1) :
        if is_prime(my_list[i]) == False :
            my_list.pop(i)

def filter_negative(my_list) :
    '''
    removes all the non negative elements from a list
    '''
    for i in range(len(my_list) - 1, -1, -1) :
        if my_list[i] >= 0 :
            my_list.pop(i)

def gcd(my_list, from_index, to_index) :
    '''
    gets the greatest common divisor of all the numbers between 2 indexes
    '''
    ok = 0
    g_c_d = 1
    for i in range(1, my_list[from_index] + 1) :
        for j in range(from_index, to_index + 1) :
            if my_list[j] % i == 0 :
                ok = 1
            else :
                ok = 0
                break
        if ok == 1 :
            g_c_d = i
    return g_c_d

def undo_step(my_list, undo, step) :
    '''
    reverses the last made command
    '''
    my_list = undo[step - 1]
    undo.pop(step-1)
    return my_list

