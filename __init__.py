"""
    @author: Josue Carbonel
    @creation date:  3/12/2018
"""

import json
import os
import sys

import time
from flask import Flask, render_template, request

app = Flask(__name__)

# Importing libraries from different path
sys.path.insert(0, os.path.join(app.root_path, "bin", "stc", "Connection.py"))
from DatabaseQueries import DatabaseQueries
import test


# This is our home page for our code challenge.
@app.route('/')
def homepage():
    """
    I built just one page for our project where we have
    all the specific actions and buttons to get the job done

    I have built a simple UI to manage the database and
    access to our API
    :return:
    """
    t = str(int(round(time.time() * 1000)))
    print("Accessed time: " + t)
    # @param str t:  we will pass this argument to avoid permanent cache on CSS and JS files
    # so we will append this time to our CSS and JS link
    return render_template("main.html", t=t)


# Get a list with all product data
@app.route('/api/products/', methods=['GET'])
def display_products():
    """
    List in json string
    :return dictionary: list of all products as json
    """
    d = DatabaseQueries()
    result = d.list_all()
    return str(json.dumps(result))


# Deletes the product with specific product name
@app.route('/api/delete/<string:product_name>', methods=['DELETE'])
def delete_product(product_name):
    if request.method == 'DELETE':
        # avoids an empty entry
        if product_name is '':
            return "Product name is empty."

        print(product_name)

        d = DatabaseQueries()
        product_id = d.search_product_by_name(product_name)

        print("Deleting product with id: " + str(product_id[0]))

        if product_id is not None:
            d.delete_product(product_id[0])
            return "true"
        else:
            return "Product doesn't exist."

    return "false"


# Updates the product by specifying the id of the product
@app.route('/api/update/', methods=['UPDATE'])
def update_product():
    if request.method == 'UPDATE':
        # avoids empty id
        if not request.form['product_id']:
            return "Specify product id."

        # Make price optional to modify if empty
        if not request.form['product_price']:
            price = None
        else:
            price = request.form['product_price']

        # make category optional to modify if empty
        if not request.form['product_category']:
            category = None
        else:
            category = request.form['product_category']

        d = DatabaseQueries()
        d.update_product(
            request.form['product_id'],
            request.form['product_name'],
            price,
            category
        )

        return "Product updated!"


# Creates or Inserts the product
@app.route('/api/create/', methods=['POST'])
def create_product():
    if request.method == 'POST':
        d = DatabaseQueries()

        try:
            # make category optional to modify if empty
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


# search the product by the specific name, if it doesn't exist it will return nothing
@app.route('/api/search/<string:product_name>', methods=['GET'])
def search_product(product_name):
    # print(product_name)
    d = DatabaseQueries()
    product_id = d.search_product_by_name(product_name)
    if product_id is not None:
        data = d.get_product_data(product_id[0])
        return str(data)


# Read, searches the product by the the product id, if it doesn't exist it will return nothing
@app.route('/api/read/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    d = DatabaseQueries()
    data = d.get_product_data(product_id)
    return str(data)


# Inserts an extra attribute on our product table
@app.route('/api/add_attribute/', methods=['UPDATE'])
def add_product_attribute():
    if request.method == 'UPDATE':
        d = DatabaseQueries()
        if request.form['attribute_name'] and request.form['attribute_description']:
            try:
                attribute_name = request.form['attribute_name']
                attribute_description = request.form['attribute_description']

                d.add_attribute(attribute_name, attribute_description)
            except Exception as e:
                print(e)

            return "Attribute added!"


# Deletes an attribute from our product table
@app.route('/api/delete_attribute/<string:attribute_name>', methods=['DELETE'])
def remove_product_attribute(attribute_name):
    # Avoids to remove key attributes, it would break the whole api if one of them is deleted
    # only extra attributes will be able to be deleted
    if attribute_name is 'id' \
            or attribute_name is 'category' \
            or attribute_name is 'timestamp' \
            or attribute_name is 'name' \
            or attribute_name is 'price':
        return "This attributes are not removable."

    if request.method == 'DELETE':
        d = DatabaseQueries()
        if attribute_name:
            try:
                d.remove_attribute(attribute_name)
            except Exception as e:
                print(e)

            return "Attribute added!"


# This gets all existing attributes in our product table
@app.route('/api/get_attributes/', methods=['GET'])
def get_product_attributes():
    d = DatabaseQueries()
    return json.dumps(d.get_product_attributes())


# This builds our database
@app.route('/api/build_database/', methods=['GET'])
def build_database():
    test.build_database()
    return "Database built."


# Drops the database
@app.route('/api/delete_database/', methods=['GET'])
def drop_database():
    test.drop_database()
    return "Database dropped!."


# Populates the database with dumb data
@app.route('/api/populate_database/', methods=['GET'])
def populate_database():
    test.create_test_products()
    return "Database populated!."


if __name__ == "__main__":
    app.run()
