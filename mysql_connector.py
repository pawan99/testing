import pymysql
from pymysql import MySQLError
# from mysql.connector import MySQLConnection, Error, errors
from db_config import main_db_config

class PyMYSQLDBConn(object):
	"""docstring for PyMYSQLDBConn"""
	def __init__(self, db_conn=main_db_config):
		super(PyMYSQLDBConn, self).__init__()
		self.db_conn = db_conn
		try:
			self.connection = pymysql.connect(**db_conn)
			self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
		except MySQLError as e:
			print(e)
	def execute_query(self,query):
		try:
			self.cursor.execute(query)
			return self.cursor.fetchall()
		except Exception, e:
			raise e
	def crud_data(self,insert_stmt):
		try:
			self.cursor.execute(insert_stmt)
			self.connection.commit()
		except Exception, e:
			self.connection.rollback()
			print "Error in inserting data, {0}".format(insert_stmt)
			raise e
	def __del__(self):
		self.connection.close()
		self.cursor.close()


# class MySQLDBConn(object):
# 	"""docstring for MySQLDBConn"""
# 	def __init__(self,db_conn=main_db_config):
# 		super(MySQLDBConn, self).__init__()
# 		self.db_conn = db_conn
# 		try:
# 			self.connection = MySQLConnection(**db_conn)
# 			self.cursor = self.connection.cursor(dictionary=True)
# 		except Error as e:
# 			print(e)
# 	def execute_query(self,query):
# 		try:
# 			self.cursor.execute(query)
# 			return self.cursor.fetchall()
# 		except errors.InterfaceError as IE:
# 			print "Lost connection to MySQL server during query", IE
# 			try:
# 				self.connection = MySQLConnection(**db_conn)
# 				self.cursor = self.connection.cursor(dictionary=True)
# 				self.cursor.execute(query)
# 				return self.cursor.fetchall()
# 			except Error as e:
# 				print(e)
# 		except Exception, e:
# 			raise e

# 	def crud_data(self,insert_stmt):
# 		try:
# 			self.cursor.execute(insert_stmt)
# 			self.connection.commit()
# 		except Exception, e:
# 			self.connection.rollback()
# 			print "Error in inserting data, {0}".format(insert_stmt)
# 			raise e
# 	def __del__(self):
# 		self.cursor.close()
# 		self.connection.close()

