from car_bst import Car, CarBST
from inquiry_doubly_linked_list import Inquiry, InquiryDoublyLinkedList
import random 
car_bst = CarBST()
inquiry_list = InquiryDoublyLinkedList()

def add_car():
    try:
        car_id = int(input("Enter Car ID: "))
        make = input("Enter Make: ")
        model = input("Enter Model: ")
        year = int(input("Enter Year: "))
        price = float(input("Enter Price (positive number): "))
        if price < 0:
            print("Price must be positive.")
            return
        specifications = input("Enter Specifications: ")

        car = Car(car_id, make, model, year, price, specifications)
        car_bst.insert(car)
    except ValueError:
        print("Invalid input. Please enter correct data types.")

def delete_car():
    try:
        car_id = int(input("Enter Car ID to delete: "))
        car_bst.delete_car(car_id)
    except ValueError:
        print("Invalid input. Car ID must be an integer.")

def update_car():
    try:
        car_id = int(input("Enter Car ID to update: "))
        new_price = input("Enter new price (or press Enter to skip): ")
        new_specifications = input("Enter new specifications (or press Enter to skip): ")

        new_price = float(new_price) if new_price else None
        if new_price is not None and new_price < 0:
            print("Price must be positive.")
            return

        car_bst.update_car(car_id, new_price, new_specifications)
    except ValueError:
        print("Invalid input. Please enter correct data types.")

def add_inquiry():
    try:
        customer_name = input("Enter Customer Name: ")
        car_id = int(input("Enter Car ID for the inquiry: "))
        inquiry_text = input("Enter Inquiry Details: ")
        
        # Generate a unique inquiry_id, here we use a random integer for simplicity
        inquiry_id = random.randint(1000, 9999)
        
        inquiry = Inquiry(inquiry_id, customer_name, car_id, inquiry_text)
        inquiry_list.add_inquiry(inquiry)
    except ValueError:
        print("Invalid input. Please ensure Car ID is an integer.")

def view_cars():
    if car_bst.cars:
        print("\nCar Inventory:")
        for car in car_bst.cars:
            print(f"{car.car_id}, {car.make}, {car.model}, {car.year}, ${car.price:.2f}, {car.specifications}")
        print(f"\nTotal cars in inventory: {len(car_bst.cars)}")
    else:
        print("No cars in inventory.")

def view_inquiries():
    if inquiry_list.inquiries:
        print("\nCustomer Inquiries:")
        for inquiry in inquiry_list.inquiries:
            print(f"Inquiry ID: {inquiry.inquiry_id},Customer: {inquiry.customer_name}, Car ID: {inquiry.car_id}, Inquiry: {inquiry.inquiry_text}")
        print(f"\nTotal Inquiries: {len(inquiry_list.inquiries)}")
    else:
        print("No inquiries found.")

def search_and_process_inquiry():
    inquiry_list.search_and_process_inquiry()

def main():
    while True:
        print("\nCar Dealership Management System")
        print("1. Add Car")
        print("2. View Cars")
        print("3. Delete Car")
        print("4. Update Car Information")
        print("5. Add Inquiry")
        print("6. View Inquiries")
        print("7. Search and Process Inquiry")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_car()
        elif choice == "2":
            view_cars()
        elif choice == "3":
            delete_car()
        elif choice == "4":
            update_car()
        elif choice == "5":
            add_inquiry()
        elif choice == "6":
            view_inquiries()
        elif choice == "7":
            search_and_process_inquiry()
        elif choice == "8":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
