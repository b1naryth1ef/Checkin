from time import *
import random
import db

t = gmtime()
date = str(t[0])+"/"+str(t[1])+"/"+str(t[2])

def checkinmode():
	iny = raw_input("NAME:   ")
	def markin(uid,current):
		current += 1
		db.checkin(current,uid)
		checkinmode()
	try:
		x = db.find_user("name",iny)
		markin(x.id,x.checkins)
	except: #@Error 001
		print "EXCEPTION ERROR 001 [Report to admin please!]"
		checkinmode()

def home():
	print "[N]ew User" 
	print "[L]ist Users"
	print "[S]earch"
	print "[C]heck-in mode"
	print "[E]dit user"
	xin = raw_input("Input:   ")
	if xin in ("N","n"):
		home_newuser()
	if xin in ("L","l"):
		home_list()
	if xin in ("S","s"):
		home_search()
	if xin in ("C","c"):
		home_checkin()
	if xin in ("E","e"):
		home_edituser()

def home_newuser():
	print "--->NEW USER MENU<---"
	print "====================="
	newfname = raw_input("NEW USER FIRST NAME:   ")
	newlname = raw_input("NEW USER LAST NAME:   ")
	today = raw_input("MARK PRESENT FOR TODAY [Y/N]   ")
	if today in ("Y","y"):
		db.add_user(newfname,newlname,"1")
	else:
		db.add_user(newfname,newlname,"0")

def home_list():
	pass

def home_search():
	pass

def home_checkin():
	checkinmode()

def home_edituser():
	pass

home()