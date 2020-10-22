import mysql.connector


mydb = mysql.connector.connect(
	host='localhost',
	user='root',
	password='alphabet',
	database='discord'
	)


def CheckIfTableExists():  # for later for error handling
	'''This function should check if the table where
	the data is supposed to be entered exists.
	'''


def CreateCursorAndDb():
	global mydb
	mycursor = mydb.cursor()
	return mycursor, mydb