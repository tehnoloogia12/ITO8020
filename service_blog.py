from flask import Flask, request
import sqlite3
app = Flask(__name__)

@app.route('/blog', methods=['POST', 'GET'])
def sum():
  c=request.args.get("c",'')
  conn = sqlite3.connect('blog.sql')
  cur=conn.cursor()
  sql = """ 
    insert into blog(content,date,time)
    values ('"""+c+"""',date('now'),time('now')); 
    """
  cur.execute(sql);

  return "ok"

app.run(debug=True, port=5000)
