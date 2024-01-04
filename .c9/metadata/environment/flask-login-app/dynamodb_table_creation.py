{"filter":false,"title":"dynamodb_table_creation.py","tooltip":"/flask-login-app/dynamodb_table_creation.py","undoManager":{"mark":56,"position":56,"stack":[[{"start":{"row":0,"column":0},"end":{"row":20,"column":15},"action":"insert","lines":["def create_table():","   table = dynamodb_resource.create_table(","       TableName = 'users', # Name of the table","       KeySchema = [","           {","               'AttributeName': 'email',","               'KeyType'      : 'HASH' #RANGE = sort key, HASH = partition key","           }","       ],","       AttributeDefinitions = [","           {","               'AttributeName': 'email', # Name of the attribute","               'AttributeType': 'S'   # N = Number (B= Binary, S = String)","           }","       ],","ProvisionedThroughput={","           'ReadCapacityUnits'  : 10,","           'WriteCapacityUnits': 10","       }","   )","   return table"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["i"],"id":3},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["m"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["p"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["o"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["r"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":6},"action":"remove","lines":["import"],"id":4},{"start":{"row":0,"column":0},"end":{"row":0,"column":6},"action":"insert","lines":["import"]}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":[" "],"id":5},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["b"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["o"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["t"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["o"]}],[{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["3"],"id":6}],[{"start":{"row":0,"column":12},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["i"],"id":8},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["m"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["p"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["o"]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":4},"action":"remove","lines":["impo"],"id":9},{"start":{"row":1,"column":0},"end":{"row":1,"column":6},"action":"insert","lines":["import"]}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":[" "],"id":10},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["k"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["e"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["y"]}],[{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["_"],"id":11}],[{"start":{"row":1,"column":7},"end":{"row":1,"column":11},"action":"remove","lines":["key_"],"id":12},{"start":{"row":1,"column":7},"end":{"row":1,"column":17},"action":"insert","lines":["key_config"]}],[{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":[" "],"id":13},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["a"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":[" "],"id":14},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["k"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["e"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["y"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["s"]}],[{"start":{"row":1,"column":25},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":15},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["dynamodb = boto3.resource(","    'dynamodb',","    ACCESS_KEY_ID='AKIATKTAC7KRCPSE5S4W',","    ACCESS_SECRET_KEY='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',","    REGION_NAME='us-east-1',",")"],"id":16}],[{"start":{"row":26,"column":9},"end":{"row":27,"column":0},"action":"remove","lines":["",""],"id":17}],[{"start":{"row":26,"column":9},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":27,"column":0},"end":{"row":27,"column":7},"action":"insert","lines":["       "]}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"remove","lines":["",""],"id":19},{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"remove","lines":["'"],"id":20}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["k"],"id":21},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["e"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["y"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["s"]}],[{"start":{"row":5,"column":22},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":22},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["."]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"remove","lines":["    "],"id":23},{"start":{"row":5,"column":22},"end":{"row":6,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":44},"action":"remove","lines":["keys.AKIATKTAC7KRCPSE5S4W'"],"id":24},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["k"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":20},"action":"remove","lines":["ke"],"id":25},{"start":{"row":5,"column":18},"end":{"row":5,"column":22},"action":"insert","lines":["keys"]}],[{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["."],"id":26}],[{"start":{"row":5,"column":23},"end":{"row":5,"column":36},"action":"insert","lines":["ACCESS_KEY_ID"],"id":27}],[{"start":{"row":6,"column":22},"end":{"row":6,"column":64},"action":"remove","lines":["'8mdWMulnRXEORxY6lzFTmpbV6tPH9g5/hmpC1lMl'"],"id":28}],[{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":[" "],"id":29},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["k"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":23},"end":{"row":6,"column":25},"action":"remove","lines":["ke"],"id":30},{"start":{"row":6,"column":23},"end":{"row":6,"column":27},"action":"insert","lines":["keys"]}],[{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["."],"id":31}],[{"start":{"row":6,"column":28},"end":{"row":6,"column":45},"action":"insert","lines":["ACCESS_SECRET_KEY"],"id":32}],[{"start":{"row":7,"column":16},"end":{"row":7,"column":27},"action":"remove","lines":["'us-east-1'"],"id":33},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["k"]},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":16},"end":{"row":7,"column":18},"action":"remove","lines":["ke"],"id":34},{"start":{"row":7,"column":16},"end":{"row":7,"column":20},"action":"insert","lines":["keys"]}],[{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["."],"id":35}],[{"start":{"row":7,"column":21},"end":{"row":7,"column":32},"action":"insert","lines":["REGION_NAME"],"id":36}],[{"start":{"row":10,"column":0},"end":{"row":30,"column":15},"action":"remove","lines":["def create_table():","   table = dynamodb_resource.create_table(","       TableName = 'users', # Name of the table","       KeySchema = [","           {","               'AttributeName': 'email',","               'KeyType'      : 'HASH' #RANGE = sort key, HASH = partition key","           }","       ],","       AttributeDefinitions = [","           {","               'AttributeName': 'email', # Name of the attribute","               'AttributeType': 'S'   # N = Number (B= Binary, S = String)","           }","       ],","       ProvisionedThroughput={","           'ReadCapacityUnits'  : 10,","           'WriteCapacityUnits': 10","       }","   )","   return table"],"id":37}],[{"start":{"row":10,"column":0},"end":{"row":30,"column":15},"action":"insert","lines":["def create_table():","   table = dynamodb_resource.create_table(","       TableName = 'users', # Name of the table","       KeySchema = [","           {","               'AttributeName': 'email',","               'KeyType'      : 'HASH' #RANGE = sort key, HASH = partition key","           }","       ],","       AttributeDefinitions = [","           {","               'AttributeName': 'email', # Name of the attribute","               'AttributeType': 'S'   # N = Number (B= Binary, S = String)","           }","       ],","ProvisionedThroughput={","           'ReadCapacityUnits'  : 10,","           'WriteCapacityUnits': 10","       }","   )","   return table"],"id":38}],[{"start":{"row":30,"column":2},"end":{"row":30,"column":3},"action":"remove","lines":[" "],"id":39},{"start":{"row":30,"column":1},"end":{"row":30,"column":2},"action":"remove","lines":[" "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":[" "]},{"start":{"row":29,"column":4},"end":{"row":30,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":29,"column":4},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":40},{"start":{"row":30,"column":0},"end":{"row":30,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":24,"column":9},"end":{"row":25,"column":0},"action":"remove","lines":["",""],"id":41}],[{"start":{"row":24,"column":9},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":42},{"start":{"row":25,"column":0},"end":{"row":25,"column":7},"action":"insert","lines":["       "]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":43}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":48},"action":"insert","lines":["from flask import Flask, render_template,request"],"id":44}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"insert","lines":[","],"id":45}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"remove","lines":[","],"id":46}],[{"start":{"row":4,"column":0},"end":{"row":9,"column":1},"action":"remove","lines":["dynamodb = boto3.resource(","    'dynamodb',","    ACCESS_KEY_ID=keys.ACCESS_KEY_ID,","    ACCESS_SECRET_KEY= keys.ACCESS_SECRET_KEY,","    REGION_NAME=keys.REGION_NAME,",")"],"id":48},{"start":{"row":4,"column":0},"end":{"row":9,"column":1},"action":"insert","lines":["dynamodb_resource = boto3.resource(","    'dynamodb',","    #aws_access_key_id     = keys.ACCESS_KEY_ID,","    #aws_secret_access_key = keys.ACCESS_SECRET_KEY,","    region_name           = keys.REGION_NAME,",")"]}],[{"start":{"row":11,"column":0},"end":{"row":31,"column":15},"action":"remove","lines":["def create_table():","   table = dynamodb_resource.create_table(","       TableName = 'users', # Name of the table","       KeySchema = [","           {","               'AttributeName': 'email',","               'KeyType'      : 'HASH' #RANGE = sort key, HASH = partition key","           }","       ],","       AttributeDefinitions = [","           {","               'AttributeName': 'email', # Name of the attribute","               'AttributeType': 'S'   # N = Number (B= Binary, S = String)","           }","       ],","       ProvisionedThroughput={","           'ReadCapacityUnits'  : 10,","           'WriteCapacityUnits': 10","       }","   )","   return table"],"id":49},{"start":{"row":11,"column":0},"end":{"row":31,"column":15},"action":"insert","lines":["def create_table():","   table = dynamodb_resource.create_table(","       TableName = 'users', # Name of the table","       KeySchema = [","           {","               'AttributeName': 'email',","               'KeyType'      : 'HASH' #RANGE = sort key, HASH = partition key","           }","       ],","       AttributeDefinitions = [","           {","               'AttributeName': 'email', # Name of the attribute","               'AttributeType': 'S'   # N = Number (B= Binary, S = String)","           }","       ],","ProvisionedThroughput={","           'ReadCapacityUnits'  : 10,","           'WriteCapacityUnits': 10","       }","   )","   return table"]}],[{"start":{"row":25,"column":9},"end":{"row":26,"column":0},"action":"remove","lines":["",""],"id":50}],[{"start":{"row":25,"column":9},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":51},{"start":{"row":26,"column":0},"end":{"row":26,"column":7},"action":"insert","lines":["       "]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"remove","lines":["#"],"id":52}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"remove","lines":["#"],"id":53}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":48},"action":"remove","lines":["from flask import Flask, render_template,request"],"id":54},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["p"],"id":55},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["y"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["t"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["h"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["o"]}],[{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"remove","lines":["o"],"id":56},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"remove","lines":["h"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"remove","lines":["t"]},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":["y"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["p"]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["#"],"id":57}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["#"],"id":58}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":5},"end":{"row":6,"column":5},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":50,"mode":"ace/mode/python"}},"timestamp":1704377654580,"hash":"daee3c27ee8633f3da60e2d6c806b32adbb65dee"}