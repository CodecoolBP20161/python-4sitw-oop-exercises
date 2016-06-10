import unittest
from door import Door
from main import generate_doors, toggle_doors, collect_open_doors, format_open_door_names, main


class _100doors_door_test_case(unittest.TestCase):
    def test_door_init(self):
        result = Door(1)
        self.assertEqual(type(result).__name__, "Door")

    def test_door_id_is_set_0(self):
        result = Door(0)
        self.assertEqual(result.id, 0)

    def test_door_id_is_set_1(self):
        result = Door(1)
        self.assertEqual(result.id, 1)

    def test_door_id_is_set_99(self):
        result = Door(99)
        self.assertEqual(result.id, 99)

    def test_door_is_open_is_set_False_by_default_1(self):
        result = Door(1)
        self.assertEqual(result.is_open, False)

    def test_door_is_open_is_set_False_by_default_99(self):
        result = Door(99)
        self.assertEqual(result.is_open, False)

    def test_door_toggle_from_False_to_True(self):
        result = Door(0)
        result.toggle()
        self.assertEqual(result.is_open, True)

    def test_door_toggle_from_True_to_False(self):
        result = Door(0)
        result.toggle()
        result.toggle()
        self.assertEqual(result.is_open, False)


class _100doors_generate_doors_test_case(unittest.TestCase):
    def test_generate_doors_1_generates_1_instance(self):
        result = generate_doors(1)
        self.assertEqual(len(result), 1)

    def test_generate_doors_2_generates_2_instance(self):
        result = generate_doors(2)
        self.assertEqual(len(result), 2)

    def test_generate_doors_99_generates_99_instance(self):
        result = generate_doors(99)
        self.assertEqual(len(result), 99)

    def test_generate_doors_927_generates_927_instance(self):
        result = generate_doors(927)
        self.assertEqual(len(result), 927)

    def test_generate_doors_1_generates_Door_instance(self):
        result = generate_doors(1)
        self.assertEqual(type(result[0]).__name__, "Door")

    def test_generate_doors_1000_generates_Door_instances(self):
        result = generate_doors(1000)
        for i in range(0, 1000):
            self.assertEqual(type(result[i]).__name__, "Door")

    def test_generate_doors_1_generates_correct_id_value(self):
        result = generate_doors(1)
        self.assertEqual(result[0].id, 1)

    def test_generate_doors_1000_generates_correct_id_values(self):
        result = generate_doors(1000)
        for i in range(0, 1000):
            self.assertEqual(result[i].id, i + 1)

    def test_generate_doors_1_generates_closed_door(self):
        result = generate_doors(1)
        self.assertEqual(result[0].is_open, False)

    def test_generate_doors_1000_generates_closed_doors(self):
        result = generate_doors(1000)
        for i in range(0, 1000):
            self.assertEqual(result[i].is_open, False)


class _100doors_toggle_doors_test_case(unittest.TestCase):
    def setUp(self):
        self.data = {
            100: toggle_doors(generate_doors(100)),
            999: toggle_doors(generate_doors(999))
        }

    def test_toggle_doors_100_not_changing_length_of_doors_list(self):
        result = self.data[100]
        self.assertEqual(len(result), 100)

    def test_toggle_doors_999_not_changing_length_of_doors_list(self):
        result = self.data[999]
        self.assertEqual(len(result), 999)

    def test_toggle_doors_100_correct_result_1(self):
        result = self.data[100]
        self.assertEqual(result[0].is_open, True)

    def test_toggle_doors_100_correct_result_2(self):
        result = self.data[100]
        self.assertEqual(result[1].is_open, False)

    def test_toggle_doors_100_correct_result_3(self):
        result = self.data[100]
        self.assertEqual(result[2].is_open, False)

    def test_toggle_doors_100_correct_result_4(self):
        result = self.data[100]
        self.assertEqual(result[3].is_open, True)

    def test_toggle_doors_100_correct_result_5(self):
        result = self.data[100]
        self.assertEqual(result[4].is_open, False)

    def test_toggle_doors_100_correct_result_9(self):
        result = self.data[100]
        self.assertEqual(result[8].is_open, True)

    def test_toggle_doors_100_correct_result_16(self):
        result = self.data[100]
        self.assertEqual(result[15].is_open, True)

    def test_toggle_doors_100_correct_result_25(self):
        result = self.data[100]
        self.assertEqual(result[24].is_open, True)

    def test_toggle_doors_100_correct_result_64(self):
        result = self.data[100]
        self.assertEqual(result[63].is_open, True)

    def test_toggle_doors_100_correct_result_100(self):
        result = self.data[100]
        self.assertEqual(result[99].is_open, True)

    def test_toggle_doors_999_correct_result_1(self):
        result = self.data[999]
        self.assertEqual(result[0].is_open, True)

    def test_toggle_doors_999_correct_result_2(self):
        result = self.data[999]
        self.assertEqual(result[1].is_open, False)

    def test_toggle_doors_999_correct_result_3(self):
        result = self.data[999]
        self.assertEqual(result[2].is_open, False)

    def test_toggle_doors_999_correct_result_4(self):
        result = self.data[999]
        self.assertEqual(result[3].is_open, True)

    def test_toggle_doors_999_correct_result_5(self):
        result = self.data[999]
        self.assertEqual(result[4].is_open, False)

    def test_toggle_doors_999_correct_result_9(self):
        result = self.data[999]
        self.assertEqual(result[8].is_open, True)

    def test_toggle_doors_999_correct_result_16(self):
        result = self.data[999]
        self.assertEqual(result[15].is_open, True)

    def test_toggle_doors_999_correct_result_25(self):
        result = self.data[999]
        self.assertEqual(result[24].is_open, True)

    def test_toggle_doors_999_correct_result_64(self):
        result = self.data[999]
        self.assertEqual(result[63].is_open, True)

    def test_toggle_doors_999_correct_result_100(self):
        result = self.data[999]
        self.assertEqual(result[99].is_open, True)

    def test_toggle_doors_999_correct_result_625(self):
        result = self.data[999]
        self.assertEqual(result[624].is_open, True)

    def test_toggle_doors_999_correct_result_841(self):
        result = self.data[999]
        self.assertEqual(result[840].is_open, True)

    def test_toggle_doors_999_correct_result_961(self):
        result = self.data[999]
        self.assertEqual(result[960].is_open, True)

    def test_toggle_doors_999_correct_result_962(self):
        result = self.data[999]
        self.assertEqual(result[961].is_open, False)


class _100doors_collect_open_doors_test_case(unittest.TestCase):
    def test_collect_open_doors_10_every_left_closed(self):
        result = collect_open_doors(generate_doors(10))
        self.assertEqual(result, [])

    def test_collect_open_doors_10_toggled(self):
        result = collect_open_doors(toggle_doors(generate_doors(10)))
        self.assertEqual(result, ["1", "4", "9"])


class _100doors_format_open_door_names_test_case(unittest.TestCase):
    def test_format_open_door_names_empty(self):
        result = format_open_door_names([])
        self.assertEqual(result, "")

    def test_format_open_door_names_1_item(self):
        result = format_open_door_names(["9"])
        self.assertEqual(result, "9")

    def test_format_open_door_names_2_items(self):
        result = format_open_door_names(["1", "4"])
        self.assertEqual(result, "1, 4")

    def test_format_open_door_names_lot_of_items(self):
        result = format_open_door_names(["99", "400", "450", "X"])
        self.assertEqual(result, "99, 400, 450, X")

    def test_format_open_door_names_throws_on_integer(self):
        try:
            result = format_open_door_names([1])
            self.assertEqual(True, False)
        except TypeError:
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False)


class _100doors_main_test_case(unittest.TestCase):
    def test_main_should_not_return_value(self):
        result = main(1)
        self.assertEqual(result, None)


def test_main():
    unittest.main()


if __name__ == '__main__':
    test_main()
