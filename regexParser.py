import re
from docx import Document
from styles import *

class MarkdownParser:
    def __init__(self, doc = Document()):
        self.doc = doc
        self.style = Style()
        return

    def parseLine(self, line):
        return self.parseHeader(line)

    def parseContent(self, content):
        return self.doc.add_paragraph(content)

    def parseBold(self, para, content):
        bold = r"([^*]*)\*\*(?P<bold>[^*]+)\*\*([^*]*)"
        match = re.findall(bold, content)
        if match is None:
            return None
        return match

    def parseHeader(self, line):
        header = r"^(?P<header>#+)(?: +)(?P<content>.*)$"
        match = re.match(header, line)
        if match is None:
            return None
        height = len(match.group('header'))
        content = self.parseContent(match.group('content'))
        return self.style.header(content, height)

md = MarkdownParser()
tests = [
        "**John**",
        "Hi",
        "Hello, my **name** is...",
        "Hello, my **name** is **John**"
        ]
for t in tests:
    match = md.parseBold(None, t)
    if match is not None: print(t, match)
