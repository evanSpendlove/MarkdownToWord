from regexParser import *
from styles import *
from docx import Document

# ALIGN CENTRE!

with open('md_test.md', 'r') as f:
    lines = f.read().strip().split('\n')
    print(lines)
    md = MarkdownParser()
    for l in lines:
        md.parseLine(l)
    doc = md.doc
    # paragraph = doc.add_paragraph("List 1", "List Bullet 2")
    paras = doc.paragraphs
    for p in paras:
        print(p.text)
    doc.save('doc_test.docx')
