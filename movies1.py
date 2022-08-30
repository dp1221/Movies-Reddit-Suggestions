from __future__ import absolute_import
import spacy
import psaw
from psaw import PushshiftAPI
import utils
import tqdm
from tqdm import tqdm
import pandas as pd
from html import entities
import spacy
from spacy.tokens import DocBin
import os
import json
import importlib

nlp=spacy.blank("en")
db = DocBin()
os.chdir(r'C:\Users\danie\Dropbox\My PC (LAPTOP-LLA9H6I7)\Downloads')
f = open("annotations.json") 

TRAIN_DATA=json.load(f)

for text, annot in tqdm(TRAIN_DATA ["annotations"]):
    doc=nlp.make_doc(text)
    ents=[]
    for start, end, label in annot["entities"]:
        span=doc.char_span(start,end,label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents=ents
    db.add(doc)
db.to_disk("./annotations.spacy")

name = input ("Enter the 'Movie Title of Interest' in proper letter case: ")
api=PushshiftAPI()
subreddit_name="MovieSuggestions"
word_to_check=name
comments=api.search_comments(q=word_to_check, subreddit=subreddit_name, limit=999)

theComment=""
post_with_comments=[]
for comment in comments:
    if word_to_check in comment.body.lower():
        post_with_comments.append(
            {"comment_id":comment.id, "comment_text":comment.body,"score":comment.score,"post":comment.submission.id})
    else:
        water += comment.body + "\n"
    df=pd.DataFrame(post_with_comments)   
print(theComment)

nlp_ner = spacy.load(r"C:\Users\danie\Dropbox\My PC (LAPTOP-LLA9H6I7)\Downloads\model-best")

doc2 = nlp_ner(water)
for ent in doc2.ents:
    print(ent.text, ent.label_)
