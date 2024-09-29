from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/addItems')
def addItems():
    return render_template('addItems.html')
@app.route('/addPeople')
def addPeople():
    return render_template('addPeople.html')

if __name__ == "__main__":
    app.run(debug=True)