"""
    @author: Josue Carbonel
    @creation date:  3/12/2018
"""
import time

from Connection import Connection


class DatabaseQueries:
    """
        DatabaseQueries class
        This class helps us to make queries to our database.
        (e.i: update, read, search, insert, delete products)
    """

    # This is our constructor which will initialize with a connection
    def __init__(self):
        self.c = Connection()
        self.conn = self.c.db_connect()

    # Update product's categories if it doesn't exist it will insert it
    def update_product_category(self, where_product_id, new_category_id):
        if self.c is not None:
            cur = self.conn.cursor()
            # use our database
            cur.execute("USE " + self.c.DATABASE + ";")

            product_category = self.get_product_category(where_product_id)

            # if it doesn't exist then insert it
            if product_category is None:
                q = "INSERT INTO products_by_category SET category_id='" + str(new_category_id) + "', product_id='" + \
                    str(where_product_id) + "';"
            else:
                # otherwise update it
                q = "UPDATE products_by_category SET category_id='" + str(new_category_id) + "' WHERE product_id='" + \
                    str(where_product_id) + "';"

            print(q)
            cur.execute(q)
            self.conn.commit()

    # Gets all product table column names (fields)
    def get_product_attributes(self):
        cur = self.conn.cursor()
        cur.execute("USE " + self.c.DATABASE + ";")
        # Query to get all fields in our product table
        q = "SHOW FIELDS FROM products;"
        # print(q)
        cur.execute(q)
        self.conn.commit()

        attrs = []
        data = cur.fetchall()

        # transfer it in an array
        if data is not None:
            # print(data)
            for i in data:
                if len(i[0]) > 0:
                    attrs += [i[0]]
        return attrs

    # Deletes the product category
    def delete_product_category(self, product_id):
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "DELETE FROM products_by_category WHERE product_id='" + str(product_id) + "';"

            # print(q)
            cur.execute(q)
            self.conn.commit()

    # Finds category by name
    def find_category_by_name(self, category_name):
        """
        :param string category_name:
        :return int: returns the category id
        """
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "SELECT id FROM category WHERE name LIKE '%" + str(category_name) + "%';"

            # print(q)
            cur.execute(q)
            return cur.fetchone()

    # Gets the product category according to specific product
    def get_product_category(self, where_product_id):
        """
        :param int where_product_id: specify the product id
        :return str: returns the category name
        """
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "SELECT category.name FROM products_by_category JOIN category ON " \
                "products_by_category.category_id=category.id WHERE products_by_category.product_id='" + \
                str(where_product_id) + "';"

            # print(q)
            cur.execute(q)
            return cur.fetchone()

    # Inserts a new category into our category table
    def insert_category(self, category_name):
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "INSERT INTO " + self.c.DATABASE + ".category SET name='" + str(category_name) + "';"

            # print(q)
            cur.execute(q)
            self.conn.commit()

    # Inserts or creates a new product inside our product table, adding category name is optional
    def insert_product(self, product_name, price, category_name=None, extraAttr=None):
        # TODO: extra attributes is not implemented yet but in the future. (lack of time)
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "INSERT INTO " + self.c.DATABASE + ".products SET name='" + str(product_name) + "', price='" + str(
                price) + \
                "', timestamp='" + str(int(round(time.time() * 1000))) + "';"

            # print(q)
            cur.execute(q)
            self.conn.commit()

            # if category name is specified then we need to find the product id and category id
            # to insert it into our relational table
            if category_name is not None:
                product_id = self.search_product_by_name(product_name)[0]
                category_id = self.find_category_by_name(category_name)[0]
                self.update_product_category(product_id, category_id)

    # This gets the product data according to specific product
    def get_product_data(self, product_id):
        """
        :param int product_id: specific product id
        :return dict:  returns a dictionary object with the specific data of the product
        """
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "SELECT * FROM products WHERE id='" + str(product_id) + "';"

            # print(q)
            cur.execute(q)
            data = cur.fetchone()
            json = dict()

            # Creates the dictionary (json)
            if data is not None:
                json['id'] = data[0]
                json['name'] = data[1]
                json['price'] = data[2]
                json['timestamp'] = data[3]

                # search for the category if exists
                category = self.get_product_category(product_id)
                if category is not None:
                    json['category'] = self.get_product_category(product_id)[0]
                else:
                    json['category'] = "null"

            return json
            # for r in cur:
            #     print(r)

    # Update existing product from product table
    def update_product(self, where_product_id, new_name, new_price=None, new_category=None):
        """
        :param int where_product_id: specific product id
        :param str new_name: new name for our product
        :param str new_price: (optional) new price for our product
        :param str new_category: (optional)
        :return:
        """
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")

            q = "UPDATE products SET name='" + new_name + "', timestamp='" + str(int(round(time.time() * 1000))) + "'"

            if new_price is not None:
                q += ", price='" + str(new_price) + "'"

            q += " WHERE id='" + str(where_product_id) + "';"

            print(q)
            cur.execute(q)
            self.conn.commit()

            # if category is not null then insert it
            if new_category is not None:
                new_cat_id = self.find_category_by_name(new_category)
                if new_category is not None:
                    self.update_product_category(where_product_id, new_cat_id[0])
                else:
                    print("Category doesn't exist")

            # cur.execute(q)
            # self.conn.commit()

    # This deletes product from our product table
    def delete_product(self, product_id):
        """
        :param int product_id: specific product id
        :return:
        """
        self.delete_product_category(product_id)

        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "DELETE FROM products WHERE id='" + str(product_id) + "';"

            # print(q)
            cur.execute(q)
            self.conn.commit()

    # Gets the product list
    def list_all(self):
        """
        :return dictionary: Returns a dictionary object with all product's data
        """
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            # Gets all ids first for all the products in our database
            q = "SELECT id FROM products"
            # print(q)
            cur.execute(q)

            items = []

            # loop ids to select each one
            for id in cur:
                if not id:
                    pass
                else:
                    items.insert(0, self.get_product_data(id[0]))  # gets the product data

            return items

    # This methos will search the product by name
    # This is basically a simple sql search query
    # TODO: I think it would be better if we had a filter method. But the time was not good to make it and test it
    def search_product_by_name(self, product_name):
        """
        :param str product_name: product name to find
        :return int: the id of the product if exists
        """
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "SELECT id FROM products WHERE name LIKE '%" + str(product_name) + "%';"

            # print(q)
            cur.execute(q)
            return cur.fetchone()

    # Inserts new Attribute for our table
    def add_attribute(self, attr_name, attr_def):
        """
        :param str attr_name: new attribute name
        :param str attr_def: this must be a valid variable type rule according to mysql (e.i: VARCHAR, TEXT, INT, etc)
        :return:
        """
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "ALTER TABLE products ADD COLUMN " + attr_name + " " + attr_def + " AFTER TIMESTAMP;"

            # print(q)
            cur.execute(q)
            self.conn.commit()

    # Deletes the attribute if exists
    def remove_attribute(self, attr_name):
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "ALTER TABLE products DROP COLUMN " + attr_name + ";"

            # print(q)
            cur.execute(q)
            self.conn.commit()
