# this is the test file for the functions

#importing the functions
import functions

def add_test() :
    test_list = []
    functions.add(test_list, 1)
    assert len(test_list) == 1
    assert test_list[0] == 1
    functions.add(test_list, 5)
    assert test_list[1] == 5

def add_index_test() :
    test_list = [1, 2, 3]
    functions.add_index(test_list, 1, 4)
    assert len(test_list) == 4
    assert test_list[1] == 4
    functions.add_index(test_list, 1, 3)
    assert len(test_list) == 5

def remove_test() :
    test_list = [1, 2, 3]
    functions.remove(test_list, 1)
    assert len(test_list) == 2
    assert test_list[1] == 3
    functions.remove(test_list, 1)
    assert len(test_list) == 1

def remove_between_test() :
    test_list = [1, 2, 3, 4]
    functions.remove_between(test_list, 1, 2)
    assert len(test_list) == 2
    assert test_list[1] == 4
    functions.remove_between(test_list, 0, 1)
    assert len(test_list) == 0

def is_prime_test() :
    a = 3
    b = 4
    c = 5
    assert functions.is_prime(a) == True
    assert functions.is_prime(b) == False
    assert functions.is_prime(c) == True

def prime_between_test() :
    l = [3, 4, 5]
    assert functions.prime_between(l, 0, 2) == [3, 5]
    assert functions.prime_between(l, 0, 1) == [3]
    assert functions.prime_between(l, 1, 2) == [5]
    
def odd_between_test() :
    l = [1, 2, 3, 4, 5, 6, 7]
    assert functions.odd_between(l, 0, 2) == [1, 3]
    assert functions.odd_between(l, 3, 6) == [5, 7]
    assert functions.odd_between(l, 1, 5) == [3, 5]

def sum_test() :
    l = [1, 2, 3, 4, 5, 6, 7]
    assert functions.sum(l, 0, 3) == 10
    assert functions.sum(l, 3, 5) == 15
    assert functions.sum(l, 0, 6) == 28

def replace_test() :
    l = [1, 2, 3, 4, 5, 6, 7]
    functions.replace(l, [1, 2, 3], [3, 2, 1])
    assert l == [3, 2, 1, 4, 5, 6, 7]
    functions.replace(l, [2, 1], [1, 2, 3, 4])
    assert l == [3, 1, 2, 3, 4, 4, 5, 6, 7]
    functions.replace(l, [3, 1, 2, 3, 4, 5], [1, 2, 3])
    assert l == [3, 1, 2, 3, 4, 4, 5, 6, 7]

def max_between_test() :
    l = [1, 2, 3, 4, 5, 6, 7]
    assert functions.max_between(l, 1, 4) == 5
    assert functions.max_between(l, 3, 5) == 6
    assert functions.max_between(l, 0, 3) == 4

def filter_prime_test() :
    l = [1, 2, 3, 4, 5, 6, 7]
    functions.filter_prime(l)
    assert l == [2, 3, 5, 7]
    l = [1, 3, 5, 7, 11, 13]
    functions.filter_prime(l)
    assert l == [3, 5, 7, 11, 13]
    l = [11, 13, 17, 18]
    functions.filter_prime(l)
    assert l == [11, 13, 17]

def filter_negative_test() :
    l = [-1, -2, -3, 1, 2, 3]
    functions.filter_negative(l)
    assert l == [-1, -2, -3]
    l = [2, -1, 3, -4, 5, -6]
    functions.filter_negative(l)
    assert l == [-1, -4, -6]
    l = [9, 8, 7, 6, 5, 4, -1]
    functions.filter_negative(l)
    assert l == [-1]

def gcd_test() :
    l = [1, 2, 3, 4, 5, 6]
    assert functions.gcd(l, 0, 5) == 1
    assert functions.gcd(l, 3, 5) == 1
    assert functions.gcd(l, 2, 5) == 1

def undo_test() :
    undo = []
    step = 0
    l = [1, 2, 3]
    undo.append(l[:])
    step += 1
    functions.add(l, 1)
    l = functions.undo_step(l, undo, step)
    step -= 1
    assert l == [1, 2, 3]
    undo.append(l[:])
    step += 1
    functions.add(l, 1)
    undo.append(l[:])
    step += 1
    functions.add(l, 10)
    l = functions.undo_step(l, undo, step)
    step -= 1
    assert l == [1, 2, 3, 1]
    l = functions.undo_step(l, undo, step)
    step -= 1
    assert l == [1, 2, 3]