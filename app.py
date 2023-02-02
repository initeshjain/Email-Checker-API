#import json
from flask import Flask, jsonify
#from flask.wrappers import Response
from numerize import numerize
from emck import emck

app = Flask(__name__)
#server = app.server

@app.get('/<int:n>')
def response(n):
    return numerize.numerize(n)

@app.get('/<string:s>')
def error(s):
    return jsonify('Please type a number after / at the end of the URL.')

@app.get('/em/<string:a>')
def em(a):
    return emck(a)

if __name__ == "__main__":
    from waitress import serve
    # app.run(debug=False)
    serve(app, host="0.0.0.0", port=80)
