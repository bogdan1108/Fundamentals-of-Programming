# importing the functions from the functions.py file
import functions
import tests

with open("input.txt") as f :
      my_list = f.read().splitlines()

fp = open("output.txt", "w")

for i in range(len(my_list)) :
      my_list[i] = int(my_list[i])

# runs the test functions
tests.add_test()
tests.add_index_test()
tests.remove_test()
tests.remove_between_test()
tests.is_prime_test()
tests.prime_between_test()
tests.odd_between_test()
tests.sum_test()
tests.replace_test()
tests.max_between_test()
tests.filter_prime_test()
tests.filter_negative_test()
tests.gcd_test()
tests.undo_test()

# gives an arbitrary value to x
x = 100

# create the list that you work with
# creates an empty list for the undo function
undo = []

# counters the steps of actions that modifies the list for the undo function
step = 0

# fp = open("name.txt", "r") <- read from a file
# fp = open("name.txt", "w") <- write from a file
# fp.readline() <- reads a line
# fp.writeline(" ") <- write a line

# creating the user menu and for every menu that x takes
# makes the action that is assigned to the specific number
# and if the command is 0 the program stops
while x != 0 :
      print("1: Add a number at the end of the list \n"
      "2: Insert a number at the index \n"
      "3: Remove a number at index \n"
      "4: Remove the numbers between 2 given index \n"
      "5: Replace numbers \n"
      "6: Get prime numbers between 2 given index \n"
      "7: Get odd numbers between 2 given index \n"
      "8: Get sum of numbers between 2 given index \n"
      "9: Get greatest common divisor between 2 given index \n"
      "10: Get maximum of numbers between 2 given indexes \n"
      "11: Keep only the prime numbers \n"
      "12: Keep only negative numbers \n"
      "13: Print the list \n"
      "14: Write the list in 'output.txt' file \n"
      "15: Undo \n"
      "0: Exit program \n")
      x = input("Choose your option: ") # inputs the action that the user wants to make
      print('\n')

      # checks if the inputed number is integer, otherwise return an error message
      try:
            x = int(x)
            # using the 'add' function inserts a number to the 
            # end of the list if the action is '1'
            if x == 1 :
                  undo.append(my_list[:])
                  step += 1
                  value = input("Choose a value: ")
                  try: # checks if the inputed value is an integer, otherwise return an error message
                        value = int(value)
                        functions.add(my_list, value)
                        print('\n')
                  except ValueError:
                        print("Please insert an integer!", '\n')

            # using the 'add_index' function inserts a number to a 
            # specific index of the list if the action is '2'
            elif x == 2 :
                  undo.append(my_list[:])
                  step += 1
                  index = input("Choose an index: ")
                  # checks if the inputed value is an integer, otherwise return an error message
                  try:
                        # checks if the index is valid, otherwise return an error message
                        if 0 <= int(index) < len(my_list): 
                              index = int(index)
                              value = input("Choose a value: ")
                              # checks if the inputed value is an integer, otherwise return an error message
                              try: 
                                    value = int(value)
                                    functions.add_index(my_list, index, value)
                                    print('\n')
                              except ValueError:
                                    print("Invalid value!", '\n')
                        else :
                              print("Invalid index!", '\n')
                  except ValueError:
                        print("Invalid index!", '\n')

            # using the 'remove' function removes a number at a specific 
            # index of the list if the actions is '3'
            elif x == 3 :
                  undo.append(my_list[:])
                  step += 1
                  index = input("Choose an index: ")
                  # checks if the inputed value is an integer, otherwise return an error message
                  try:
                        # checks if the index is valid, otherwise return an error message
                        if 0 <= int(index) < len(my_list) :
                              index = int(index)  
                              functions.remove(my_list, index)
                              print('\n')
                        else :
                              print("Invalid index!", '\n')
                  except ValueError:
                        print("Invalid index!", '\n')

            # using the 'remove_between' function removes all the number 
            # between 2 specific indexes if the action is '4'
            elif x == 4 :
                  undo.append(my_list[:])
                  step += 1
                  index1 = input("Choose your first index: ")
                  # checks if the inputed value is an integer, otherwise return an error message
                  try:
                        # checks if the index is valid, otherwise return an error message
                        if 0 <= int(index1) < len(my_list) :
                              index1 = int(index1)
                              index2 = input("Choose your second index: ")
                              # checks if the inputed value is an integer, otherwise return an error message
                              try: 
                                    # checks if the index is valid, otherwise return an error message
                                    if 0 <= int(index2) < len(my_list) : 
                                          index2 = int(index2)
                                          # checks which index is bigger to do the action
                                          if index1 > index2 :
                                                functions.remove_between(my_list, index2, index1)
                                          else :
                                                functions.remove_between(my_list, index1, index2)
                                          print('\n')
                                    else :
                                          print("Invalid index!", '\n')
                              except ValueError:
                                    print("Invalid index!", '\n')
                        else :
                              print("Invalid index!", '\n')
                  except ValueError :
                        print("Invalid index!", '\n')

            # using the 'replace' function replaces a sequance of the list
            # with another one if the action is '5'
            elif x == 5 :
                  undo.append(my_list[:])
                  step += 1
                  
                  old_value = []
                  new_value = []
                  input_index = 1
                  while input_index != 0 :
                        input_index = input("Choose a number from the sequance of the numbers to be deleted (ends if you insert 0): ")
                        # checks if the inputed value is an integer, otherwise return an error message
                        try: 
                              input_index = int(input_index)
                              if input_index != 0 :
                                    old_value.append(input_index)
                        except ValueError :
                              print("Invalid value!", '\n')

                  input_index = 1
                  while input_index != 0 :
                        input_index = input("Choose a number from the sequance of numbers to be inserted(ends if you insert 0): ")
                        # checks if the inputed value is an integer, otherwise return an error message
                        try: 
                              input_index = int(input_index)
                              if input_index != 0 :
                                    new_value.append(input_index)
                        except ValueError :
                              print("Invalid value!", '\n')
                  
                  functions.replace(my_list, old_value, new_value)
                  print('\n')
            # using the 'prime_between' function returns all the prime numbers
            # between 2 indexes if the action is '6'
            elif x == 6 :
                  index1 = input("Choose your first index: ")
                  # checks if the inputed value is an integer, otherwise return an error message
                  try:
                        # checks if the index is valid, otherwise return an error message
                        if 0 <= int(index1) < len(my_list): 
                              index1 = int(index1)
                              index2 = input("Choose your second index: ")
                              # checks if the inputed value is an integer, otherwise return an error message
                              try:
                                    # checks if the index is valid, otherwise return an error message
                                    if 0 <= int(index2) < len(my_list) : 
                                          index2 = int(index2) 
                                          # checks which index is bigger to do the action
                                          if index1 < index2 :
                                                print(functions.prime_between(my_list, index1, index2), '\n')
                                          else :
                                                print(functions.prime_between(my_list, index2, index1), '\n')
                                    else :
                                          print("Invalid index!", '\n')
                              except ValueError :
                                    print("Invalid index!", '\n')
                        else :
                              print("Invalid index!", '\n')
                  except ValueError :
                        print("Invalid index!", '\n')

            # using the 'odd_between' function returns all the odd numbers 
            # between 2 specific indexes if the actions is '7'
            elif x == 7 :
                  index1 = input("Choose your first index: ")
                  # checks if the inputed value is an integer, otherwise return an error message
                  try:
                        # checks if the index is valid, otherwise return an error message
                        if 0 <= int(index1) < len(my_list) : 
                              index1 = int(index1)
                              index2 = input("Choose your second index: ")
                              # checks if the inputed value is an integer, otherwise return an error message
                              try:
                                    # checks if the index is valid, otherwise return an error message
                                    if 0 <= int(index2) < len(my_list) : 
                                          index2 = int(index2)
                                          # checks which index is bigger to do the action
                                          if index1 < index2 :
                                                print(functions.odd_between(my_list, index1, index2), '\n')
                                          else :
                                                print(functions.odd_between(my_list, index2, index1), '\n')
                                    else :
                                          print("Invalid index!", '\n')
                              except ValueError :
                                    print("Invalid index!, '\n")
                        else :
                              print("Invalid index!", '\n')
                  except ValueError :
                        print("Invalid index!", '\n')
            # using the 'sum' function returns the sum of all the numbers
            # between 2 specific indexes if the actions is '8'
            elif x == 8 :
                  index1 = input("Choose your first index: ")
                  # checks if the inputed value is an integer, otherwise return an error message
                  try:
                        # checks if the index is valid, otherwise return an error message
                        if 0 <= int(index1) < len(my_list) : 
                              index1 = int(index1)
                              index2 = input("Choose your second index: ")
                              # checks if the inputed value is an integer, otherwise return an error message
                              try:
                                    # checks if the index is valid, otherwise return an error message
                                    if 0 <= int(index2) < len(my_list) : 
                                          index2 = int(index2)
                                          # checks which index is bigger to do the action
                                          if index1 < index2 :
                                                print(functions.sum(my_list, index1, index2), '\n')
                                          else :
                                                print(functions.sum(my_list, index2, index1), '\n')
                                    else :
                                          print("Invalid index!", '\n')
                              except ValueError :
                                    print("Invalid index!", '\n')
                        else :
                              print("Invalid index!", '\n')
                  except ValueError :
                        print("Invalid index!", '\n')
            # using the 'gcd' function returns the greatest common divisor
            # of all the numbers between 2 specific indexes if the action is '9'
            elif x == 9 :
                  index1 = input("Choose your first index: ")
                  # checks if the inputed value is an integer, otherwise return an error message
                  try:
                        # checks if the index is valid, otherwise return an error message
                        if 0 <= int(index1) < len(my_list) : 
                              index1 = int(index1)
                              index2 = input("Choose your second index: ")
                              # checks if the inputed value is an integer, otherwise return an error message
                              try: 
                                    # checks if the index is valid, otherwise return an error message
                                    if 0 <= int(index2) < len(my_list) : 
                                          index2 = int(index2)
                                          # checks which index is bigger to do the action
                                          if index1 < index2 :
                                                print(functions.gcd(my_list, index1, index2), '\n')
                                          else :
                                                print(functions.gcd(my_list, index2, index1), '\n')
                                    else :
                                          print("Invalid index!", '\n')
                              except ValueError : 
                                    print("Invalid index!", '\n')
                        else :
                              print("Invalid index!", '\n')
                  except ValueError :
                        print("Invalid index!", '\n')
            # using the 'max_between' function returns the greatest value
            # of all the numbers between 2 specific indexes if the action is '10'
            elif x == 10 :
                  index1 = input("Choose your first index: ")
                  # checks if the inputed value is an integer, otherwise return an error message
                  try:
                        # checks if the index is valid, otherwise return an error message
                        if 0 <= int(index1) < len(my_list) : 
                              index1 = int(index1)
                              index2 = input("Choose your second index: ")
                              # checks if the inputed value is an integer, otherwise return an error message
                              try:
                                    # checks if the index is valid, otherwise return an error message
                                    if 0 <= int(index2) < len(my_list) : 
                                          index2 = int(index2)
                                          # checks which index is bigger to do the action
                                          if index1 < index2 :
                                                print(functions.max_between(my_list, index1, index2), '\n')
                                          else :
                                                print(functions.max_between(my_list, index2, index1), '\n')
                                    else :
                                          print("Invalid Index!", '\n')
                              except ValueError :
                                    print("Invalid index!", '\n')
                        else :
                              print("Invalid index!", '\n')
                  except ValueError :
                        print("Invalid index!", '\n')
            # using the 'filter_prime' function is filtering the list such that all
            # the prime numbers remains in the list and all the others are deleted
            # if the action is '11'
            elif x == 11 :
                  undo.append(my_list[:])
                  step += 1
                  functions.filter_prime(my_list)
                  print('\n')
            
            # using the 'filter_negative' function is filtering the list such that all
            # the negative numbers remains in the list and all the others are deleted
            # if the action is '12'
            elif x == 12 :
                  undo.append(my_list[:])
                  step += 1
                  functions.filter_negative(my_list)
                  print('\n')

            # prints the list if the action is '13'
            elif x == 13 :
                  print(my_list, '\n')
            # prints the list in a file
            elif x == 14 :
                  for i in my_list :
                        index = str(i)
                        fp.write(index)
                        fp.write(" ")
                  fp.write('\n')
                  print('\n')
            # using the 'undo' function undo the last action to the list 
            # if the action is '14'
            elif x == 15 :
                  if step > 0 :
                        my_list = functions.undo_step(my_list, undo, step)
                        step -= 1
                        print('\n')
                  else :
                        print("Nothing left to undo!", '\n')

            # prints 'Invalid option' if the selected action is not in the list above
            elif x != 0 :
                  print("Invalid option!", '\n')
            
            # prints that the program is closing if the action is '0'
            elif x == 0 :
                  print("Closing the program...", '\n')
      # if the inputed value is not part of the list prints an error
      except ValueError:
            print("Invalid option!", '\n')