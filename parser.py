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

    def applyStyles(self, tabs, runs):
        para = self.document.add_paragraph('')
        if tabs > 0:
            para = self.style.setIndent(para, tabs)
        for r in runs:
            content, style = r[1], r[0]
            run = para.add_run(content)
            self.style.styleRun(run, style)
        return para

    def parseTabs(self, line):
        print(line)
        tabs = 0
        if '\t' in line:
            print('Tab found')
            while line[tabs] == '\t': tabs += 1
        if line[0] == ' ':
            print('Space found')
            count = 0
            while line[count] == ' ': count += 1
            tabs += count // 4
        print(tabs)
        return tabs

    def parseWords(self, line, tabs):
        # if '*' not in line:
            # return self.document.add_paragraph(line)
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
        runs.append(("NONE", line[start:end]))
        print(runs)
        return self.applyStyles(tabs, runs)

    def parseHeader(self, line, tabs):
        level = 0
        while line[level] == '#': level += 1
        para = self.parseWords(line[level+1:], tabs)
        return self.style.setHeader(para, level)

    def parseList(self, line, tabs):
        line = line[line.index('-')+2:]
        para = self.parseWords(line, tabs)
        return self.style.setList(para)

    def parseLine(self, line):
        tabs = self.parseTabs(line)
        if '# ' in line:
            return self.parseHeader(line, tabs)
        if '- ' in line:
            return self.parseList(line, tabs)
        # otherwise, regular text object
        return self.parseWords(line, tabs)
