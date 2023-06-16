from default import Plane
from default import Passenger

class UI:
    def __init__(self, ctrl) :
        """
        constructor
        """
        self.__ctrl = ctrl
    
    @staticmethod
    def readInput() :
        """
        Reads the input from the user.
        """
        try:
            option = int(input(">> "))
            return option
        except Exception:
            UI.readInput()

    @staticmethod
    def readPassenger() :
        """
        Reads a passenger from the user.
        """
        try:
            print("First name: ")
            first_name = input('>> ')
            print("Last name: ")
            last_name = input('>> ')
            print("Passport number: ")
            passport_number = input('>> ')
            return Passenger(first_name, last_name, passport_number)
        except Exception:
            raise Exception("\nInvalid passenger!\n")

    @staticmethod
    def readPlane() :
        """
        Reads a plane from the user.
        """
        try:
            print("Number: ")
            number = int(input('>> '))
            print("Company: ")
            company = input('>> ')
            print("Capacity: ")
            capacity = int(input('>> '))
            print("Destination: ")
            destination = input('>> ')
            print("List of passengers: ")
            list_of_passengers = []
            print("Number of passengers: ")
            number_of_passengers = int(input('>> '))
            print('\n')
            for i in range(number_of_passengers) :
                print("Passenger: ")
                passenger = UI.readPassenger()
                print('\n')
                list_of_passengers.append(passenger)
            return Plane(number, company, capacity, destination, list_of_passengers)
        except Exception:
            raise Exception("\nInvalid plane!\n")

    @staticmethod
    def print_menu() :
        """
        Prints the menu.
        """
        menu = "Commands: \n"
        menu += "1. Sort by last name \n"
        menu += "2. Sort by number of passengers \n"
        menu += "3. Sort by number of passengers with the first name starting with a given substring \n"
        menu += "4. Sort by the string obtained by concatenation of the number of passengers in the plane and the destination \n"
        menu += "5. Identify planes that have passengers with passport numbers starting with the same 3 letters \n"
        menu += "6. Identify passengers from a given plane for which the first name or last name contain a string given as a parameter \n"
        menu += "7. Identify planes where there is a passenger with given name \n"
        menu += "8. Form groups of k passengers from the same plane but with different last names \n"
        menu += "9. Form  groups  of k planes  with  the  same  destination  but  belonging  to  different  airline companies \n"
        menu += "10. Print repository\n"
        menu += "***********\n"
        menu += "11. Add plane \n"
        menu += "12. Remove plane \n"
        menu += "13. Update plane \n"
        menu += "0. Exit \n"
        print(menu)

    def run(self) :
        """
        Runs the application.
        """
        while True :
            UI.print_menu()
            try :
                try:
                    command = int(input(">> "))
                except Exception:
                    raise Exception("\nInvalid command!\n")
                if command == 0 :
                    print("Bye!")
                    exit()

                elif command == 1 :
                    try:
                        print("Plane number: ")
                        plane_nr = int(input('>> '))
                        self.__ctrl.sortByLastName(plane_nr)
                    except Exception:
                        raise Exception("\nInvalid plane number!\n")
                    print('\n')
                    
                elif command == 2 :
                    self.__ctrl.sortByNumberOfPassengers()
                    print('\n')

                elif command == 3 :
                    substring = input("Substring: ")
                    self.__ctrl.sortByNumberOfPassengersWithTheFirstNameStartingWithAGivenSubstring(substring)
                    print('\n')

                elif command == 4 :
                    self.__ctrl.sortByTheStringObtainedByConcatenation()

                elif command == 5 :
                    res = self.__ctrl.identifyPlanesThatHavePassengersWithPassportNumberStartingWithTheSame3Letters()
                    res2 = []
                    for el in res :
                        res2.append(el.get_number())
                    print(res2)

                elif command == 6 :
                    string = input("String: ")
                    plane = int(input("Plane: "))
                    res = self.__ctrl.identifyPassengersFromAGivenPlaneContainingAString(plane, string)
                    for elem in res :
                        print(str(elem) + '\n')
                    

                elif command == 7 :
                    name = input("Name: ")
                    res = self.__ctrl.identifyPlanesWhereThereIsAPassengerWithGivenName(name)
                    res2 = []
                    for el in res :
                        res2.append(el.get_number())
                    print(res2)

                elif command == 8 :
                    gs = int(input("Group size: "))
                    print("---------------------")
                    for el in self.__ctrl.groupPassengersByLastName(gs) :
                        for el2 in el :
                            for el3 in el2 :
                                print(str(el3))
                            print('\n')
                        print("---------------------")

                elif command == 9 :
                    gs = int(input("Group size: "))
                    print("---------------------")
                    for el in self.__ctrl.groupPlanesByDestination(gs) :
                        for el2 in el :
                            print("Plane number: ", el2.get_number())
                        print("---------------------")

                elif command == 10 :
                    print(self.__ctrl.printrepo())

                elif command == 11 :
                    plane = UI.readPlane()
                    self.__ctrl.add(plane)
                    print('\n')

                elif command == 12 :
                    try:
                        print("Plane number: ")
                        plane_nr = int(input('>> '))
                    except Exception:
                        raise Exception("\nInvalid plane number!\n")
                    self.__ctrl.remove(plane_nr)
                    print('\n')

                elif command == 13 :
                    try:
                        print("Plane number: ")
                        plane_nr = int(input('>> '))
                    except Exception:
                        raise Exception("\nInvalid plane number!\n")
                    plane = UI.readPlane()
                    self.__ctrl.update(plane_nr, plane)
                    print('\n')

                else :
                    print("Invalid command!")

            except Exception as e :
                print(e)

