import csv
import os
from pprint import pprint
import mysql.connector

mydb = mysql.connector.connect(	user='root', 
								password='root', 
								database='premier_league', 
								host='localhost')

team = input("Enter team > ")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM tables WHERE Team = '" + team + "'")

for x in mycursor:
  print(x)