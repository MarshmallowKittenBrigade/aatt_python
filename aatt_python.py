#!/usr/bin/python

import json
import requests

class Aatt:

	def __init__(self):
		self.aattUrl = 'https://jarvis.marshmallowkittens.org/sync'
		self.post = {}
		self.action = {}
		self.records = {}
		self.checks = {}
		
	def setSyncUrl(self,url):
		self.aattUrl = url

	def setAccount(self,acctId,acctKey):
		self.post.update({'APP':'aatt_python','ACCOUNT':acctId,'KEY':acctKey})

	def setDevice(self,deviceId):
		self.post.update({'DEVICE':deviceId})

	def setAction(self,action):
		self.post.update({'ACT':action})

	def record(self,item,value):
		self.records.update({'ITEM':item,'VALUE':value})

	def check(self,item):
		self.checks.update({'ITEM':item})

	def compile(self):
		if self.action is 'RECORD':
			self.post.update({'RECORDS':records})
		elif self.action is 'CHECK':
			self.post.update({'CHECKS':checks})
		return self.post

	def send(self):
		self.compile()
		self.payload = json.dumps(self.post)
		r = requests.post(self.aattUrl,data=self.post)
		return r.json()
		
