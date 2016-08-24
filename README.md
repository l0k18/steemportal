# steemportal

https://github.com/l0k1-smirenski/steemportal

A python3/Gtk+-3.0 based application for accesing and interacting with the
Steem blockchain forum system. It uses Piston, from the user @xeroc, whose
main page can be found here: http://piston.readthedocs.io/en/stable/

### Motivations for this project

#### Web Browsers are Slow and Inefficient

This project is just beginning and I am going to spend a lot of time working
on it while I have the opportunity. There is a lot of work being done on the
Steem blockchain system, but the main official web portal's web interface is
heavy and slow especially with long comment threads. 

#### Personalised Blocking of Posts by Users

There is also absolutely no mechanism aside from when a user gets flagged so
much they end up with zero or lower reputation score, they disappear from 
the comment feed. The 'mute' mechanism does nothing but really highlight who
you muted, just as pixellation, blurring, black boxes, beeps and silence in
offensive content censorship systems actually draw attention to the supposed
offensive material. Obviously this small thing may be eventually fixed on
the steemit.com website.

#### Topic and Social Grouping

The above two goals are primary, but after these are added and functional,
I will be implementing a simple, small permissioned blockchain system 
similar to Namecoin, except also with group membership moderation, and a
mechanism based on secret shares to allow delegation similar to a board.
https://en.wikipedia.org/wiki/Secret_sharing This blockchain will run as 
part of this application, but there is no reason why it cannot be 
stand-alone, although being so small there is no real reason for it to not
be simply integrated into viewer applications. 

This system will allow you to filter posts according to the posters' 
membership in the group, group administrators will be able to include and 
exclude individual users based on their behaviour. It effectively should 
enable multiple level hierarchic 'page management' functions as well. The 
main goal, however, is to help group by subject and affinity, which will
become more important the bigger the Steem community gets.

### Installation

You must have python3 and install python3-pip, and then with these two pre-
requisites, you can then install piston using:

> pip3 install steem-piston [--user]

Then, to run whatever has been written so far, you just run:

> python3 steemportal.py

I am still working on other elements. It uses the dconf registry system to
store credentials and settings in an instantaneously active manner, and to
persist sessions between launch, so there is a script to install the schema
called **install_compile_schema.sh** which must be run as root or using sudo
to place it in the right place. This adds a configuration branch you can see
if you open dconf-editor and look for org.ascension.

### Copyright, or lack thereof

I claim no copyright on this work, nor do I, by doing so, permit the
redistribution of it without this lack of copyright. Only because if you do,
you will get flagged for plagiarism and it certainly won't have record of
prior art. Not that I think it's going to be anything special, but you can
do whatever you like with it, but unless you change it substantially, you
simply can't claim it is your work.
