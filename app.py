import cross_reference as cr
import json
from flask import Flask
app = Flask(__name__)

data = json.dumps(cr.get_attack_weather(197001090001))
print data

@app.route('/')
def hello():
    return '<pre>' + data + '</pre>'

if __name__ == '__main__':
    app.run()
