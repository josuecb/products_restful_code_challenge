import time

from Connection import Connection


class DatabaseAccess:
    def __init__(self):
        self.c = Connection()
        self.conn = self.c.db_connect()

    def update_product_category(self, where_product_id, new_category_id):
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")

            product_category = self.get_product_category(where_product_id)
            if product_category is None:
                q = "INSERT INTO products_by_category SET category_id='" + str(new_category_id) + "', product_id='" + \
                    str(where_product_id) + "';"
            else:
                q = "UPDATE products_by_category SET category_id='" + str(new_category_id) + "' WHERE product_id='" + \
                    str(where_product_id) + "';"

            print(q)
            cur.execute(q)
            self.conn.commit()

    def get_product_attributes(self, ):
        cur = self.conn.cursor()
        cur.execute("USE " + self.c.DATABASE + ";")
        q = "SHOW FIELDS FROM products;"
        # print(q)
        cur.execute(q)
        self.conn.commit()

        attrs = []
        data = cur.fetchall()

        if data is not None:
            # print(data)
            for i in data:
                if len(i[0]) > 0:
                    attrs += [i[0]]
        return attrs

    def delete_product_category(self, product_id):
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "DELETE FROM products_by_category WHERE product_id='" + str(product_id) + "';"

            # print(q)
            cur.execute(q)
            self.conn.commit()

    def find_category_by_name(self, category_name):
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "SELECT id FROM category WHERE name LIKE '%" + str(category_name) + "%';"

            # print(q)
            cur.execute(q)
            return cur.fetchone()

    def get_product_category(self, where_product_id):
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "SELECT category.name FROM products_by_category JOIN category ON " \
                "products_by_category.category_id=category.id WHERE products_by_category.product_id='" + \
                str(where_product_id) + "';"

            # print(q)
            cur.execute(q)
            return cur.fetchone()

    def insert_category(self, category_name):
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "INSERT INTO fluent_city.category SET name='" + str(category_name) + "';"

            # print(q)
            cur.execute(q)
            self.conn.commit()

    def insert_product(self, product_name, price, category_name=None, extraAttr=None):
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "INSERT INTO fluent_city.products SET name='" + str(product_name) + "', price='" + str(price) + \
                "', timestamp='" + str(int(round(time.time() * 1000))) + "';"

            # print(q)
            cur.execute(q)
            self.conn.commit()

            if category_name is not None:
                product_id = self.search_product_by_name(product_name)[0]
                category_id = self.find_category_by_name(category_name)[0]
                self.update_product_category(product_id, category_id)

    def get_product_data(self, product_id):
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "SELECT * FROM products WHERE id='" + str(product_id) + "';"

            # print(q)
            cur.execute(q)
            data = cur.fetchone()
            json = dict()
            if data is not None:
                json['id'] = data[0]
                json['name'] = data[1]
                json['price'] = data[2]
                json['timestamp'] = data[3]

                category = self.get_product_category(product_id)
                if category is not None:
                    json['category'] = self.get_product_category(product_id)[0]
                else:
                    json['category'] = "null"

            return json
            # for r in cur:
            #     print(r)

    def update_product(self, where_product_id, new_name, new_price=None, new_category=None):
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

            if new_category is not None:
                new_cat_id = self.find_category_by_name(new_category)
                if new_category is not None:
                    self.update_product_category(where_product_id, new_cat_id[0])
                else:
                    print("Category doesn't exist")

            # cur.execute(q)
            # self.conn.commit()

    def delete_product(self, product_id):
        self.delete_product_category(product_id)

        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "DELETE FROM products WHERE id='" + str(product_id) + "';"

            # print(q)
            cur.execute(q)
            self.conn.commit()

    def list_all(self):
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "SELECT id FROM products"
            # print(q)
            cur.execute(q)

            items = []

            for id in cur:
                if not id:
                    pass
                else:
                    items.insert(0, self.get_product_data(id[0]))

            return items

    def search_product_by_name(self, product_name):
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "SELECT id FROM products WHERE name LIKE '%" + str(product_name) + "%';"

            # print(q)
            cur.execute(q)
            return cur.fetchone()

    def add_attribute(self, attr_name, attr_def):
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "ALTER TABLE products ADD COLUMN " + attr_name + " " + attr_def + " AFTER TIMESTAMP;"

            # print(q)
            cur.execute(q)
            self.conn.commit()

    def remove_attribute(self, attr_name):
        if self.c is not None:
            cur = self.conn.cursor()
            cur.execute("USE " + self.c.DATABASE + ";")
            q = "ALTER TABLE products DROP COLUMN " + attr_name + ";"

            # print(q)
            cur.execute(q)
            self.conn.commit()
