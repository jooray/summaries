import spacy
import pytextrank

nlp = spacy.load('en_core_web_sm')

tr = pytextrank.TextRank()
nlp.add_pipe(tr.PipelineComponent, name='textrank', last=True)

def process_chapter(nlp,s):
    doc = nlp(s)

    # examine the top-ranked phrases in the document
    for p in doc._.phrases[:8]:
        print(p.text)

chapters_file = open("chapters.txt","r")

chapters = {}
for c in chapters_file:
    index,chapter=c.split(' ',1)
    chapters[chapter] = index

text_file = open("restart-en.txt","r")

last_chapter = ''
for s in text_file:
    if s in chapters:
        process_chapter(nlp,last_chapter)
        last_chapter = ''
        print('')
        print(chapters[s]+" "+s)
    else:
        last_chapter = last_chapter + s

