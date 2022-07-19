from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods = ["GET","POST"])
def index():
    name = ["aaron", "bolu","yemi"]
    return render_template("second.html",page="home", dat=name)

@app.get("/dashboard")
def dashboard():
    return render_template("dashboard.html", page="dashboard")


@app.get("/about")
def about():
    return render_template("about.html", page="about")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
