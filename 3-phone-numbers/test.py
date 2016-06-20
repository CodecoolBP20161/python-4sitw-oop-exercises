import unittest
from person import Person
from main import open_csv, get_csv_file_name, format_output, get_person_by_phone_number

# open_csv(file_name)
# get_csv_file_name(argv_list)
# format_output(person)
# get_person_by_phone_number(person_list, user_input_phone_number)


class person_class_test_case(unittest.TestCase):
    def test_person_init_type(self):
        result = Person('Hugh Jass', '123')
        self.assertEqual(type(result).__name__, 'Person')

    def test_person_init_name(self):
        result = Person('Hugh Jass', '123')
        self.assertEqual(result._name, 'Hugh Jass')

    def test_person_init_phone_number(self):
        result = Person('Hugh Jass', '123')
        self.assertEqual(result._phone_number, '123')

    def test_person_get_name(self):
        result = Person('Hugh Jass', '123')
        self.assertEqual(result.get_name(), 'Hugh Jass')

    def test_person_normalize_phone_number_1(self):
        self.assertEqual(Person.normalize_phone_number('123'), '123')

    def test_person_normalize_phone_number_2(self):
        self.assertEqual(Person.normalize_phone_number('123-456'), '123456')

    def test_person_normalize_phone_number_3(self):
        self.assertEqual(Person.normalize_phone_number('123 456'), '123456')

    def test_person_normalize_phone_number_4(self):
        self.assertEqual(Person.normalize_phone_number('123-456-789'), '123456789')

    def test_person_normalize_phone_number_5(self):
        self.assertEqual(Person.normalize_phone_number('123 456 789'), '123456789')

    def test_person_normalize_phone_number_6(self):
        self.assertEqual(Person.normalize_phone_number('123/456'), '123/456')

    def test_person_normalize_phone_number_7(self):
        self.assertEqual(Person.normalize_phone_number('12x3'), '12x3')

    def test_person_normalize_phone_number_8(self):
        self.assertEqual(Person.normalize_phone_number('123--789'), '123789')

    def test_person_normalize_phone_number_9(self):
        self.assertEqual(Person.normalize_phone_number('123  789'), '123789')

    def test_person_is_phone_number_matching_1(self):
        result = Person('Hugh Jass', '123')
        self.assertEqual(result.is_phone_number_matching('123'), True)

    def test_person_is_phone_number_matching_2(self):
        result = Person('Hugh Jass', '123')
        self.assertEqual(result.is_phone_number_matching('456'), False)


class phone_numbers_test_case(unittest.TestCase):
    def test_get_csv_file_name_1(self):
        result = get_csv_file_name(['filename'])
        self.assertEqual(result, None)

    def test_get_csv_file_name_2(self):
        result = get_csv_file_name(['filename', 'a'])
        self.assertEqual(result, 'a')

    def test_get_csv_file_name_3(self):
        result = get_csv_file_name(['filename', 'a', 'b'])
        self.assertEqual(result, 'a')

    def test_format_output_with_none(self):
        result = format_output(None)
        self.assertEqual(result, 'No match found.')

    def test_format_output_with_person_1(self):
        person = Person('Hugh Jass', '123')
        result = format_output(person)
        self.assertEqual(result, 'This number belongs to: ' + 'Hugh Jass')

    def test_format_output_with_person_2(self):
        person = Person('Al Coholic', '456')
        result = format_output(person)
        self.assertEqual(result, 'This number belongs to: ' + 'Al Coholic')

    def test_get_person_by_phone_number_no_match(self):
        person_1 = Person('Sal Ami', '123')
        person_2 = Person('Pepe Roni', '456')
        result = get_person_by_phone_number([person_1, person_2], '789')
        self.assertEqual(result, None)

    def test_get_person_by_phone_number_match_1(self):
        person_1 = Person('Sal Ami', '123')
        person_2 = Person('Pepe Roni', '456')
        result = get_person_by_phone_number([person_1, person_2], '123')
        self.assertEqual(result, person_1)

    def test_get_person_by_phone_number_match_2(self):
        person_1 = Person('Sal Ami', '123')
        person_2 = Person('Pepe Roni', '456')
        result = get_person_by_phone_number([person_1, person_2], '456')
        self.assertEqual(result, person_2)


def test_main():
    unittest.main()


if __name__ == '__main__':
    test_main()
