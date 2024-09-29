from flask import Flask, render_template, url_for, jsonify, request, redirect

app = Flask(__name__)

items = {
    'Chicken': 12,
    'Apples': 6,
    'Carrots': 8,
    'Dinner Rolls': 9
}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', items=items)

@app.route('/addItems')
def addItems():
    return render_template('addItems.html')
@app.route('/addPeople')
def addPeople():
    return render_template('addPeople.html')

@app.route('/chart-data')
def chart_data():
    # Data for the pie chart
    labels = list(items.keys())  # Get item names
    values = list(items.values())  # Get item prices
    return jsonify({'labels': labels, 'values': values})


@app.route('/add', methods=['POST'])
def add_item():
    new_item_name = request.form['name']
    new_item_cost = request.form['cost']

    # Add the new item to the dictionary
    items[new_item_name] = int(new_item_cost)

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)