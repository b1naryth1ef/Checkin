"""The install file for checkin. """
#from reqs import db
import getpass
import MySQLdb
import sys

def db_create(server,user,passwd):
	db = MySQLdb.connect(user=user, passwd=passwd, host=server)
	c = db.cursor()
	print "Creating DB  \"pycheckins\"...",
	cmd = "create database pycheckins"
	c.execute(cmd)
	print "DONE!"
	return None

def end(user,passwd,server,tdb):
	print "Done installing tables!"
	print "Writing config file...",
	f = open("config.py","w")
	f.write("server = \"%s\"\n" % (server))
	f.write("user = \"%s\"\n" % (user))
	f.write("db = \"%s\"\n" %(tdb))
	f.write("password = \"%s\"\n" % (passwd))
	print "Done!"
	print "\n All done!"
	raw_input("Press [ENTER] to try starting the script!")
	import start
	start.init()

def dbtest(user,passwd,server,tdb):
	#Initiate curser
	try:
		db = MySQLdb.connect(user=user, passwd=passwd, host=server, db=tdb)
		c = db.cursor()
		return True
	except:
		return False

def dbinstall(user,passwd,server,tdb):
	db = MySQLdb.connect(user=user, passwd=passwd, host=server, db=tdb)
	c = db.cursor()
	def tables():
		c.execute("""CREATE TABLE `checkins` (
	  `id` int(100) NOT NULL,
	  `year` int(100) NOT NULL,
	  `month` int(100) NOT NULL,
	  `day` int(100) NOT NULL,
	  `time` char(100) NOT NULL
	) ENGINE=MyISAM DEFAULT CHARSET=latin1;""")
		c.execute("""CREATE TABLE `users` (
	  `id` int(11) NOT NULL AUTO_INCREMENT,
	  `name` char(100) DEFAULT NULL,
	  `first_name` char(100) DEFAULT NULL,
	  `last_name` char(100) DEFAULT NULL,
	  `checkins` int(11) DEFAULT NULL,
	  PRIMARY KEY (`id`)
	) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;""")
		db.commit()
		end(user,passwd,server,tdb)
	z = raw_input("Script will create tables 'User' and 'Checkins'. Is this ok? [Y/N]:  ").lower()
	if z == "y":
		tables()
	elif z =="n":
		sys.exit()
	else:
		print "Didnt get that"
		install(user,passwd,server,tdb)
	
	

def config():
	print "Let's set up your config! [Press enter to use default]"
	c_server = raw_input("Your MySQL Server [localhost]:  ")
	if c_server == "":
		c_server = "localhost"
	c_user = raw_input("MySQL Username [root]:  ")
	if c_user == "":
		c_user = "root"
	c_password = getpass.getpass("MySQL Password (Hidden):  ")
	c_database = raw_input("MySQL Database [NEW] to create new:  ").lower()
	if c_database == "new":
		db_create(c_server,c_user,c_password)
		c_db = "pycheckins"
	else:
		c_db = c_database
	print "Okay... Testing config...",
	f = dbtest(c_user,c_password,c_server,c_db)
	if f is True:
		print "DONE"
		print "\n"
		print "Looks like your all set! Moving on to DB Setup!"
		dbinstall(c_user,c_password,c_server,c_db)
	if f is False:
		print "DB Test was unsuccessful!!"
		z = raw_input("Try again? [Y/N]:  ").lower()
		if z == "y":
			config()
		else:
			sys.exit()

def main():
	x = raw_input("Ready to install? [Y/N]:  ").lower()
	if x == "y":
		config()
	elif x == "n":
		sys.exit()
	else:
		print "Sorry. Didnt get that. [Exiting...]"

main()
