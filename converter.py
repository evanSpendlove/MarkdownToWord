from docx.text.parfmt import ParagraphFormat
from styler import *
from parser import *

class Converter():
    def parse(self, lines):
        md = MarkdownParser()
        paragraphs = []
        for l in lines:
            paragraphs.append(md.parseLine(l))
        return paragraphs

    def style(self, paragraphs):
        st = Styler()
        for p in paragraphs:
            para = st.paragraph(p)
            for run in p.runs:
                st.applyStyle(para, run)
        return st.doc

    def convert(self, markdownFile, wordFile):
        with open(markdownFile, 'r') as f:
            lines = f.read().strip().split('\n')
        paras = self.parse(lines)
        doc = self.style(paras)

        paras = doc.paragraphs
        for p in paras:
            print(p.text)

        doc.save(wordFile)
