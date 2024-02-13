from flask import Flask, current_app as app, json

# File to store all helper functions

# Functions in alphabetical order
################################
# 1. json_decode()
    # Takes stringified JSON and returns decoded json object
# 2. bar()
# 3. baz()
################################

def json_decode(data) :
  decoded_json = data.decode('utf8').replace('"','"')
  data = json.loads(decoded_json)
  return data