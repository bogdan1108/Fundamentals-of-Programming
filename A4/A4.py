import matplotlib.pyplot as plt

class MyVector:
    """
    Class that represents a vector.
    Attributes: name_id, color, type, values
    """
    def __init__(self, name_id, color, type, values) :
        self.name_id = name_id
        self.color = color
        self.type = type
        self.values = values

    # getters
    def get_name_id(self) :
        return self.name_id
    
    def get_color(self) :
        return self.color

    def get_type(self) :
        return self.type

    def get_values(self) :
        return self.values

    # setters
    def set_name_id(self, new_value) :
        self.name_id = new_value
    
    def set_color(self, new_value) :
        self.color = new_value
    
    def set_type(self, new_value) :
        self.type = new_value

    def set_values(self, new_values) :
        self.values = new_values

    # scalar operations
    def add_scalar(self, scalar) :
        """
        Adds a scalar to the vector.
        Input: scalar
        """
        new_vector = []
        for element in self.values :
            element += scalar
            new_vector.append(element)
        self.values = new_vector
    
    # vector operations
    def add_vector(self, value) :
        """
        Adds a vector to the vector.
        Input: value
        """
        new_vector = []
        if len(self.values) == len(value.get_values()) :
            new_vector2 = value.get_values()
            for i, element in enumerate(self.values) :
                element += new_vector2[i]
                new_vector.append(element)
            self.values = new_vector
        else :
            raise ValueError("Vectors must have the same size! \n")

    def sub_vector(self, value) :
        """
        Subtracts a vector from the vector.
        Input: value
        """
        new_vector = []
        if len(self.values) == len(value.get_values()) :
            new_vector2 = value.get_values()
            for i, element in enumerate(self.values) :
                element -= new_vector2[i]
                new_vector.append(element)
            self.values = new_vector
        else :
            raise ValueError("Vectors must have the same size! \n")

    def mul_vector(self, value) :
        """
        Multiplies a vector with the vector.
        Input: value
        """
        new_value = 0
        if len(self.values) == len(value.get_values()) :
            new_vector2 = value.get_values()
            for i, element in enumerate(self.values) :
                new_value += element * new_vector2[i]
            return new_value
        else :
            raise ValueError("Vectors must have the same size! \n")

    # reduction operations
    def sum_of_elements(self) :
        """
        Returns the sum of the elements of the vector.
        """
        summ = 0
        for element in self.values :
            summ += element
        return summ

    def product_of_elements(self) :
        """
        Returns the product of the elements of the vector.
        """
        product = 1
        for element in self.values :
            product *= element
        return product
    
    def avarage_of_elements(self) :
        """
        Returns the avarage of the elements of the vector.
        """
        avg = 0
        for element in self.values :
            avg += element
        return avg/len(self.values)

    def minimum_of_elements(self) :
        """
        Returns the minimum of the elements of the vector.
        """
        minn = self.values[0]
        for element in self.values :
            if element < minn :
                minn = element
        return minn

    def maximum_of_elements(self) :
        """
        Returns the maximum of the elements of the vector.
        """
        maxx = self.values[0]
        for element in self.values :
            if element > maxx :
                maxx = element
        return maxx

    # string return
    def __str__(self) :
        return f"Vector [{self.name_id}] of color {self.color} and type {self.type} with values {self.values}." 

class Repository:
    """
    Class that represents a repository.
    Attributes: data
    """
    def __init__(self) :
        self.__data = []

    def addNew(self, vector) :
        """
        Adds a new vector to the repository.
        Input: vector
        """
        self.__data.append(vector)

    def __str__(self) :
        """
        Returns a string representation of the repository.
        """
        res = ""
        for element in self.__data :
            res += str(element)
            res += "\n"
            res += " "
        return res

    def getVector(self, index) :
        """
        Returns the vector at the given index.
        Input: index
        """
        return str(self.__data[index])

    def updateVectorByI(self, index, new_vector) :
        """
        Updates the vector at the given index with the new vector.
        Input: index, new_vector
        """
        self.__data[index] = new_vector

    def updateVectorByNI(self, name_id, new_vector) :
        """
        Updates the vector with the given name_id with the new vector.
        Input: name_id, new_vector
        """
        for i, element in enumerate(self.__data) :
            if element.get_name_id() == name_id :
                self.__data[i] = new_vector

    def deleteVectorByI(self, index) :
        """
        Deletes the vector at the given index.
        Input: index
        """
        del self.__data[index]

    def deleteVectorByNI(self, name_id) :
        """
        Deletes the vector with the given name_id.
        Input: name_id
        """
        for i, element in enumerate(self.__data) :
            if element.get_name_id() == name_id :
                del self.__data[i]

    def plotVector(self, index) :
        """
        Returns the values of the vector at the given index in order to plot it.
        Input: index
        """
        x = []
        y = []
        c = []
        for i in range(len(self.__data[index].get_values())) :
            x.append(i)
            c.append(self.__data[index].get_color())
        for element in self.__data[index].get_values() :
            y.append(element)
        if self.__data[index].get_type() == 1 :
            t = "o"
        elif self.__data[index].get_type() == 2 :
            t = "s"
        elif self.__data[index].get_type() == 3 :
            t = "^"
        else :
            t = "D"
        return x, y, c, t

    def uniqueId(self, nr_id) :
        """
        Checks if the given id is unique.
        Input: nr_id
        """
        for i in range(len(self.__data)) :
            if self.__data[i].get_name_id() == nr_id :
                return False
        return True

    def __len__(self) :
        """
        Returns the length of the repository.
        """
        return len(self.__data)

class Controller:
    """
    Class that represents a controller.
    Attributes: repo
    """
    def __init__(self, repo) :
        self.__repo = repo
        s1 = (1, "yellow", 1, [1, 4, 9, 16, 25])
        s2 = (2, "green", 2, [1, 2.5, 4, 5.5])
        s3 = (3, "red", 5, [1, 2, 3])

        self.add(s1[0], s1[1], s1[2], s1[3])
        self.add(s2[0], s2[1], s2[2], s2[3])
        self.add(s3[0], s3[1], s3[2], s3[3])

    def add(self, name_id, color, type, values) :
        """
        Adds a new vector to the repository.
        Input: name_id, color, type, values
        """
        s = MyVector(name_id, color, type, values)
        self.__repo.addNew(s)

    def getUniqueId(self, nr_id) :
        """
        Checks if the given id is unique.
        Input: nr_id
        """
        return self.__repo.uniqueId(nr_id)

    def printRepo(self) :
        """
        Returns a string representation of the repository.
        """
        return str(self.__repo)

    def printVectorByIndex(self, index) :
        """
        Returns a string representation of the vector at the given index.
        Input: index
        """
        return self.__repo.getVector(index)

    def updateVectorByIndex(self, index, new_vector) :
        """
        Updates the vector at the given index with the new vector.
        Input: index, new_vector
        """
        self.__repo.updateVectorByI(index, new_vector)

    def updateVectorByNameId(self, name_id, new_vector) :
        """
        Updates the vector with the given name_id with the new vector.
        Input: name_id, new_vector
        """
        self.__repo.updateVectorByNI(name_id, new_vector)

    def deleteVectorByIndex(self, index) :
        """
        Deletes the vector at the given index.
        Input: index
        """
        self.__repo.deleteVectorByI(index)

    def deleteVectorByNameId(self, name_id) :
        """
        Deletes the vector with the given name_id.
        Input: name_id
        """
        self.__repo.deleteVectorByNI(name_id)

    def plotV(self, index) :
        """
        Returns the values of the vector at the given index in order to plot it.
        Input: index
        """
        return self.__repo.plotVector(index)

    def length(self) :
        """
        Returns the length of the repository.
        """
        return len(self.__repo)

class UI:
    """
    Class that represents a user interface.
    Attributes: ctrl"""
    def __init__(self, ctrl) :
        self.__ctrl = ctrl

    @staticmethod
    def readInput() :
        """
        Reads the input from the user.
        """
        try:
            option = int(input())
            return option
        except Exception:
            UI.readInput()

    def printResult(s) :
        """
        Prints the result of the operation.
        Input: s
        """
        for element in s :
            print(str(element))

    def readVector(self):
        """
        Reads a vector from the user.
        """
        print("Give name id:")
        name_id = UI.readInput()
        if self.getUniqueId(name_id) == False :
            raise ValueError("Name id must be unique! \n")
        color = input("Give color: \n")
        if UI.getSpecificColor(color) == False :
            raise ValueError("Color must be red, green, blue, yellow or magenta! \n")
        print("Give type:")
        type = UI.readInput()
        print("Give values:")
        new_values = []
        x = UI.readInput()
        while x != 0 :
            new_values.append(x)
            x = UI.readInput()
        return MyVector(name_id, color, type, new_values)

    def getSpecificColor(color) :
        """
        Checks if the given color is valid.
        Input: color
        """
        if color == "red" or color == "green" or color == "blue" or color == "yellow" or color == "magenta":
            return True
        return False

    @staticmethod
    def printMenu() :
        """
        Prints the menu.
        """
        menu = "Commands: \n"
        menu += "\t************\n"
        menu += "\t1: Add new vector \n"
        menu += "\t2: Print all vectors \n"
        menu += "\t3: Get a vector at a given index \n"
        menu += "\t4: Update a vector at a given index \n"
        menu += "\t5: Update a vector identified by a given name id \n"
        menu += "\t6: Delete a vector at a given index \n"
        menu += "\t7: Delete a vector identified by a given name id \n"
        menu += "\t8: Plot all vectors \n"
        menu += "\t************\n"
        menu += "\t0: Exit \n"
        print(menu)

    def run(self) :
        """
        Runs the user interface.
        """
        while True :
            UI.printMenu()
            try :
                print("Give option: ")
                opt = UI.readInput()

                if opt == 0 :
                    print("Closing program...")
                    exit()

                elif opt == 1 :
                    new_vector = UI.readVector(self.__ctrl)
                    self.__ctrl.add(new_vector.get_name_id(), new_vector.get_color(), new_vector.get_type(), new_vector.get_values())

                elif opt == 2 :
                    print("Vectors are: \n", self.__ctrl.printRepo())

                elif opt == 3 :
                    index = int(input("Give index: \n"))
                    print(self.__ctrl.printVectorByIndex(index))

                elif opt == 4 :
                    index = int(input("Give index: \n"))
                    new_vector = UI.readVector(self.__ctrl)
                    self.__ctrl.updateVectorByIndex(index, new_vector)

                elif opt == 5 :
                    name_id = int(input("Give name id: \n"))
                    new_vector = UI.readVector(self.__ctrl)
                    self.__ctrl.updateVectorByNameId(name_id, new_vector)

                elif opt == 6 :
                    index = int(input("Give index: \n"))
                    self.__ctrl.deleteVectorByIndex(index)

                elif opt == 7 :
                    name_id = int(input("Give name id: \n"))
                    self.__ctrl.deleteVectorByNameId(name_id)

                elif opt == 8 :
                    print("Plotting...")
                    for i in range(self.__ctrl.length() -1, -1, -1) :
                        x, y, c, t = self.__ctrl.plotV(i)
                        plt.scatter(x, y, c = c, marker = t)
                    plt.show()

            except Exception as e:
                print("\nError! \n", e)

def start() :
    """
    Starts the program.
    """
    repo = Repository()
    ctrl = Controller(repo)
    ui = UI(ctrl)
    ui.run()

if __name__ == "__main__" :
    start()