#!flask/bin/python

import sys
import tweepy

from flask import Flask, render_template, request, redirect, Response
import random, json
from flask_cors import CORS

consumer_key = '8HMKlKJtXx44MqiBQld7qHM9d'
consumer_secret = '70vU3Qs6STydQXvqx8Jk6QtCZBuQ1Eho3bKCglD8QkdCvYXndh'
access_token =  '1018141995062030337-HkiVhxqwamOxsrT7p8aEn2081pHVta'
access_token_secret = 'gcnYabO0MM82cxM4s4AbFg11y5KBm6SzbrD1bbmXyp6DW'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

app = Flask(__name__)
CORS(app)

@app.route('/')
def output():
	# serve index template
	return render_template('index.html', name='Joe')

@app.route('/twitterbot', methods = ['POST'])
def twitterbot():
	# read json + reply
	data = request.data
	result = str(data)
	print(result)
	api.update_status(status=result)
	return result

if __name__ == '__main__':
	# run!
	app.run()