import unittest


class IntegerListTest(unittest.TestCase):
    def setUp(self):
        self.integer_list = IntegerList(1, 2, 3, 4, 5, 6)

    def test_add_function_correct_case(self):
        self.integer_list.add(100)
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3, 4, 5, 6, 100])

    def test_add_function_error_case(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add('es')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_function_correct_case(self):
        self.integer_list.remove_index(5)
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3, 4, 5])

    def test_remove_function_error_case(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(6)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_init(self):
        self.integer_list = IntegerList(1, 2, 3, 4, 5, 6, 'es', 'es')
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3, 4, 5, 6])

    def test_get_function_correct_case(self):
        self.assertEqual(self.integer_list.get(5), 6)

    def test_get_function_error_case(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(6)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert_function_first_error(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(6, 'ss')
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert_function_second_error(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(5, 'ss')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_insert_function_correct_case(self):
        self.integer_list.insert(5, 7)
        self.assertEqual([1, 2, 3, 4, 5, 7, 6], self.integer_list.get_data())

    def test_get_biggest_func(self):
        self.assertEqual(self.integer_list.get_biggest(), 6)

    def test_get_index_func(self):
        self.assertEqual(self.integer_list.get_index(6), 5)


if __name__ == '__main__':
    unittest.main()
