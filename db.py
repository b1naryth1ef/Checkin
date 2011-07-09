import MySQLdb
db = MySQLdb.connect(user="root", passwd="", db="python")
users = []

c = db.cursor()

class User(object):
    """A simple User class"""
    def __init__(self, userid,first_name=None, last_name=None,checkins=None):
        self.id = userid
        self.first_name = first_name
        self.last_name = last_name
        self.checkins = checkins

def get_users():
	c.execute("""SELECT * FROM users""")
	for userid, first_name, last_name, company in c.fetchall():
		u = User(userid, first_name, last_name)
    	print u.first_name

def add_user(zid,fname,lname,checkins):
	c.executemany("""INSERT INTO users (id, first_name, last_name, checkins) VALUES (%s, %s, %s, %s)""", [(zid, fname, lname, checkins)])

def update_user(uid,field,change):
	"""Update a row in format ID|FIELD|CHANGE"""
	c.execute("UPDATE Users SET %s = %s WHERE Id = %s", (field, change, uid)) 
	db.commit()

def find_user(field,value):
	c.execute("""SELECT * FROM Users WHERE %s = "%s" """ % (field,value))
	for userid, first_name, last_name, checkins in c.fetchall():
		u = User(id, first_name, last_name, checkins)
		return u

