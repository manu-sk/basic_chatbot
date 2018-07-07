import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root', password='hacker',database='chatbot')
cursor = cnx.cursor()

query = ("SELECT intents_tag, intents_patterns, intents_responses FROM trainingData")
data = cursor.execute(query)

for (data) in cursor:
  print(data)

cursor.close()
cnx.close()
