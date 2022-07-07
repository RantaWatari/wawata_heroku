from django import db
from flask import render_template,request,Blueprint,g
from flask_file.db_control import show_db,get_db

bp =Blueprint("server",__name__)

@bp.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        select = request.args.get("select")
        return render_template("index.html",select=select,posts=show_db())

    if request.method == "POST":
        sql_cmd = request.form.get("sql_cmd")
        db = get_db()
        match sql_cmd:
            case "insert":
                insert_text = request.form.get("insert_text")
                db.cursor().execute("INSERT INTO text(str) VALUES (%s)",(insert_text,))
            
            case "delete":
                delete_id = request.form.getlist("delete_id")
                for delete_num in delete_id:
                    db.cursor().execute("DELETE FROM text WHERE id = %s",(delete_num,))
            
            case "update":
                update_texts = request.form.getlist("update_texts")
                update_id = request.form.getlist("update_id")
                for n in range(0,len(update_texts)):
                    db.cursor().execute("UPDATE text SET str = %s where id = %s",(update_texts[n],update_id[n]))

        db.commit()
        return render_template("index.html",posts=show_db())
