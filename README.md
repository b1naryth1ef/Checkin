##Checkin
*The coolest Open Source, pure-Python, MySQL-Enabled Checkin System around!*

###What is Checkin?
Checkin is a simple script that enables admins of work, school, or other environments to keep track of peoples status. It's a simple program which tracks users in MySQL, and allows them to checkin once per day. It records the wide timestamp of all checkins.

###Why Checkin?
The big reason, is because Checkin is 100% Open Source, and free. And if that doesn't get you, get this. It's constantly in development which means it's always getting better. You can run checkin on practically any computer or os,  and it's built in a language thats easy to understand and develop in. 

The use of MySQL allows for thousands of manipulations of your data. Whether thats a graph of checkins, a spreadsheet of data, or a good old CSV of your users, it's easy to access, display, and publish your data. (Making it great for research studies)

Checkin is extremely secure, being able to run completely off network, or on your local server (It can even run over the internet). It's uses a minimal amount of RAM and Processor space, meaning you can run it on the simplest of systems.

###Features

* Fast (It runs at about 0.1% CPU, with 7.5MB RAM, 32.3MB VRAM)
* Free and Open Source (It's the way to go!)
* Built on strong technologies (The popular development language Python, with MySQL backing it )
* Simple (<450 lines of code)
* Customizable

###Setting up
In the future dependencies will be built in. Currently though you'll need to set them up.

*[Python 2.6+](http://www.python.org/download/) (Tested mostly on 2.6)    
*[MySQL](http://dev.mysql.com/downloads/) (Any recent version should do)   
*[MySQLdb](http://sourceforge.net/projects/mysql-python/) (Tested on 5.1.53)
*[Colorama](http://pypi.python.org/pypi/colorama) (Tested on 0.2.4)
*[Termcolor](http://pypi.python.org/pypi/termcolor) (Tested on 1.1.0)

Checkin also has some precompiled versions of the above requirements. They may or may not work depending on your operating system, but go ahead and give them a try: [Reqs Branch](https://github.com/b1naryth1ef/Checkin/zipball/reqs)
 
To install and setup the database and config automatically, just run ```python install.py``` and follow the prompts

###Thanks / Credits
Thanks to the people who made those awesome scripts listed above. Without them this would have been a lot harder of a project. If you like the script, [follow me](http://twitter.com/b1naryth1ef) on twitter and tell me!