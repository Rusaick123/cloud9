from flask import Flask, render_template,request
import boto3
import key_config as keys
from boto3.dynamodb.conditions import Key, Attr
import dynamodb_table_creation as dtc



app = Flask(__name__)


dynamodb = boto3.resource(
    'dynamodb',
    #aws_access_key_id     = keys.ACCESS_KEY_ID,
    #aws_secret_access_key = keys.ACCESS_SECRET_KEY,
    region_name           = keys.REGION_NAME,
)

@app.route('/')
def index():
    #dtc.create_table()
    #return "Table is created"
    return render_template('index.html')

@app.route('/signup', methods=["post"])
def signup():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        
        table = dynamodb.Table('users')
        
        table.put_item(
            Item={
                'name': name,
                'email': email,
                'password': password
            }
        )
        
        msg = "Registration Complete. Please Login to your account !"
        return render_template('login.html',msg = msg)
    return render_template('index.html')
    
@app.route('/login')
def login():    
    return render_template('login.html')   

@app.route('/check', methods=["post"])
def check():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        
        table = dynamodb.Table('users')
        
        response = table.query(
                KeyConditionExpression=Key('email').eq(email)
        )
        
        items = response['Items']
        name = items[0]['name']
        password_from_db = items[0]['password']
        
        if password == password_from_db:
            return render_template("home.html",name = name)
    
    return render_template("login.html")
    
if __name__ == '__main__':
    app.run(debug=True,port=8080,host='0.0.0.0')