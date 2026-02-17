from todo import TodoList
from flask import Flask, render_template, request, redirect, url_for
from datetime import date

app = Flask(__name__)

todo_list = TodoList()
# todo_list.load()

@app.route("/")
def home():
    # todo_list.load()
    return render_template("home.html", todos=todo_list.items)


@app.route("/add", methods=['POST', 'GET'])
def add():
    today = date.today().isoformat()
    if request.method == 'POST':
        todo_list.add(
        priority = int(request.form['priority']),
        done = bool(request.form.get('option1', False)),
        
        due = request.form['due'],
        note = request.form['description']
        )
        return redirect(url_for('home'))
    return render_template("add.html", today=today)
    
@app.route("/done/<item_id>")
def done(item_id):
    for item in todo_list.items:
        if item.identifier == item_id:
            item.done = True
            break
    todo_list.save()
    return redirect(url_for("home"))




@app.route("/edit/<int:item_id>", methods=['POST', 'GET'])
def edit(item_id):
    items = None
    for item in todo_list.items:
        if item.identifier == item_id:
            items = item
            break

    if items is None:
        return redirect(url_for("home"))

    if request.method == 'POST':
        items.priority = int(request.form["priority"])
        items.done = "option1" in request.form
        items.due = request.form["due"]
        items.note = request.form["description"]
    
        return redirect(url_for("home"))

    return render_template("edit.html", item=items)

if __name__ == "__main__":
    app.run(debug=True)
