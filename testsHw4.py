import unittest
import data
from HwParts123 import cast


class test_cases(unittest.TestCase):
    def test_cast_ray(self):
        ray = data.Ray((data.Point(2, 0, 0)), (data.Vector(8, 0, 0)))
        sphere = data.Sphere(data.Point(7, 0, 0), 4)
        sphere2 = data.Sphere(data.Point(3, 12, 4), 2)
        input_list = [sphere, sphere2]
        self.assertEqual(cast.cast_ray(ray, input_list), True)

    def test_cast_ray2(self):
        ray = data.Ray((data.Point(2.4, 1, 0)), (data.Vector(6, 2.5, 0)))
        sphere = data.Sphere(data.Point(12, 5, 0), 3)
        sphere2 = data.Sphere(data.Point(3, 12, 4), 2)
        input_list = [sphere, sphere2]
        self.assertEqual(cast.cast_ray(ray, input_list), True)






if __name__ == "__main__":
    unittest.main()