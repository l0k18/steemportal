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

def printmodulename ():
    print ("Importing dconf configuration backend module")
    
class SPconfig ():
    """
    This class defines all the backend functions for storing user settings,
    logs url history/manages log, and other settings
    """
    def __init__(self, frontend_obj, core_obj):
        """
        opens up configuration backend and loads handler for log
        
        opens up user configuration database including blocklist,
        appearance configuration and other interface settings
        """
        print ("initialising configuration")
        self.gui = frontend_obj
        self.core = core_obj
        
    def open ():
        """
        Opens up interface configuration and log
        """
        pass
    
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
