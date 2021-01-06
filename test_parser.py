import unittest
from parser import *

class TestParser(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.md = MarkdownParser()

    def test_parseHeader(self):
        test_cases = [
                ["## Header", [[('HEADER', 2, '')], ["Header"]]],
                ["# Header", [[('HEADER', 1, '')], ["Header"]]],
                ["#### Headerzz", [[('HEADER', 4, '')], ["Headerzz"]]],
                ["Header", None]
                ]
        for t in test_cases:
            self.assertEqual(t[1], self.md.parseHeader(t[0]))

    def test_parseLine(self):
        test_cases = [
                ["## Header", [[('HEADER', 2, '')], ['Header']]],
                ["# Header with *italics*!", [[('HEADER', 1, '')], [[['Header with ', ('ITALICS', 'italics'), '!']]]]],
                ["#### Headerzz with *italics* and **bold**.", [[('HEADER', 4, '')], [[[[['Headerzz with ', ('ITALICS', 'italics'), ' and ']], ('BOLD', 'bold'), '.']]]]],
                ["Header", "Header"]
                ]
        for t in test_cases:
            self.assertEqual(t[1], self.md.parseLine(t[0]))

    def test_parseHyperlink(self):
        test_cases = [
                ["this is a [hyperlink](www.lololol.com/?query=bob%n) ha", [['this is a ', 'hyperlink', 'www.lololol.com/?query=bob%n', ' ha']]],
                ["Two [hyper](www.lol.com) exist [here](lol.com) woo!", [['Two ', 'hyper', 'www.lol.com', ' exist '], ['', 'here', 'lol.com', ' woo!']]],
                ["Not a hyperlink", None]
                ]
        for t in test_cases:
            self.assertEqual(t[1], self.md.parseHyperlink(t[0]))

    def test_parseBold(self):
        test_cases = [
                ["Hello, this is **bold** text.", [['Hello, this is ', ('BOLD', 'bold'), ' text.']]],
                ["Hello, this is *italics* and **bold** text.!", [['Hello, this is *italics* and ', ('BOLD', 'bold'), ' text.!']]],
                ["Hello, this is not bold text.", None]
                ]
        for t in test_cases:
            self.assertEqual(t[1], self.md.parseBold(t[0]))

    def test_parseItalics(self):
        test_cases = [
                ["Hello, this is *italics* text.", [['Hello, this is ', ('ITALICS', 'italics'), ' text.']]],
                ["Hello, this is *italics* and *italics* text.!", [['Hello, this is *italics* and ', ('ITALICS', 'italics'), ' text.!']]],
                ["Hello, this is not bold text.", None]
                ]
        for t in test_cases:
            self.assertEqual(t[1], self.md.parseItalics(t[0]))

if __name__ == '__main__':
    unittest.main()

