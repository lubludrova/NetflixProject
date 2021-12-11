from flask import render_template, url_for, request
from project_report import app, data
@app.route('/')
def index():
    page = request.args.get("page",0,int)
    df = data.iloc[page*15:page*15+15,:]
    return render_template("index.html", columns = df.columns.values, values = df.values.tolist(),page=page)


@app.route('/general')
def general():
    return render_template("general.html")

@app.route('/genres')
def genres():
    return render_template("genres.html")

@app.route('/languages')
def languages():
    return render_template("languages.html")


