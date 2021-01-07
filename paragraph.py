class Paragraph:
    def __init__(self, runs=[], header=False, level=0):
        self.header = header
        self.level = level
        self.runs = runs

    def __str__(self):
        return f"H:{self.header}({self.level}): {self.runs}"

    def __repr__(self):
        return f"H:{self.header}({self.level}): {self.runs}"
