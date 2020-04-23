class PrintError(RuntimeError):
    pass

class Printer:
    def __init__(self,pages_per_s,capacity):
        self.pages_per_s = pages_per_s
        self.capacity = capacity

    def print(self,pages):
        if pages > self.capacity:
            raise PrintError("Printer doesnt have anough capacity")

        self.capacity -= pages

        return f"Printer {pages} page in {pages/self.pages_per_s:2f} seconds"