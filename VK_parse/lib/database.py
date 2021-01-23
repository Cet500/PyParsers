import pymysql


class MySQL:
	def __init__( self, db_path, db_user, db_pass, db_name ):
		self.connection = pymysql.connect(host = db_path, user = db_user, password = db_pass, database = db_name)
		self.cursor = self.connection.cursor()

	def __str__( self ):
		return "Класс для работы с MySQL"

	def check_connect( self ):
		# простой тест соединения
		version = self.cursor.execute( "SELECT VERSION()" )
		return bool( version )

	def execute( self, sql, parameters ):
		# выполнение запроса
		self.cursor.execute( sql, parameters )
		self.connection.commit()

	def __close__( self ):
		# неявное закрытие соединения с базой данных
		self.connection.close()

	def close( self ):
		# явное закрытие соединения с базой данных
		self.connection.close()
