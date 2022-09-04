import spacy
from psaw import PushshiftAPI
import utils
from tqdm import tqdm
import pandas as pd
from html import entities
from spacy.tokens import DocBin
import json
from flask import Flask,render_template,request
import sqlite3
from googleapiclient.discovery import build
from private_youtube_key import api_key


nlp=spacy.blank("en")
db = DocBin()
file = open("annotations (1).json") 
TRAIN_DATA=json.load(file)
conn = sqlite3.connect("movies.db",check_same_thread=False) #make into function!
conn.execute("CREATE TABLE IF NOT EXISTS 'movies'('name'varchar(255))")#rowid already exists

def update_db():
    for text, annot in TRAIN_DATA ["annotations"]:
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

def call_movie(name):
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
            theComment += comment.body + "\n"
        df=pd.DataFrame(post_with_comments) 

    nlp_ner = spacy.load("model-best")
    doc2 = nlp_ner(theComment)
    for ent in doc2.ents:
        temp_ent=ent.text.replace(',','').replace('*','').replace('|','').replace('/','').replace(')','').replace('(','').strip()
        conn.execute('INSERT INTO movies VALUES (?)',(temp_ent,))

def main(name):
    update_db()
    call_movie(name) 

def youtube_parser(q):
    youtube=build('youtube','v3',developerKey=api_key)
    request=youtube.search().list(
    part='snippet',
    maxResults=1,
    q=f'{q} Trailer')
    return request.execute()

app=Flask(__name__, template_folder='template')

@app.route("/")
def front():
    return render_template("front.html")

@app.route("/submission",methods=["POST"])
def submission():
    name=request.form.get("search")
    if not name:
        return "failure"
    main(name)

    movies_temp=[]
    rows=conn.execute("SELECT DISTINCT name, COUNT(name) FROM movies GROUP BY name ORDER BY COUNT(name) DESC  limit 5;")

    for row in rows:
        movie_json=youtube_parser(row[0])
        video_id='https://www.youtube.com/watch?v='+str(movie_json['items'][0]['id']['videoId'])
        video_thumbnail_url=movie_json['items'][0]['snippet']['thumbnails']['medium']['url']
        movies_temp.append([row[0],video_id,video_thumbnail_url])

    return render_template("index.html",movies_temp=movies_temp)

app.run()

