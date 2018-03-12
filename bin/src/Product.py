class Product:
    """
    Product class
    Created to represent our table and display it later on
    """

    def __init__(self, id, name, price, category):
        """
        :param int id:  unique product id
        :param str name: unique name for product
        :param double price: price for product
        :param str category:
        """
        self.id = id
        self.name = name
        self.price = price
        self.category = category
