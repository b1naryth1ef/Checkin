"""Holds the minimal UI for Checkin. Built on termcolor and colorama. Reqs: Colorama, Termcolor"""
from colorama import init
from termcolor import colored

green = "green"
red = "red"
yellow = "yellow"
blue = "blue"
cyan = "cyan"
magenta = "magenta"

class Colory():
	"""Class to allow for dynamic coloring. Call x = Colory("TEXT","COLOR",attr=['bold']) and print x.msg"""
	def __init__(self,text="New Colored Text",color=green,attr=[]):
		self.msg = colored(text,color, attrs=attr)
		self.clear = text
		self.color = color
		self.attr = attr
		return None

def ok():
	"""User Checked in message [Green]"""
	print colored("-------------USER CHECKED IN-------------", green)

def fail():
	"""Invalid User ID message [Red, Bold]"""
	print colored("-------------INVALID USER ID-------------", red, attrs=['bold'])

def err(err):
	"""Dynamic Error Message [Red,Blinking]
	Usage: err("#001") """
	print colored("-------------ERROR: %s-------------" % (err), red, attrs=['blink'])
	print colored("PLEASE REPORT TO ADMIN (ERR ID #%s)" % (err), blue)

def srch1():
	"""Name/Checkins display for search. [cyan, bold]"""
	print colored("NAME           CHECK-INS", cyan, attrs=['bold'])

def srch2():
	"""Year/Month/Day/Time display for search. [cyan, bold]"""
	print colored("YEAR | MONTH | DAY | TIME", cyan, attrs=['bold'])

def srch():
	"""Search Mode Display. [Green outline, magenta intext(bold)]"""
	print colored("=====================",green)
	print colored("---> ",green)+colored("SEARCH MODE", magenta, attrs=['bold'])+colored(" <---", green)
	print colored("=====================",green)	

def chk():
	"""Checkin Mode Display. [Green outline, magenta intext(bold)]"""
	print colored("=====================",green)
	print colored("--->",green)+colored("CHECK IN MODE", magenta, attrs=['bold'])+colored("<---", green,)
	print colored("=====================",green)

def lst1():
	"""List All Mode. [Green outline, magenta intext(bold)]"""
	print colored("=====================",green)
	print colored("--->",green)+colored("LIST ALL MODE", magenta, attrs=['bold'])+colored("<---", green)
	print colored("=====================",green)	

def lst2():
	"""Name, Checkins"""
	print colored("NAME        CHECK-INS", cyan, attrs=['bold'])

def sep():
	""" Red Seperator: |"""
	print colored("|", red, attrs=['bold'])

def statstime():
	"""Stats display of TIME tag. [Cyan,Bold]"""
	return colored("TIME:",cyan,attrs=['bold'])

def statsid():
	"""Stats display of ID tag. [Cyan, Bold]"""
	return colored("ID:",cyan,attrs=['bold'])

def mont1(month):
	"""Overview for month text. [Cyan, Bold]
	Usage: mont1("Month")"""
	print colored("Overview for month: %s" % (month),cyan,attrs=['bold'])

def chkold():
	"""User already checked in text [Red]"""
	print colored("-------------USER ALREADY CHECKED IN!-------------", red, attrs=['bold'])

def newy1():
	"""New User Menu"""
	print colored("=====================",green)
	print colored("--->",green)+colored("NEW USER MENU", magenta, attrs=['bold'])+colored("<---", green)
	print colored("=====================",green)

def usr_err_1():
	"""User already exsists error"""
	print colored("USER ALREADY EXSISTS! (OPERATION ABORTED!)", red, attrs=['bold'])