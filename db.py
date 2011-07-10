import MySQLdb
import os
import datetime


db = MySQLdb.connect(user="root", passwd="", db="python")
users = []

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

def get_users():
	z = []
	c.execute("""SELECT * FROM users""")
	x = c.fetchall()
	#return x
	for id, name, first_name, last_name, checkins in x:
		#u = User(id, name, first_name, last_name, checkins)
		z.append((id, name, first_name, last_name, checkins))
	return z
	#for i in x:
	#	for id, name, first_name, last_name, checkins in i:
	#		u = User(id, name, first_name, last_name, checkins)
    #		print u.first_name			


def add_user(fname,lname,checkins):
	name = fname+" "+lname
	c.executemany("""INSERT INTO users ( name, first_name, last_name, checkins) VALUES (%s, %s, %s, %s)""", [(name, fname, lname, checkins)])

def update_user(change_field,change,iden_field,iden):
	"""Update a row in format IDENITY|SELECT FIELD|CHANGE|CHANGE FIELD"""
	c.execute("""UPDATE Users SET %s = "%s" WHERE %s = "%s" """, (change_field,change,iden_field,iden)) 
	db.commit()

def checkin(tid):
	"""Checkin a user"""
	#t = gmtime()
	#tyear = t.tm_year
	#tmonth = t.tm_mon
	#tday = t.tm_mday
	#ttime = str(t.tm_hour)+":"+str(t.tm_min)+":"+str(t.tm_sec)
	now = datetime.datetime.now()
	tyear = now.year
	tmonth = now.month
	tday = now.day
	ttime = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
	c.executemany("""INSERT INTO checkins ( id, year, month, day, time) VALUES (%s, %s, %s, %s, %s)""", [(tid, tyear, tmonth, tday, ttime)])
	db.commit()

def find_user(field,value):
	c.execute("""SELECT * FROM Users WHERE %s = "%s" """ % (field,value))
	for id, name, first_name, last_name, checkins in c.fetchall():
		u = User(id, name, first_name, last_name, checkins)
		return u

def dfind_user(field1,field2,value1,value2):
	c.execute("""SELECT * FROM Users WHERE %s = %s AND %s = %s""", (field1, value1, field2, value2))
	for userid, first_name, last_name, checkins in c.fetchall():
		u = User(userid, first_name, last_name, checkins)
		return u

def checky(uid):
	xy = []
	now = datetime.datetime.now()
	tmonth = now.month
	tday = now.day
	c.execute("""SELECT * FROM Checkins WHERE month = %s AND day=%s AND id=%s""" % (tmonth, tday, uid))
	for id, year, month, day, time in c.fetchall():
		xy.append((month,day,time))
		return xy
		
def checkins(uid):
	xy = []
	c.execute("""SELECT * FROM Checkins WHERE id = "%s" """ % (uid))
	for id, year, month, day, time in c.fetchall():
		xy.append((year,month,day,time))
		return xy
