import super_modul
import unittest

# print(super_modul.dividiere(6,2))

class TestDividiere(unittest.TestCase):
    # Assert 1: Normalfall (Positive Zahlen)
    def test_normal(self):
        self.assertEqual(super_modul.dividiere(10,5),2,msg="A1 Failed")

    # Assert 2: Negative Zahlen
    def test_negativ(self):
        self.assertEqual(super_modul.dividiere(6, -2), -3, msg="A2 Failed")

    # Assert 3: Null Werte -> Ergebnis
    def test_durch_null(self):
        self.assertEqual(super_modul.dividiere(10,0), "Error", msg="A3 Failed")

unittest.main()


