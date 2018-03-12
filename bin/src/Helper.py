"""
    @author: Josue Carbonel
    @creation date:  3/12/2018
"""
import os


def get_squema(root_path):
    """
    :param str root_path: specify the root path of the project
    :return str: the asset path
    """
    db_squema_path = os.path.join(root_path, "bin", "assets", "database.sql")
    print("Squema path: " + str(db_squema_path))
    f = open(db_squema_path, "r")
    return f.read()
