aatt_python
===========
Introduction
-----------
#####Required Packages
Requests
Usage
-----
1. Import the package
	>import Aatt

2. Instantiate an Aatt object
	>aatt = Aatt()

3. Set your account info and device ID
	>aatt.setAccount("phooltest","CrazyPassword456")
	>aatt.setDevice("1");

4. Add Activity & Data
	- For adding records, you set the activity to RECORD and call the record method on your aatt object.  Pass the endpoint ID and the value as parameters.
		>aatt.setAct("RECORD")
		>aatt.record("1","42")
		>aatt.record("2","86")
		>aatt.record("3","-10")
		>aatt.record("4","0")

	- For checking state of attributes, you set the activity to CHECK and call the check method.  Pass the endpoint ID and the attribute ID as parameter.
		>aatt.setAct("CHECK")
		>aatt.check("1","1")
		>aatt.check("1","2")
		>aatt.check("1","3")
		>aatt.check("2","4")
		>aatt.check("2","5")
		>aatt.check("2","6")
		>aatt.check("3","7")

5. Call the send method to post the data to the aatt server.  It will return a response from the server formatted as a JSON string.
	>print(aatt.send())


