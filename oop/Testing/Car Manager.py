import unittest


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car(fuel_capacity=100, fuel_consumption=5.6, make='Test', model='TestModel')

    def test_init_car(self):
        self.assertEqual('Test', self.car.make)
        self.assertEqual('TestModel', self.car.model)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(5.6, self.car.fuel_consumption)

    def test_if_wrong_values_raise_exception_model(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_if_wrong_values_raise_exception_make(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_if_wrong_values_raise_exception_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_if_wrong_values_raise_exception_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_refuel_exception_case(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_correct_case_v1(self):
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, 10)

    def test_drive_error_case(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_correct_case(self):
        self.car.fuel_amount = 100
        self.car.drive(1000)
        self.assertEqual(44, self.car.fuel_amount)


if __name__ == "__main__":
    unittest.main()
