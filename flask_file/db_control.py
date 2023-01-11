import click
import psycopg2
from flask import g,current_app
from flask.cli import with_appcontext
import datetime


def get_db():
    if "db" not in g:
        g.db = psycopg2.connect(current_app.config["DATABASE"])
    return g.db
    
def show_db():
    posts = get_db().cursor()
    posts.execute("select * from text order by id;")
    posts = posts.fetchall()
    
    print(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))))
    #DBのデータ確認用
    #[print(posts[i]) for i in range(len(posts))]
    
    return posts

def close_db(e=None):
    db =  g.pop("db",None)
    if db is not None:
        db.close()


@click.command("init-db")
@with_appcontext
def init_db():
    db = get_db()
    db.cursor().execute("set time zone 'asia/tokyo'")
    db.cursor().execute("CREATE TABLE IF NOT EXISTS text(id SERIAL PRIMARY KEY ,str TEXT, time TIMESTAMP(0) dafault current_timestamp);")
    #　メモ：with time zone default current_timestamp
    db.commit()
    print("init!!")



@click.command("clean-db")
@with_appcontext
def clean_db():
    db = get_db()

    print("""
    1:Delete 2:Truncate  3:Drop 4:Cancel
    """)

    clean_command = int(input())
    match clean_command:
        case 1:
            db.cursor().execute("DELETE FROM text")
            clean_command = "DELETE"
        case 2:
            db.cursor().execute("TRUNCATE TABLE text")     
            clean_command = "TRUNCATE"
        case 3:
            db.cursor().execute("DROP TABLE text")
            clean_command = "DROP"
        case 4:
            clean_command = "Cancel"
        case _:
            raise ValueError("Not definition command")
    db.commit()
    print(clean_command + "!!")
