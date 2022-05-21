from flask import Flask,render_template
from projects_skills import skills
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html",len_skills=len(skills),skills=skills)

if __name__ == '__main__':
    app.run(debug=True)