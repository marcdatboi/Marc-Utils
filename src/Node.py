
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


    # --- Getters ---
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev


    # --- Setters ---
    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev
