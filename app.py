from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

@app.route("/")
def homepage(name=None):
  return render_template('index.html', name=name)
  # return "<p>test</p>"
# @app.route("/calculator")
# def calculator():
#     return  
@app.route("/test")
def testpage():
  return "<p>test</p>"