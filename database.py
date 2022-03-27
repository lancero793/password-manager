'''
File: PasswordManager
Author: Carlos Alberto Guzmán
Description: 
'''
from decouple import config
import sqlite3
import random
from hashlib import sha256
from time import sleep
import os 
class PasswordManager:
	def __init__(self, name_aplication:str = "Undefined", large:int = 10):
		self.name_aplication = name_aplication
		self.large = large
		self.database = config("DATABASE")
		self.__password = "Undefined"
	
	def password_generator(self):
		password = None
		upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		lower = "abcdefghijklmnopqrstuvxyz"
		numbers = "9876543210"
		simbols = "(){}[]=×%~<>!&/"
		all_characters = upper + lower + numbers + simbols
		try:
			password = "".join(random.sample(all_characters, self.large))
		except Exception as e:
			#print("A ocurrido un error")
			raise TypeError("A ocurrido un error inesperado")
		return password
	def saving_message(self):
		print("Save...")
		sleep(1)
	
	def encripte_password(self):
		hashed = sha256
		
	def save_in_database(self):
		if os.path.isfile(self.database):
			connection = sqlite3.connect(self.database)
			cursor = connection.cursor()
			cursor.execute("CREATE TABLE IF NOT EXISTS users(name_aplication CHARFIELD, password CHARFIELD)")
			cursor.execute("SELECT name_aplication FROM users WHERE name_aplication={}".format("name_aplication"))
			exists = cursor.fetchall()
			cursor.execute("INSERT INTO users VALUES('{}', '{}')".format(self.name_aplication, self.get_password))
			connection.commit()
			#print("Agregando información...")
		#	sleep(1)
			print("contraseña -> {} generada exitosamente ✓".format(self.name_aplication))
		else:
			os.system("touch {}".format(self.database))
			connection = sqlite3.connect(self.database)
			cursor = connection.cursor()
			cursor.execute("CREATE TABLE IF NOT EXISTS users(name_aplication CHARFIELD, password CHARFIELD)")
			exists = cursor.fetchall()
			cursor.execute("INSERT INTO users VALUES('{}', '{}')".format(self.name_aplication, self.get_password))
			connection.commit()
			#print("Base de datos creada ✓")
			#sleep(1)
			print("contraseña -> {} generada exitosamente ✓".format(self.name_aplication))
			
			
	@classmethod
	def instance_from_txtfile(cls):
		all_objects = []
		with open("./passwd.txt", "r") as file:
			lines = file.readlines()
			for line in lines:
				line = line.rstrip("\n")
				all_objects.append(PasswordManager(
					name_aplication = line
					))
				file.close()
		return all_objects
		
	@property
	def set_password(self):
		self.__password = self.password_generator()
		
	@property
	def get_password(self):
		return self.__password
	
objects = PasswordManager.instance_from_txtfile()
for obj in objects:
	obj.set_password
	obj.save_in_database()
	obj.saving_message()

