class Inquiry:
    def __init__(self, inquiry_id, customer_name, car_id, inquiry_text):
        self.inquiry_id = inquiry_id
        self.customer_name = customer_name
        self.car_id = car_id
        self.inquiry_text = inquiry_text

    def to_string(self):
        return f"{self.inquiry_id},{self.customer_name},{self.car_id},{self.inquiry_text}\n"

    @staticmethod
    def from_string(data):
        try:
            inquiry_id, customer_name, car_id, inquiry_text = data.strip().split(",")
            return Inquiry(int(inquiry_id), customer_name, int(car_id), inquiry_text)
        except ValueError:
            print("Error reading inquiry data from file.")
            return None

class InquiryDoublyLinkedList:
    def __init__(self):
        self.inquiries = []
        self.load_inquiries_from_file()

    def load_inquiries_from_file(self):
        try:
            with open("inquiries.txt", "r") as file:
                for line in file:
                    inquiry = Inquiry.from_string(line)
                    if inquiry:
                        self.inquiries.append(inquiry)
        except FileNotFoundError:
            print("No existing inquiries found. Starting with an empty inquiry list.")
        except IOError:
            print("Error reading inquiries.txt.")

    def save_all_inquiries_to_file(self):
        try:
            with open("inquiries.txt", "w") as file:
                for inquiry in self.inquiries:
                    file.write(inquiry.to_string())
        except IOError:
            print("Error saving inquiries to file.")

    def add_inquiry(self, inquiry):
        self.inquiries.append(inquiry)
        self.save_all_inquiries_to_file()
        print("Inquiry added successfully.")

    def search_and_process_inquiry(self):
        try:
            inquiry_id = int(input("Enter the Inquiry ID to search: "))
            inquiry = next((inq for inq in self.inquiries if inq.inquiry_id == inquiry_id), None)
            if inquiry:
                print(f"Found Inquiry - Customer: {inquiry.customer_name}, Car ID: {inquiry.car_id}, Inquiry: {inquiry.inquiry_text}")
                process = input("Finish processing this inquiry? (yes or no): ").strip().lower()
                if process == 'yes':
                    self.inquiries = [inq for inq in self.inquiries if inq.inquiry_id != inquiry_id]
                    self.save_all_inquiries_to_file()
                    print("Finished processing the inquiry you chose.")
                else:
                    print("Try to process the inquiry first , try again later.")
            else:
                print("Inquiry ID not found.")
        except ValueError:
            print("Invalid input. Inquiry ID must be an integer.")
