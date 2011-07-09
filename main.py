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
	elif xin in ("L","l"):
		home_list()
	elif xin in ("S","s"):
		home_search()
	elif xin in ("C","c"):
		home_checkin()
	elif xin in ("E","e"):
		home_edituser()

def home_newuser():
	print "====================="
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
	print "====================="
	print "--->LIST ALL MENU<---"
	print "====================="
	print "NAME        CHECK-INS"
	x = db.get_users()
	for i in x:
		z = len(i[2])
		f = 14-z
		l = " "*f
		print i[2], l, i[4]

def home_search():
	def outy(iny):
		print "NAME           CHECK-INS"
		y = 14 - len(iny.name)
		l = " "*y 
		print iny.name, l, iny.checkins
	print "====================="
	print "---> SEARCH MENU <---"
	print "====================="
	do = raw_input("Search by [N]ame or [I]D    ")
	if do in ("N", "n"):
		x = raw_input("Search by Full Name:   ")
		z = db.find_user("name",x)
		outy(z)
	elif do in ("I","i"):
		x = raw_input("Search by ID:   ")
		z = db.find_user("id",x)
		outy(z)

def home_checkin():
	print "====================="
	print "--->CHECK IN MODE<---"
	print "====================="
	checkinmode()

def home_edituser():
	pass

home()