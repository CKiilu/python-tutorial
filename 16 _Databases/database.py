#!/usr/bin/python3

import sqlite3

def main():
	db = sqlite3.connect('files.db')

	db.row_factory = sqlite3.Row

	db.execute('drop table if exists files')
	db.execute('create table files (t1 text, i1 int)')
	db.execute('insert into files(t1, i1) values (?, ?)',('one', 1))
	db.execute('insert into files(t1, i1) values (?, ?)',('two', 2))
	db.execute('insert into files(t1, i1) values (?, ?)',('three', 3))
	db.commit()
	db.close

	cursor = db.execute('select i1, t1 from files order by i1')
	for row in cursor:
		print(dict(row))
		print(row['t1'], row['i1'])

if __name__ == "__main__":
	main()