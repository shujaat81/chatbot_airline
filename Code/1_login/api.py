from pymongo import MongoClient

client = MongoClient('****')



analytics = client['***B']

sample_colletion = analytics['****']
print(sample_colletion)


from flask import Flask, render_template, url_for, request, session, redirect,flash,jsonify,send_file
from flask_pymongo import PyMongo
import gridfs
from werkzeug import secure_filename
from PIL import Image
import io



app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
	return 'Hello'


@app.route('/login',methods= ['POST','GET','OPTIONS'])

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


@app.route('/upload',methods=['GET', 'POST'])
def info():
    
    fs = gridfs.GridFS(analytics)
    
    if 'file' not in request.files:
        print("Not found anything")
    else:
        print('working')
        file = request.files['file']
        
        a = fs.put(file,filename="image") 
    
    return "done!"
@app.route('/download',methods=['GET','POST'])
def download():
    key = request.form
    print(key['key'])
    fs = gridfs.GridFS(analytics)
    b = fs.get_last_version(key['key']).read()
    print(type(b))
    image = Image.open(io.BytesIO(b))
    
    return send_file(image, mimetype='image/gif')



if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True,port=8080)