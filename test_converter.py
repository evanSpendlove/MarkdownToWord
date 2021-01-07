import unittest
from converter import *
from collections import deque

class TestConverter(unittest.TestCase):

    # Bugs identified:
    # - Header 1 is repeated twice... as is Header 2
    def test_convert(self):
        mdFile = 'data/easy_test.md'
        wordFile = 'data/docx_test.docx'
        con = Converter()
        con.convert(mdFile, wordFile)
        return

    def test_deque(self):
        para = [1, 2, (3, 4), 5]
        runs = deque(para)
        parsedRuns = []
        while len(runs) != 0:
            r = runs.popleft()
            if type(r) is not tuple:
                parsedRuns.append(r)
                continue
            else:
                content =  list(r)
                for c in reversed(content):
                    runs.appendleft(c)
                continue
        return 1

if __name__ == '__main__':
    unittest.main()
