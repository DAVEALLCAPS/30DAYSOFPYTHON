# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo
import certifi
ca = certifi.where()
MONGODB_URI = 'mongodb+srv://DAVE:<password>@30daysofpython.zux1vda.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI, tlsCAFile=ca)
students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
db = client.thirty_days_of_python    
for student in students:
    db.students.insert_one(student)

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)