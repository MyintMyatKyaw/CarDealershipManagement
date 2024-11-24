class InquiryQueue:
    """Queue to process inquiries in order."""
    def __init__(self):
        self.queue = []

    def enqueue(self, inquiry):
        self.queue.append(inquiry)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("No inquiries to process.")

    def is_empty(self):
        return len(self.queue) == 0
