"""
    @author: Josue Carbonel
    @creation date:  3/12/2018
"""

import json
import os
import sys
from flask import Flask, render_template, flash

app = Flask(__name__)

# Importing libraries from different path
sys.path.insert(0, os.path.join(app.root_path, "bin", "stc", "Connection.py"))
from DatabaseAccess import DatabaseQueries
from Connection import Connection


def build_database():
    c = Connection()
    c.re_build_database(app.root_path)


def drop_database():
    c = Connection()
    c.drop_database()


def create_test_products():
    d = DatabaseQueries()
    try:
        d.insert_product("banana", 1.88, "food")
    except Exception as e:
        print(e)

    try:
        d.insert_product("stove", 245.99, "kitchen")
    except Exception as e:
        print(e)

    try:
        d.insert_product("JBL speakers", 150.19, "electronics")
    except Exception as e:
        print(e)

    try:
        d.insert_product("gold necklace", 29.33, "luxury")
    except Exception as e:
        print(e)

    try:
        d.insert_product("blue cotton t-shirt", 9.99, "handmade")
    except Exception as e:
        print(e)


def read_test():
    d = DatabaseQueries()
    print(d.get_product_data(d.search_product_by_name("blue cotton t-shirt")[0]))
    print(d.get_product_data(d.search_product_by_name("gold necklace")[0]))
    print(d.get_product_data(d.search_product_by_name("stove")[0]))
    print(d.get_product_data(d.search_product_by_name("JBL speakers")[0]))
    print(d.get_product_data(d.search_product_by_name("banana")[0]))


def add_default_categories():
    d = DatabaseQueries()
    d.insert_category("electronics")
    d.insert_category("food")
    d.insert_category("handmade")
    d.insert_category("luxury")
    d.insert_category("kitchen")


def update_test():
    d = DatabaseQueries()

    d.update_product(6, "strawberry", 2.10, "food")


def search_test():
    d = DatabaseQueries()
    print(d.search_product_by_name("strawb"))


def get_all_products():
    d = DatabaseQueries()
    print(json.dumps(d.list_all()))


def add_product_attribute():
    d = DatabaseQueries()
    d.add_attribute("joder", "VARCHAR(100)")


def remove_product_attribute():
    d = DatabaseQueries()
    try:
        d.remove_attribute("joder")
    except Exception as e:
        print(e)
    try:
        d.remove_attribute("phone")
    except Exception as e:
        print(e)
    try:
        d.remove_attribute("phone2")
    except Exception as e:
        print(e)


def get_attributes():
    d = DatabaseQueries()
    print(d.get_product_attributes())


if __name__ == '__main__':
    get_attributes()
    # create_test_products()
