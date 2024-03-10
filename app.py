from flask import Flask, current_app as app, render_template, request
from databases import db
from tracking import st

app = Flask(__name__)
db.init_app(app)

# Not sure how these decorators work. Could do with some more research! RESEARCH NEEDED
@app.route("/", methods=["POST","GET"])
def home():
    if request.method == 'POST':
        data = st.spacetrack()
        db.insert_Data(data)
    return render_template(
        'index.html', 
        title="Aerospace Project",
        description="Pathfinding algo for shortest path between space debris"
    )
