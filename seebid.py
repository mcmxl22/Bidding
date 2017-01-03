import sqlite3


def seebid():
    # defines variable conn.
    conn = sqlite3.connect('Bid.db')

    # defines variable cursor.
    cursor = conn.cursor()

    # defines variable sql as an SQLite command.
    sql = '''select * from bid'''

    # defines variable results.
    results = cursor.execute(sql)

    # defines variable all_employees.
    all_employees = results.fetchall()

    # for-loop to print contents of variable all_employees.
    for employee in all_employees:
        print employee

if __name__ == "__main__":
    seebid()
