#Holds the [minimal] "UI" for Checkin.
from colorama import init
from termcolor import colored

green = "green"
red = "red"
yellow = "yellow"
blue = "blue"

def ok():
	print colored("-------------USER CHECKED IN-------------", green)

def fail():
	print colored("-------------INVALID USER ID-------------", red)

def err(err):
	print colored("-------------ERROR: %s-------------" % (err), red)
	print colored("PLEASE REPORT TO ADMIN (ERR ID #002)", blue)

def chk():
	print colored("=====================",green)
	print colored("--->CHECK IN MODE<---", blue)
	print colored("=====================",green)