from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api')
def home():
    file = open('data.json','r')
    data = json.load(file)
    file.close()
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
