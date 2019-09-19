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

def connect(username, created_at, tweet, retweet_count, place , location):

	# Connect to a MySQL dataabase and insert twitter data
	try:
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
			# Insert the new tweet
			cursor.execute(tweet, (username, created_at, tweet, retweet_count, location, place))
			conn.commit()

	except Error as e:
		print(e)

	cursor.close()
	conn.close()

class Streamlistener(tweepy.StreamListener):

	def on_connect(self):
		print('You are connected to the Twitter API')

	def on_error(self):
		if error_code != 200:
			print('error found')
			# returning false disconnects the stream
			return False

	def on_data(self, data):

		try:
			raw_data = json.loads(data)

			#If the raw_data object actually has a tweet in it - pull the values from each key
			if 'text' in raw_data:
				username = raw_data['user']['screen_name']
				created_at = parser.parse(raw_data['created_at'])
				tweet = raw_data['text']
				retweet_count = raw_data['retweet_count']

				if raw_data['place'] is not None:
					place = raw_data['place']['country']
					print(place)
				else:
					place = None

				location = raw_data['user']['location']

				# Write all data to the DB
				connect(username, created_at, tweet, retweet_count, location, place)
				print('Tweet collected at: {}'.format(str(created_at)))

		except Error as e:
			print(e)
if __name__ == '__main__':

	# Allow user input

	track = []
	while True:
		input1 = input('What do you want to collect tweets on: ')
		track.append(input1)

		input2 = input('Do you wish to enter nother word (y/n): ')
		if input2 == 'n' or input2 =='N':
			break
	print('You want to search for {}'.format(track))
	print('Initializing connection to Twitter API...')
	time.sleep(1)




	# authentification so we can access twitter
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, wait_on_rate_limit = True)

	# Create instance of Stream Listener
	listener = Streamlistener(api=api)
	stream = tweepy.Stream(auth, listener = listener)
	stream.filter(track=track, languages = ['en'])


















