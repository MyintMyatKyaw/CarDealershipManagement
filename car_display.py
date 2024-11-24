def display_car(car):
    """Displays information of a single car."""
    if car:
        print(f"Car ID: {car.car_id}")
        print(f"Make: {car.make}")
        print(f"Model: {car.model}")
        print(f"Year: {car.year}")
        print(f"Price: ${car.price}")
        print(f"Specifications: {car.specifications}")
        print("=" * 30)
    else:
        print("Car not found.")

def display_all_cars(cars):
    """Displays information for all cars in the list."""
    if cars:
        print("Current Inventory:")
        print("=" * 30)
        for car in cars:
            display_car(car)
    else:
        print("No cars in inventory.")
