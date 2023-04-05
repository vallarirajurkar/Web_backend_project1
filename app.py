from flask import Flask, render_template,url_for
import pymysql
app = Flask(__name__)

conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "abcd1234",
        db='test_flask',
		cursorclass=pymysql.cursors.DictCursor
        )
cur = conn.cursor()

@app.route("/")

def index():
	
	return render_template('index.html')
if __name__ == "__main__":
  app.run()