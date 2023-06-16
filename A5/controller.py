from default import Plane
from default import Passenger

class Controller :
    def __init__(self, repo) :
        """
        constructor
        """
        self.__repo = repo
        p1 = Passenger('John', 'Voe', '12234')
        p2 = Passenger('Jane', 'Dove', '1234321')
        p3 = Passenger('Martha', 'Stewart', '123141')

        p4 = Passenger('George', 'Bush', 'abc1115')
        p5 = Passenger('Philip', 'David', 'abc115180')

        p6 = Passenger('Rupert', 'David', '192')
        p7 = Passenger('Michael', 'Jackson', '175')

        p8 = Passenger('Lidia', 'Buble', '342a')
        p9 = Passenger('George', 'Clooney', '9214b')
        p10 = Passenger('Michelle', 'Obama', '24ab')
        p11 = Passenger('George', 'Washington', '1934bc')

        plane1 = Plane(1, 'Wizz Air', 100, 'London', [p1, p2, p3])
        plane2 = Plane(2, 'Ryan Air', 200, 'Paris', [p4, p5])
        plane3 = Plane(3, 'Lufthansa', 100, 'London', [p6, p7])
        plane4 = Plane(4, 'Blue Air', 150, 'China', [p8, p9, p10, p11])

        self.__repo.add_plane(plane1)
        self.__repo.add_plane(plane2)
        self.__repo.add_plane(plane3)
        self.__repo.add_plane(plane4)

    def add(self, plane) :
        """
        adds a plane to the list of planes
        input: plane - Plane
        """
        self.__repo.add_plane(plane)

    def remove(self, nr_plane) :
        """
        removes a plane from the list of planes
        input: nr_plane - integer
        """
        self.__repo.delete_plane(nr_plane)

    def update(self, nr_plane, plane) :
        """
        updates a plane from the list of planes
        input: nr_plane - integer
        input: plane - Plane
        """
        self.__repo.update_plane(nr_plane, plane)

    def getPlaneByIndex(self, index) :
        """
        returns the plane at the given index
        input: index - integer
        """
        return self.__repo.get_plane(index)

    def updatePlaneByIndex(self, index, plane) :
        """
        updates the plane at the given index
        input: index - integer
        input: plane - Plane
        """
        self.__repo.update_plane(index, plane)

    def deletePlaneByIndex(self, index) :
        """
        deletes the plane at the given index
        input: index - integer
        """
        self.__repo.delete_plane(index)

    def sortByLastName(self, plane_nr) :
        """
        sorts the passengers of a given plane by last name
        input: plane_nr - integer
        """
        self.__repo.sort_by_last_name(plane_nr)

    def sortByNumberOfPassengers(self) :
        """
        sorts the planes by number of passengers
        """
        self.__repo.sort_by_number_of_passengers()

    def sortByNumberOfPassengersWithTheFirstNameStartingWithAGivenSubstring(self, substring) :
        """
        sorts the planes by number of passengers with the first name starting with a given substring
        input: substring - string
        """
        self.__repo.sort_by_number_of_passengers_with_the_first_name_starting_with_a_given_substring(substring)

    def sortByTheStringObtainedByConcatenation(self) :
        """
        sorts the planes by the string obtained by concatenation of the number of passengers in the plane and the destination
        """
        self.__repo.sort_by_the_string_obtained_by_concatenation_of_the_number_of_passengers_in_the_plane_and_the_destination()

    def identifyPlanesThatHavePassengersWithPassportNumberStartingWithTheSame3Letters(self) :
        """
        identifies the planes that have passengers with passport number starting with the same 3 letters
        input: substring - string
        """
        return self.__repo.identify_planes_that_have_passengers_with_passport_numbers_starting_with_the_same_3_letters()

    def identifyPassengersFromAGivenPlaneContainingAString(self, plane_nr, string) :
        """
        identifies the passengers from a given plane containing a string
        input: plane_nr - integer
        input: string - string
        """
        return self.__repo.identify_passengers_from_a_given_plane_containing_a_string(plane_nr, string)

    def identifyPlanesWhereThereIsAPassengerWithGivenName(self, name) :
        """
        identifies the planes where there is a passenger with a given name
        input: name - string
        """
        return self.__repo.identify_planes_where_there_is_a_passenger_with_given_name(name)

    def groupPassengersByLastName(self, gs) :
        """
        groups the passengers by last name
        input: gs - GroupService
        """
        aux = []
        for dep in self.__repo.getAll() :
            aux.append(self.__repo.group_passengers_by_last_name(gs, dep))
        return aux

    def groupPlanesByDestination(self,gs) :
        """
        groups the passengers by destination
        input: gs - GroupService
        """
        return self.__repo.group_planes_by_destination(gs)

    def get(self) :
        """
        returns the list of planes
        """
        return self.__repo.getAll()

    def length(self) :
        """
        returns the length of the list of planes
        """
        return len(self.__repo)

    def printrepo(self) :
        """
        prints the list of planes
        """
        return str(self.__repo)

    