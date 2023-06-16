from default import Plane
from default import Passenger
import utils

class Repository:
    def __init__(self) :
        """
        constructor
        """
        self.list_of_planes = []#Plane(1, 'Wizz Air', 100, 'London', [Passenger('John', 'Voe', '12234'), Passenger('Jane', 'Dove', '1234321'), Passenger('Martha', 'Stewart', '123141')]),
                     #Plane(2, 'Ryan Air', 200, 'Paris', [Passenger('George', 'Bush', 'abc1115'), Passenger('Philip', 'David', 'abc115180')]),
                     #Plane(3, 'Wizz Air', 100, 'London', [Passenger('Rupert', 'David', '192'), Passenger('Michael', 'Jackson', '175')])]
    
    def getAll(self) :
        """
        returns the list of planes
        """
        return self.list_of_planes

    def add_plane(self, plane) :
        """
        adds a plane to the list of planes
        """
        self.list_of_planes.append(plane)

    def get_plane(self, index) :
        """
        returns the plane at the given index
        input: index - integer
        """
        return str(self.list_of_planes[index])

    def update_plane(self, index, plane) :
        """
        updates the plane at the given index
        input: index - integer
        """
        for i in range(len(self.list_of_planes)) :
            if self.list_of_planes[i].get_number() == index :
                index = i
        self.list_of_planes[index] = plane

    def delete_plane(self, index) :
        """
        deletes the plane at the given index
        input: index - integer
        """
        for i in range(len(self.list_of_planes)) :
            if self.list_of_planes[i].get_number() == index :
                index = i
        del self.list_of_planes[index]

    def sort_by_last_name(self, plane_nr) :
        """
        sorts the passengers of a plane by last name
        input: plane_nr - integer
        """
        for i in range(len(self.list_of_planes)) :
            if self.list_of_planes[i].get_number() == plane_nr :
                index = i
        utils.mySort(self.list_of_planes[index].get_list_of_passengers(), 
                     lambda x, y : x.get_last_name() > y.get_last_name())

    def sort_by_number_of_passengers(self) :
        """
        sorts the planes by number of passengers
        """
        utils.mySort(self.list_of_planes, 
                     lambda x, y : len(x.get_list_of_passengers()) > len(y.get_list_of_passengers()))
            
    def sort_by_number_of_passengers_with_the_first_name_starting_with_a_given_substring(
        self, substring) :
        """
        sorts the planes by number of passengers with the first name starting with a given substring
        input: substring - string
        """
        utils.mySort(self.list_of_planes, 
                     lambda x, y : len(list(filter(
                         lambda z : z.get_first_name().startswith(substring), 
                         x.get_list_of_passengers()))) < len(list(filter(
                             lambda z : z.get_first_name().startswith(substring), 
                             y.get_list_of_passengers()))))

    def sort_by_the_string_obtained_by_concatenation_of_the_number_of_passengers_in_the_plane_and_the_destination(self) :
        """
        sorts the planes by the string obtained by concatenation of the number of passengers in the plane and the destination
        """
        utils.mySort(self.list_of_planes, 
                     lambda x, y : str(len(x.get_list_of_passengers())) + x.get_destination() < str(len(y.get_list_of_passengers())) + y.get_destination())

    def identify_planes_that_have_passengers_with_passport_numbers_starting_with_the_same_3_letters(self) :
        """
        identifies the planes that have passengers with passport numbers starting with the same 3 letters
        input: substring - string
        """
        list = self.list_of_planes[:]
        return utils.myFilter(list, lambda x : x.get_prefix() > 0)

    def identify_passengers_from_a_given_plane_containing_a_string(self, plane_nr, string) :
        """
        identifies the passengers from a given plane containing a string
        input: plane_nr - integer
        input: string - string
        """
        for element in self.list_of_planes :
            if element.get_number() == plane_nr :
                plane_nr = element
        return utils.myFilter(plane_nr.get_list_of_passengers(), lambda x : string in x.get_first_name() or string in x.get_last_name())

    def identify_planes_where_there_is_a_passenger_with_given_name(self, name) :
        """
        identifies the planes where there is a passenger with given name
        input: name - string
        """
        def checkPlane(plane) :
            """
            checks if a plane has a passenger with given name
            input: plane - Plane
            """
            for el in plane.get_list_of_passengers() :
                if el.get_first_name() == name or el.get_last_name() == name :
                    return True
            return False
        return utils.myFilter(self.list_of_planes, checkPlane)

    def constructSolution(self, sol, myList):
        """
        Constructs a solution from a list of indexes
        IN: sol - list of indexes
        myList - list of objects
        OUT: a list of objects
        """
        aux  = []
        for i in sol:
            aux.append( myList[i] )
        return aux
    
    def group_passengers_by_last_name(self, gs, d):
        """
        Groups passengers by last name using backtracking
        IN: gs - genetic algorithm
        d - dictionary
        OUT: a list of lists of objects
        """
        def c1(sol, myList):
            '''
            Checks if all elements are unique after they are added.
            '''
            for i in range(len(sol) - 1):
                if myList[sol[i]].get_last_name() == myList[sol[len(sol) - 1]].get_last_name():
                    return False
            return True
        
        def c2(sol, myList):
            '''
            Checks if all elements are unique after they are added. 
            '''
            for i in range(len(sol) - 1):
                if myList[sol[i]].get_first_name() == myList[sol[len(sol) - 1]].get_first_name():
                    if myList[sol[i]].get_last_name() == myList[sol[len(sol) - 1]].get_last_name():
                        return False
            return True

        myList = d.get_list_of_passengers()
        param = [gs]
        constraints = [c1, c2]
        aux = []
        for el in utils.myBacktracking(param, myList, constraints):
            aux.append( self.constructSolution(el, myList) )
        return aux

    def group_planes_by_destination(self, gs):
        """
        Groups planes by destination using backtracking
        IN: gs - genetic algorithm
        d - dictionary
        OUT: a list of lists of objects
        """
        def c1(sol, myList):
            '''
            Checks if all elements are unique after they are added.
            '''
            for i in range(len(sol) - 1):
                if myList[sol[i]].get_destination() != myList[sol[len(sol) - 1]].get_destination():
                    if myList[sol[i]].get_company() != myList[sol[len(sol) - 1]].get_company():
                        return False
            return True
        
        def c2(sol, myList):
            '''
            Checks if all elements are unique after they are added. 
            '''
            for i in range(len(sol) - 1):
                if myList[sol[i]].get_number() == myList[sol[len(sol) - 1]].get_number():
                    return False
            return True

        myList = self.list_of_planes
        param = [gs]
        constraints = [c1, c2]
        aux = []
        for el in utils.myBacktracking(param, myList, constraints):
            aux.append( self.constructSolution(el, myList) )
        print(aux)
        return aux

    def __str__(self) :
        """
        Returns a string representation of the repository.
        """
        res = ""
        for element in self.list_of_planes :
            res += str(element)
            res += "\n"
            res += " "
        return res

    def __len__(self) :
        """
        Returns the length of the repository.
        """
        return len(self.list_of_planes)