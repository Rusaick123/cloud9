from flask import Flask, request, render_template
import boto3

app = Flask(__name__)


@app.route('/') 
def index():
    return render_template("index.html")
    
@app.route('/put-via-form') 
def addItem():
    return render_template("putItem.html")

@app.route('/create-table', methods=["POST"]) 
def create_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table_name = request.form["tableName"]
    partition_key = request.form["partitionKey"]
    sort_key = request.form["sortKey"]

    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': partition_key,
                'KeyType': 'HASH'  #Partition key
            },
            {
                'AttributeName': sort_key,
                'KeyType': 'RANGE'  #Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': partition_key,
                'AttributeType': 'S'
            },
            {
                'AttributeName': sort_key,
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    # Wait until the table is created
    table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

    # Check the table status
    if table.table_status == 'ACTIVE':
        return f"Table '{table_name}' created successfully"
    else:
        return f"Error creating table. Table status: {table.table_status}"

@app.route('/put-item') 
def put_item():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('StudentDetails')
    
    item = {
        'regNO': '001',
        'name': 'John Wick',
        'age': 20
    }
    
    response = table.put_item(Item=item)
    
    return "Sucessfully added the item"  
    
@app.route('/put-via-form', methods=["POST"]) 
def update_table_via_form():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('StudentDetails')
    
    data = request.form.to_dict()
    #regNo = request.form['regNo']
    #name = request.form['name']
    #age = request.form['age']
    
    table.put_item(Item=data)
    
    return "Sucessfully added the item"  
    
    
@app.route('/get-item') 
def get_item():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('StudentDetails') 
    
    response = table.get_item(
        Key = {
            'regNO': '003',
            'name':'Namal'
        },
        AttributesToGet=['name','age']
            
        
    )
    
    return response
if __name__ == '__main__':
    app.run(debug=True,port=8080,host='0.0.0.0')