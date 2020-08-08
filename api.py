from pymongo import MongoClient

client = MongoClient('xxxxx')



analytics = client['****']

sample_colletion = analytics['****']


from flask import Flask, render_template, url_for, request, session, redirect,flash,jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS,cross_origin



app = Flask(__name__)
cors = CORS(app,resources={r"/login":{"origins":"http://localhost:8100"}})

#app.config['MONGO_DBNAME'] = 'analyticsDB'

# mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[database][?options]]
#"mongodb://username:" + urllib.quote("p@ssword") + "@127.0.0.1:27001/"
#mongo = PyMongo(app)
#users = mongo.db.kpi.summary
@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username'] + "<b><a href = '/logout'>click here to logout</a></b>"
    print('false ?')
    
    return False

@app.route('/login',methods= ['POST','GET','OPTIONS'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def login():
    data = request.get_json()
    print("What the data:",data)

    login_user= sample_colletion.find_one({'username':data['username']})

    if login_user:
        if login_user['password']== data['password']:

            details=session['username']= data['username']
            print('true')
            return jsonify("true")
    print('false')
    return jsonify("false")


@app.route('/logout')
def logout():

    session.clear()

    return redirect(url_for('index'))




if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True,port=8080)