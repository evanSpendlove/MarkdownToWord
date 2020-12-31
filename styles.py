from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm

class Style:
    def __init__(self):
        return

    def setHeader(self, para, level):
        # If Heading 1, align center
        if level > 9:
            raise Exception('Heading level cannot be greater than 9')
        para.style = f"Heading {level}"
        if level == 1:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        return para

    def setIndent(self, para, tabs):
        TAB_INDENT = 0.63       # Cm
        para.paragraph_format.left_indent = Cm(TAB_INDENT * tabs)
        return para

    def setList(self, para, tabs):
        listStyle = 'List Bullet'
        # if tabs > 0: listStyle += f" {tabs + 1}"
        para.style = listStyle
        return para

    def styleRun(self, run, style):
        if style == "BOLD":
            run.bold = True
        return run


# Other things:
# List styling with indenting
# Bold formatting - **word** = word.bold = True
# Hyperlinks
