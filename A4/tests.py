import unittest
from A4 import Repository
from A4 import MyVector

class TestMyVector(unittest.TestCase):
    """
    Test class for MyVector
    """
    def test_get(self) :
        """
        Test get methods
        """
        v1 = MyVector(1, "yellow", 1, [1, 4, 9, 16, 25])
        self.assertEqual(v1.get_name_id(), 1)
        self.assertEqual(v1.get_color(), "yellow")
        self.assertEqual(v1.get_type(), 1)
        self.assertEqual(v1.get_values(), [1, 4, 9, 16, 25])

        v2 = MyVector(2, "green", 2, [1, 2.5, 4, 5.5])
        self.assertEqual(v2.get_name_id(), 2)
        self.assertEqual(v2.get_color(), "green")
        self.assertEqual(v2.get_type(), 2)
        self.assertEqual(v2.get_values(), [1, 2.5, 4, 5.5])

        v3 = MyVector(3, "red", 5, [1, 2, 3])
        self.assertEqual(v3.get_name_id(), 3)
        self.assertEqual(v3.get_color(), "red")
        self.assertEqual(v3.get_type(), 5)
        self.assertEqual(v3.get_values(), [1, 2, 3])

    def test_set(self) :
        """
        Test set methods
        """
        v1 = MyVector(1, "yellow", 1, [1, 4, 9, 16, 25])
        v1.set_name_id(4)
        v1.set_color("blue")
        v1.set_type(3)
        v1.set_values([1, 2, 3, 4])
        self.assertEqual(v1.get_name_id(), 4)
        self.assertEqual(v1.get_color(), "blue")
        self.assertEqual(v1.get_type(), 3)
        self.assertEqual(v1.get_values(), [1, 2, 3, 4])

        v2 = MyVector(2, "green", 2, [1, 2.5, 4, 5.5])
        v2.set_name_id(5)
        v2.set_color("red")
        v2.set_type(4)
        v2.set_values([1, 2, 3, 4, 5])
        self.assertEqual(v2.get_name_id(), 5)
        self.assertEqual(v2.get_color(), "red")
        self.assertEqual(v2.get_type(), 4)
        self.assertEqual(v2.get_values(), [1, 2, 3, 4, 5])

        v3 = MyVector(3, "red", 5, [1, 2, 3])
        v3.set_name_id(6)
        v3.set_color("yellow")
        v3.set_type(1)
        v3.set_values([1, 2, 3, 4, 5, 6])
        self.assertEqual(v3.get_name_id(), 6)
        self.assertEqual(v3.get_color(), "yellow")
        self.assertEqual(v3.get_type(), 1)
        self.assertEqual(v3.get_values(), [1, 2, 3, 4, 5, 6])

    def test_add_scalar(self) :
        """
        Test add_scalar method
        """
        v1 = MyVector(1, "yellow", 1, [1, 4, 9, 16, 25])
        v1.add_scalar(2)
        self.assertEqual(v1.get_values(), [3, 6, 11, 18, 27])

        v2 = MyVector(2, "green", 2, [1, 2.5, 4, 5.5])
        v2.add_scalar(3)
        self.assertEqual(v2.get_values(), [4, 5.5, 7, 8.5])

        v3 = MyVector(3, "red", 5, [1, 2, 3])
        v3.add_scalar(4)
        self.assertEqual(v3.get_values(), [5, 6, 7])

    def test_add_vector(self) :
        """
        Test add_vector method
        """
        v1 = MyVector(1, "yellow", 1, [1, 4, 9, 16])
        v2 = MyVector(2, "green", 2, [1, 2.5, 4, 5.5])
        v1.add_vector(v2)
        self.assertEqual(v1.get_values(), [2, 6.5, 13, 21.5])

        v3 = MyVector(3, "red", 5, [1, 2, 3])
        v4 = MyVector(4, "blue", 3, [2, 3, 4])
        v3.add_vector(v4)
        self.assertEqual(v3.get_values(), [3, 5, 7])

        v5 = MyVector(5, "magenta", 4, [1, 2, 3, 4, 5])
        v6 = MyVector(6, "red", 1, [3123, 645, 234, 856, 6325])
        v5.add_vector(v6)
        self.assertEqual(v5.get_values(), [3124, 647, 237, 860, 6330])

    def test_sub_vector(self) :
        """
        Test sub_vector method
        """
        v1 = MyVector(1, "yellow", 1, [1, 4, 9, 16])
        v2 = MyVector(2, "green", 2, [1, 2.5, 4, 5.5])
        v1.sub_vector(v2)
        self.assertEqual(v1.get_values(), [0, 1.5, 5, 10.5])

        v3 = MyVector(3, "red", 5, [1, 2, 3])
        v4 = MyVector(4, "blue", 3, [2, 3, 4])
        v3.sub_vector(v4)
        self.assertEqual(v3.get_values(), [-1, -1, -1])

        v5 = MyVector(5, "magenta", 4, [1, 2, 3, 4, 5])
        v6 = MyVector(6, "red", 1, [3123, 645, 234, 856, 6325])
        v5.sub_vector(v6)
        self.assertEqual(v5.get_values(), [-3122, -643, -231, -852, -6320])

    def test_mul_vector(self) :
        """
        Test mul_vector method
        """
        v1 = MyVector(1, "yellow", 1, [1, 4, 9, 16])
        v2 = MyVector(2, "green", 2, [1, 2.5, 4, 5.5])
        self.assertEqual(v1.mul_vector(v2) , 1*1 + 4*2.5 + 9*4 + 16*5.5)

        v3 = MyVector(3, "red", 5, [1, 2, 3])
        v4 = MyVector(4, "blue", 3, [2, 3, 4])
        self.assertEqual(v3.mul_vector(v4) , 1*2 + 2*3 + 3*4)

        v5 = MyVector(5, "magenta", 4, [1, 2, 3, 4, 5])
        v6 = MyVector(6, "red", 1, [3123, 645, 234, 856, 6325])
        self.assertEqual(v5.mul_vector(v6) , 1*3123 + 2*645 + 3*234 + 4*856 + 5*6325)

    def test_sum_of_elements(self) :
        """
        Test sum_of_elements method
        """
        v1 = MyVector(1, "yellow", 1, [1, 4, 9, 16])
        self.assertEqual(v1.sum_of_elements() , 1 + 4 + 9 + 16)

        v2 = MyVector(2, "green", 2, [1, 2.5, 4, 5.5])
        self.assertEqual(v2.sum_of_elements() , 1 + 2.5 + 4 + 5.5)

        v3 = MyVector(3, "red", 5, [1, 2, 3])
        self.assertEqual(v3.sum_of_elements() , 1 + 2 + 3)

    def test_product_of_elements(self) :
        """
        Test product_of_elements method
        """
        v1 = MyVector(1, "yellow", 1, [1, 4, 9, 16])
        self.assertEqual(v1.product_of_elements() , 1 * 4 * 9 * 16)

        v2 = MyVector(2, "green", 2, [1, 2.5, 4, 5.5])
        self.assertEqual(v2.product_of_elements() , 1 * 2.5 * 4 * 5.5)

        v3 = MyVector(3, "red", 5, [1, 2, 3])
        self.assertEqual(v3.product_of_elements() , 1 * 2 * 3)

    def test_avarage_of_elements(self) :
        """
        Test avarage_of_elements method
        """
        v1 = MyVector(1, "yellow", 1, [1, 4, 9, 16])
        self.assertEqual(v1.avarage_of_elements() , (1 + 4 + 9 + 16) / 4)

        v2 = MyVector(2, "green", 2, [1, 2.5, 4, 5.5])
        self.assertEqual(v2.avarage_of_elements() , (1 + 2.5 + 4 + 5.5) / 4)

        v3 = MyVector(3, "red", 5, [1, 2, 3])
        self.assertEqual(v3.avarage_of_elements() , (1 + 2 + 3) / 3)

    def test_minimum_of_elements(self) :
        """
        Test minimum_of_elements method
        """
        v1 = MyVector(1, "yellow", 1, [1, 4, 9, 16])
        self.assertEqual(v1.minimum_of_elements() , 1)

        v2 = MyVector(2, "green", 2, [1, 2.5, 4, 5.5])
        self.assertEqual(v2.minimum_of_elements() , 1)

        v3 = MyVector(3, "red", 5, [1, 2, 3])
        self.assertEqual(v3.minimum_of_elements() , 1)

    def test_maximum_of_elements(self) :
        """
        Test maximum_of_elements method
        """
        v1 = MyVector(1, "yellow", 1, [1, 4, 9, 16])
        self.assertEqual(v1.maximum_of_elements() , 16)

        v2 = MyVector(2, "green", 2, [1, 2.5, 4, 5.5])
        self.assertEqual(v2.maximum_of_elements() , 5.5)

        v3 = MyVector(3, "red", 5, [1, 2, 3])
        self.assertEqual(v3.maximum_of_elements() , 3)


class TestA4(unittest.TestCase):
    """
    Test class for A4
    """
    def test_create(self) :
        """
        Test create method
        """
        s1 = (1, "yellow", 1, [1, 4, 9, 16, 25])
        s2 = (2, "green", 2, [1, 2.5, 4, 5.5])
        s3 = (3, "red", 5, [1, 2, 3])

        repo = Repository()

        repo.addNew(s1)
        repo.addNew(s2)
        repo.addNew(s3)

        self.assertEqual(len(repo),  3)
        s4 = (4, "blue", 3, [1, 2, 3, 4])
        repo.addNew(s4)
        self.assertEqual(len(repo),  4)

    def test_getVector(self) :
        """
        Test getVector method
        """
        s1 = (1, "yellow", 1, [1, 4, 9, 16, 25])
        s2 = (2, "green", 2, [1, 2.5, 4, 5.5])
        s3 = (3, "red", 5, [1, 2, 3])

        repo = Repository()

        repo.addNew(s1)
        repo.addNew(s2)
        repo.addNew(s3)
        
        self.assertEqual(repo.getVector(0), "(1, 'yellow', 1, [1, 4, 9, 16, 25])")
        self.assertEqual(repo.getVector(1), "(2, 'green', 2, [1, 2.5, 4, 5.5])")
        self.assertEqual(repo.getVector(2), "(3, 'red', 5, [1, 2, 3])")

    def test_UpdateVectorByI(self) :
        """
        Test updateVectorByI method
        """
        s1 = (1, "yellow", 1, [1, 4, 9, 16, 25])
        s2 = (2, "green", 2, [1, 2.5, 4, 5.5])
        s3 = (3, "red", 5, [1, 2, 3])

        repo = Repository()

        repo.addNew(s1)
        repo.addNew(s2)
        repo.addNew(s3)
        repo.updateVectorByI(0, (4, "blue", 3, [1, 2, 3, 4]))
        self.assertEqual(repo.getVector(0), "(4, 'blue', 3, [1, 2, 3, 4])")
        self.assertEqual(repo.getVector(1), "(2, 'green', 2, [1, 2.5, 4, 5.5])")
        self.assertEqual(repo.getVector(2), "(3, 'red', 5, [1, 2, 3])")

        repo.updateVectorByI(1, (5, "black", 4, [1, 2, 3, 4, 5]))
        self.assertEqual(repo.getVector(0), "(4, 'blue', 3, [1, 2, 3, 4])")
        self.assertEqual(repo.getVector(1), "(5, 'black', 4, [1, 2, 3, 4, 5])")
        self.assertEqual(repo.getVector(2), "(3, 'red', 5, [1, 2, 3])")

        repo.updateVectorByI(2, (6, "white", 6, [1, 2, 3, 4, 5, 6]))
        self.assertEqual(repo.getVector(0), "(4, 'blue', 3, [1, 2, 3, 4])")
        self.assertEqual(repo.getVector(1), "(5, 'black', 4, [1, 2, 3, 4, 5])")
        self.assertEqual(repo.getVector(2), "(6, 'white', 6, [1, 2, 3, 4, 5, 6])")

    def test_deleteVectorByI(self) :
        """
        Test deleteVectorByI method
        """
        s1 = (1, "yellow", 1, [1, 4, 9, 16, 25])
        s2 = (2, "green", 2, [1, 2.5, 4, 5.5])
        s3 = (3, "red", 5, [1, 2, 3])

        repo = Repository()

        repo.addNew(s1)
        repo.addNew(s2)
        repo.addNew(s3)
        repo.deleteVectorByI(0)
        self.assertEqual(repo.getVector(0), "(2, 'green', 2, [1, 2.5, 4, 5.5])")
        self.assertEqual(repo.getVector(1), "(3, 'red', 5, [1, 2, 3])")
        repo.deleteVectorByI(1)
        self.assertEqual(repo.getVector(0), "(2, 'green', 2, [1, 2.5, 4, 5.5])")

    def test_deleteVectorByNI(self) :
        """
        Test deleteVectorByNI method
        """
        s1 = MyVector(1, "yellow", 1, [1, 4, 9, 16, 25])
        s2 = MyVector(2, "green", 2, [1, 2.5, 4, 5.5])
        s3 = MyVector(3, "red", 5, [1, 2, 3])

        repo = Repository()

        repo.addNew(s1)
        repo.addNew(s2)
        repo.addNew(s3)
        repo.deleteVectorByNI(1)
        self.assertEqual(repo.getVector(0), "Vector [2] of color green and type 2 with values [1, 2.5, 4, 5.5].")
        self.assertEqual(repo.getVector(1), "Vector [3] of color red and type 5 with values [1, 2, 3].")
        
        s4 = MyVector(4, "blue", 3, [1, 2, 3, 4])
        s5 = MyVector(5, "magenta", 4, [1, 2, 3, 4, 5])
        s6 = MyVector(6, "red", 6, [1, 2, 3, 4, 5, 6])

        repo.addNew(s4)
        repo.addNew(s5)
        repo.addNew(s6)
        repo.deleteVectorByNI(4)
        self.assertEqual(repo.getVector(0), "Vector [2] of color green and type 2 with values [1, 2.5, 4, 5.5].")
        self.assertEqual(repo.getVector(1), "Vector [3] of color red and type 5 with values [1, 2, 3].")
        self.assertEqual(repo.getVector(2), "Vector [5] of color magenta and type 4 with values [1, 2, 3, 4, 5].")
        self.assertEqual(repo.getVector(3), "Vector [6] of color red and type 6 with values [1, 2, 3, 4, 5, 6].")

        repo.deleteVectorByNI(6)
        self.assertEqual(repo.getVector(0), "Vector [2] of color green and type 2 with values [1, 2.5, 4, 5.5].")
        self.assertEqual(repo.getVector(1), "Vector [3] of color red and type 5 with values [1, 2, 3].")
        self.assertEqual(repo.getVector(2), "Vector [5] of color magenta and type 4 with values [1, 2, 3, 4, 5].")

if __name__ == '__main__':
    unittest.main()