#!/usr/bin/python

from aatt_python import Aatt

aatt = Aatt()

aatt.setAccount("phooltest","CrazyPassword456")
aatt.setDevice(1);
aatt.setAction("RECORD")
aatt.record(1,42)
print(aatt.send())
