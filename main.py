from time import *
import random
import db
import os

t = gmtime()
date = str(t[0])+"/"+str(t[1])+"/"+str(t[2])
def clear(numlines="100"):
	if os.name == "posix":
		# Unix/Linux/MacOS/BSD/etc
		os.system('clear')
	elif os.name in ("nt", "dos", "ce"):
		# DOS/Windows
		os.system('CLS')
	else:
		# Fallback for other operating systems.
		print '\n' * numlines

def checkinmode():
	iny = raw_input("NAME:   ")
	def markin(uid):
		db.checkin(uid)
		checkinmode()
	try:
		x = db.find_user("name",iny)
		markin(x.id)
		print "USER CHECK IN! [GREEN]"
		time.sleep(3)
	except: #@Error 001
		print "EXCEPTION ERROR 001 [Report to admin please!]"
		checkinmode()
	home()

def home():
	clear()
	print "[N]ew User" 
	print "[L]ist Users"
	print "[S]earch"
	print "[C]heck-in mode"
	print "[E]dit user"
	print "[Q]uit"
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
	elif xin in ("Q","q"):
		quit()
	else:
		raw_input("Whoops... Didnt get that. Press [enter] to try again.")
		home()


def home_newuser():
	print "====================="
	print "--->NEW USER MENU<---"
	print "====================="
	newfname = raw_input("NEW USER FIRST NAME:   ")
	newlname = raw_input("NEW USER LAST NAME:   ")
	today = raw_input("MARK PRESENT FOR TODAY [Y/N]   ")
	if today in ("Y","y"):
		db.add_user(newfname,newlname,"1")
		print "USER ADDED... PRESS [ENTER] TO GOTO HOMESCREEN"
		raw_input()
	else:
		db.add_user(newfname,newlname,"0")
		print "USER ADDED... PRESS [ENTER] TO GOTO HOMESCREEN"
		raw_input()
	home()
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
	raw_input("Press [enter] to goto homescreen")
	home()
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
	raw_input("Press [enter] to go home")
	home()
def home_checkin():
	print "====================="
	print "--->CHECK IN MODE<---"
	print "====================="
	checkinmode()

def home_edituser():
	pass

home()