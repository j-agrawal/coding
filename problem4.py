#!/usr/bin/python3
import os 
import crypt
uname = str(input("enter your username:"))
if uname.isalpha():
	upass ="hello"+uname
	ucrypt=crypt.crypt(upass,"ck")
	print("password set")
	os.system("useradd -m -p "+ucrypt+" "+uname)
	print("user created succefully")
else:
	print("enter a valid username")
		


