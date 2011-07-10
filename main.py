from time import *
import time
import random
import db, ui
import os, sys

t = gmtime()
date = str(t[0])+"/"+str(t[1])+"/"+str(t[2])

def chky(uid):
	x = db.checky(uid)
	if x == None:
		return False
	else:
		return True

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
	clear()
	ui.chk()
	iny = raw_input("NAME:   ")
	if iny == ":EXIT":
		home()
	else:
		pass
	def markin(uid):
		db.checkin(uid)
	try:
		x = db.find_user("name",iny)
		if chky(x.id) is False:
			markin(x.id)
			ui.ok()
			time.sleep(1)
			checkinmode()
		elif chky(x.id) is True:
			ui.chkold()
			time.sleep(1)
			checkinmode()
		else:	#@error 003
			ui.err("#003")
			time.sleep(1)
			checkinmode()
	except AttributeError: #@Error 001
		ui.fail()
		time.sleep(1)
		checkinmode()
	except: #@error 002
		print sys.exc_info()[0]
		ui.err("#002")
		time.sleep(1)
		sys.exit()
	

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
		sys.exit()
	else:
		raw_input("Whoops... Didnt get that. Press [enter] to try again.")
		home()


def home_newuser():
	print "====================="
	print "--->NEW USER MENU<---"
	print "====================="
	newfname = raw_input("NEW USER FIRST NAME:   ")
	if newfname == ":EXIT":
		home()
	else:
		pass
	newlname = raw_input("NEW USER LAST NAME:   ")
	today = raw_input("MARK PRESENT FOR TODAY [Y/N]   ")
	if today in ("Y","y"):
		db.add_user(newfname,newlname,"1")
		print "USER ADDED... PRESS [ENTER] TO GOTO HOMESCREEN"
		raw_input()
	elif today == ":EXIT":
		home()
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
	checkinmode()

def home_edituser():
	pass

home()