import sqlite3


def remove_bid():

    conn = sqlite3.connect('Bid.db')
    cursor = conn.cursor()

    while True:
        print('Enter name to be deleted.')
        choice1 = raw_input('\n> ')
		
        sql = '''delete from Bid...'''

        cursor.execute(sql)

        conn.commit()
        cursor.close()


def choice():
    print('Delete bid?')
	
    answer = ('yes', 'no')

    for a in answer:
        print('\n%s' % a)
    choice1 = raw_input('\n> ')
    if choice1 == answer[0]:
        remove_bid()
    elif choice1 == answer[1]:
        choice()

if __name__ == "__main__":
    choice()
