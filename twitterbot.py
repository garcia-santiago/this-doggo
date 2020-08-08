import tweepy, time, os
from random import *

def botfun():
	print('The bot is starting..', flush=True)
	#TWITTER API CONECTION

	c_key = os.environ.get('CONSUMER_KEY')
	c_sec = os.environ.get('CONSUMER_SECRET')
	t_key = os.environ.get('ACCESS_KEY')
	t_sec = os.environ.get('ACCESS_SECRET')

	auth = tweepy.OAuthHandler(c_key, c_sec)
	auth.set_access_token(t_key,t_sec)
	api = tweepy.API(auth)


	############################################


	#EXCLUDE SEEN TWEETS

	FILE_NAME = 'last_seen_id.txt'

	def retrieve_last_seen_id(file_name):
	    f_read = open(file_name, 'r')
	    last_seen_id = int(f_read.read().strip())
	    f_read.close()
	    return last_seen_id

	def store_last_seen_id(last_seen_id, file_name):
	    f_write = open(file_name, 'w')
	    f_write.write(str(last_seen_id))
	    f_write.close()
	    return

	########################################
	#REPLY TO NEW TWEETS

	#SELECT A RANDOM TEXT STRING TO ATACH TO THE TWEET
	randomtext = {
		0: " HEY LOOK AT THIS UNIT RIGHT HERE",
	    1: " I ASSURE YOU, HE IS A GOOD BOY!",
	    2: " LOOK AT THIS!",
	    3: " SHE IS PRETTY CUTE NGL",
	    4: " ISN'T HE CUTE?",
	    5: " YES, SHE IS GOOFY INDEED",
	    6: " HE'S LOOKING KINDA THICC",
	    7: " PROTECT HIM PLS",
	    8: " BEEP BOOP, LOOK AT THIS BOY!",
	    9: " CHECK OUT THIS SMILE!",
	}
	#SELECT A IMGAGE TO ATACH TO THE TWEET

	dogimg = {
		"#americanbulldog": "./img/american-bulldog.jpg",
		"#britishbulldog": "./img/british-bulldog.jpg",
		"#frenchbulldog": "./img/french-bulldog.jpg",
		"#goldenretriever": "./img/golden-retriever.png",
		"#labradorretriever": "./img/labrador-retriever.jpg",
		"#germanshepherd": "./img/german-shepherd.jpg"
	}
	# LIST TO EASE THE FILTERING OF THE HASHTAGS


	hashtag = ["#americanbulldog",
				"#britishbulldog",
				"#frenchbulldog",
				"#goldenretriever",
				"#labradorretriever",
				"#germanshepherd"]

	#MAIN FUNCTION
	def reply_to_tweets():
		print('Looking for tweets', flush=True)

		last_seen_id = retrieve_last_seen_id(FILE_NAME)
		mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')


		for mention in reversed(mentions):
			print(str(mention.id) + ' -- ' + mention.full_text, flush=True)

			last_seen_id = mention.id
			store_last_seen_id(last_seen_id, FILE_NAME)

			for item in hashtag:
				if item in mention.full_text.lower():
					print('Responding back', flush=True)

					imagePath = dogimg[item]
					api.update_with_media(imagePath, '@' + mention.user.screen_name + randomtext[randrange(10)], in_reply_to_status_id=mention.id, auto_populate_reply_metadata=True)


	#######################################
	#LOOP THE REPLY FUNCTION

	while True:
		reply_to_tweets()
		time.sleep(20)

#####################################
botfun()
