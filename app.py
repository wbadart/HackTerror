import cross_reference as cr
import json
import flask
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/<eventID>')
def data(eventID):
    data = json.dumps(cr.get_attack_weather(eventID))
    res = flask.Response(data)
    res.headers['Content-Type'] = 'application/json'
    return res

@app.route('/temp/<event>')
def temp(event):
    data = json.dumps(cr.get_attack_temp(cr.get_attack_weather(event)))
    res = flask.Response(data)
    res.headers['Content-Type'] = 'application/json'
    return res

@app.route('/summary/<event>')
def summary(event):
    data = json.dumps(cr.get_summary(event))
    res = flask.Response(data)
    res.headers['Content-Type'] = 'application/json'
    return res

@app.route('/app')
def index():
    return flask.send_file('index.html')

if __name__ == '__main__':
    app.run()
