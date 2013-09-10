#!/usr/bin/python

import json
import requests

class Aatt:
	"""
	Automate All The Things Python Module
	"""
	def __init__(self):
		self.aattUrl = 'https://jarvis.marshmallowkittens.org/sync/'
		self.auth = {}
		self.data = {}
		self.post = {}
		self.act = {}
		self.records = {}
		self.checks = {}
		self.actions = {}
		self.status = ''
		
	def setSyncUrl(self,url):
		"""
		This is used to change the sync url.  It can also be set by hand in the aatt_python.py file.
		"""
		self.aattUrl = url

	def setAccount(self,acctId,acctKey):
		"""
		All requests to the aatt server must include your account id and your account key.
		"""
		self.auth.update({'APP':'aatt_python','ACCOUNT':acctId,'KEY':acctKey})

	def setDevice(self,deviceId):
		"""
		Device ID must be specified for all requests, whether they are records or checks.
		"""
		self.data['DEVICE'] = deviceId

	def setAct(self,act):
		"""
		Valid options for this method are RECORD, CHECK, ACTION, or REGISTER
		"""
		if act == 'RECORD' or act == 'CHECK' or act == 'ACTION' or act == 'REGISTER':
			self.act = act
			self.post['ACT'] = act
		else:
			self.status = 'BADACT'

	def record(self,endpoint,value):
		"""
		If RECORD is set as the action you can add all the items you need to record with this method.  As many records can be included as needed and sent in a batch.  If you choose CHECK as your action, any records added will be ignored.
		"""
		self.records.update({endpoint:value})

	def check(self,endpoint,attribute):
		"""
		If CHECK is set as teh action you can add all items to check with this method.  Checks can be batched by calling this as many times as necessary before calling send().  If RECORD is chosen as the action, these are ignored.
		"""
		if endpoint in self.checks:
			self.checks[endpoint].update({attribute:attribute})
		else:
			self.checks.update({endpoint:{attribute:attribute}})

	def addAction(self,item,action):
		"""
		This method allows a device to set an action for another device.
		"""
		self.actions.update({item:action})

	def compile(self):
		"""
		This compiles all the various pieces into a properly formatted dict.  This does not need to be called separately from send.
		"""
		self.post.update({'AUTH':self.auth})
		if self.act is 'RECORD':
			self.data.update({'RECORDS':self.records})
		elif self.act is 'CHECK':
			self.data.update({'CHECKS':self.checks})
		elif self.act is 'ACTION':
			self.data.update({'ACTION':self.actions})
		elif self.act is 'REGISTER':
			self.data.update({'REGISTER':self.register})
		self.post.update({'DATA':self.data})
		return self.post

	def send(self):
		"""
		This compiles all the dicts into the proper format, converts them to json, then posts them to the aartUrl.
		"""
		if self.status != 'BADACT':
			self.compile()
			payload = json.dumps(self.post)
			header = {'content-type': 'application/json','User-Agent':'aatt Python'}
			r = requests.post(self.aattUrl,data=payload,headers=header,verify=True)
			return r.content
		else:
			return self.status
		
