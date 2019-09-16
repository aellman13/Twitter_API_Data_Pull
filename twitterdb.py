import mysql.connector
from mysql.connector import Error
import json
from dateutil import parser
import os
import time
import subprocess
import tweepy


consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')
password = os.environ.get('mysql_password_twitterdb')

def connect(username, created_at, tweet, retweet_count, place , location)

	# Connect to a MySQL dataabase and insert twitter data
	try;
		conn = mysql.connector.connect(user = 'root', host = 'localhost', 
										password = password, database = twitterdb,
										charset = 'utf8')
		if conn.is_connected():

			#Insert twitter data in to the MySQL DB

			cursor = conn.cursor()
			# Add tweet
			tweet = ("Insert INTO tweets "
					"(username, created_at, tweet, retweet_count, location, place) "
					"VALUES (%s,%s,%s,%s,%s,%s)")






