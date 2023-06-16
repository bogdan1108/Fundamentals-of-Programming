import matplotlib.pyplot as plt
import math

# the class that creates the objects
class MyPoint:
    def __init__(self, coordonate_x, coordonate_y, color) :
        '''
        function that initiates the coordinates and color of points
        '''
        self.coordonate_x = coordonate_x
        self.coordonate_y = coordonate_y
        self.color = color

    def __str__(self) :
        '''
        function that returns how the points should be printed
        '''
        return f"Point ({self.coordonate_x}, {self.coordonate_y}) of color {self.color}."

    def get_coordonate_x(self) :
        '''
        function to get x coordinate
        '''
        return self.coordonate_x

    def set_coordonate_x(self, new_value) :
        '''
        function to set x coordinate
        '''
        self.coordonate_x = new_value

    def get_coordonate_y(self) :
        '''
        function to get y coordinate
        '''
        return self.coordonate_y

    def set_coordonate_y(self, new_value) :
        '''
        function to set y coordinate
        '''
        self.coordonate_y = new_value

    def get_color(self) :
        '''
        function to get color
        '''
        return self.color

    def set_color(self, new_value) :
        '''
        function to set color
        '''
        self.color = new_value

class Repository:
    def __init__(self) :
        '''
        initiates the list
        '''
        self.__data = []

    def addNew(self, s) :
        '''
        adds point to the list
        '''
        self.__data.append(s)

    def getColors(self, givenColor) :
        '''
        get the number of points of a specific color
        '''
        k = 0
        for element in self.__data :
            if element.get_color() == givenColor :
                k += 1
        return k

    def updateIndex(self, index, x, y, color) :
        '''
        updates the point at a specific index
        '''
        self.__data[index].set_coordonate_x(x)
        self.__data[index].set_coordonate_y(y)
        self.__data[index].set_color(color)

    def deleteIndex(self, index) :
        '''
        delete the point at a specific index
        '''
        self.__data.pop(index)

    def getAllColors(self, givenColor) :
        '''
        gets all the point of a speicifc color
        '''
        res = " "
        for element in self.__data :
            if element.get_color() == givenColor :
                res += str(element)
                res += "\n"
                res += " "
        return res

    def getPoint(self, index) :
        '''
        get a point at a specific index
        '''
        return str(self.__data[index])

    def getPointsSquare(self, length, x_corner, y_corner) :
        '''
        get all the points inside a given square
        '''
        res = " "
        for element in self.__data :
            if int(element.get_coordonate_x()) > x_corner and int(element.get_coordonate_x()) < (x_corner + length) :
                if int(element.get_coordonate_y()) < y_corner and int(element.get_coordonate_y()) > (y_corner - length) :
                    res += str(element)
                    res += "\n"
                    res += " "
        return res

    def deletePointsSquare(self, length, x_corner, y_corner) :
        '''
        deletes all the points in a specific square
        '''
        for i in range(len(self.__data)-1, -1, -1) :
            if int(self.__data[i].get_coordonate_x()) > x_corner and int(self.__data[i].get_coordonate_x()) < (x_corner + length) :
                if int(self.__data[i].get_coordonate_y()) < y_corner and int(self.__data[i].get_coordonate_y()) > (y_corner - length) :
                    self.__data.pop(i)

    def goInX(self) :
        '''
        gets all the x coordinates of all the points into a list
        '''
        x = []
        for i in range(len(self.__data)) :
            x.append(int(self.__data[i].get_coordonate_x()))
        return x

    def goInY(self) :
        '''
        gets all the y coordinates of all the points into a list
        '''
        y = []
        for i in range(len(self.__data)) :
            y.append(int(self.__data[i].get_coordonate_y()))
        return y

    def goInC(self) :
        '''
        gets all the y coordinates of all the points into a list
        '''
        col = []
        for i in range(len(self.__data)) :
            col.append(self.__data[i].get_color())
        return col

    def pointsInCircle(self, radius, x_coord, y_coord) :
        '''
        gets all the points inside a given circle
        '''
        sol = " "
        for element in self.__data :
            x1 = element.get_coordonate_x()
            y1 = element.get_coordonate_y()
            if math.sqrt((x_coord-x1)**2 + (y_coord-y1)**2) < radius :
                sol += str(element)
                sol += "\n"
                sol += " "
        return sol

    def shiftOnY(self, number) :
        '''
        shifts all the points by the y axis
        '''
        for element in self.__data :
            element.set_coordonate_y(element.get_coordonate_y() + number)

    def minimumDist(self) :
        minn = 9999999999
        for element1 in self.__data:
            for element2 in self.__data:
                x1 = element1.get_coordonate_x()
                y1 = element1.get_coordonate_y()
                x2 = element2.get_coordonate_x()
                y2 = element2.get_coordonate_y()
                dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                if dist < minn and dist != 0:
                    minn = dist
        return minn
        


    def __str__(self):
        '''
        functions that determines the way the list is written
        '''
        res = " "
        for element in self.__data :
            res += str(element)
            res += '\n'
            res += " "
        return res

    def __len__(self):
        '''
        length of list
        '''
        return len(self.__data)

class Controller:
    def __init__(self, repo) :
        self.__repo = repo
        s1 = (1, 1, "red")
        s2 = (5, 1, "red")
        s3 = (7, 4, "yellow")
        s4 = (2, 5, "blue")
        s5 = (4, 4, "blue")
        s6 = (4, 9, "red")
        s7 = (2, 6, "magenta")
        s8 = (-1, -7, "green")
        s9 = (-2, 4, "green")
        s10 = (4, -5, "red")

        self.add(s1[0], s1[1], s1[2])
        self.add(s2[0], s2[1], s2[2])
        self.add(s3[0], s3[1], s3[2])
        self.add(s4[0], s4[1], s4[2])
        self.add(s5[0], s5[1], s5[2])
        self.add(s6[0], s6[1], s6[2])
        self.add(s7[0], s7[1], s7[2])
        self.add(s8[0], s8[1], s8[2])
        self.add(s9[0], s9[1], s9[2])
        self.add(s10[0], s10[1], s10[2])


    def circle(self, radius, x_coord, y_coord) :
        return self.__repo.pointsInCircle(radius, x_coord, y_coord)

    def add(self, x_coord, y_coord, color) :
        s = self.createPoint(x_coord, y_coord, color)
        self.__repo.addNew(s)

    def createPoint(self, x_coord, y_coord, color) :
        s = MyPoint(x_coord, y_coord, color)
        return s

    def printAllColors(self, color) :
        return str(self.__repo.getAllColors(color))

    def printPointsSquare(self, length, x_corner, y_corner) :
        return str(self.__repo.getPointsSquare(length, x_corner, y_corner))

    def printRepoIndex(self, index) :
        return str(self.__repo.getPoint(index))

    def printDist(self) :
        return self.__repo.minimumDist()

    def upIndex(self, index, x, y, color) :
        self.__repo.updateIndex(index, x, y, color)

    def delIndex(self, index) :
        self.__repo.deleteIndex(index)

    def delPointsSquare(self, length, x_corner, y_corner) :
        self.__repo.deletePointsSquare(length, x_corner, y_corner)

    def getInX(self) :
        return self.__repo.goInX()

    def getInY(self) :
        return self.__repo.goInY()

    def getInCol(self) :
        return self.__repo.goInC()

    def printColors(self, color) :
        return self.__repo.getColors(color)

    def shiftY(self, number) :
        self.__repo.shiftOnY(number)

    def printRepo(self) :
        return str(self.__repo)

class UI:
    def __init__(self, ctrl) :
        self.__ctrl = ctrl
    
    def readPoint():
        '''
        function that reads a point
        '''
        print("Give x coordinate: ")
        x_coord = UI.readInput()
        print("Give y coordinate: ")
        y_coord = UI.readInput()
        color = input("Give color: \n")
        if UI.getSpecificColor(color) == False :
            print("Invalid Color!")
            return None, None, None
        return x_coord, y_coord, color

    def readInput():
        '''
        function to real input
        '''
        try:
            option = int(input())
            return option
        except Exception:
            UI.readInput()
    
    def printResult(s) :
        '''
        function to print results
        '''
        for element in s :
            print(str(element))

    def getSpecificColor(color):
        '''
        function to verify if the inputed color is correct
        '''
        if color != "red" and color != "blue" and color != "green" and color != "magenta" and color != "yellow" :
            return False
        return True

    def printMenu():
        '''
        function to print the menu
        '''
        menu = "1: Add point to the repository \n"
        menu += "2: Get all points \n"
        menu += "3: Get a point at given index \n"
        menu += "4: Get all points of a given color \n"
        menu += "5: Get all points that are inside a given square \n"
        menu += "6: Get the minimum distance between 2 points \n"
        menu += "7: Update a point at a given index \n"
        menu += "8: Delete a point by index \n"
        menu += "9: Delete all points that are inside a given square \n"
        menu += "10: Plot all points in a chart \n"
        menu += "11: Get the number of points of a given color \n"
        menu += "12: Get all points inside a given circle \n"
        menu += "13: Shift all points on the y axis \n"
        menu += "0: Exit \n"
        print(menu) 

    def run(self) :
        '''
        function to run the program
        '''
        UI.printMenu()
        while True:
            try:
                print("Give option: ")
                opt = UI.readInput()
                if opt == 0:
                    print("Closing the program...")
                    exit()

                elif opt == 1:
                    x_coord, y_coord, color = UI.readPoint()
                    if x_coord != None and y_coord != None and color != None:
                        self.__ctrl.add(x_coord, y_coord, color)

                elif opt == 2:
                    print("POINTS ARE: \n", self.__ctrl.printRepo())

                elif opt == 3:
                    index = int(input("Give index: "))
                    print(self.__ctrl.printRepoIndex(index))

                elif opt == 4:
                    color = input("Give a color: ")
                    if UI.getSpecificColor(color) == True :
                        result = self.__ctrl.printAllColors(color)
                        print(result)
                    else :
                        print("Invalid color! \n")

                elif opt == 5 :
                    length = int(input("Length: "))
                    x_corner = int(input("X coordinate corner: "))
                    y_corner = int(input("Y coordinate corner: "))
                    print(self.__ctrl.printPointsSquare(length, x_corner, y_corner))

                elif opt == 6 :
                    print(self.__ctrl.printDist())

                elif opt == 7 :
                    index = int(input("Give index: "))
                    x = int(input("New x: "))
                    y = int(input("New y: "))
                    color = input("New Color: ")
                    if UI.getSpecificColor(color) == True :
                        self.__ctrl.upIndex(index, x, y, color)
                    else :
                        print("Invalid Color! \n")


                elif opt == 8 :
                    index = int(input("Give index: "))
                    self.__ctrl.delIndex(index)

                elif opt == 9 :
                    length = int(input("Length: "))
                    x_corner = int(input("X coordinate corner: "))
                    y_corner = int(input("Y coordinate corner: "))
                    self.__ctrl.delPointsSquare(length, x_corner, y_corner)
                
                elif opt == 10 :
                    x = self.__ctrl.getInX()
                    y = self.__ctrl.getInY()
                    col = self.__ctrl.getInCol()
                    plt.scatter(x, y, c = col)
                    plt.show()

                elif opt == 11:
                    color1 = input("Give a color: ")
                    if UI.getSpecificColor(color1) == True :
                        result = self.__ctrl.printColors(color1)
                        print(result)
                    else :
                        print("Invalid color! \n")

                elif opt == 12:
                    center_x = int(input("Give x coordinate of the center of the circle: "))
                    center_y = int(input("Give y coordinate of the center of the circle: "))
                    radius = int(input("Give the radius of the circle: "))
                    print(self.__ctrl.circle(radius, center_x, center_y))

                elif opt == 13:
                    number = int(input("Number to be shifted: "))
                    self.__ctrl.shiftY(number)

                else :
                    print("Option is invalid! \n")
                UI.printMenu()
            except Exception as e:
                print("\nError! \n", e)

def testPoints() :
    '''
    test function for all the functions in the object creation class
    '''
    s = MyPoint(1, 1, "red")
    assert MyPoint.get_color(s) == "red"
    assert MyPoint.get_coordonate_x(s) == 1
    assert MyPoint.get_coordonate_y(s) == 1
    MyPoint.set_color(s, "green")
    MyPoint.set_coordonate_x(s, 2)
    MyPoint.set_coordonate_y(s, 2)
    assert MyPoint.get_color(s) == "green"
    assert MyPoint.get_coordonate_x(s) == 2
    assert MyPoint.get_coordonate_y(s) == 2
    s1 = MyPoint(5, 4, "blue")
    
    assert MyPoint.get_color(s1) == "blue"
    assert MyPoint.get_coordonate_x(s1) == 5
    assert MyPoint.get_coordonate_y(s1) == 4
    MyPoint.set_color(s1, "magenta")
    MyPoint.set_coordonate_x(s1, 3)
    MyPoint.set_coordonate_y(s1, 1)
    assert MyPoint.get_color(s1) == "magenta"
    assert MyPoint.get_coordonate_x(s1) == 3
    assert MyPoint.get_coordonate_y(s1) == 1

class TestRepo(Repository) :
    def testFunctions(self) :
        '''
        test function for all the functions in the repository
        '''
        s = MyPoint(1, 1, "red")
        repo = Repository()
        repo.addNew(s)
        assert len(repo) == 1
        assert repo.getColors("red") == 1
        repo.updateIndex(0, 2, 2, "blue")
        assert s.get_coordonate_x() == 2
        assert s.get_coordonate_y() == 2
        assert s.get_color() == "blue"
        repo.deleteIndex(0)
        assert len(repo) == 0
        repo.addNew(s)
        repo.deletePointsSquare(10, 0, 10)
        assert len(repo) == 0
        repo.addNew(s)
        repo.shiftOnY(-1)
        assert s.get_coordonate_y() == 1
        assert repo.getPointsSquare(10, 0, 10) == " " + str(s) + "\n" + " "
        assert repo.getPoint(0) == str(s)
        assert repo.getAllColors("blue") == " " + str(s) + "\n" + " "
        assert repo.goInX() == [2]
        assert repo.goInY() == [1]
        assert repo.goInC() == ["blue"]
        assert repo.pointsInCircle(100, 0, 0) == " " + str(s) + "\n" + " "
        assert str(repo) == " " + str(s) + "\n" + " "
        s1 = MyPoint(1, 4, "red")
        s2 = MyPoint(7, 3, "blue")
        s3 = MyPoint(1, 5, "green")
        repo = Repository()
        repo.addNew(s1)
        repo.addNew(s2)
        repo.addNew(s3)
        assert len(repo) == 3
        assert repo.getColors("blue") == 1
        repo.updateIndex(0, 2, 2, "blue")
        assert s1.get_coordonate_x() == 2
        assert s1.get_coordonate_y() == 2
        assert s1.get_color() == "blue"
        repo.deleteIndex(0)
        assert len(repo) == 2
        repo.addNew(s)
        repo.deletePointsSquare(10, 0, 10)
        assert len(repo) == 0
        repo.addNew(MyPoint(2, 2, "blue"))
        repo.shiftOnY(-1)
        assert s.get_coordonate_y() == 1
        assert repo.getPointsSquare(10, 0, 10) == " " + str(s) + "\n" + " "
        assert repo.getPoint(0) == str(s)
        assert repo.getAllColors("blue") == " " + str(s) + "\n" + " "
        assert repo.goInX() == [2]
        assert repo.goInY() == [1]
        assert repo.goInC() == ["blue"]
        assert repo.pointsInCircle(100, 0, 0) == " " + str(s) + "\n" + " "
        assert str(repo) == " " + str(s) + "\n" + " "

def start():
    '''
    function that starts the program
    '''
    tests = TestRepo()
    tests.testFunctions()
    testPoints()
    repo = Repository()
    controller = Controller(repo)
    ui = UI(controller)
    ui.run()

start()






