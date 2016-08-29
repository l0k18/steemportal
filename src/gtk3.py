#!/usr/bin/python3
#
# gtk..py
#
# Gtk+-3.0 interface frontend
# Also requires GLib-2.0 and other related Gnome modules
#
# Here's your stinkin' licence: http://unlicense.org/
#
# - l0k1
#
# Contact details for l0k1
# steemit.com - https://steemit.com/@l0k1
# bitmessage - BM-2cXWxTVaXJbNyMxv5tAjNg87xS98hrAg8P
# torchat - xq6xcvqc2vy34qtx
# email - l0k1@null.net

def printmodulename ():
    print ("Importing Gtk+-3.0 frontend module")
    
class SPinterface ():
    """
    Each distinct interface module will replicate the same class and core
    module's interfacing calls. Each module can contain other classes and
    functions, including imports, that are relevant to the module. This top
    level class abstracts the calls so the core can remain agnostic about
    which frontend is being used.
    """
