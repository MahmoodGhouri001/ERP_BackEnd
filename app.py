from flask import Flask, redirect, url_for, request
import json
import pymysql
import pandas as pd
import uuid

app = Flask(__name__)


@app.route('/health_check', methods=['GET','POST'])
def health_check():
   return "Running!",200

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

def create_db_connection():
    try:
        connection = pymysql.connect(host='localhost',user='root',password='admin',database='master_db')
        cursor = connection.cursor()
        if connection:
            return connection,cursor
        else:
            print("Connection failed")
    except Exception as e:
        print("Exception while creating connection with DB",e)

@app.route('/get_all',methods = ['POST', 'GET'])
def get_records():

    _,cursor = create_db_connection()
    sql_query = 'select * from notes'
    cursor.execute(sql_query)
    result = cursor.fetchall()
    #connection.close()
    final_list = []
    for each in result:
        all_records = {}
        all_records['notes_id'] = each[0]
        all_records['notes_title'] = each[1]
        all_records['notes_desc'] = each[2]
        final_list.append(all_records)

    return json.dumps(final_list)

from init import branch
@app.route('/add_branch',methods = ['POST'])
def insert_record():
    if request.method == 'POST':
        request_data = request.get_json()
        brn = branch()
        branch_id = brn.add_branch(request_data)

        return ("successfully branch created with branch id : {}".format(branch_id),200)
    else:
        return 'request method is other than post'

@app.route('/alter_record',methods = ['POST'])
def alter_record():
    if request.method == 'POST':
        request_data = request.get_json()
        notes_id = request_data['notes_id']
        title = request_data['notes_title']
        desc = request_data['notes_desc']
        connection, cursor = create_db_connection()
        sql_query = "UPDATE notes SET notes_title = '{}', notes_desc = '{}' WHERE notes_id = '{}'".format(title,desc,notes_id);
        cursor.execute(sql_query)
        connection.commit()
        return "successfully updated!",200

@app.route('/delete_record',methods = ['POST'])
def delete_record():
    if request.method == 'POST':
        request_data = request.get_json()
        notes_id = request_data['notes_id']
        connection, cursor = create_db_connection()
        sql_query = "DELETE FROM notes WHERE notes_id='{}';".format(notes_id);
        cursor.execute(sql_query)
        connection.commit()
        return "successfully deleted!",200


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)