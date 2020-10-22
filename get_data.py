from sql import *


def regdata(author, content):  # short for register data
	'''
	This function will input 'content' into the mysql db
	called 'user_input'
	'''
	command = "INSERT INTO user_input (user_name, msg) VALUES (%s, %s)"
	val = (str(author), str(content))
	cursor, db = CreateCursorAndDb()
	cursor.execute(command, val)
	db.commit()

def sdata(author):  # short for set data
	'''
	This function will 'set' or 'update' the 
	'content' that had been entered into the db
	'''
