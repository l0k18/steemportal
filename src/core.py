#!/usr/bin/python3
#
# filename.py
#
# component description 
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

print ("launching core module")

class steemportal ():
    """
    This class handles the core functions, and passes the details onto 
    the modules that deal with the implementation details.
    """
    
    def __init__ (self, frontend_obj, config_obj):
        """
        In this function, the configuration and interface classes are
        instantiated, the configuration inteface is established and linked
        to the interface
        
        Log is queried for last opened URL in history log
        """
        print ("starting steemportal")
        self.gui = frontend_obj.SPinterface (config_obj, self)
        self.config = config_obj.SPconfig (frontend_obj, self)
                
    def close ():
        """
        Shuts down interface, persists configuration
        """
        pass
        
    def open_url (urlspec):
        """
        When user clicks a link handled by this application, this function
        interfaces with piston to gather the data, and then passes it to
        the interface frontend
        
        The url is added to the log so it can be recalled with the 'back' 
        function
        """
        pass
        
    def prev_url ():
        """
        Move log position one URL back, and then display it
        """
        pass
        
    def next_url ():
        """
        move log position one URL forward, and then display it
        """
        
    
