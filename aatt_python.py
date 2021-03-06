#!/usr/bin/python

import json, sys, socket, ssl, pprint

class Aatt:
	"""
	Automate All The Things Python Module
	"""
	def __init__(self):
		self.aattUrl = ''
		self.port = 8421
		self.auth = {}
		self.data = {}
		self.post = {}
		self.act = {}
		self.records = {}
		self.checks = {}
		self.state = {}
		self.status = ''
		
	def setSyncUrl(self,url,port):
		"""
		This is used to change the sync url.  It can also be set by hand in the aatt_python.py file.
		"""
		self.aattUrl = url
		self.port = port

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
		Valid options for this method are RECORD, CHECK, SET, or UPDATE
		"""
		if act == 'RECORD' or act == 'CHECK' or act == 'SET' or act == "UPDATE":
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

	def modify(self,attribute,value):
		"""
		Placeholder for the set method
		"""
		if attribute not in self.state.keys():
			self.state[attribute] = value

	def compile(self):
		"""
		This compiles all the various pieces into a properly formatted dict.  This does not need to be called separately from send.
		"""
		self.post.update({'AUTH':self.auth})
		if self.act is 'RECORD':
			self.data.update({'RECORDS':self.records})
		elif self.act is 'CHECK':
			self.data.update({'CHECKS':self.checks})
		elif self.act is 'SET':
			self.data.update({'CHANGES':self.state})
		elif self.act is 'UPDATE':
			self.data.update({'UPDATES':self.state})
		self.post.update({'DATA':self.data})
		return self.post

	def send(self):
		"""
		This compiles all the dicts into the proper format, converts them to json, then posts them to the aartUrl.
		"""
		if self.status != 'BADACT':
			self.compile()
			payload = json.dumps(self.post)
			print payload
			try:
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			except socket.error, msg:
				print 'Failed to create socket. Error code: %s , Error Message: %s ' % (msg)
				sys.exit();
			sock.settimeout(2)
			ip = socket.gethostbyname(self.aattUrl)
			
			sock.connect((ip,self.port))
			sock.send(payload)
			result = sock.recv(1024)
			sock.close()
			self.post['DATA'] = {}
			self.post['AUTH'] = {}
			return result
		else:
			return self.status
