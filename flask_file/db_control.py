#import click
import os
import psycopg2
from flask import g,current_app
#from flask.cli import with_appcontext


def get_db():
    if "db" not in g:
        g.db = psycopg2.connect(current_app.config["DATABASE"])
        #g.db = psycopg2.connect('postgres://ysbwuosrjdfhgh:8b051cb08b652e9001292338f20ef2f82d4199edc4e13acf9c5131679bb4f716@ec2-3-226-163-72.compute-1.amazonaws.com:5432/dvataoqaroqce')
        g.db.cursor().execute("set time zone 'asia/tokyo'")
        g.db.cursor().execute("CREATE TABLE IF NOT EXISTS text(id SERIAL PRIMARY KEY ,str TEXT, time TIMESTAMP(0) with time zone DEFAULT CURRENT_TIMESTAMP);")
    return g.db
    
def show_db():
    posts = get_db().cursor()
    posts.execute("select * from text;")
    posts = posts.fetchall()
    return posts

def close_db(e=None):
    db =  g.pop("db",None)
   
    if db is not None:
        db.close()

'''
@click.command("init-db")
@with_appcontext
def init_db():
    db = get_db()
    db.cursor().execute("set time zone 'asia/tokyo'")
    db.cursor().execute("CREATE TABLE IF NOT EXISTS text(id SERIAL PRIMARY KEY ,str TEXT, time TIMESTAMP(0) with time zone DEFAULT CURRENT_TIMESTAMP);")
    print("init!!")
'''