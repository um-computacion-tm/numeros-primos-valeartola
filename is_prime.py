import unittest

def is_prime(value):
    for n in range(2, value):
        if value % n == 0:
            return False
    return True
    
    

class Testisprime(unittest.TestCase):
    def test_with_1(self):
        result = is_prime(1)
        self.assertTrue(result) #self.assertEqual(result, True)

    def test_with_2(self):
        result = is_prime(2)
        self.assertTrue(result)

    def test_with_3(self):
        result = is_prime(3)
        self.assertTrue(result)

    def test_with_4(self):
        result = is_prime(4)
        self.assertFalse(result)

    def test_with_5(self):
        result = is_prime(5)
        self.assertTrue(result)

    def test_with_6(self):
        result = is_prime(6)
        self.assertFalse(result)


    def test_with_8(self):
        result = is_prime(8)
        self.assertFalse(result)

    def test_with_11(self):
        result = is_prime(11)
        self.assertTrue(result)

    def test_with_21(self):
        result = is_prime(21)
        self.assertFalse(result)






unittest.main()
