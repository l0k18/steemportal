#!/usr/bin/python3
#
# dconf.py
#
# dconf configuration backend
#
# class and functions are a prototype that can be adapted to other backends
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
    
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GObject, Gio

debugflag = True

def debug (debugtext, header):
    if debugflag:
        if header: 
            debugtext = ">>> " + debugtext
        else:
            debugtext = "    " + debugtext
        print (debugtext)

def printmodulename ():
    print ("Importing dconf configuration backend module")
    
class SPconfig ():
    """
    This class defines all the backend functions for storing user settings,
    logs url history/manages log, and other settings
    """
    def __init__(self):
        """
        opens up configuration backend and loads handler for log
        
        opens up user configuration database including blocklist,
        appearance configuration and other interface settings
        """
        debug ("initialising configuration", True)
        self.open ()
        
    def open (self):
        """
        Opens up interface configuration and log
        """
        self.settings = Gio.Settings.new ("org.ascension.steemportal")
        debug ("last viewed: '" + self.get_lastviewed () + "'", False)
        debug ("wif: '" + self.get_wif () + "'", False)
        debug ("history: '" + self.get_history () + "'", False)
        debug ("interface: '" + self.get_interface () + "'", False)                
        
    def get_lastviewed (self):
        return self.settings.get_string ("lastviewed")
        
    def set_lastviewed (self, lastviewed):
        self.settings.set_string ("lastviewed", lastviewed)
    
    def get_wif (self):  
        return self.settings.get_string ("wif")
        
    def set_wif (self, wif):
        self.settings.set_string ("wif", wif)
        
    def get_history (self):
        return self.settings.get_string ("history")
        
    def set_history (self, history):
        self.settings.set_string ("history", history)
        
    def get_interface (self):
        return self.settings.get_string ("interface")
       
    def set_interface (self, interface):
        self.settings.set_string ("interface", interface)
    
class log ():    
    """
    Interacts with URL log, moves cursor, stores changes and history
    """
    def new ():
        """
        At current log cursor, add new entry, and truncate all forward
        entries in navigation log 
        
        Add new item to persistent history log
        """
        pass
    
    def latest ():
        """
        returns most recent log entry URL string
        """
        pass
        
    def back ():
        """
        set log cursor to previous log entry to current cursor location
        return URL string
        """
        pass
        
    def forward ():
        """
        set log cursor to next log entry
        return URL string
        """
        pass
        
config = SPconfig ()
        
