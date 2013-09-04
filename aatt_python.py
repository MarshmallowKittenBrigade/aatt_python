#!/usr/bin/python

import json
import requests

class Aatt:
	"""
	Automate All The Things Python Module
	"""
	def __init__(self):
		self.aattUrl = 'https://jarvis.marshmallowkittens.org/sync'
		self.post = {}
		self.action = {}
		self.records = {}
		self.checks = {}
		
	def setSyncUrl(self,url):
		"""
		This is used to change the sync url.  It can also be set by hand in the aatt_python.py file.
		"""
		self.aattUrl = url

	def setAccount(self,acctId,acctKey):
		"""
		All requests to the aatt server must include your account id and your account key.
		"""
		self.post.update({'APP':'aatt_python','ACCOUNT':acctId,'KEY':acctKey})

	def setDevice(self,deviceId):
		"""
		Device ID must be specified for all requests, whether they are records or checks.
		"""
		self.post.update({'DEVICE':deviceId})

	def setAction(self,action):
		"""
		Valid options for this method are RECORD or CHECK
		"""
		self.post.update({'ACT':action})

	def record(self,item,value):
		"""
		If RECORD is set as the action you can add all the items you need to record with this method.  As many records can be included as needed and sent in a batch.  If you choose CHECK as your action, any records added will be ignored.
		"""
		self.records.update({'ITEM':item,'VALUE':value})

	def check(self,item):
		"""
		If CHECK is set as teh action you can add all items to check with this method.  Checks can be batched by calling this as many times as necessary before calling send().  If RECORD is chosen as the action, these are ignored.
		"""
		self.checks.update({'ITEM':item})

	def compile(self):
		"""
		This compiles all the various pieces into a properly formatted dict.  This does not need to be called separately from send.
		"""
		if self.action is 'RECORD':
			self.post.update({'RECORDS':records})
		elif self.action is 'CHECK':
			self.post.update({'CHECKS':checks})
		return self.post

	def send(self):
		"""
		This compiles all the dicts into the proper format, converts them to json, then posts them to the aartUrl.
		"""
		self.compile()
		self.payload = json.dumps(self.post)
		r = requests.post(self.aattUrl,data=self.post)
		return r.json()
		
