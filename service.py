from model import Data

def list():
    dt = Data()
    values = ()
    query = "select * from accounts"
    return dt.get_data(query, values)

def get_by_id(id):
    dt = Data()
    query = "select * from accounts where account_id = %s"
    values = (id,)
    return dt.get_data(query, values)

def create(input):
    dt = Data()
    try:
        username = input["username"]
        password = input["password"]
        email = input["email"]

        query = "insert into accounts (username, password, email) values (%s,%s,%s)"
        values = (username,password,email,)
        dt.insert_data(query, values)
    except Exception as e:
        e.with_traceback()

def update(id, input):
    dt = Data()
    values = ()
    try:
        values += (id,)
        query = "update accounts set account_id = %s "
        
        if "username" in input:
            username = input['username']
            values += (username, )
            query += ", username = %s"
        if "password" in input:    
            password = input['password']
            values += (password, )
            query += ", password = %s"
        if "email" in input:        
            email = input['email']
            values += (email, )
            query += ", email = %s"

        query += " where account_id = %s "
        values += (id,)
        dt.insert_data(query, values)
    except Exception as e:
        e.with_traceback()

def delete(id):
    dt = Data()
    try:
        query = "delete from accounts where account_id = %s"
        values = (id,)
        dt.insert_data(query, values)
    except Exception as e:
        e.with_traceback()
