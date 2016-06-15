import unittest
from truck import Truck
from car import Car


class car_dealer_truck_test_cases(unittest.TestCase):
    def test_truck_has_ccm(self):
        truck = Truck()
        self.assertEqual(hasattr(truck, 'ccm'), True)

    def test_truck_has_top_speed(self):
        truck = Truck()
        self.assertEqual(hasattr(truck, 'top_speed'), True)

    def test_truck_changable_ccm(self):
        truck = Truck()
        truck.ccm = 100
        self.assertEqual(truck.ccm, 100)

    def test_truck_changable_top_speed(self):
        truck = Truck()
        truck.top_speed = 100
        self.assertEqual(truck.top_speed, 100)

    def test_truck_has_carry_limit(self):
        truck = Truck()
        truck.carry_limit = 1000
        self.assertEqual(truck.carry_limit, 1000)

    def test_truck_has_carriage_when_has_none(self):
        truck = Truck()
        self.assertEqual(truck.has_carriage(), False)

    def test_truck_has_carriage_when_has(self):
        truck = Truck()
        truck.current_carriage_weight = 100
        self.assertEqual(truck.has_carriage(), True)

    def test_truck_can_attach_light_carriage(self):
        truck = Truck()
        truck.carry_limit = 1000
        result = truck.attach_carriage(200)
        self.assertEqual(result, True)

    def test_truck_can_attach_limit_carriage(self):
        truck = Truck()
        truck.carry_limit = 1000
        result = truck.attach_carriage(1000)
        self.assertEqual(result, True)

    def test_truck_can_attach_heavy_carriage(self):
        truck = Truck()
        truck.carry_limit = 1000
        result = truck.attach_carriage(2000)
        self.assertEqual(result, False)

    def test_truck_can_detach_cariage(self):
        truck = Truck()
        truck.current_carriage_weight = 100
        truck.detach_carriage()
        self.assertEqual(truck.current_carriage_weight, None)

    def test_truck_not_runns_to_error_when_try_to_detach_not_existing_cariage(self):
        truck = Truck()
        truck.detach_carriage()
        self.assertEqual(truck.current_carriage_weight, None)


class car_dealer_car_test_cases(unittest.TestCase):
    def test_car_has_ccm(self):
        car = Car()
        self.assertEqual(hasattr(car, 'ccm'), True)

    def test_car_has_top_speed(self):
        car = Car()
        self.assertEqual(hasattr(car, 'top_speed'), True)

    def test_car_does_not_have_carry_limit(self):
        car = Car()
        self.assertEqual(hasattr(car, 'carry_limit'), False)

    def test_car_does_not_have_carriage(self):
        car = Car()
        self.assertEqual(hasattr(car, 'current_carriage_weight'), False)

    def test_car_changable_ccm(self):
        car = Car()
        car.ccm = 100
        self.assertEqual(car.ccm, 100)

    def test_car_changable_top_speed(self):
        car = Car()
        car.top_speed = 100
        self.assertEqual(car.top_speed, 100)

    def test_car_has_is_running(self):
        car = Car()
        self.assertEqual(car.is_running, False)

    def test_car_has_is_running(self):
        car = Car()
        car.is_running = True
        self.assertEqual(car.is_running, True)

    def test_car_can_be_started(self):
        car = Car()
        car.start_engine()
        self.assertEqual(car.is_running, True)

    def test_car_can_be_stopped(self):
        car = Car()
        car.start_engine()
        car.stop_engine()
        self.assertEqual(car.is_running, False)

    def test_car_can_be_started_twice(self):
        car = Car()
        car.start_engine()
        car.start_engine()
        self.assertEqual(car.is_running, True)

    def test_car_can_be_stopped_twice(self):
        car = Car()
        car.stop_engine()
        car.stop_engine()
        self.assertEqual(car.is_running, False)


def test_main():
    unittest.main()


if __name__ == '__main__':
    test_main()
