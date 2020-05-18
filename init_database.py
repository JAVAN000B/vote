from project import db

def init_database():
    db.create_all()

init_database()
