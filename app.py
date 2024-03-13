from flask import Flask, current_app as app, render_template, request, redirect, url_for
from databases import db
from tracking import st

app = Flask(
    __name__,
    template_folder = "templates"
)
db.init_app(app)

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == 'POST':
        spacetrack = st.spacetrack()
        db.orbitalbodies(spacetrack)
        return redirect(url_for("ready"))
    return render_template(
        'index.html', 
        title="Aerospace Project",
        description="Pathfinding algo for shortest path between space debris"
    )

@app.route("/pathfinder")
def ready():
    return render_template(
        "pathfinder.html"
    )