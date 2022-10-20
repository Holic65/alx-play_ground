#!/usr/bin/python3
'''
    a script that takes in an argument and displays all
    values in the table that matches the argument
'''
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    state_name = sys.argv[4]
    sql = ("SELECT * FROM states WHERE states.name = '%s' ORDER BY states.id" % (state_name))
    cur.execute(sql)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
