from flask import Flask, render_template, url_for, jsonify, request, redirect

app = Flask(__name__)

items = {
    'Chicken': 12,
    'Apples': 6,
    'Carrots': 8,
    'Dinner Rolls': 9
}

people = [

]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', items=items)

@app.route('/chart-data')
def chart_data():
    # Data for the pie chart
    labels = list(items.keys())
    values = list(items.values())
    return jsonify({'labels': labels, 'values': values})

# Route to handle adding items via form submission
@app.route('/add-item', methods=['POST'])
def submit_item():
    new_item_name = request.form.get('name')  # Get the 'name' field from the form
    new_item_cost = request.form.get('price')  # Get the 'price' field from the form

    if new_item_name and new_item_cost:
        # Convert price to integer and add the item to the 'items' dictionary
        items[new_item_name] = int(new_item_cost)
        return jsonify({'message': 'Item added successfully!', 'items': items})

    return jsonify({'message': 'Failed to add item, please provide a valid name and cost'}), 400

# Route to handle adding people via form submission
@app.route('/add-person', methods=['POST'])
def submit_person():
    person_name = request.form.get('name')  # Get the person's name from the form

    if person_name:
        # Add the new person to the people list
        people.append({'name': person_name})
        return jsonify({'message': 'Person added successfully!', 'people': people})

    return jsonify({'message': 'Failed to add person, please provide a valid name'}), 400



if __name__ == "__main__":
    app.run(debug=True)