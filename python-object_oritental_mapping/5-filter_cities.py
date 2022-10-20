#!/usr/bin/python3
'''
    A script that takes name of a stae and list
    all cities of that state, using the database hbtn_0e_4_usa
'''
import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) == 5:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3])
        cur = db.cursor()
        state_name = sys.argv[4]
        cur.execute("""SELECT cities.name FROM cities RIGHT JOIN states ON \
                     cities.state_id = states.id WHERE states.name = %s""", (state_name,))
        state = cur.fetchall()
        print(", ".join(city[0] for city in state))
        cur.close()
        db.close()
