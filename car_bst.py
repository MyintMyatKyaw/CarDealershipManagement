class Car:
    def __init__(self, car_id, make, model, year, price, specifications):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.specifications = specifications

    def to_string(self):
        return f"{self.car_id},{self.make},{self.model},{self.year},{self.price},{self.specifications}\n"

    @staticmethod
    def from_string(data):
        try:
            car_id, make, model, year, price, specifications = data.strip().split(",")
            return Car(int(car_id), make, model, int(year), float(price), specifications)
        except ValueError:
            print("Error reading car data from file.")
            return None

class CarBST:
    def __init__(self):
        self.cars = []
        self.load_cars_from_file()
        self.root = None

    def load_cars_from_file(self):
        try:
            with open("cars.txt", "r") as file:
                for line in file:
                    car = Car.from_string(line)
                    if car:
                        self.cars.append(car)
        except FileNotFoundError:
            print("No existing car data found. Starting with an empty inventory.")
        except IOError:
            print("Error reading cars.txt.")

    def save_all_cars_to_file(self):
        try:
            with open("cars.txt", "w") as file:
                for car in self.cars:
                    file.write(car.to_string())
        except IOError:
            print("Error saving cars to file.")

    def insert(self, car):
        if any(existing_car.car_id == car.car_id for existing_car in self.cars):
            print("Car ID already exists. Please use a unique Car ID.")
            return
        self.cars.append(car)
        self.save_all_cars_to_file()
        print("Car added successfully.")

    def delete_car(self, car_id):
        original_len = len(self.cars)
        self.cars = [car for car in self.cars if car.car_id != car_id]
        if len(self.cars) < original_len:
            self.save_all_cars_to_file()
            print("Car deleted successfully.")
        else:
            print("Car ID not found.")

    def update_car(self, car_id, new_price=None, new_specifications=None):
        car = next((c for c in self.cars if c.car_id == car_id), None)
        if car:
            if new_price:
                car.price = new_price
            if new_specifications:
                car.specifications = new_specifications
            self.save_all_cars_to_file()
            print("Car information updated.")
        else:
            print("Car ID not found.")
    def _in_order_traversal(self, node, cars):
        if node:
            self._in_order_traversal(node.left, cars)
            cars.append(node.car)  # Collect car data in the list
            self._in_order_traversal(node.right, cars)

    def get_all_cars(self):
        cars = []
        self._in_order_traversal(self.root, cars)
        return cars