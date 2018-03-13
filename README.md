# FLUENT CITY CODE CHALLENGE

## Challenge

#### Description:
We ask that you use Python. At Fluent City we use Django and Django Rest Framework but you are welcome to pick any 3rd party library you like.
Alternatively, if you prefer, you can roll your own implementation.

Create a small database for "products",
give each product 3 or so attributes in a related table,
and then provide URL's for updating all aspects of those objects.


```
Create
Read
Update
Delete
List
Search
(For Products:)
Add Attribute
Remove Attribute
```

#### Some Notes:

- 1) Make your main focus the Python/DB. You can consider
any front end work an optional added bonus.

- 2) Feel free to get as nuanced and detailed as you like when implementing the
"search" endpoint.

- 3) Using the web and openly available tutorials is encouraged.

- 4) If you have any questions, feel free to ask. Points are not deducted
for questions. Part of the exercise is to see how we communicate and if
we can be efficient.

- 5) Make sure to include unit tests. It's important to know there is attention
to detail in your work.

# Requisites

- Uses python v2.7
- Install python Flask framework.
- Install pymysql api to access to MySQL database.

# Project description

# How Front-end Works

- First of all we need to build the database.
- Then we need to populate the database, there are already predefine products to insert.
- You can drop the database whenever you need but you need to rebuild the database again if so.

- Then you can do any action if you want to manage the database.


# API Structure

### Asked

```
- API LINK                                          METHOD_TYPE         DESCRIPTION

- '/api/delete/<string:product_name>'               DELETE              Delete
- '/api/update/'                                    UPDATE              Update
- '/api/products/'                                  GET                 List
- '/api/create/'                                    POST                Create
- '/api/search/<string:product_name>'               GET                 Search
- '/api/read/<int:product_id>'                      GET                 Read
- '/api/add_attribute/'                             UPDATE              Add Attribute
- '/api/delete_attribute/<string:attribute_name>'   DELETE              Remove Attribute
```

### Extras

```
- API LINK                            METHOD_TYPE           DESCRIPTION

- '/api/get_attributes/'              GET                   Gets All attributes
- '/api/build_database/'              GET                   Build the database
- '/api/delete_database/'             GET                   Drops the database
- '/api/populate_database/'           GET                   Populate the database with random products
```