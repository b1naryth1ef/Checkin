#Imports
import MySQLdb
import os
import datetime

#Initiate curser
db = MySQLdb.connect(user="root", passwd="", db="python")
c = db.cursor()

class User(object):
    """A simple User class"""
    def __init__(self, userid, name=None, first_name=None, last_name=None,checkins=None):
        self.id = userid
        self.name = name
        self.first_name = first_name
        self.last_name = last_name
        self.checkins = checkins

class Checkin(object):
    """A simple Checkin class"""
    def __init__(self, id, year=None, month=None, day=None,time=None):
        self.id = id
        self.year = year
        self.month = month
        self.day = day
        self.time = time

class deprecated(Exception):
	"""Error for functions that have been deprecated."""
    def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)

def get_users():
	"""Simple object that returns a list full of all our users info in tuples"""
	z = []
	c.execute("""SELECT * FROM users""")
	x = c.fetchall()
	for id, name, first_name, last_name, checkins in x:
		z.append((id, name, first_name, last_name, checkins))
	return z


def new_user(fname,lname,checkinz):
	"""Adds a user in format new_user("FirstName", "LastName", True) where true is bool of whether to mark present for today"""
	if checkinz == True:
		name = fname+" "+lname
		c.executemany("""INSERT INTO users ( name, first_name, last_name, checkins) VALUES (%s, %s, %s, %s)""", [(name, fname, lname, checkins)])
		x = find_user("name", name)
		checkin(x.id)
	elif checkinz == False:
		name = fname+" "+lname
		c.executemany("""INSERT INTO users ( name, first_name, last_name, checkins) VALUES (%s, %s, %s, %s)""", [(name, fname, lname, checkins)])	
	else:
		pass
		
def update_user(change_field,change,iden_field,iden):
	"""Update a row in format IDENITY|SELECT FIELD|CHANGE|CHANGE FIELD @bad Replacement of this function is in the works"""
	c.execute("""UPDATE Users SET %s = "%s" WHERE %s = "%s" """, (change_field,change,iden_field,iden)) 
	db.commit()

def county(uid):
	"""Err what?"""
	c.execute("""SELECT * FROM users where id = "%s" """ % (uid))
	for id, name, first_name, last_name, checkins in c.fetchall():
		u = User(id, name, first_name, last_name, checkins)
		return u

def checkin(tid):
	"""Checks a user in. @planned add more options for selecting user to checkin."""
	now = datetime.datetime.now()
	tyear = now.year
	tmonth = now.month
	tday = now.day
	ttime = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
	c.executemany("""INSERT INTO checkins ( id, year, month, day, time) VALUES (%s, %s, %s, %s, %s)""", [(tid, tyear, tmonth, tday, ttime)])
	db.commit()
	x = county(tid)
	y = int(x.checkins)+1
	c.execute("""UPDATE Users SET checkins = %s WHERE id = "%s" """ % (y,tid))

def search(field,value):
	"""Finds a user."""
	f = []
	c.execute("""SELECT * FROM Users WHERE %s = "%s" """ % (field,value))
	for id, name, first_name, last_name, checkins in c.fetchall():
		f.append((id,name,first_name,last_name,checkins))
	return f

def checkins_today(uid):
	"""Checks if any checkins exsist for the user today."""
	xy = []
	now = datetime.datetime.now()
	tmonth = now.month
	tday = now.day
	c.execute("""SELECT * FROM Checkins WHERE month = %s AND day=%s AND id=%s""" % (tmonth, tday, uid))
	for id, year, month, day, time in c.fetchall():
		xy.append((month,day,time))
		return xy
		
def checkins(uid):
	"""Get all checkins for a user @planned add more options for selecting users"""
	xy = []
	c.execute("""SELECT * FROM Checkins WHERE id = "%s" """ % (uid))
	for id, year, month, day, time in c.fetchall():
		xy.append((year,month,day,time))
		return xy

def cquery(field,value):
	"""Gets checkins for a user depending on options you give it. Returns tuple of number of checkins and another tuple of ("id", "time") """
	xy = [1]
	xz = []
	c.execute("""SELECT * FROM Checkins WHERE %s = "%s" """ % (field,value))
	for id, year, month, day, time in c.fetchall():
		xy[0] += 1
		xz.append((id,time))
	return (xy,xz)

########################
##DEPRECATED FUNCTIONS##
########################
def find_user(field,value):
	"""@DEPRECATED use search()"""
	try:
    	raise MyError("search()")
 	except MyError as e:
    	print 'This function or class has been deprecated in place of: ', e.value

def add_user(fname,lname,checkins):
	"""@DEPRECATED use new_user()"""
	try:
    	raise MyError("new_user()")
 	except MyError as e:
    	print 'This function or class has been deprecated in place of: ', e.value

def dfind_user(field1,field2,value1,value2):
	"""@DEPRECATED use search()"""
	try:
    	raise MyError("search()")
 	except MyError as e:
    	print 'This function or class has been deprecated in place of: ', e.value