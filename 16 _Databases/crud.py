#!/usr/bin/python3
import sqlite3

def main:
	db = sqlite3.connect('trial.db')
	db.row_Factory = sqlite3.row_Factory
	print("Create test table")
	db.execute('drop table if exists trial')
	db.execute('create table trial (t1 text, i1 int)')

	print("Create rows")
	insert(db, dict(t1 = 'one', i1 = 1))
	insert(db, dict(t1 = 'two', i1 = 2))
	insert(db, dict(t1 = 'three', i1 = 3))
	insert(db, dict(t1 = 'four', i1 = 4))
	disp_rows(db)

if __name__ == "__main__":
	main()