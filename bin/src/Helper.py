import os


def get_squema(path):
    db_squema_path = os.path.join(path, "bin", "assets", "database.sql")
    f = open(db_squema_path, "r")
    return f.read()
