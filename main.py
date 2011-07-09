from time import *
import random
import save

t = gmtime()
date = str(t[0])+"/"+str(t[1])+"/"+str(t[2])

def imp():
	pass

def exp():
	pass
def create_user(fname,lname,id):
	pass

def home():
	print "[N]ew User" 
	print "[L]ist Users"
	print "[S]earch"
	print "[C]heck-in mode"
	xin = raw_input("Input:   ")
	if xin in ("N","n"):
		home_newuser()
	if xin in ("L","l"):
		home_list()
	if xin in ("S","s"):
		home_search()
	if xin in ("C","c"):
		home_checkin()

def home_newuser():
	new = type_user("Andrei", "Zbikowski")

def home_list():
	pass

def home_search():
	pass

def home_checkin():
	pass

home()