class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}): ${self.cost:,.2f}"

    def get_age(self):
        age = 2022-self.year
        return age

    def is_vintage(self):
        age = self.get_age()
        if age >= 50:
            return True
        else:
            return False
