# Structure
# Styling rules object
# Parser for markdown
# Main script
from docx import Document
from styles import *

class MarkdownParser:
    def __init__(self, doc = Document()):
        self.document = doc
        self.style = Style()

    def parseWords(self, line):
        if '*' not in line:
            return self.document.add_paragraph(line)
        # Parse bold
        runs = []
        start, end = 0, 0
        bold = False
        while end < len(line):
            if line[end] == '*':
                if line[end - 1] == '*':
                    if not bold:
                        bold = True
                        runs.append(("NONE", line[start:end-1]))
                    else:
                        bold = False
                        runs.append(("BOLD", line[start:end-1]))
                    start = end + 1
            end += 1
        print(runs)
        para = self.document.add_paragraph('')
        for r in runs:
            content, style = r[1], r[0]
            if style == "BOLD":
                para.add_run(content).bold = True
            else:
                para.add_run(content)
        return para

    def parseHeader(self, line):
        level = 0
        while line[level] == '#': level += 1
        para = self.parseWords(line[level+1:])
        return self.style.setHeader(para, level)

    def parseList(self, line):
        line = line[line.index('-')+2:]
        para = self.document.add_paragraph(line)
        return self.style.setList(para)

    def parseLine(self, line):
        if line[0] == '#':
            return self.parseHeader(line)
        if line[0] == '-':
            return self.parseList(line)
        # otherwise, regular text object
        return self.parseWords(line)
