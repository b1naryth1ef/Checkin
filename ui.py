#Holds the [minimal] "UI" for Checkin.
from colorama import init
from termcolor import colored

green = "green"
red = "red"
yellow = "yellow"
blue = "blue"
cyan = "cyan"
magenta = "magenta"

def ok():
	print colored("-------------USER CHECKED IN-------------", green)

def fail():
	print colored("-------------INVALID USER ID-------------", red, attrs=['bold'])

def err(err):
	print colored("-------------ERROR: %s-------------" % (err), red, attrs=['blink'])
	print colored("PLEASE REPORT TO ADMIN (ERR ID #002)", blue)

def srch1():
	print colored("NAME           CHECK-INS", cyan, attrs=['bold'])

def srch2():
	print colored("YEAR | MONTH | DAY | TIME", cyan, attrs=['bold'])

def srch():
	print colored("=====================",green)
	print colored("---> ",green)+colored("SEARCH MODE", magenta, attrs=['bold'])+colored(" <---", green)
	print colored("=====================",green)	

def chk():
	print colored("=====================",green)
	print colored("--->",green)+colored("CHECK IN MODE", magenta, attrs=['bold'])+colored("<---", green,)
	print colored("=====================",green)

def lst1():
	print colored("=====================",green)
	print colored("--->",green)+colored("LIST ALL MODE", magenta, attrs=['bold'])+colored("<---", green)
	print colored("=====================",green)	

def lst2():
	print colored("NAME        CHECK-INS", cyan, attrs=['bold'])

def sep():
	print colored("|", red, attrs=['bold'])

def statstime():
	return colored("TIME:",cyan,attrs=['bold'])

def statsid():
	return colored("ID:",cyan,attrs=['bold'])

def mont1(month):
	print colored("Overview for month: %s" % (month),cyan,attrs=['bold'])

def chkold():
	print colored("-------------USER ALREADY CHECKED IN!-------------", red)

def newy1():
	print colored("=====================",green)
	print colored("--->",green)+colored("NEW USER MENU", magenta, attrs=['bold'])+colored("<---", green)
	print colored("=====================",green)

def usr_err_1():
	print colored("USER ALREADY EXSISTS! (OPERATION ABORTED!)", red, attrs=['bold'])