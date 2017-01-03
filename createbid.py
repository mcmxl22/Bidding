import sqlite3


class bid(object):

    def createbd(self):

        conn = sqlite3.connect('Bid.db')
        cursor = conn.cursor()

        while True:
            Name = raw_input('Employee\'s name: ')
            Seniority = raw_input('Employee\'s seniority: ')
            BidLine = raw_input('Employee\'s bid: ')
            sql = '''insert into Bid
                       (Name, Seniority, BidLine)
                       values
                       (:em_Name, :em_Seniority, :em_BidLine)''' 
            cursor.execute(sql,
                           {'em_Name': Name,
                            'em_Seniority': Seniority,
                            'em_BidLine': BidLine})
            conn.commit()
            cont = raw_input('Another Employee? ')
            if cont[0].lower() == 'n':
                break
        cursor.close()

if __name__ == "__main__":
    bid = bid()
    bid.createbd()
