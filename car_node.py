class CarNode:
    """Node class for BST where each node represents a car."""
    def __init__(self, car_id, make, model, year, price, specifications):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.specifications = specifications
        self.left = None
        self.right = None
