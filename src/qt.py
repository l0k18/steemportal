#!/usr/bin/python3
#
# qt.py
#
# Qt interface frontend module 
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
    print ("Importing Qt frontend module")
    
class SPinterface ():
    """
    Each distinct interface module will replicate the same class and core
    module's interfacing calls. Each module can contain other classes and
    functions, including imports, that are relevant to the module. This top
    level class abstracts the calls so the core can remain agnostic about
    which frontend is being used.
    """
    def __init__(self, config_obj, core_obj):
        """
        Interface initialisation
        This function opens the window, calls back through the core, to 
        get the configuration, to load the initial interface. 
        
        The configuration tells the interface what to set up in the initial
        startup.
        """
        print ("starting interface")
        self.config = config_obj
        self.core = core_obj
        
    def open ():
        """
        This opens up the main window, places all the widgets, and from the
        configuration, loads the content that belongs in them.
        """
        pass
        
    def persist ():
        """
        This collects the current interface status for shutdown of the app
        and 
        """
        pass
        
    def config ():
        """
        This opens up the user configuration dialog for user configuration
        of the interface and specifying the users' desired modes of 
        operation
        """
        pass
        
    def open_url (urlstring):
        """
        This takes the parameter of a URL and queries the core to gather
        the data required to display the new URL
        """
        pass
