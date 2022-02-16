import mysql.connector
from flask import Flask, request, abort, jsonify, Response, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from datetime import datetime

now = datetime.now()
app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

mydb = mysql.connector.connect(
       host="localhost",
       user="Hannes",
       password="Hannes",
       database="Warehouse"
        )

@app.route('/products/<int:_id>', methods=['DELETE','GET', 'PUT'])
def products(_id):
    mycursor = mydb.cursor()
    if request.method == 'DELETE':
        mycursor.execute( "DELETE FROM products WHERE product_id = %s",[_id])
        mydb.commit()
        return Response("", status=200, mimetype='application/json')
    elif request.method == 'GET':
        print("execiute!")
        mycursor.execute("SELECT * FROM products WHERE product_id = %s",[_id])
        print("executed")
        products = mycursor.fetchone()
        json_products = jsonify(products)
        return make_response(json_products, 200)
    else:
        json = request.get_json()
        price = json['price']
        amount = json['amount']
        mycursor.execute("UPDATE products SET price = %s, amount = %s WHERE product_id = %s", (price, amount, _id))
        mydb.commit()
        return Response("", status=200, mimetype='application/json')


@app.route('/products_', methods=['POST', 'GET'])
def products_():
    mycursor = mydb.cursor()
    if request.method == 'POST':
        json = request.get_json()
        product_name = json['product_name']
        price = json['price']
        amount = json['amount']
        mycursor.execute( "INSERT INTO products (product_name, price, amount) VALUES (%s, %s, %s)", (product_name, price, amount))
        mydb.commit()
        fetch = mycursor.fetchall()
        return jsonify(fetch) and Response("", status=201, mimetype='application/json')
    else:
        request.method == 'GET'
        print("execiute!")
        mycursor.execute("SELECT * FROM products")
        print("executed")
        customer = mycursor.fetchall()
        json_customer = jsonify(customer)
        return make_response(json_customer, 200)
 





# Använd denna kod
@app.route('/customers/<int:_id>', methods=['DELETE','GET', 'PUT'])
def customers(_id):
    mycursor = mydb.cursor()
    if request.method == 'DELETE':
        mycursor.execute( "DELETE FROM customers WHERE customer_id = %s",[_id])
        mydb.commit()
        return Response("", status=200, mimetype='application/json')
    elif request.method == 'GET':
        mycursor.execute("SELECT * FROM customers WHERE customer_id = %s",[_id])
        customer = mycursor.fetchone()
        json_customer = jsonify(customer)
        return make_response(json_customer, 200)
    else:
        json = request.get_json()
        age = json['age']
        mycursor.execute ("UPDATE customers SET age  = %s WHERE customer_id = %s", (age, _id))
        mydb.commit()
        return Response("", status=200, mimetype='application/json')

    

@app.route('/customers_', methods=['POST', 'GET'])
def customers_():
    mycursor = mydb.cursor()
    if request.method == 'POST':
        json = request.get_json()
        first_name = json['first_name']
        last_name = json['last_name']
        adress = json['adress']
        postal_code = json['postal_code']
        mycursor.execute( "INSERT INTO customers (first_name, last_name, adress, postal_code) VALUES (%s, %s, %s, %s)", (first_name, last_name, adress, postal_code))
        mydb.commit()
        fetch = mycursor.fetchall()
        print(first_name, last_name, adress, postal_code)
        return jsonify(fetch) and Response("", status=201, mimetype='application/json')
    else:
        request.method == 'GET'
        print("execiute!")
        mycursor.execute("SELECT * FROM customers")
        print("executed")
        customer = mycursor.fetchall()
        json_customer = jsonify(customer)
        return make_response(json_customer, 200)
   

@app.route('/staff/<int:_id>', methods=['DELETE','GET', 'PUT'])
def staff(_id):
    mycursor = mydb.cursor()
    if request.method == 'DELETE':
        mycursor.execute( "DELETE FROM staff WHERE staff_id = %s",[_id])
        mydb.commit()
        return Response("", status=200, mimetype='application/json')
    elif request.method == 'GET':
        mycursor.execute("SELECT * FROM staff WHERE staff_id = %s",[_id])
        customer = mycursor.fetchone()
        json_customer = jsonify(customer)
        return make_response(json_customer, 200)
    else:
        json = request.get_json()
        last_name = json['last_name']
        mycursor.execute ("UPDATE staff SET last_name = %s WHERE staff_id = %s", (last_name, _id))
        mydb.commit()
        return Response("", status=200, mimetype='application/json')


@app.route('/staff_', methods=['POST', 'GET'])
def staff_():
    mycursor = mydb.cursor()
    if request.method == 'POST':
        json = request.get_json()
        first_name = json['first_name']
        last_name = json['last_name']
        employee_since = json['employee_since']
        age = json['age']
        mycursor.execute( "INSERT INTO staff (first_name, last_name, employee_since, age) VALUES (%s, %s, %s, %s)", (first_name, last_name, employee_since, age))
        mydb.commit()
        fetch = mycursor.fetchall()
        print(first_name, last_name, employee_since, age)
        return jsonify(fetch) and Response("", status=201, mimetype='application/json')
    else:
        request.method == 'GET'
        mycursor.execute("SELECT * FROM staff")
        customer = mycursor.fetchall()
        json_customer = jsonify(customer)
        return make_response(json_customer, 200)


#En parameter

@app.route('/orders/<int:_id>', methods=['DELETE','GET', 'PUT'])
def orders(_id):
    mycursor = mydb.cursor()
    if request.method == 'DELETE':
        mycursor.execute( "DELETE FROM staff WHERE staff_id = %s",[_id])
        mydb.commit()
        return Response("", status=200, mimetype='application/json')
    elif request.method == 'GET':
        mycursor.execute("SELECT * FROM orders WHERE product_id = %s",[_id])
        order = mycursor.fetchall()
        json_order = jsonify(order)
        return make_response(json_order, 200)
    else:
        json = request.get_json()
        last_name = json['last_name']
        mycursor.execute ("UPDATE staff SET last_name = %s WHERE staff_id = %s", (last_name, _id))
        mydb.commit()
        return Response("", status=200, mimetype='application/json')


@app.route('/orders_', methods=['POST', 'GET'])
def orders_():
    mycursor = mydb.cursor()
    if request.method == 'POST':
        json = request.get_json()
        product_id = json['product_id']
        customer_id = json['customer_id']
        staff_id = json['staff_id']
        mycursor.execute( "INSERT INTO orders (product_id, customer_id, staff_id) VALUES (%s, %s, %s)", (product_id, customer_id, staff_id))
        mydb.commit()
        fetch = mycursor.fetchall()
        print(product_id, customer_id, staff_id)
        return jsonify(fetch) and Response("", status=201, mimetype='application/json')
    else:
        request.method == 'GET'
        mycursor.execute("SELECT * FROM orders")
        customer = mycursor.fetchall()
        json_customer = jsonify(customer)
        return make_response(json_customer, 200)
 


@app.route('/more_orders/<int:_id>/<int:_id2>', methods=['DELETE','GET', 'PUT'])
def more_orders(_id, _id2):
    mycursor = mydb.cursor()
    if request.method == 'DELETE':
        mycursor.execute( "DELETE FROM staff WHERE staff_id = %s",[_id])
        mydb.commit()
        return Response("", status=200, mimetype='application/json')
    elif request.method == 'GET':
        mycursor.execute("SELECT * FROM orders WHERE product_id = %s AND customer_id = %s",[_id, _id2])
        order = mycursor.fetchall()
        print (order)
        json_order = jsonify(order)
      #  print (json_order)
       # return make_response(json_order, 200)
        return make_response(json_order)
    else:
        json = request.get_json()
        last_name = json['last_name']
        mycursor.execute ("UPDATE staff SET last_name = %s WHERE staff_id = %s", (last_name, _id))
        mydb.commit()
        return Response("", status=200, mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True)
