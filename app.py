from flask import Flask, jsonify, render_template, request
from flask import current_app as app

app = Flask(__name__)

@app.route("/")
def home():
  return render_template(
    'index.html', 
    title="Aerospace Project",
    description="Project to calculate a series of transfers for space trash deorbit"
  )
 