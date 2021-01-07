import enum

class Run:
    def __init__(self, content, style=None):
        self.content = content
        self.style = style

    def __repr__(self):
        return f"({self.style}) {self.content}"

    def __str__(self):
        return f"({self.style}) {self.content}"
