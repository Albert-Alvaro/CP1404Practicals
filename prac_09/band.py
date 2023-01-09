class Band:
    def __init__(self, name=""):
        self.name = name
        self.members = []
        self.member_dictionary = {}

    def __str__(self):
        return f"{self.name} ({str(self.members).lstrip('[').rstrip(']')})"

    def add(self, musician):
        self.member_dictionary[musician.name] = musician.instruments
        self.members.append(f"{musician.name} ({musician.instruments})")

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument."""
        for member in self.member_dictionary:
            if not self.member_dictionary[member]:
                print(f"{member} needs an instrument!")
            else:
                print(f"{member} is playing: {self.member_dictionary[member][0]}")

