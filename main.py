 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

assignments = []

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
      "title": title,
      "description": description,
      "due_date": due_date
    }

    assignments.append(new_assignment)

    return redirect(url_for("index"))

  return render_template("create_assignment.html")

@app.route("/view_assignment/<assignment_id>")
def view_assignment(assignment_id):
  assignment = next((assignment for assignment in assignments if assignment["title"] == assignment_id), None)

  if assignment is None:
    return render_template("error.html", message="Assignment not found.")

  return render_template("view_assignment.html", assignment=assignment)

@app.route("/edit_assignment/<assignment_id>", methods=["GET", "POST"])
def edit_assignment(assignment_id):
  assignment = next((assignment for assignment in assignments if assignment["title"] == assignment_id), None)

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
