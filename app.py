from flask import Flask
from flask import json
from flask import jsonify

class d:
    title: ''
    body: ""
    def __init__(self, title, body):
        self.title = title
        self.body = body
        return
    def obj(self):
        return {"title" : self.title, "body" : self.body}

myD = [
    d("hello", "world").obj(),
    d("goodbye", "world").obj(),
    d("starplatinum the", "world").obj()
]


app = Flask(__name__)

@app.route('/')
def get_json():
    return jsonify(
        name= "my awesome api",
        data= myD
    )

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
