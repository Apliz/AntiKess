from flask import Flask, jsonify, render_template, request
from databases import db
from flask import current_app as app

app = Flask(__name__)
db.init_app(app)

@app.route("/", methods=["POST","GET"])
def home():
  data = request.get_data()
  print(data)
  return render_template(
    'index.html', 
    title="Aerospace Project",
    description="Project to calculate a series of transfers for space trash deorbit"
  )
 