import mysql.connector

class General:

	def __init__(self):
		self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="toko")
		self.c = self.conn.cursor()

	def action(self, q):
		self.c.execute(q)
		self.conn.commit()


	def result(self, q):
		self.c.execute(q)
		data = self.c.fetchall()
		return data


	def row(self, q):
		self.c.execute(q)
		data = self.c.fetchone()
		return data


	def read(self, table):
		data = self.result("SELECT * FROM " + table)

		print(data)
		
		tb = {}
		i = 0
		for item in data:
			i += 1
			s = "%s" % i
			tb[s] = item

		return tb


	def read_id(self, table, id):
		key = [*id][0]
		data = self.row("SELECT * FROM " + table + " WHERE " + key + "=% s" % id[key])
		return data


	def insert(self, table, fields):
		key = ''
		val = ''
		n = 0
		for x, y in fields.items():
			if n > 0:
				key += ','
				val += ','

			key += x
			val += "'%s" % y + "'"
			
			n += 1

		self.action("INSERT INTO " + table + " (" + key + ")" + " VALUES (" + val + ")")


	def update(self, table, fields, id):
		data = ''
		for x, y in fields.items():
			data += x + "= '%s" % y + "' "

		key = [*id][0]

		self.action("UPDATE " + table + " SET " + data + "WHERE " + key + "=% s" % id[key])


	def delete(self, table, id):
		key = [*id][0]
		self.action("DELETE FROM " + table + " WHERE " + key + "=% s" % id[key])


crud = General()