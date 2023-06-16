class Plane:
    def __init__(self, number, company, capacity, destination, list_of_passengers) :
        """
        constructor
        """
        self.number = number
        self.company = company
        self.capacity = capacity
        self.destination = destination
        self.list_of_passengers = list_of_passengers

    # getters
    def get_number(self) :
        """
        returns the number of the plane
        """
        return self.number
    
    def get_company(self) :
        """
        returns the company of the plane
        """
        return self.company

    def get_capacity(self) :
        """
        returns the capacity of the plane
        """
        return self.capacity
    
    def get_destination(self) :
        """
        returns the destination of the plane
        """
        return self.destination

    def get_list_of_passengers(self) :
        """
        returns the list of passengers of the plane
        """
        return self.list_of_passengers

    # setters
    def set_number(self, number) :
        """
        sets the number of the plane
        """
        self.number = number

    def set_company(self, company) :
        """
        sets the company of the plane
        """
        self.company = company
    
    def set_capacity(self, capacity) :
        """
        sets the capacity of the plane
        """
        self.capacity = capacity

    def set_destination(self, destination) :
        """
        sets the destination of the plane
        """
        self.destination = destination

    def set_list_of_passengers(self, list_of_passengers) :
        """
        sets the list of passengers of the plane
        """
        self.list_of_passengers = list_of_passengers

    def __len__(self) :
        """
        returns the number of passengers of the plane
        """
        return len(self.list_of_passengers)

    def get_prefix(self) :
        """
        returns the prefix of the plane
        """
        x = self.list_of_passengers[0].get_passport_number()[:3]
        for elem in self.list_of_passengers :
            if elem.get_passport_number()[:3] != x :
                return False
        return True

    def __str__(self) :
        """
        returns a string representation of the plane
        """
        sol = 'Plane number: [' + str(self.number) + '], company: [' + self.company + '], capacity: [' + str(self.capacity) + '], destination: [' + self.destination + '], list of passengers: \n'
        for element in self.list_of_passengers :
            sol += '\t['
            sol += str(element) + '] \n'
        return sol

class Passenger:
    def __init__(self, first_name, last_name, passport_number) :
        """
        constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number

    # getters
    def get_first_name(self) :
        """
        returns the first name of the passenger
        """
        return self.first_name

    def get_last_name(self) :
        """
        returns the last name of the passenger
        """
        return self.last_name

    def get_passport_number(self) :
        """
        returns the passport number of the passenger
        """
        return self.passport_number

    # setters
    def set_first_name(self, first_name) :
        """
        sets the first name of the passenger
        """
        self.first_name = first_name

    def set_last_name(self, last_name) :
        """
        sets the last name of the passenger
        """
        self.last_name = last_name

    def set_passport_number(self, passport_number) :
        """
        sets the passport number of the passenger
        """
        self.passport_number = passport_number

    def __str__(self) :
        """
        returns a string representation of the passenger
        """
        return 'Passenger first name: ' + self.first_name + ', last name: ' + self.last_name + ', passport number: ' + self.passport_number