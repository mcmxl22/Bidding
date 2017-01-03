import sqlite3


class DataBase(object):

    def createdb(self):
        conn = sqlite3.connect('bid.db') 
        cursor = conn.cursor()
        sql = '''create table bid (
            Name text,
            Seniority int,
            Bidline int)'''
        cursor.execute(sql)
        cursor.close()

if __name__ == "__main__":
    bid = DataBase()
    bid.createdb()
