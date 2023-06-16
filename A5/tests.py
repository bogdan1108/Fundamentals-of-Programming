import unittest
from repo import Repository
from default import Plane
from default import Passenger

class TestPlane(unittest.TestCase) :
    """
    Tests the Plane class.
    """
    def test_get(self) :
        """
        Tests the getters.
        """
        plane = Plane(1, 'WizzAir', 200, 'London', [])
        self.assertEqual(plane.get_number(), 1)
        self.assertEqual(plane.get_company(), 'WizzAir')
        self.assertEqual(plane.get_capacity(), 200)
        self.assertEqual(plane.get_destination(), 'London')
        self.assertEqual(plane.get_list_of_passengers(), [])

    def test_set(self) :
        """
        Tests the setters.
        """
        plane = Plane(1, 'WizzAir', 200, 'London', [])
        plane.set_number(2)
        plane.set_company('RyanAir')
        plane.set_capacity(100)
        plane.set_destination('Paris')
        self.assertEqual(plane.get_number(), 2)
        self.assertEqual(plane.get_company(), 'RyanAir')
        self.assertEqual(plane.get_capacity(), 100)
        self.assertEqual(plane.get_destination(), 'Paris')

class TestPassenger(unittest.TestCase) :
    """
    Tests the Passenger class.
    """
    def test_get(self) :
        """
        Tests the getters.
        """
        passenger = Passenger('John', 'Doe', '123456789')
        self.assertEqual(passenger.get_first_name(), 'John')
        self.assertEqual(passenger.get_last_name(), 'Doe')
        self.assertEqual(passenger.get_passport_number(), '123456789')

    def test_set(self) :
        """
        Tests the setters.
        """
        passenger = Passenger('John', 'Doe', '123456789')
        passenger.set_first_name('Jane')
        passenger.set_last_name('Doe')
        passenger.set_passport_number('987654321')
        self.assertEqual(passenger.get_first_name(), 'Jane')
        self.assertEqual(passenger.get_last_name(), 'Doe')
        self.assertEqual(passenger.get_passport_number(), '987654321')

class TestRepository(unittest.TestCase) :
    """
    Tests the Repository class.
    """
    def test_add(self) :
        """
        Tests the add method.
        """
        repo = Repository()
        plane = Plane(1, 'WizzAir', 200, 'London', [])
        repo.add_plane(plane)
        self.assertEqual(repo.get_plane(0), str(plane))
        plane = Plane(2, 'RyanAir', 100, 'Paris', [])
        repo.add_plane(plane)
        self.assertEqual(repo.get_plane(1), str(plane))
        plane = Plane(3, 'BlueAir', 150, 'Bucharest', [])
        repo.add_plane(plane)
        self.assertEqual(repo.get_plane(2), str(plane))

    def test_remove(self) :
        """
        Tests the remove method.
        """
        repo = Repository()
        plane1 = Plane(1, 'WizzAir', 200, 'London', [])
        repo.add_plane(plane1)
        plane2 = Plane(2, 'RyanAir', 100, 'Paris', [])
        repo.add_plane(plane2)
        plane3 = Plane(3, 'BlueAir', 150, 'Bucharest', [])
        repo.add_plane(plane3)
        repo.delete_plane(1)
        self.assertEqual(repo.get_plane(1), str(plane3))
        repo.delete_plane(0)
        self.assertEqual(repo.get_plane(0), str(plane3))
        repo.delete_plane(0)
        self.assertEqual(len(repo), 0)

    def test_update(self) :
        """
        Tests the update method.
        """
        repo = Repository()
        plane1 = Plane(1, 'WizzAir', 200, 'London', [])
        repo.add_plane(plane1)
        plane2 = Plane(2, 'RyanAir', 100, 'Paris', [])
        repo.add_plane(plane2)
        plane3 = Plane(3, 'BlueAir', 150, 'Bucharest', [])
        repo.add_plane(plane3)
        plane4 = Plane(4, 'BlueAir', 150, 'Bucharest', [])
        repo.update_plane(1, plane4)
        self.assertEqual(repo.get_plane(0), str(plane4))
        plane5 = Plane(5, 'BlueAir', 150, 'Bucharest', [])
        repo.update_plane(0, plane5)
        self.assertEqual(repo.get_plane(0), str(plane5))
        plane6 = Plane(6, 'BlueAir', 150, 'Bucharest', [])
        repo.update_plane(2, plane6)
        self.assertEqual(repo.get_plane(1), str(plane6))

    def test_sort_by_last_name(self) :
        """
        Tests the sort_by_last_name method.
        """
        repo = Repository()
        plane1 = Plane(1, 'WizzAir', 200, 'London', [Passenger('John', 'Doe', '123456789'), Passenger('Bane', 'Doe', '987654321')])
        repo.add_plane(plane1)
        plane2 = Plane(2, 'RyanAir', 100, 'Paris', [Passenger('Bob', 'Doe', '123456789'), Passenger('Alice', 'Rock', '987654321')])
        repo.add_plane(plane2)
        plane3 = Plane(3, 'BlueAir', 150, 'Bucharest', [Passenger('Cristina', 'Doe', '123456789'), Passenger('Alex', 'Martinez', '987654321')])
        repo.add_plane(plane3)
        repo.sort_by_last_name(1)
        self.assertEqual(plane1.get_list_of_passengers()[0].get_last_name(), 'Doe')
        repo.sort_by_last_name(2)
        self.assertEqual(plane2.get_list_of_passengers()[1].get_last_name(), 'Rock')
        repo.sort_by_last_name(3)
        self.assertEqual(plane3.get_list_of_passengers()[0].get_last_name(), 'Doe')

    def test_sort_by_number_of_passengers(self) :
        """
        Tests the sort_by_number_of_passengers method.
        """
        repo = Repository()
        plane1 = Plane(1, 'WizzAir', 200, 'London', [Passenger('John', 'Doe', '123456789'), Passenger('Bane', 'Doe', '987654321')])
        repo.add_plane(plane1)
        plane2 = Plane(2, 'RyanAir', 100, 'Paris', [Passenger('Bob', 'Doe', '123456789'), Passenger('Alice', 'Rock', '987654321')])
        repo.add_plane(plane2)
        plane3 = Plane(3, 'BlueAir', 150, 'Bucharest', [Passenger('Cristina', 'Doe', '123456789'), Passenger('Alex', 'Martinez', '987654321')])
        repo.add_plane(plane3)
        repo.sort_by_number_of_passengers()
        self.assertEqual(repo.get_plane(0), str(plane1))
        self.assertEqual(repo.get_plane(1), str(plane2))
        self.assertEqual(repo.get_plane(2), str(plane3))

    def test_sort_by_number_of_passengers_with_the_first_name_starting_with_a_given_substring(self) :
        """
        Tests the sort_by_number_of_passengers_with_the_first_name_starting_with_a_given_substring method.
        """
        repo = Repository()
        plane1 = Plane(1, 'WizzAir', 200, 'London', [Passenger('John', 'Doe', '123456789'), Passenger('Bane', 'Doe', '987654321')])
        repo.add_plane(plane1)
        plane2 = Plane(2, 'RyanAir', 100, 'Paris', [Passenger('Bob', 'Doe', '123456789'), Passenger('Alice', 'Rock', '987654321')])
        repo.add_plane(plane2)
        plane3 = Plane(3, 'BlueAir', 150, 'Bucharest', [Passenger('Cristina', 'Doe', '123456789'), Passenger('Alex', 'Martinez', '987654321')])
        repo.add_plane(plane3)
        repo.sort_by_number_of_passengers_with_the_first_name_starting_with_a_given_substring('A')
        self.assertEqual(repo.get_plane(0), str(plane2))
        self.assertEqual(repo.get_plane(1), str(plane3))
        self.assertEqual(repo.get_plane(2), str(plane1))

    def test_sort_by_the_string_obtained_by_concatenation_of_the_number_of_passengers_in_the_plane_and_the_destination(self) :
        """
        Tests the sort_by_the_string_obtained_by_concatenation_of_the_number_of_passengers_in_the_plane_and_the_destination method.
        """
        repo = Repository()
        plane1 = Plane(1, 'WizzAir', 200, 'London', [Passenger('John', 'Doe', '123456789'), Passenger('Bane', 'Doe', '987654321')])
        repo.add_plane(plane1)
        plane2 = Plane(2, 'RyanAir', 100, 'Paris', [Passenger('Bob', 'Doe', '123456789'), Passenger('Alice', 'Rock', '987654321')])
        repo.add_plane(plane2)
        plane3 = Plane(3, 'BlueAir', 150, 'Bucharest', [Passenger('Cristina', 'Doe', '123456789'), Passenger('Alex', 'Martinez', '987654321')])
        repo.add_plane(plane3)
        repo.sort_by_the_string_obtained_by_concatenation_of_the_number_of_passengers_in_the_plane_and_the_destination()
        self.assertEqual(repo.get_plane(0), str(plane2))
        self.assertEqual(repo.get_plane(1), str(plane1))
        self.assertEqual(repo.get_plane(2), str(plane3))

    def test_identify_planes_that_have_passengers_with_passport_numbers_starting_with_the_same_3_letters(self) :
        """
        Tests the identify_planes_that_have_passengers_with_passport_numbers_starting_with_the_same_3_letters method.
        """
        repo = Repository()
        plane1 = Plane(1, 'WizzAir', 200, 'London', [Passenger('John', 'Doe', '123456789'), Passenger('Bane', 'Doe', '123456789')])
        repo.add_plane(plane1)
        self.assertEqual(repo.identify_planes_that_have_passengers_with_passport_numbers_starting_with_the_same_3_letters(), [plane1])
        plane2 = Plane(2, 'RyanAir', 100, 'Paris', [Passenger('Bob', 'Doe', '123456789'), Passenger('Alice', 'Rock', '123456789')])
        repo.add_plane(plane2)
        self.assertEqual(repo.identify_planes_that_have_passengers_with_passport_numbers_starting_with_the_same_3_letters(), [plane1, plane2])
        plane3 = Plane(3, 'BlueAir', 150, 'Bucharest', [Passenger('Cristina', 'Doe', '123456789'), Passenger('Alex', 'Martinez', '123654321')])
        repo.add_plane(plane3)
        self.assertEqual(repo.identify_planes_that_have_passengers_with_passport_numbers_starting_with_the_same_3_letters(), [plane1, plane2, plane3])
    
    def test_identify_passengers_from_a_given_plane_containing_a_string(self) :
        """
        Tests the identify_passengers_from_a_given_plane_containing_a_string method.
        """
        repo = Repository()
        plane1 = Plane(1, 'WizzAir', 200, 'London', [Passenger('John', 'Doe', '123456789'), Passenger('Bane', 'Doe', '123456789')])
        repo.add_plane(plane1)
        self.assertEqual(repo.identify_passengers_from_a_given_plane_containing_a_string(plane1, 'a'), [plane1.get_list_of_passengers()[1]])
        plane2 = Plane(2, 'RyanAir', 100, 'Paris', [Passenger('Bob', 'Doe', '123456789'), Passenger('Alice', 'Rock', '123456789')])
        repo.add_plane(plane2)
        self.assertEqual(repo.identify_passengers_from_a_given_plane_containing_a_string(plane2, 'o'), [plane2.get_list_of_passengers()[0], plane2.get_list_of_passengers()[1]])
        plane3 = Plane(3, 'BlueAir', 150, 'Bucharest', [Passenger('Cristina', 'Doe', '123456789'), Passenger('Alex', 'Martinez', '123654321')])
        repo.add_plane(plane3)
        self.assertEqual(repo.identify_passengers_from_a_given_plane_containing_a_string(plane3, 'a'), [plane3.get_list_of_passengers()[0], plane3.get_list_of_passengers()[1]])

    def test_identify_planes_where_there_is_a_passenger_with_given_name(self) :
        """
        Tests the identify_planes_where_there_is_a_passenger_with_given_name method.
        """
        repo = Repository()
        plane1 = Plane(1, 'WizzAir', 200, 'London', [Passenger('John', 'Doe', '123456789'), Passenger('Bane', 'Doe', '123456789')])
        repo.add_plane(plane1)
        self.assertEqual(repo.identify_planes_where_there_is_a_passenger_with_given_name('John'), [plane1])
        plane2 = Plane(2, 'RyanAir', 100, 'Paris', [Passenger('Bob', 'Doe', '123456789'), Passenger('Alice', 'Rock', '123456789')])
        repo.add_plane(plane2)
        self.assertEqual(repo.identify_planes_where_there_is_a_passenger_with_given_name('Bob'), [plane2])
        plane3 = Plane(3, 'BlueAir', 150, 'Bucharest', [Passenger('Cristina', 'Doe', '123456789'), Passenger('Alex', 'Martinez', '123654321')])
        repo.add_plane(plane3)
        self.assertEqual(repo.identify_planes_where_there_is_a_passenger_with_given_name('Cristina'), [plane3])

if __name__ == '__main__' :
    unittest.main(exit = False)
