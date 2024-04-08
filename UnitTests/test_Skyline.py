import sys
import unittest
sys.path.append("C:\\Users\\mhaye\\code\\School\\6045 Algorithms\\SkylineProblem\\AA-Assignment-2")
from Skyline import Building, Skyline

class TestSkyline(unittest.TestCase):
    """
             _________
            |    _____|________
            |   |     |        |
            |   |     |        |
    """
    def test_scenario1(self):
        buildings = [
            Building(4, 4, 9),
            Building(2, 7, 12)
        ]
        skyline = Skyline()
        results = skyline.recursive_function2(buildings)
        string_results = ",".join(str(result) for result in results)
        self.assertEqual(string_results, "(4,4),(2,9),(0,12)")
    """
                 _________
                |         |
             ___|______   |
            |   |     |   |
            |   |     |   |
            |   |     |   |
    """
    def test_scenario2(self):
        buildings = [
            Building(2, 7, 12),
            Building(7, 11, 14)
        ]
        skyline = Skyline()
        results = skyline.recursive_function2(buildings)
        string_results = ",".join(str(result) for result in results)
        self.assertEqual(string_results, "(2,7),(7,11),(0,14)")

    """
                ________
                |      |
             ___|______|_____
            |   |      |     |
            |   |      |     |
            |   |      |     |
    """
    def test_scenario3(self):
        buildings = [
            Building(6, 1, 6),
            Building(8, 3, 5)
        ]
        skyline = Skyline()
        results = skyline.recursive_function2(buildings)
        string_results = ",".join(str(result) for result in results)
        self.assertEqual(string_results, "(6,1),(8,3),(6,5),(0,6)")

    """
             _________
            |         |
            |         |
            |         |
    """
    def test_scenario4(self):
        buildings = [
            Building(6, 1, 6)
        ]
        skyline = Skyline()
        results = skyline.recursive_function2(buildings)
        string_results = ",".join(str(result) for result in results)
        self.assertEqual(string_results, "(6,1),(0,6)")

    """
             _________    _________
            |         |  |         |
            |         |  |         |
            |         |  |         |
    """
    def test_scenario5a(self):
        buildings = [
            Building(6, 1, 6),
            Building(6, 7, 12)
        ]
        skyline = Skyline()
        results = skyline.recursive_function2(buildings)
        string_results = ",".join(str(result) for result in results)
        self.assertEqual(string_results, "(6,1),(0,6),(6,7),(0,12)")

    
    """
             _________ _________
            |         |         |
            |         |         |
            |         |         |
    """
    def test_scenario5b(self):
        buildings = [
            Building(6, 1, 6),
            Building(6, 6, 12)
        ]
        skyline = Skyline()
        results = skyline.recursive_function2(buildings)
        string_results = ",".join(str(result) for result in results)
        self.assertEqual(string_results, "(6,1),(0,12)")

    """
             _________ 
            |   ___   |    
            |  |   |  |
            |  |   |  |
    """
    def test_scenario6(self):
        buildings = [
            Building(6, 1, 6),
            Building(3, 2, 5)
        ]
        skyline = Skyline()
        results = skyline.recursive_function2(buildings)
        string_results = ",".join(str(result) for result in results)
        self.assertEqual(string_results, "(6,1),(0,6)")

    def test_scenario7(self):
        buildings = [
            Building(6, 1, 6),
            Building(8, 3, 5),
            Building(4, 4, 9),
            Building(2, 7, 12),
            Building(7, 11, 14)
        ]
        skyline = Skyline()
        results = skyline.recursive_function2(buildings)
        string_results = ",".join(str(result) for result in results)
        self.assertEqual(string_results, "(6,1),(8,3),(6,5),(4,6),(2,9),(7,11),(0,14)")

    def test_scenario8(self):
        buildings = [
            Building(11, 1, 5),
            Building(6, 2, 7),
            Building(13, 3, 9),
            Building(7, 12, 16),
            Building(3, 14, 25),
            Building(18, 19, 22),
            Building(13, 23, 29),
            Building(4, 24, 28)
        ]
        skyline = Skyline()
        results = skyline.recursive_function2(buildings)
        string_results = ",".join(str(result) for result in results)
        self.assertEqual(string_results, "(11,1),(13,3),(0,9),(7,12),(3,16),(18,19),(3,22),(13,23),(0,29)")

    def test_scenario9(self):
        buildings = [
            Building(11, 1, 5),
            Building(6, 2, 7),
            Building(13, 3, 9)
        ]
        skyline = Skyline()
        results = skyline.recursive_function2(buildings)
        string_results = ",".join(str(result) for result in results)
        self.assertEqual(string_results, "(11,1),(13,3),(0,9)")

    def test_scenario10(self):
        buildings = [
            Building(7, 12, 16),
            Building(3, 14, 25),
            Building(18, 19, 22),
            Building(13, 23, 29),
            Building(4, 24, 28)
        ]
        skyline = Skyline()
        results = skyline.recursive_function2(buildings)
        string_results = ",".join(str(result) for result in results)
        self.assertEqual(string_results, "(7,12),(3,16),(18,19),(3,22),(13,23),(0,29)")

    def test_scenario11(self):
        buildings = [
            Building(13, 1, 5),
            Building(6, 2, 7),
            Building(11, 3, 9),
            Building(7, 12, 16),
            Building(3, 14, 25),
            Building(18, 19, 22),
            Building(13, 23, 29),
            Building(4, 24, 28)
        ]
        skyline = Skyline()
        results = skyline.recursive_function2(buildings)
        string_results = ",".join(str(result) for result in results)
        self.assertEqual(string_results, "(13,1),(11,5),(0,9),(7,12),(3,16),(18,19),(3,22),(13,23),(0,29)")

    def test_scenario12(self):
        buildings = [
            Building(13, 1, 5),
            Building(6, 2, 7),
            Building(11, 3, 9),
            Building(5, 15, 20),
        ]
        skyline = Skyline()
        results = skyline.recursive_function2(buildings)
        string_results = ",".join(str(result) for result in results)
        self.assertEqual(string_results, "(13,1),(11,5),(0,9),(5,15),(0,20)")

    def test_scenario13(self):
        buildings = [
            Building(10, 2, 9),
            Building(15,3,7),
            Building(12,5,12),
            Building(10,15,20),
            Building(8,19,24),
        ]
        skyline = Skyline()
        results = skyline.recursive_function2(buildings)
        string_results = ",".join(str(result) for result in results)
        self.assertEqual(string_results, "(10,2),(15,3),(12,7),(0,12),(10,15),(8,20),(0,24)")

if __name__ == '__main__':
    unittest.main()