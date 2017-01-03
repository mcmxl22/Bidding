import sqlite3


conn = sqlite3.connect('Bid.db')
cursor = conn.cursor()
who = {1: 'Micah C McConnaughey', 2: 'name2', 3: 'name3'}


def bid():

    ask = raw_input('Name? ')

    if ask == who[1]:
        results = cursor.execute("SELECT * FROM Bid WHERE names = (%s, %s, %s)"
                                 ('Micah C McConnaughey', 'name2', 'name3'))
        names = results.fetchall()
        print (names)
		
if __name__ == "__main__":
    bid()
