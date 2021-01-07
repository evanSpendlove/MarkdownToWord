import re
from docx import Document
from paragraph import Paragraph
from run import Run
from collections import deque
# from styles import *

# TODO(evanSpendlove): Add run creation with styles to each parser

class MarkdownParser:
    def parseIndent(self, line):
        tabs = 0
        tabMarker = line[0] if line[0] in ' \t' else '\0'
        while tabs < len(line) and line[tabs] == tabMarker:
            tabs += 1
        if tabMarker == ' ':
            tabs //= 4
        return tabs

    def parseLine(self, line):
        parsers = [self.parseHyperlink, self.parseBold, self.parseItalics]
        para = self.parseHeader(line)
        runs = deque(para.runs)
        parsedRuns = []
        while len(runs) != 0:
            print(f"Runs: {runs}")
            r = runs.popleft()
            print("R: ", r)
            if r.style is not None:
                parsedRuns.append(r)
                continue
            p = 0
            parserMatch = False
            while not parserMatch and p < len(parsers):
                content = parsers[p](r.content)
                print("Parser: ", parsers[p], ", result: ", content)
                if content is not None:
                    for c in reversed(content):
                        runs.appendleft(c) # Add parsed runs to queue at the front
                    parserMatch = True
                    break
                p += 1
            if not parserMatch:
                parsedRuns.append(r)
                # Need to end infinite loop

        print(f"Line: {line}, parsed runs: {parsedRuns}")
        para.runs = parsedRuns
        return para

    def parseLineOld(self, para, line):
        parsers = [self.parseHyperlink, self.parseBold, self.parseItalics]

        for r in runs:
            if r.style == None:
                for p in parsers:
                    attempt = p(r.content)
                    if attempt is not None:
                        return 1
                        # Replace r with a list of runs...

        for p in parsers:
            content = p(run.content)

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

    def parseLineOld(self, line):
        parsers = [self.parseHeader, self.parseHyperlink, self.parseBold, self.parseItalics]
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

    # Working
    def parseItalics(self, content):
        italics = r"(.*)\*(?P<italics>[^*]+)\*(.*)"
        matches = re.findall(italics, content)
        if len(matches) == 0:
            return None
        matches = [[Run(r) for r in list(m)] for m in matches]
        for m in matches:
            m[1].style = 'ITALIC'
        return [r for m in matches for r in m]

    # Working
    def parseBold(self, content):
        bold = r"(.*)\*\*(?P<bold>[^*]+)\*\*(.*)"
        matches = re.findall(bold, content)
        if len(matches) == 0:
            return None
        matches = [[Run(r) for r in list(m)] for m in matches]
        for m in matches:
            m[1].style = 'BOLD'
        return [r for m in matches for r in m]

    # Working
    def parseHeader(self, line):
        header = r"^(?P<header>#+)(?: +)(?P<content>.*)$"
        match = re.match(header, line)
        if match is None:
            return Paragraph([Run(line)])
        run = [Run(match.group('content'))]
        height = int(len(match.group('header')))
        return Paragraph(run, True, height)
