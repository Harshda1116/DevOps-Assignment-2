from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://Harshda11:Harshda2222@cluster0.e6gy5g7.mongodb.net/?appName=Cluster0g")
db = client["student_db"]
collection = db["students"]

@app.route('/')
def form():
    return render_template("form.html")
    
@app.route('/submit', methods = ['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        data ={
            "name" : name,
            "email" : email
        }

        collection.insert_one(data)
        return redirect(url_for('success'))

    except Exception as e:
        return render_template("form.html", error=str(e))

@app.route('/success')
def success():
    return render_template("success.html")

if __name__ =='__main__':
    app.run(debug=True)