 **Problem Analysis**

The problem is to build a Flask application that tracks assignments. The application should allow users to create, view, and edit assignments. It should also allow users to track the status of their assignments.

**Design**

The application will consist of the following HTML files:

* `index.html`: This will be the home page of the application. It will contain a list of all the assignments.
* `create_assignment.html`: This page will allow users to create new assignments.
* `view_assignment.html`: This page will allow users to view the details of an assignment.
* `edit_assignment.html`: This page will allow users to edit the details of an assignment.

The application will also have the following routes:

* `/`: This route will render the `index.html` page.
* `/create_assignment`: This route will render the `create_assignment.html` page.
* `/view_assignment/<assignment_id>`: This route will render the `view_assignment.html` page, where `assignment_id` is the ID of the assignment to be viewed.
* `/edit_assignment/<assignment_id>`: This route will render the `edit_assignment.html` page, where `assignment_id` is the ID of the assignment to be edited.

**Implementation**

The application can be implemented using the Flask framework. The following code shows how to create the `index.html` page:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Assignment Tracker</title>
</head>
<body>
  <h1>Assignment Tracker</h1>
  <ul>
    {% for assignment in assignments %}
      <li><a href="/view_assignment/{{ assignment.id }}">{{ assignment.title }}</a></li>
    {% endfor %}
  </ul>
  <a href="/create_assignment">Create New Assignment</a>
</body>
</html>
```

The following code shows how to create the `create_assignment.html` page:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Create Assignment</title>
</head>
<body>
  <h1>Create Assignment</h1>
  <form action="/create_assignment" method="POST">
    <label for="title">Title:</label>
    <input type="text" name="title">
    <br>
    <label for="description">Description:</label>
    <textarea name="description"></textarea>
    <br>
    <label for="due_date">Due Date:</label>
    <input type="date" name="due_date">
    <br>
    <input type="submit" value="Create">
  </form>
</body>
</html>
```

The following code shows how to create the `view_assignment.html` page:

```html
<!DOCTYPE html>
<html>
<head>
  <title>View Assignment</title>
</head>
<body>
  <h1>View Assignment</h1>
  <h2>{{ assignment.title }}</h2>
  <p>{{ assignment.description }}</p>
  <p>Due Date: {{ assignment.due_date }}</p>
  <a href="/edit_assignment/{{ assignment.id }}">Edit</a>
</body>
</html>
```

The following code shows how to create the `edit_assignment.html` page:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Edit Assignment</title>
</head>
<body>
  <h1>Edit Assignment</h1>
  <form action="/edit_assignment/{{ assignment.id }}" method="POST">
    <label for="title">Title:</label>
    <input type="text" name="title" value="{{ assignment.title }}">
    <br>
    <label for="description">Description:</label>
    <textarea name="description">{{ assignment.description }}</textarea>
    <br>
    <label for="due_date">Due Date:</label>
    <input type="date" name="due_date" value="{{ assignment.due_date }}">
    <br>
    <input type="submit" value="Update">
  </form>
</body>
</html>
```

The following code shows how to create the routes for the application:

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

assignments = [
  {
    "id": 1,
    "title": "Assignment 1",
    "description": "This is the first assignment.",
    "due_date": "2023-03-08"
  },
  {
    "id": 2,
    "title": "Assignment 2",
    "description": "This is the second assignment.",
    "due_date": "2023-03-15"
  }
]

@app.route("/")
def index():
  return render_template("index.html", assignments=assignments)

@app.route("/create_assignment", methods=["GET", "POST"])
def create_assignment():
  if request.method == "POST":
    title = request.form["title"]
    description = request.form["description"]
    due_date = request.form["due_date"]

    new_assignment = {
      "id": len(assignments) + 1,
      "title": title,
      "description": description,
      "due_date": due_date
    }

    assignments.append(new_assignment)

    return redirect(url_for("index"))

  return render_template("create_assignment.html")

@app.route("/view_assignment/<assignment_id>")
def view_assignment(assignment_id):
  assignment = next((assignment for assignment in assignments if assignment["id"] == int(assignment_id)), None)

  if assignment is None:
    return render_template("error.html", message="Assignment not found.")

  return render_template("view_assignment.html", assignment=assignment)

@app.route("/edit_assignment/<assignment_id>", methods=["GET", "POST"])
def edit_assignment(assignment_id):
  assignment = next((assignment for assignment in assignments if assignment["id"] == int(assignment_id)), None)

  if assignment is None:
    return render_template("error.html", message="Assignment not found.")

  if request.method == "POST":
    title = request.form["title"]
    description = request.form["description"]
    due_date = request.form["due_date"]

    assignment["title"] = title
    assignment["description"] = description
    assignment["due_date"] = due_date

    return redirect(url_for("index"))

  return render_template("edit_assignment.html", assignment=assignment)

if __name__ == "__main__":
  app.run(debug=True)
```