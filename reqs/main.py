from time import *
import time
import random
import db, ui
import os, sys

def chky(uid):
	"""Checks if a user has any previous checkins for the day."""
	x = db.checkins_today(uid)
	if x == None:
		return False
	else:
		return True

def clear(numlines="100"):
	"""Clears the screen..."""
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
	"""The checkin screen"""
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
		x = db.osearch("name",iny)
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

def home_newuser():
	"""The new user menu"""
	ui.newy1()
	newfname = raw_input("NEW USER FIRST NAME:   ")
	if newfname == ":EXIT":
		home()
	else:
		pass
	newlname = raw_input("NEW USER LAST NAME:   ")
	today = raw_input("MARK PRESENT FOR TODAY [Y/N]   ")
	if today in ("Y","y"):
		z = db.new_user(newfname,newlname,True)
		if z is True:
			print "USER ADDED... PRESS [ENTER] TO GOTO HOMESCREEN"
		elif z is False:
			print "USER WAS NOT ADDED... PRESS [ENTER] TO GOTO HOMESCREEN"
		raw_input()
	elif today == ":EXIT":
		home()
	else:
		z = db.new_user(newfname,newlname,False)
		if z is True:
			print "USER ADDED... PRESS [ENTER] TO GOTO HOMESCREEN"
		elif z is False:
			print "USER WAS NOT ADDED... PRESS [ENTER] TO GOTO HOMESCREEN"
		raw_input()
	home()

def home_list():
	"""The list all menu"""
	ui.lst1()
	ui.lst2()
	x = db.get_users()
	for i in x:
		z = len(i[1])
		f = 16-z
		l = " "*f
		print i[1], l, i[4]
	raw_input("Press [enter] to goto homescreen")
	home()

def home_search():
	"""The search menu"""
	def outy(iny):
		x = db.checkins(iny.id)
		ui.srch1()
		y = 14 - len(iny.name)
		l = " "*y 
		print iny.name, l, iny.checkins
		ui.srch2()
		for i in x:
			y2 = 6 - len(str(i[1]))
			f = " "*y2
			print str(i[0]),"|",str(i[1])+f+"|",str(i[2]),"|",str(i[3])
	ui.srch()
	do = raw_input("Search by [N]ame or [I]D    ")
	if do in ("N", "n"):
		x = raw_input("Search by Full Name:   ")
		z = db.osearch("name",x)
		try:
			outy(z)
		except AttributeError: #@Error 004
			ui.err("#004")
			time.sleep(1)
			home_search()
	elif do in ("I","i"):
		x = raw_input("Search by ID:   ")
		z = db.osearch("id",x)
		outy(z)
	elif do == ":EXIT":
		home()
	raw_input("Press [enter] to go home")
	home()

def home_checkin():
	"""Stupid pointer to the check in mode. (@change for [b1naryth1ef])"""
	checkinmode()

def home_edituser():
	"""@planned allows admins to edit users"""
	pass

def home_stats():
	"""Pulls up stats."""
	def month(m):
		"""Shows both total number of checkins for a month, and individual checkins."""
		x = db.cquery("month",m)
		print "Total:", x[0] #@BUG when zero sometimes displays "1"
		f = raw_input("[L]ist [N]ew overview or[B]ack to home   ").lower()
		if f == "l":
			ui.mont1(m)
			for i in x[1]:
				print ui.statsid(), i[0],"  ",ui.statstime(), i[1]
			raw_input("[Enter] to go back to search")
			home_stats()
		elif f == "n":
			home_stats()
		elif f == "b":
			home()
		else:
			raw_input("I didnt get that... Press [Enter] to go back to stats...")
			home_stats()

	def day(d):
		""" Shows both total number of checkins for a day and the individual checkins"""
		x = db.cquery("day",d)
		print "Total:", x[0]
		f = raw_input("[L]ist [N]ew overview or [B]ack to home   ").lower()
		if f == "l":
			for i in x[1]:
				print "ID:", i[0],
				print "TIME:", i[1]
			raw_input("[Enter] to go back to search")
			home_stats()
		elif f == "n":
			home_stats()
		elif f == "b":
			home()
		else:
			pass

	x = raw_input("[M]onth or [D]ay stats:   ").lower()
	if x == "m":
		m = raw_input("Month (as integer):   ")
		month(m)
	elif x == "d":
		d = raw_input("Day (as integer):   ")
		day(d)
	elif x == ":exit":
		home()
	else:
		raw_input("Didnt get that... press [enter] to try again.")
		home_stats()
def admin():
	pass	

def home():
	"""Home menu @credit [HarryD]"""
	clear()
	print "[N]ew User" 
	print "[L]ist Users"
	print "[S]earch"
	print "[C]heck-in mode"
	#print "[E]dit user"
	print "[O]verview (stats)"
	print "[Q]uit"
	d = {'n': home_newuser,
		'l': home_list,
		's': home_search,
		'c': home_checkin,
		'e': home_edituser,
		'o': home_stats,
		'q': sys.exit,
		'a': admin}
	xin = raw_input("Input:   ").lower()
	if xin in d:
		d[xin]()
	else:
		raw_input("Whoops... Didnt get that. Press [enter] to try again.")
		home()

home()