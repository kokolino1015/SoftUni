import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.w = Worker('Test', 100, 100)

    def test_worker_init(self):
        self.assertEqual(self.w.name, 'Test')
        self.assertEqual(self.w.salary, 100)
        self.assertEqual(self.w.energy, 100)

    def test_rest_worker(self):
        self.w = Worker('Test', 100, 100)
        self.w.rest()
        self.assertEqual(self.w.energy, 101)

    def test_if_worker_works_with_negative_energy_raises(self):
        self.w = Worker('test', 100, 0)
        with self.assertRaises(Exception) as ex:
            self.w.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_worker_get_money(self):
        self.w = Worker('Test', 100, 100)
        self.w.work()
        self.assertEqual(self.w.money, self.w.salary)

    def test_if_workers_energy_is_decreased(self):
        self.w = Worker('Test', 100, 100)
        self.w.work()
        self.assertEqual(self.w.energy, 99)

    def test_workers_get_info(self):
        self.w = Worker('Test', 100, 100)
        self.assertEqual(self.w.get_info(), f'{self.w.name} has saved {self.w.money} money.')


if __name__ == '__main__':
    unittest.main()
