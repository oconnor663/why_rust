class Mess:
    def __init__(self, size):
        print(f"Make a {size} mess.")
        self.size = size

    def cleanup(self):
        print(f"Clean up the {self.size} mess.")

    def look(self):
        print(f"Look at the {self.size} mess!")

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.cleanup()


with Mess("giant") as giant_mess:
    giant_mess.look()