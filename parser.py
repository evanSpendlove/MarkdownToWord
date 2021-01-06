import re
from docx import Document
# from styles import *

class MarkdownParser:
    def __init__(self, doc = Document()):
        self.doc = doc
        # self.style = Style()
        return

    def parseIndent(self, line):
        return -1

    def parseLine(self, line):
        parsers = [self.parseHeader, self.parseHyperlink, self.parseBold, self.parseItalics]
        content = []
        for p in parsers:
            content = p(line)
            # print(f"Parser: {p}, Line: {line}, Content: {content}")
            if content is not None:
                for match in content:
                    # print('Match: ', match)
                    for i in range(len(match)):
                        if type(match[i]) is not tuple:
                            # print(match[i])
                            match[i] = self.parseLine(match[i])
                return content
        # print(f"PARSING FAILED FOR: {line}")
        return line

    def parseHyperlink(self, content):
        hyperlink = r"([^[]*)\[(?P<text>[^]]+)\]\((?P<url>[^)]+)\)([^[]*)"
        matches = re.findall(hyperlink, content)
        matches = [list(m) for m in matches]
        return matches if len(matches) > 0 else None

    def parseItalics(self, content):
        italics = r"(.*)\*(?P<italics>[^*]+)\*(.*)"
        matches = re.findall(italics, content)
        matches = [list(m) for m in matches]
        for m in matches:
            m[1] = ('ITALICS', m[1])
        return matches if len(matches) > 0 else None

    def parseBold(self, content):
        bold = r"(.*)\*\*(?P<bold>[^*]+)\*\*(.*)"
        matches = re.findall(bold, content)
        matches = [list(m) for m in matches]
        for m in matches:
            # print(m)
            m[1] = ('BOLD', m[1])
        return matches if len(matches) > 0 else None

    def parseHeader(self, line):
        header = r"^(?P<header>#+)(?: +)(?P<content>.*)$"
        match = re.match(header, line)
        if match is None:
            return None
        height = len(match.group('header'))
        # content = self.parseLine([match.group('content')])
        return [[("HEADER", height, '')], [match.group('content')]]
        # return self.style.header(content, height)

if False:

    md = MarkdownParser()
    # Header tests
    head = [
            "## Easy header",
            "## Header with *italics*...",
            "## Header with **bold** and *italics*!"
            ]
    for h in head:
        match = md.parseLine(h)
        print(match)
    
    tests = [
            "**John**",
            "Hi",
            "Hello, my **name** is...",
            "Hello, my **name** is **John**"
            ]
    for t in tests:
        match = md.parseLine(t)
        if match is not None: 
            print(t)
            print(match)
    
    hyper = "Hello, this is a [hyperlink](www.lololol.com/?query=bob%n) haha!"
    hyper += hyper
    print(hyper)
    print(md.parseHyperlink(hyper))
    
    test = "This **is** super awesome **bold** text"
    print(re.split(r"\*\*", test))
    smartGex = r"([^*]*)\*\*(?P<bold>[^*]+)\*\*([^*]*)"
    print(re.findall(smartGex, test))
