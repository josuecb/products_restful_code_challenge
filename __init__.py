import json
import os
import sys

import time
from flask import Flask, render_template, flash, request

app = Flask(__name__)

# Importing libraries from different path
sys.path.insert(0, os.path.join(app.root_path, "bin", "stc", "Connection.py"))
from DatabaseAccess import DatabaseAccess
import test


@app.route('/')
def homepage():
    t = str(int(round(time.time() * 1000)))
    print(t)
    return render_template("main.html", css=t)


@app.route('/api/products/', methods=['GET'])
def display_products():
    d = DatabaseAccess()
    result = d.list_all()
    return str(json.dumps(result))


@app.route('/api/delete/<string:product_name>', methods=['DELETE'])
def delete_product(product_name):
    if request.method == 'DELETE':
        if product_name is '':
            return "Product name is empty."

        print(product_name)

        d = DatabaseAccess()
        product_id = d.search_product_by_name(product_name)

        print("Deleting product with id: " + str(product_id[0]))

        if product_id is not None:
            d.delete_product(product_id[0])
            return "true"
        else:
            return "Product doesn't exist."

    return "false"


@app.route('/api/update/', methods=['UPDATE'])
def update_product():
    if request.method == 'UPDATE':
        if not request.form['product_id']:
            return "Specify product id."

        if not request.form['product_price']:
            price = None
        else:
            price = request.form['product_price']

        if not request.form['product_category']:
            category = None
        else:
            category = request.form['product_category']

        d = DatabaseAccess()
        d.update_product(
            request.form['product_id'],
            request.form['product_name'],
            price,
            category
        )

        return "Product updated!"


@app.route('/api/create/', methods=['POST'])
def create_product():
    if request.method == 'POST':
        d = DatabaseAccess()

        try:
            if not request.form['product_category']:
                category = None
            else:
                category = request.form['product_category']

            # Avoids empty values
            if request.form['product_name'] != '' and request.form['product_price'] != '':
                d.insert_product(request.form['product_name'], request.form['product_price'], category)
            else:
                return "Product Name or Price is Empty!"
        except Exception as e:
            print(e)

        return "Product created!"


@app.route('/api/search/<string:product_name>', methods=['GET'])
def search_product(product_name):
    # print(product_name)
    d = DatabaseAccess()
    product_id = d.search_product_by_name(product_name)
    if product_id is not None:
        data = d.get_product_data(product_id[0])
        return str(data)


@app.route('/api/read/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    d = DatabaseAccess()
    data = d.get_product_data(product_id)
    return str(data)


@app.route('/api/add_attribute/', methods=['UPDATE'])
def add_product_attribute():
    if request.method == 'UPDATE':
        d = DatabaseAccess()
        if request.form['attribute_name'] and request.form['attribute_description']:
            try:
                attribute_name = request.form['attribute_name']
                attribute_description = request.form['attribute_description']

                d.add_attribute(attribute_name, attribute_description)
            except Exception as e:
                print(e)

            return "Attribute added!"


@app.route('/api/delete_attribute/<string:attribute_name>', methods=['DELETE'])
def remove_product_attribute(attribute_name):
    if request.method == 'DELETE':
        d = DatabaseAccess()
        if attribute_name:
            try:
                d.remove_attribute(attribute_name)
            except Exception as e:
                print(e)

            return "Attribute added!"


@app.route('/api/get_attributes/', methods=['GET'])
def get_product_attributes():
    d = DatabaseAccess()
    return json.dumps(d.get_product_attributes())


@app.route('/api/build_database/', methods=['GET'])
def build_database():
    test.build_database()
    return "Database built."


@app.route('/api/delete_database/', methods=['GET'])
def drop_database():
    test.drop_database()
    return "Database dropped!."


@app.route('/api/populate_database/', methods=['GET'])
def populate_database():
    test.create_test_products()
    return "Database populated!."


if __name__ == "__main__":
    app.run()