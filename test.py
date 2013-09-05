#!/usr/bin/python

from aatt_python import Aatt

aatt = Aatt()

aatt.setAccount("phooltest","CrazyPassword456")
aatt.setDevice("1");
"""
aatt.setAction("RECORD")
aatt.record("1","42")
aatt.record("2","86")
aatt.record("3","-10")
aatt.record("4","0")
"""
aatt.setAction("CHECK")
aatt.check("1")
aatt.check("2")
aatt.check("3")

print(aatt.send())
