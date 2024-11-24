def display_inquiry(inquiry):
    """Displays information of a single inquiry."""
    if inquiry:
        print(f"Customer Name: {inquiry.customer_name}")
        print(f"Car ID: {inquiry.car_id}")
        print(f"Inquiry: {inquiry.inquiry}")
        print("=" * 30)
    else:
        print("Inquiry not found.")

def display_all_inquiries(inquiries):
    """Displays all inquiries in the list."""
    if inquiries:
        print("Customer Inquiries:")
        print("=" * 30)
        for inquiry in inquiries:
            display_inquiry(inquiry)
    else:
        print("No inquiries available.")
