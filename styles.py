class Style:
    def __init__(self):
        return

    def setHeader(self, para, level):
        # If Heading 1, align center
        if level > 9:
            raise Exception('Heading level cannot be greater than 9')
        para.style = f"Heading {level}"
        return para

    def setList(self, para):
        para.style = 'List Bullet'
        return para

# Other things:
# List styling with indenting
# Bold formatting - **word** = word.bold = True
# Hyperlinks
