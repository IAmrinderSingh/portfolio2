from flask import Flask,render_template
from projects_skills import skills,projects,mypic
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html",len_skills=len(skills),skills=skills,len_pro=len(projects),projects=projects,mypic=mypic)

if __name__ == '__main__':
    app.run(debug=True)