class InquiryNode:
    """Node class for Doubly Linked List where each node represents an inquiry."""
    def __init__(self, customer_name, car_id, inquiry):
        self.customer_name = customer_name
        self.car_id = car_id
        self.inquiry = inquiry
        self.prev = None
        self.next = None
